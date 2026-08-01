from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
PROTECTED = set(yaml.safe_load((ROOT / "constitution/immutable.yaml").read_text(encoding="utf-8"))["protected_paths"])


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def save_yaml(path: Path, data: dict[str, Any]) -> None:
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")


def get_parent(data: dict[str, Any], parts: list[str]) -> tuple[Any, str]:
    cur: Any = data
    for part in parts[:-1]:
        if not isinstance(cur, dict) or part not in cur:
            raise KeyError(".".join(parts))
        cur = cur[part]
    return cur, parts[-1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--policy", required=True)
    ap.add_argument("--patch", required=True)
    args = ap.parse_args()
    policy_path = Path(args.policy)
    patch_path = Path(args.patch)
    policy = load_yaml(policy_path)
    patch = json.loads(patch_path.read_text(encoding="utf-8"))
    schema = json.loads((ROOT / "schemas/policy-patch.schema.json").read_text(encoding="utf-8"))
    errors = list(Draft202012Validator(schema).iter_errors(patch))
    if errors:
        print(json.dumps({"status": "REJECTED", "reason": errors[0].message}, ensure_ascii=False, indent=2))
        return 1
    path = patch["path"]
    allowed = set(policy.get("allowed_patch_paths", []))
    if path not in allowed or any(path == p or path.startswith(p + ".") for p in PROTECTED):
        print(json.dumps({"status": "REJECTED", "reason": "PROTECTED_OR_UNAUTHORIZED_PATH", "path": path}, ensure_ascii=False, indent=2))
        return 1
    parent, leaf = get_parent(policy, path.split("."))
    op = patch["operation"]
    value = patch.get("value")
    if op == "add":
        target = parent.get(leaf)
        if isinstance(target, list):
            if value not in target:
                target.append(value)
        elif isinstance(target, dict) and isinstance(value, dict):
            target.update(value)
        else:
            parent[leaf] = value
    elif op == "replace":
        parent[leaf] = value
    elif op == "remove":
        target = parent.get(leaf)
        if isinstance(target, list) and value in target:
            target.remove(value)
        elif leaf in parent:
            del parent[leaf]
    save_yaml(policy_path, policy)
    history = policy_path.with_name("policy-history.jsonl")
    with history.open("a", encoding="utf-8") as f:
        f.write(json.dumps(patch, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "APPLIED", "path": path, "operation": op}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
