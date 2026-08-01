from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "EXECUTION.yaml",
    "CONTRACT_VERSION",
    "constitution/immutable.yaml",
    "constitution/integrity.json",
    "contracts/execution-protocol.md",
    "contracts/workflow.enforced.yaml",
    "adaptive/default-policy.yaml",
    "adaptive/policy.schema.json",
    "schemas/s00-brief.schema.json",
    "schemas/s01-concepts.schema.json",
    "schemas/s02-treatment.schema.json",
    "schemas/s03-script.schema.json",
    "schemas/evaluation.schema.json",
    "schemas/s13-full-package.schema.json",
    "schemas/policy-patch.schema.json",
    "scripts/contract_runner.py",
    "scripts/apply_policy_patch.py",
    "evals/climax-force-check.md",
    "evals/character-age-fit-check.md",
    "evals/meaning-and-thematic-necessity-check.md",
    "tests/test_meaning_gate.py",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        p = ROOT / rel
        if not p.exists():
            errors.append(f"missing:{rel}")
        elif p.stat().st_size == 0:
            errors.append(f"empty:{rel}")
    try:
        execution = yaml.safe_load((ROOT / "EXECUTION.yaml").read_text(encoding="utf-8"))
        if execution.get("kind") != "contract-skill":
            errors.append("EXECUTION.kind must be contract-skill")
        workflow = yaml.safe_load((ROOT / execution["workflow"]).read_text(encoding="utf-8"))
        for stage_id, stage in workflow.get("stages", {}).items():
            schema_path = ROOT / stage["output_schema"]
            if not schema_path.exists():
                errors.append(f"{stage_id} schema missing")
            for rel in stage.get("instruction_files", []):
                if not (ROOT / rel).exists():
                    errors.append(f"{stage_id} instruction missing:{rel}")
        for gate_id, gate in workflow.get("gates", {}).items():
            if not (ROOT / gate["evaluation_schema"]).exists():
                errors.append(f"{gate_id} eval schema missing")
    except Exception as exc:
        errors.append(f"parse:{exc}")
    try:
        integrity = json.loads((ROOT / "constitution/integrity.json").read_text(encoding="utf-8"))
        for rel, expected in integrity.get("protected_files", {}).items():
            p = ROOT / rel
            if not p.exists() or sha256(p) != expected:
                errors.append(f"integrity:{rel}")
    except Exception as exc:
        errors.append(f"integrity-parse:{exc}")
    try:
        subprocess.run([sys.executable, "-m", "py_compile", str(ROOT / "scripts/contract_runner.py"), str(ROOT / "scripts/apply_policy_patch.py")], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as exc:
        errors.append(f"python-compile:{exc.stderr}")
    result = {"contract_skill": "ai-native-video-architect-zh", "contract_version": execution.get("contract_version", "UNKNOWN"), "status": "FAIL" if errors else "PASS", "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
