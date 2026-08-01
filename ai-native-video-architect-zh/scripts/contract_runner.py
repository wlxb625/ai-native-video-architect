from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
EXECUTION_FILE = ROOT / "EXECUTION.yaml"
WORKFLOW_FILE = ROOT / "contracts/workflow.enforced.yaml"
CONSTITUTION_FILE = ROOT / "constitution/immutable.yaml"
INTEGRITY_FILE = ROOT / "constitution/integrity.json"
TASKS_DIR = ROOT / ".execution/tasks"


class ContractError(RuntimeError):
    pass


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ContractError(f"missing file: {path.relative_to(ROOT)}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ContractError(f"invalid mapping: {path.relative_to(ROOT)}")
    return data


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ContractError(f"missing file: {path.relative_to(ROOT)}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ContractError(f"invalid json object: {path.relative_to(ROOT)}")
    return data


def dump_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_integrity() -> None:
    manifest = load_json(INTEGRITY_FILE)
    mismatches: list[str] = []
    for rel, expected in manifest.get("protected_files", {}).items():
        path = ROOT / rel
        if not path.exists():
            mismatches.append(f"missing:{rel}")
            continue
        actual = sha256(path)
        if actual != expected:
            mismatches.append(f"changed:{rel}")
    if mismatches:
        raise ContractError("IMMUTABLE_CORE_CHANGED: " + ", ".join(mismatches))


def validate_schema(instance: Any, schema_rel: str) -> None:
    schema = load_json(ROOT / schema_rel)
    errors = sorted(Draft202012Validator(schema).iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        formatted = []
        for e in errors[:20]:
            loc = ".".join(str(x) for x in e.path) or "$"
            formatted.append(f"{loc}: {e.message}")
        raise ContractError("SCHEMA_VALIDATION_FAILED: " + " | ".join(formatted))


def task_path(task_id: str) -> Path:
    return TASKS_DIR / task_id


def state_path(task_id: str) -> Path:
    return task_path(task_id) / "state.json"


def load_state(task_id: str) -> dict[str, Any]:
    return load_json(state_path(task_id))


def save_state(task_id: str, state: dict[str, Any]) -> None:
    state["updated_at"] = utc_now()
    dump_json(state_path(task_id), state)


def workflow() -> dict[str, Any]:
    return load_yaml(WORKFLOW_FILE)


def stage_config(stage_id: str) -> dict[str, Any]:
    stages = workflow().get("stages", {})
    if stage_id not in stages:
        raise ContractError(f"unknown stage: {stage_id}")
    return stages[stage_id]


def gate_config(gate_id: str) -> dict[str, Any]:
    gates = workflow().get("gates", {})
    if gate_id not in gates:
        raise ContractError(f"unknown gate: {gate_id}")
    return gates[gate_id]


def add_audit(task_id: str, event: str, **payload: Any) -> None:
    path = task_path(task_id) / "audit.jsonl"
    record = {"time": utc_now(), "event": event, **payload}
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def read_request(args: argparse.Namespace) -> str:
    if getattr(args, "request_file", None):
        return Path(args.request_file).read_text(encoding="utf-8").strip()
    if getattr(args, "request", None):
        return args.request.strip()
    raise ContractError("request or request-file required")


def cmd_start(args: argparse.Namespace) -> None:
    verify_integrity()
    req = read_request(args)
    task_id = args.task_id or f"T-{datetime.now().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:6]}"
    path = task_path(task_id)
    if path.exists():
        raise ContractError(f"task already exists: {task_id}")
    path.mkdir(parents=True)
    state = {
        "task_id": task_id,
        "contract": "ai-native-video-architect-zh",
        "contract_version": load_yaml(EXECUTION_FILE)["contract_version"],
        "evaluation_nonces": {},
        "status": "ACTIVE",
        "current_stage": workflow()["initial_stage"],
        "phase": "READY_FOR_STAGE",
        "request": req,
        "target_stage": args.target_stage,
        "revision_counts": {},
        "gate_results": {},
        "artifacts": {},
        "created_at": utc_now(),
        "updated_at": utc_now(),
    }
    dump_json(path / "request.json", {"task_id": task_id, "request": req})
    save_state(task_id, state)
    receipt = {
        "receipt_type": "ACTIVATION_RECEIPT",
        "task_id": task_id,
        "status": "ACTIVE",
        "current_stage": state["current_stage"],
        "target_stage": state["target_stage"],
        "immutable_integrity": "PASS",
        "execution_mode": "ENFORCED",
    }
    dump_json(path / "activation-receipt.json", receipt)
    add_audit(task_id, "ACTIVATED", stage=state["current_stage"])
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


def compose_stage_packet(state: dict[str, Any]) -> str:
    stage_id = state["current_stage"]
    cfg = stage_config(stage_id)
    parts = [
        "# CONTRACT STAGE PACKET",
        f"- task_id: {state['task_id']}",
        f"- current_stage: {stage_id}",
        f"- stage_name: {cfg['name']}",
        f"- phase: {state['phase']}",
        "",
        "## 不可变规则摘要",
        "1. 只完成当前阶段，不得提前撰写未来阶段产物。",
        "2. 输出必须严格符合指定JSON Schema。",
        "3. 不得自行宣告门禁通过。",
        "4. 评分必须由独立评估产物完成并提供ref_id证据。",
        "5. 未取得CONTRACT_COMPLETE不得称为最终成品。",
        "",
        "## 用户请求",
        state["request"],
        "",
        "## 当前阶段需读取文件",
    ]
    for rel in cfg.get("instruction_files", []):
        parts.append(f"- {rel}")
    parts += [
        "",
        "## 输出Schema",
        f"- {cfg['output_schema']}",
        "",
        "## 提交命令",
        f"python scripts/contract_runner.py submit --task-id {state['task_id']} --artifact <artifact.json>",
    ]
    if cfg.get("gate"):
        parts += [
            "",
            "## 当前阶段存在门禁",
            f"- gate: {cfg['gate']}",
            "- 提交产物后必须生成独立evaluation.json并调用evaluate命令。",
        ]
    return "\n".join(parts) + "\n"


def cmd_prepare(args: argparse.Namespace) -> None:
    verify_integrity()
    state = load_state(args.task_id)
    if state["status"] not in {"ACTIVE", "REVISION_REQUIRED"}:
        raise ContractError(f"task not preparable: {state['status']}")
    if state["phase"] not in {"READY_FOR_STAGE", "REVISION_REQUIRED"}:
        raise ContractError(f"invalid phase for prepare: {state['phase']}")
    stage_id = state["current_stage"]
    cfg = stage_config(stage_id)
    if cfg.get("gate"):
        nonce = uuid.uuid4().hex + uuid.uuid4().hex
        state.setdefault("evaluation_nonces", {})[stage_id] = nonce
        save_state(args.task_id, state)
    packet = compose_stage_packet(state)
    if cfg.get("gate"):
        packet += "\n## Evaluation Challenge\n"
        packet += f"- evaluation_nonce: {state['evaluation_nonces'][stage_id]}\n"
        rule_files = cfg.get("instruction_files", [])
        h = hashlib.sha256()
        for rel in rule_files:
            if rel.startswith("evals/") and (ROOT / rel).exists():
                h.update((ROOT / rel).read_bytes())
        packet += f"- evaluator_rules_sha256: {h.hexdigest()}\n"
    out = task_path(args.task_id) / f"packet-{state['current_stage']}.md"
    out.write_text(packet, encoding="utf-8")
    add_audit(args.task_id, "STAGE_PREPARED", stage=state["current_stage"], packet=str(out.relative_to(ROOT)))
    print(packet)


def check_s01_deterministic(artifact: dict[str, Any], adaptive_policy: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    params = load_yaml(CONSTITUTION_FILE).get("execution_minimums", {})
    minimum = int(params.get("internal_candidate_count", 10))
    candidates = artifact.get("candidates", [])
    if len(candidates) < minimum:
        errors.append(f"candidate_count {len(candidates)} < required {minimum}")
    shortlist_count = int(params.get("shortlist_count", 3))
    if len(artifact.get("shortlist", [])) < shortlist_count:
        errors.append(f"shortlist_count < required {shortlist_count}")
    ids = [c.get("concept_id") for c in candidates]
    if len(ids) != len(set(ids)):
        errors.append("duplicate concept_id")
    selected = artifact.get("selected_concept_id")
    if selected not in ids:
        errors.append("selected_concept_id not in candidates")
    fp_fields = ["relationship_type", "setting_type", "conflict_engine", "climax_action_type", "final_image_type"]
    shortlist = artifact.get("shortlist", [])
    if len(shortlist) != len(set(shortlist)):
        errors.append("duplicate shortlist concept_id")
    unknown_shortlist = sorted(set(shortlist) - set(ids))
    if unknown_shortlist:
        errors.append(f"shortlist contains unknown concept ids: {unknown_shortlist}")
    if selected not in shortlist:
        errors.append("selected_concept_id not in shortlist")
    seen_pairs: dict[tuple[str, str], str] = {}
    for c in candidates:
        pair = (re.sub(r"\s+", "", str(c.get("logline", ""))).lower(), re.sub(r"\s+", "", str(c.get("core_promise", ""))).lower())
        if pair in seen_pairs and all(pair):
            errors.append(f"semantic duplicate candidate pair: {seen_pairs[pair]} and {c.get('concept_id')}")
        else:
            seen_pairs[pair] = str(c.get("concept_id"))
    for i, c1 in enumerate(candidates):
        fp1 = c1.get("fingerprint", {})
        for c2 in candidates[i+1:]:
            fp2 = c2.get("fingerprint", {})
            same = sum(1 for f in fp_fields if fp1.get(f) and fp1.get(f) == fp2.get(f))
            if same >= 3:
                errors.append(f"candidate pair duplicates on {same} fingerprint fields: {c1.get('concept_id')} / {c2.get('concept_id')}")

    history = adaptive_policy.get("creative_history", {}).get("used_concepts", []) + adaptive_policy.get("creative_history", {}).get("rejected_concepts", [])
    for c in candidates:
        fp = c.get("fingerprint", {})
        for old in history:
            old_fp = old.get("fingerprint", old)
            same = sum(1 for f in fp_fields if fp.get(f) and fp.get(f) == old_fp.get(f))
            if same >= 3:
                errors.append(f"{c.get('concept_id')} duplicates history on {same} fingerprint fields")
    relationships = {c.get("fingerprint", {}).get("relationship_type") for c in candidates}
    settings = {c.get("fingerprint", {}).get("setting_type") for c in candidates}
    climax_types = {c.get("fingerprint", {}).get("climax_action_type") for c in candidates}
    if len(settings) < int(params.get("minimum_distinct_settings", 4)):
        errors.append("insufficient distinct settings")
    if len(climax_types) < int(params.get("minimum_distinct_climax_action_types", 4)):
        errors.append("insufficient distinct climax action types")
    max_ratio = float(params.get("maximum_same_relationship_ratio", 0.4))
    for rel in relationships:
        count = sum(1 for c in candidates if c.get("fingerprint", {}).get("relationship_type") == rel)
        if candidates and count / len(candidates) > max_ratio:
            errors.append(f"relationship ratio too high: {rel}={count}/{len(candidates)}")
    return errors




def _age_band_valid(age: Any, band: str) -> bool:
    if band == "AGELESS_OR_NONHUMAN":
        return age is None
    if not isinstance(age, int):
        return False
    ranges = {
        "CHILD": (1, 12),
        "TEEN": (13, 19),
        "YOUNG_ADULT": (18, 35),
        "MIDDLE_AGED": (36, 59),
        "OLDER_ADULT": (60, 120),
    }
    lo, hi = ranges.get(band, (-1, -1))
    return lo <= age <= hi


def _check_age_choice(age_choice: dict[str, Any], label: str) -> list[str]:
    errors: list[str] = []
    band = age_choice.get("age_band")
    age = age_choice.get("approximate_age")
    if not _age_band_valid(age, str(band)):
        errors.append(f"{label}: approximate_age does not match age_band")
    start_age = age_choice.get("plausible_experience_start_age")
    required_years = age_choice.get("required_experience_years")
    if isinstance(age, int) and isinstance(start_age, int) and isinstance(required_years, int):
        if age < start_age + required_years:
            errors.append(f"{label}: age cannot support declared experience years")
    market = age_choice.get("target_market_context")
    youth_applies = age_choice.get("youth_priority_applies") is True
    young = band in {"TEEN", "YOUNG_ADULT"}
    decision = age_choice.get("decision")
    if market in {"SHORT_VIDEO", "WEB_FICTION"} and youth_applies and not young:
        if decision not in {"OLDER_SELECTED_FOR_STORY_FIT", "AGE_SPECIFIC_SELECTED"}:
            errors.append(f"{label}: non-young choice in youth-priority context lacks story-fit override")
        if len(str(age_choice.get("what_breaks_if_younger", "")).strip()) < 8:
            errors.append(f"{label}: older protagonist requires concrete younger counterfactual")
    if young and decision not in {"YOUNG_SELECTED", "AGE_SPECIFIC_SELECTED", "AGE_NEUTRAL"}:
        errors.append(f"{label}: young age band conflicts with decision")
    if band == "AGELESS_OR_NONHUMAN" and decision != "AGELESS_OR_NONHUMAN":
        errors.append(f"{label}: ageless/nonhuman band conflicts with decision")
    return errors


def check_character_age_contract(artifact: dict[str, Any], stage_id: str, state: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if stage_id == "S01":
        for c in artifact.get("candidates", []):
            errors.extend(_check_age_choice(c.get("age_choice", {}), f"concept {c.get('concept_id')}"))
        s00_rel = state.get("artifacts", {}).get("S00")
        if s00_rel:
            brief = load_json(ROOT / s00_rel)
            market = brief.get("market_context")
            strategy = brief.get("age_strategy")
            for c in artifact.get("candidates", []):
                ac = c.get("age_choice", {})
                if ac.get("target_market_context") != market:
                    errors.append(f"concept {c.get('concept_id')}: target_market_context differs from S00")
                expected = strategy == "YOUTH_PRIORITY_WITH_STORY_FIT_OVERRIDE" and market in {"SHORT_VIDEO", "WEB_FICTION"}
                if ac.get("youth_priority_applies") is not expected:
                    errors.append(f"concept {c.get('concept_id')}: youth_priority_applies differs from S00 strategy")
    elif stage_id == "S02":
        audit = artifact.get("protagonist_age_audit", {})
        errors.extend(_check_age_choice(audit, "S02 protagonist_age_audit"))
        s01_rel = state.get("artifacts", {}).get("S01")
        if s01_rel:
            s01 = load_json(ROOT / s01_rel)
            selected = next((x for x in s01.get("candidates", []) if x.get("concept_id") == s01.get("selected_concept_id")), None)
            if selected:
                source = selected.get("age_choice", {})
                if audit.get("age_continuity_source_concept_id") != selected.get("concept_id"):
                    errors.append("S02 age audit source concept mismatch")
                for key in ["protagonist_name", "approximate_age", "age_band", "target_market_context"]:
                    if audit.get(key) != source.get(key):
                        errors.append(f"S02 age continuity mismatch: {key}")
    elif stage_id == "S03":
        audit = artifact.get("protagonist_age_audit", {})
        errors.extend(_check_age_choice(audit, "S03 protagonist_age_audit"))
        s02_rel = state.get("artifacts", {}).get("S02")
        if s02_rel:
            source = load_json(ROOT / s02_rel).get("protagonist_age_audit", {})
            for key in ["protagonist_name", "approximate_age", "age_band", "target_market_context"]:
                if audit.get(key) != source.get(key):
                    errors.append(f"S03 age continuity mismatch: {key}")
        profiles = artifact.get("character_profiles", [])
        protagonist = next((x for x in profiles if x.get("name") == audit.get("protagonist_name")), None)
        if not protagonist:
            errors.append("protagonist missing from character_profiles")
        else:
            if protagonist.get("approximate_age") != audit.get("approximate_age") or protagonist.get("age_band") != audit.get("age_band"):
                errors.append("character profile age differs from protagonist_age_audit")
    return errors

def check_climax_contract(artifact: dict[str, Any], stage_id: str, adaptive_policy: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    profile = artifact.get("climax_profile") or adaptive_policy.get("execution_parameters", {}).get("default_climax_profile")
    if not profile:
        errors.append("missing climax_profile")
        return errors
    if stage_id == "S01":
        for c in artifact.get("candidates", []):
            if c.get("climax_profile") == "STRONG_DRAMATIC_PEAK":
                if len(c.get("climax_escalation", [])) < 2:
                    errors.append(f"{c.get('concept_id')}: strong peak needs >=2 escalation steps")
                if c.get("opposing_value_a", "").strip() == c.get("opposing_value_b", "").strip():
                    errors.append(f"{c.get('concept_id')}: opposing values are identical")
    elif stage_id in {"S02", "S03"}:
        audit = artifact.get("climax_audit", {})
        if profile == "STRONG_DRAMATIC_PEAK":
            escalation_key = "escalation_beats" if stage_id == "S02" else "escalation_scene_ids"
            if len(audit.get(escalation_key, [])) < 2:
                errors.append("strong peak needs at least two escalation steps")
            if audit.get("value_a", "").strip() == audit.get("value_b", "").strip():
                errors.append("climax values must differ")
            for key in ["pressure_source", "point_of_no_return", "audience_uncertainty", "irreversible_external_or_relational_change", "aftermath_state"]:
                if not str(audit.get(key, "")).strip():
                    errors.append(f"missing climax field: {key}")
            if stage_id == "S03":
                scene_ids = {s.get("scene_id") for s in artifact.get("scenes", [])}
                climax_id = artifact.get("climax_scene_id")
                if climax_id not in scene_ids:
                    errors.append("climax_scene_id not found in scenes")
                for sid in audit.get("escalation_scene_ids", []):
                    if sid not in scene_ids:
                        errors.append(f"unknown escalation scene: {sid}")
    return errors




def _meaning_text_ok(value: Any, minimum: int = 8) -> bool:
    text = str(value or "").strip()
    generic = {"勇敢做自己", "珍惜眼前人", "正义战胜邪恶", "亲情可贵", "爱能战胜一切", "成长", "救赎", "希望"}
    return len(text) >= minimum and text not in generic

def _check_meaning_unit(unit: dict[str, Any], label: str, primary_path: str | None = None) -> list[str]:
    errors: list[str] = []
    profile = unit.get("profile")
    basis = unit.get("genre_basis")
    if profile == "THEMATIC_MEANING_REQUIRED":
        fields = ["human_question", "competing_value_a", "competing_value_b", "protagonist_initial_belief", "belief_pressure_or_change", "climax_thematic_answer", "ending_residue_or_question", "contemporary_relevance", "why_worth_telling"]
        for key in fields:
            if not _meaning_text_ok(unit.get(key)):
                errors.append(f"{label}: weak or missing meaning field {key}")
        if str(unit.get("competing_value_a", "")).strip() == str(unit.get("competing_value_b", "")).strip():
            errors.append(f"{label}: competing values are identical")
        if basis != "STANDARD_NARRATIVE":
            errors.append(f"{label}: thematic profile requires STANDARD_NARRATIVE basis")
    elif profile == "FORMAL_ABSURDIST_EXCEPTION":
        if basis not in {"ABSTRACT", "ABSURDIST", "FORMAL_EXPERIMENT"}:
            errors.append(f"{label}: invalid exception genre_basis")
        if primary_path not in {None, "EXPERIMENTAL", "HYBRID"}:
            errors.append(f"{label}: formal/absurdist exception cannot bypass a non-experimental primary path")
        for key in ["formal_intent", "audience_experience", "pattern_logic", "formal_culmination", "anti_randomness_proof", "why_exception_applies"]:
            if not _meaning_text_ok(unit.get(key), 12):
                errors.append(f"{label}: weak or missing formal exception field {key}")
    else:
        errors.append(f"{label}: unknown meaning profile")
    return errors

def check_meaning_contract(artifact: dict[str, Any], stage_id: str, state: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if stage_id == "S01":
        for c in artifact.get("candidates", []):
            errors.extend(_check_meaning_unit(c.get("meaning_contract", {}), f"concept {c.get('concept_id')}", c.get("primary_path")))
    elif stage_id in {"S02", "S03"}:
        audit = artifact.get("meaning_audit", {})
        errors.extend(_check_meaning_unit(audit, f"{stage_id} meaning_audit", artifact.get("primary_path")))
        source_rel = state.get("artifacts", {}).get("S01")
        if source_rel:
            s01 = load_json(ROOT / source_rel)
            selected = next((x for x in s01.get("candidates", []) if x.get("concept_id") == s01.get("selected_concept_id")), None)
            if selected:
                src = selected.get("meaning_contract", {})
                if audit.get("source_concept_id") != selected.get("concept_id"):
                    errors.append(f"{stage_id}: meaning source concept mismatch")
                for key in ["profile", "genre_basis"]:
                    if audit.get(key) != src.get(key):
                        errors.append(f"{stage_id}: meaning continuity mismatch {key}")
                if audit.get("profile") == "THEMATIC_MEANING_REQUIRED":
                    for key in ["human_question", "competing_value_a", "competing_value_b"]:
                        if str(audit.get(key, "")).strip() != str(src.get(key, "")).strip():
                            errors.append(f"{stage_id}: thematic continuity mismatch {key}")
        ids = {str(x.get("beat_id" if stage_id == "S02" else "scene_id")) for x in artifact.get("beats" if stage_id == "S02" else "scenes", [])}
        if audit.get("profile") == "THEMATIC_MEANING_REQUIRED":
            keys = ["theme_setup_beat_ids", "theme_test_beat_ids"] if stage_id == "S02" else ["theme_setup_scene_ids", "theme_test_scene_ids"]
            singles = ["climax_answer_beat_id", "ending_residue_beat_id"] if stage_id == "S02" else ["climax_answer_scene_id", "ending_residue_scene_id"]
        else:
            keys = ["pattern_setup_beat_ids", "pattern_development_beat_ids"] if stage_id == "S02" else ["pattern_setup_scene_ids", "pattern_development_scene_ids"]
            singles = ["formal_culmination_beat_id"] if stage_id == "S02" else ["formal_culmination_scene_id"]
        for key in keys:
            unknown = set(map(str, audit.get(key, []))) - ids
            if unknown:
                errors.append(f"{stage_id}: unknown meaning refs in {key}: {sorted(unknown)}")
        for key in singles:
            if str(audit.get(key)) not in ids:
                errors.append(f"{stage_id}: unknown meaning ref {key}={audit.get(key)}")
    return errors

def is_nonempty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict, tuple, set)):
        return len(value) > 0
    return True


def check_progression_contract(artifact: dict[str, Any], stage_id: str) -> list[str]:
    errors: list[str] = []
    flat_markers = {"none", "no change", "没有变化", "无变化", "重复", "不变"}
    if stage_id == "S02":
        beats = artifact.get("beats", [])
        ids = [str(b.get("beat_id")) for b in beats]
        if len(ids) != len(set(ids)):
            errors.append("duplicate beat_id")
        valid = set(ids)
        audit = artifact.get("climax_audit", {})
        for key in ["setup_beats", "escalation_beats"]:
            unknown = sorted(set(audit.get(key, [])) - valid)
            if unknown:
                errors.append(f"unknown {key}: {unknown}")
        changed = 0
        actions = set()
        for b in beats:
            if b.get("entry_state") != b.get("exit_state"):
                changed += 1
            actions.add(re.sub(r"\s+", "", str(b.get("action_or_formal_event", ""))).lower())
        if changed < max(3, len(beats) - 2):
            errors.append("insufficient beat state changes")
        if len(actions) < max(3, len(beats) - 2):
            errors.append("insufficient distinct beat actions")
        mid = str(artifact.get("middle_audit", {}).get("what_changes", "")).strip().lower()
        if not mid or mid in flat_markers or any(x in mid for x in ["没有变化", "无变化"]):
            errors.append("middle_audit does not establish a real change")
    elif stage_id == "S03":
        scenes = artifact.get("scenes", [])
        ids = [str(s.get("scene_id")) for s in scenes]
        if len(ids) != len(set(ids)):
            errors.append("duplicate scene_id")
        valid = set(ids)
        audit = artifact.get("climax_audit", {})
        for key in ["setup_scene_ids", "escalation_scene_ids"]:
            unknown = sorted(set(audit.get(key, [])) - valid)
            if unknown:
                errors.append(f"unknown {key}: {unknown}")
        climax = artifact.get("climax_scene_id")
        if climax in set(audit.get("escalation_scene_ids", [])):
            errors.append("climax scene cannot be counted as a pre-climax escalation scene")
        positions = {sid:i for i,sid in enumerate(ids)}
        if climax in positions:
            for sid in audit.get("escalation_scene_ids", []):
                if sid in positions and positions[sid] >= positions[climax]:
                    errors.append(f"escalation scene must precede climax: {sid}")
        actions = {re.sub(r"\s+", "", "|".join(map(str, s.get("observable_action", [])))).lower() for s in scenes}
        if len(actions) < max(3, len(scenes) - 2):
            errors.append("insufficient distinct scene actions")
        changed = sum(1 for i,s in enumerate(scenes) if i == 0 or s.get("exit_state") != scenes[i-1].get("exit_state"))
        if changed < max(3, len(scenes) - 2):
            errors.append("insufficient scene state progression")
    return errors


def check_generic_stage_contract(artifact: dict[str, Any], cfg: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if cfg.get("content_must_be_nonempty") and not is_nonempty(artifact.get("content")):
        errors.append("stage content is empty")
    coverage = artifact.get("coverage", {})
    for key in cfg.get("required_coverage_keys", []):
        if coverage.get(key) is not True:
            errors.append(f"coverage not confirmed: {key}")
    return errors


def validate_applicability(evaluation: dict[str, Any], artifact: dict[str, Any], stage_id: str) -> list[str]:
    failures: list[str] = []
    results = {r.get("evaluator"): r for r in evaluation.get("results", [])}
    names = [r.get("evaluator") for r in evaluation.get("results", [])]
    if len(names) != len(set(names)):
        failures.append("duplicate evaluator names")
    if stage_id in {"S02", "S03"}:
        mech = results.get("mechanism_overuse_check")
        if artifact.get("uses_speculative_mechanism") and mech and mech.get("status") == "NOT_APPLICABLE":
            failures.append("mechanism_overuse_check cannot be NOT_APPLICABLE when mechanism is used")
        twist = results.get("twist_legality_check")
        if artifact.get("uses_twist") and (not twist or twist.get("status") == "NOT_APPLICABLE"):
            failures.append("twist_legality_check must run when twist is used")
    if stage_id == "S03":
        dia = results.get("dialogue_check")
        if artifact.get("contains_dialogue") and dia and dia.get("status") == "NOT_APPLICABLE":
            failures.append("dialogue_check cannot be NOT_APPLICABLE when dialogue exists")
    return failures

def artifact_reference_ids(artifact: dict[str, Any], stage_id: str) -> set[str]:
    if stage_id == "S01":
        return {str(x.get("concept_id")) for x in artifact.get("candidates", []) if x.get("concept_id")}
    if stage_id == "S02":
        return {str(x.get("beat_id")) for x in artifact.get("beats", []) if x.get("beat_id")}
    if stage_id == "S03":
        return {str(x.get("scene_id")) for x in artifact.get("scenes", []) if x.get("scene_id")}
    return set()


def validate_evaluation_context_and_refs(evaluation: dict[str, Any], artifact_path: Path, artifact: dict[str, Any], stage_id: str) -> list[str]:
    failures: list[str] = []
    ctx = evaluation.get("evaluation_context", {})
    if ctx.get("generator_context_id") == ctx.get("evaluator_context_id"):
        failures.append("generator_context_id must differ from evaluator_context_id")
    if ctx.get("generator_rationale_visible") is not False:
        failures.append("generator rationale must not be visible to evaluator")
    if ctx.get("artifact_sha256") != sha256(artifact_path):
        failures.append("evaluation artifact_sha256 mismatch")
    valid_refs = artifact_reference_ids(artifact, stage_id)
    if valid_refs:
        for result in evaluation.get("results", []):
            for ev in result.get("evidence", []):
                tokens = set(re.findall(r"[A-Z]{1,4}\d{1,4}", str(ev.get("ref_id", ""))))
                if not tokens:
                    failures.append(f"{result.get('evaluator')}: evidence has no locatable ref_id")
                elif not tokens.issubset(valid_refs):
                    failures.append(f"{result.get('evaluator')}: unknown evidence refs {sorted(tokens - valid_refs)}")
    c = next((r for r in evaluation.get("results", []) if r.get("evaluator") == "climax_force_check"), None)
    if c:
        expected = {
            "removable_without_changing_ending": False,
            "choice_has_obvious_correct_answer": False,
            "cost_paid_on_screen": True,
            "climax_distinct_from_resolution": True,
            "pressure_escalates_before_action": True,
            "post_climax_state_cannot_return": True,
        }
        answers = c.get("counterfactual_challenges", {})
        for key, value in expected.items():
            if answers.get(key) is not value:
                failures.append(f"climax counterfactual failed: {key} expected {value}")
    m = next((r for r in evaluation.get("results", []) if r.get("evaluator") == "meaning_and_thematic_necessity_check"), None)
    if m:
        profile = None
        if stage_id == "S01":
            selected_id = artifact.get("selected_concept_id")
            selected = next((x for x in artifact.get("candidates", []) if x.get("concept_id") == selected_id), None)
            profile = (selected or {}).get("meaning_contract", {}).get("profile")
        else:
            profile = artifact.get("meaning_audit", {}).get("profile")
        answers = m.get("meaning_counterfactual_challenges", {})
        if profile == "THEMATIC_MEANING_REQUIRED":
            expected = {
                "theme_survives_genre_removal": True,
                "competing_values_both_understandable": True,
                "protagonist_belief_is_tested": True,
                "climax_answers_theme_through_action": True,
                "ending_adds_residue_not_slogan": True,
                "meaning_not_added_after_plot": True,
            }
        else:
            expected = {
                "exception_is_declared_and_justified": True,
                "formal_logic_is_consistent": True,
                "audience_experience_is_intentional": True,
                "not_random_for_randomness_sake": True,
                "form_culminates_or_transforms": True,
            }
        for key, value in expected.items():
            if answers.get(key) is not value:
                failures.append(f"meaning counterfactual failed: {key} expected {value}")
    return failures


def cmd_submit(args: argparse.Namespace) -> None:
    verify_integrity()
    state = load_state(args.task_id)
    if state["phase"] not in {"READY_FOR_STAGE", "REVISION_REQUIRED"}:
        raise ContractError(f"submission not allowed in phase: {state['phase']}")
    artifact = load_json(Path(args.artifact))
    stage_id = state["current_stage"]
    cfg = stage_config(stage_id)
    validate_schema(artifact, cfg["output_schema"])
    if artifact.get("task_id") != args.task_id:
        raise ContractError("artifact task_id mismatch")
    if artifact.get("stage_id") != stage_id:
        raise ContractError("artifact stage_id mismatch")
    deterministic_errors: list[str] = []
    policy_path = Path(args.policy) if args.policy else ROOT / "adaptive/default-policy.yaml"
    policy = load_yaml(policy_path)
    if stage_id == "S01":
        deterministic_errors.extend(check_s01_deterministic(artifact, policy))
    if stage_id in {"S01", "S02", "S03"}:
        deterministic_errors.extend(check_character_age_contract(artifact, stage_id, state))
    if stage_id in {"S01", "S02", "S03"}:
        deterministic_errors.extend(check_climax_contract(artifact, stage_id, policy))
    if stage_id in {"S01", "S02", "S03"}:
        deterministic_errors.extend(check_meaning_contract(artifact, stage_id, state))
    if stage_id in {"S02", "S03"}:
        deterministic_errors.extend(check_progression_contract(artifact, stage_id))
    if stage_id in {"S04", "S05", "S06", "S07", "S08", "S09", "S10", "S11", "S12"}:
        deterministic_errors.extend(check_generic_stage_contract(artifact, cfg))
    if deterministic_errors:
        add_audit(args.task_id, "ARTIFACT_REJECTED", stage=stage_id, reasons=deterministic_errors)
        raise ContractError("DETERMINISTIC_CHECK_FAILED: " + " | ".join(deterministic_errors))
    artifact_dest = task_path(args.task_id) / "artifacts" / f"{stage_id}.json"
    dump_json(artifact_dest, artifact)
    state["artifacts"][stage_id] = str(artifact_dest.relative_to(ROOT))
    if cfg.get("gate"):
        state["phase"] = "AWAITING_EVALUATION"
        state["pending_gate"] = cfg["gate"]
    else:
        next_stage = cfg.get("next_on_submit")
        if cfg.get("completion_stage") or stage_id == state.get("target_stage"):
            state["phase"] = "READY_TO_FINALIZE"
            state["status"] = "READY_TO_FINALIZE"
        elif next_stage:
            state["current_stage"] = next_stage
            state["phase"] = "READY_FOR_STAGE"
    save_state(args.task_id, state)
    add_audit(args.task_id, "ARTIFACT_ACCEPTED", stage=stage_id, next_phase=state["phase"])
    print(json.dumps({"status": "ACCEPTED", "stage": stage_id, "phase": state["phase"], "current_stage": state["current_stage"]}, ensure_ascii=False, indent=2))


def result_map(evaluation: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {r["evaluator"]: r for r in evaluation.get("results", [])}


def evaluate_gate(evaluation: dict[str, Any], gate: dict[str, Any]) -> tuple[str, list[str], list[str]]:
    results = result_map(evaluation)
    failures: list[str] = []
    must_fix: list[str] = []
    conditional = False
    for name, rule in gate.get("required_evaluators", {}).items():
        if name not in results:
            failures.append(f"missing evaluator: {name}")
            continue
        r = results[name]
        evidence = r.get("evidence", [])
        if not evidence:
            failures.append(f"missing evidence: {name}")
        if r.get("hard_failures"):
            failures.append(f"hard failure in {name}: {r['hard_failures']}")
        status = r.get("status")
        allowed = rule.get("allowed_statuses")
        expected = rule.get("status")
        if allowed and status not in allowed:
            if status == "CONDITIONAL":
                conditional = True
            else:
                failures.append(f"{name} status {status} not in {allowed}")
        elif expected and status != expected:
            if status == "CONDITIONAL":
                conditional = True
            else:
                failures.append(f"{name} status {status} != {expected}")
        min_score = rule.get("minimum_score")
        if min_score is not None:
            score = r.get("score")
            if score is None or score < min_score:
                failures.append(f"{name} score {score} < {min_score}")
        for sub, threshold in rule.get("minimum_subscores", {}).items():
            val = r.get("subscores", {}).get(sub)
            if val is None or val < threshold:
                failures.append(f"{name}.{sub} {val} < {threshold}")
        must_fix.extend(r.get("must_fix", []))
    if failures:
        return "FAIL", failures, must_fix
    if conditional or evaluation.get("overall_status") == "CONDITIONAL":
        return "CONDITIONAL", [], must_fix
    if evaluation.get("overall_status") != "PASS":
        return "FAIL", [f"overall_status={evaluation.get('overall_status')}"], must_fix
    return "PASS", [], must_fix


def cmd_evaluate(args: argparse.Namespace) -> None:
    verify_integrity()
    state = load_state(args.task_id)
    if state["phase"] != "AWAITING_EVALUATION":
        raise ContractError(f"evaluation not allowed in phase: {state['phase']}")
    evaluation = load_json(Path(args.evaluation))
    gate_id = state["pending_gate"]
    gate = gate_config(gate_id)
    validate_schema(evaluation, gate["evaluation_schema"])
    if evaluation.get("task_id") != args.task_id or evaluation.get("stage_id") != state["current_stage"]:
        raise ContractError("evaluation task_id/stage_id mismatch")
    artifact_rel = state.get("artifacts", {}).get(state["current_stage"])
    if not artifact_rel:
        raise ContractError("missing submitted artifact for evaluation")
    artifact_path = ROOT / artifact_rel
    artifact = load_json(artifact_path)
    context_failures = validate_evaluation_context_and_refs(evaluation, artifact_path, artifact, state["current_stage"])
    expected_nonce = state.get("evaluation_nonces", {}).get(state["current_stage"])
    if evaluation.get("evaluation_context", {}).get("evaluation_nonce") != expected_nonce:
        context_failures.append("evaluation_nonce mismatch")
    cfg = stage_config(state["current_stage"])
    h = hashlib.sha256()
    for rel in cfg.get("instruction_files", []):
        if rel.startswith("evals/") and (ROOT / rel).exists():
            h.update((ROOT / rel).read_bytes())
    if evaluation.get("evaluation_context", {}).get("evaluator_rules_sha256") != h.hexdigest():
        context_failures.append("evaluator_rules_sha256 mismatch")
    context_failures.extend(validate_applicability(evaluation, artifact, state["current_stage"]))
    if context_failures:
        raise ContractError("EVALUATION_VALIDATION_FAILED: " + " | ".join(context_failures))
    decision, reasons, must_fix = evaluate_gate(evaluation, gate)
    eval_dest = task_path(args.task_id) / "evaluations" / f"{state['current_stage']}-{gate_id}.json"
    dump_json(eval_dest, evaluation)
    state["gate_results"][gate_id] = {"decision": decision, "reasons": reasons, "must_fix": must_fix, "evaluation": str(eval_dest.relative_to(ROOT))}
    stage_id = state["current_stage"]
    if decision == "PASS":
        if stage_id == state.get("target_stage"):
            state["phase"] = "READY_TO_FINALIZE"
            state["status"] = "READY_TO_FINALIZE"
        else:
            state["current_stage"] = gate["pass"]
            state["phase"] = "READY_FOR_STAGE"
            state["status"] = "ACTIVE"
        state.pop("pending_gate", None)
    else:
        key = gate_id
        count = int(state["revision_counts"].get(key, 0)) + 1
        state["revision_counts"][key] = count
        max_rounds = int(load_yaml(CONSTITUTION_FILE)["revision"]["maximum_rounds_per_gate"])
        if count > max_rounds:
            state["status"] = "CONTRACT_FAILED"
            state["phase"] = "FAILED"
        else:
            target = gate["conditional"] if decision == "CONDITIONAL" else gate["fail"]
            state["current_stage"] = target
            state["phase"] = "REVISION_REQUIRED"
            state["status"] = "REVISION_REQUIRED"
            state["last_must_fix"] = must_fix or reasons
            state.pop("pending_gate", None)
    save_state(args.task_id, state)
    add_audit(args.task_id, "GATE_DECISION", gate=gate_id, decision=decision, reasons=reasons, next_stage=state["current_stage"], phase=state["phase"])
    print(json.dumps({"gate": gate_id, "decision": decision, "reasons": reasons, "must_fix": must_fix, "current_stage": state["current_stage"], "phase": state["phase"], "task_status": state["status"]}, ensure_ascii=False, indent=2))


def cmd_status(args: argparse.Namespace) -> None:
    state = load_state(args.task_id)
    print(json.dumps(state, ensure_ascii=False, indent=2))


def cmd_finalize(args: argparse.Namespace) -> None:
    verify_integrity()
    state = load_state(args.task_id)
    if state["phase"] != "READY_TO_FINALIZE" and state["status"] != "READY_TO_FINALIZE":
        raise ContractError(f"finalization forbidden: phase={state['phase']} status={state['status']}")
    artifact = Path(args.artifact)
    if not artifact.exists() or artifact.stat().st_size == 0:
        raise ContractError("final artifact missing or empty")
    s13_rel = state.get("artifacts", {}).get("S13")
    if s13_rel:
        s13_artifact = load_json(ROOT / s13_rel)
        declared = s13_artifact.get("final_artifact_sha256")
        actual = sha256(artifact)
        if declared != actual:
            raise ContractError("final artifact sha256 does not match S13 package declaration")
    receipt = {
        "receipt_type": "COMPLETION_RECEIPT",
        "status": "CONTRACT_COMPLETE",
        "task_id": args.task_id,
        "completed_at": utc_now(),
        "final_artifact": str(artifact.resolve()),
        "final_artifact_sha256": sha256(artifact),
        "passed_gates": [k for k, v in state.get("gate_results", {}).items() if v.get("decision") == "PASS"],
        "revision_counts": state.get("revision_counts", {}),
        "immutable_integrity": "PASS",
    }
    dump_json(task_path(args.task_id) / "completion-receipt.json", receipt)
    state["status"] = "CONTRACT_COMPLETE"
    state["phase"] = "COMPLETE"
    state["completion_receipt"] = str((task_path(args.task_id) / "completion-receipt.json").relative_to(ROOT))
    save_state(args.task_id, state)
    add_audit(args.task_id, "CONTRACT_COMPLETE", final_sha256=receipt["final_artifact_sha256"])
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Contract Skill deterministic runner")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("start")
    p.add_argument("--request")
    p.add_argument("--request-file")
    p.add_argument("--task-id")
    p.add_argument("--target-stage", choices=[f"S{i:02d}" for i in range(14)], default="S03")
    p.set_defaults(func=cmd_start)

    p = sub.add_parser("prepare")
    p.add_argument("--task-id", required=True)
    p.set_defaults(func=cmd_prepare)

    p = sub.add_parser("submit")
    p.add_argument("--task-id", required=True)
    p.add_argument("--artifact", required=True)
    p.add_argument("--policy")
    p.set_defaults(func=cmd_submit)

    p = sub.add_parser("evaluate")
    p.add_argument("--task-id", required=True)
    p.add_argument("--evaluation", required=True)
    p.set_defaults(func=cmd_evaluate)

    p = sub.add_parser("status")
    p.add_argument("--task-id", required=True)
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("finalize")
    p.add_argument("--task-id", required=True)
    p.add_argument("--artifact", required=True)
    p.set_defaults(func=cmd_finalize)

    return parser


def main() -> int:
    try:
        args = build_parser().parse_args()
        args.func(args)
        return 0
    except (ContractError, json.JSONDecodeError, yaml.YAMLError) as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
