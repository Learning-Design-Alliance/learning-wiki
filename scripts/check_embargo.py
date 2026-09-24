#!/usr/bin/env python3
"""
check_embargo.py — keep embargoed research out of a public repository.

learning-wiki is PUBLIC. A branch is public the moment it is pushed and a PR
the moment it is opened, whether or not it is ever merged, so an embargo cannot
be kept "in an unmerged PR here". Embargoed work lives in the private
Learning-engineering-research repository until the embargo lifts, and this
script is the tripwire that stops it crossing over by accident: a session with
both repos attached, a file copied across, a finding pasted into a claim page.

It looks for one marker, which the private repo stamps on anything embargoed
(in a header comment, a front-matter field or a banner; anywhere in the text
works). The marker is spelled "LDA-" + "EMBARGO", and it is assembled here
rather than written out so this file does not trip its own check.

A marker cannot catch prose a person retypes from memory; nothing mechanical
can. It catches copying, which is how every leak this repo could have would
most plausibly happen.

It blocks at three points, because CI alone is too late: by the time a CI check
runs, the push it checks is already public.

    Claude Code (every session in this repo, via .claude/settings.json):
        python3 scripts/check_embargo.py --claude-hook
            PreToolUse on Bash (any `git push`) and on the GitHub MCP write
            tools. Exit 2 blocks the call and tells the agent why.

    git, for pushes made by hand (opt-in, once per clone):
        git config core.hooksPath scripts/hooks

    CI backstop (lint.py --type embargo), and by hand:
        python3 scripts/check_embargo.py            # scan tracked files
        python3 scripts/check_embargo.py --range origin/main..HEAD
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKER = "LDA-" + "EMBARGO"

# Files that must name the marker to document it. Nothing else may carry it.
EXEMPT = {"CLAUDE.md", "scripts/check_embargo.py", "scripts/hooks/pre-push"}

MCP_WRITE_TOOLS = {
    "mcp__github__push_files",
    "mcp__github__create_or_update_file",
    "mcp__github__create_pull_request",
    "mcp__github__update_pull_request",
    "mcp__github__add_issue_comment",
    "mcp__github__issue_write",
    "mcp__github__create_repository",
}
PUSH_RE = re.compile(r"\bgit\b[^;&|\n]*\bpush\b")
ZERO_SHA = "0" * 40


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def scan_range(rev_range: str) -> list[str]:
    """Lines ADDED in rev_range that carry the marker, as 'path: line'."""
    hits, path = [], None
    for line in git("diff", "--no-color", "-U0", rev_range).splitlines():
        if line.startswith("+++ "):
            path = line[6:] if line.startswith("+++ b/") else None
        elif line.startswith("+") and path and path not in EXEMPT and MARKER in line:
            hits.append(f"{path}: {line[1:].strip()[:120]}")
    return hits


def scan_tracked() -> list[str]:
    hits = []
    for rel in git("ls-files").splitlines():
        if rel in EXEMPT:
            continue
        try:
            text = (ROOT / rel).read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue  # binaries, and files deleted in the working tree
        if MARKER in text:
            hits.append(rel)
    return hits


def outgoing_base() -> str:
    """What this push adds to: the branch's upstream, else origin/main."""
    for ref in ("@{upstream}", "origin/main"):
        try:
            return git("rev-parse", "--verify", "--quiet", ref).strip()
        except subprocess.CalledProcessError:
            continue
    return ""


def refuse(where: str, hits: list[str]) -> int:
    print(f"BLOCKED: {where} carries the embargo marker ({MARKER}).\n"
          "learning-wiki is public: a pushed branch or an opened PR is visible to anyone, "
          "merged or not. Embargoed research stays in the private Learning-engineering-research "
          "repository until the embargo lifts. Remove it and try again.", file=sys.stderr)
    for h in hits[:20]:
        print(f"  {h}", file=sys.stderr)
    return 2


def claude_hook() -> int:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    tool, tool_input = event.get("tool_name", ""), event.get("tool_input") or {}
    if tool == "Bash":
        if not PUSH_RE.search(tool_input.get("command") or ""):
            return 0
        base = outgoing_base()
        hits = scan_range(f"{base}..HEAD") if base else scan_tracked()
        return refuse("this push", hits) if hits else 0
    if tool in MCP_WRITE_TOOLS:
        payload = json.dumps(tool_input, ensure_ascii=False)
        return refuse(f"this {tool} call", [tool]) if MARKER in payload else 0
    return 0


def pre_push() -> int:
    hits = []
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 4 or parts[1] == ZERO_SHA:  # a branch deletion pushes nothing
            continue
        local_sha, remote_sha = parts[1], parts[3]
        base = remote_sha if remote_sha != ZERO_SHA else outgoing_base()
        hits += scan_range(f"{base}..{local_sha}") if base else scan_tracked()
    return refuse("this push", hits) if hits else 0


def main() -> int:
    args = sys.argv[1:]
    if args == ["--claude-hook"]:
        return claude_hook()
    if args == ["--pre-push"]:
        return pre_push()
    if len(args) == 2 and args[0] == "--range":
        hits = scan_range(args[1])
    elif not args:
        hits = scan_tracked()
    else:
        print(__doc__, file=sys.stderr)
        return 64
    if hits:
        return refuse("the repository" if not args else args[1], hits)
    print(f"embargo: no {MARKER} marker found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
