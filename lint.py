#!/usr/bin/env python3
"""Check whether conventional commit intent matches changed files and evidence."""
import argparse
import json
from pathlib import Path


def lint(commit):
    subject = commit.get("subject", "")
    kind = subject.split(":", 1)[0].replace("!", "")
    files = commit.get("files", [])
    issues = []
    code = any(not path.endswith((".md", ".txt")) for path in files)
    if kind == "docs" and code: issues.append("docs-contains-code")
    if kind in {"fix", "feat"} and not commit.get("tests"): issues.append("change-without-tests")
    if commit.get("breaking_api") and "!" not in subject: issues.append("breaking-change-not-marked")
    if kind == "chore" and any(path.startswith("src/") for path in files): issues.append("chore-changes-product-code")
    return {"ok": not issues, "issues": issues, "type": kind}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("commit")
    args = parser.parse_args()
    report = lint(json.loads(Path(args.commit).read_text()))
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
