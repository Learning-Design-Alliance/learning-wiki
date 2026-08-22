#!/usr/bin/env python3
"""
lint.py — Health-check the ld-wiki.

Checks:
  1. Broken cross-links (/folder/slug.md link target not found)
  2. Claims pages missing evidence strength
  3. Claims pages missing a source with DOI/URL
  4. Principles missing at least one claim link
  5. Pages with status: draft and no description (empty or <!-- TODO -->)
  6. Unfilled ## Competing Claims sections on claim pages
  7. Conflict markers (<!-- CONFLICT: ... -->) — lists open conflicts for review

Usage:
    python3 scripts/lint.py [--fix] [--type <page_type>]
    --fix   : auto-promote pages that pass all checks from draft → review
"""

import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib as ok

WIKI_ROOT = Path(__file__).parent.parent

PAGE_TYPES = ["principles", "elements", "patterns", "strategies", "theories", "claims", "sources"]

# OKF cross-links are plain relative markdown links: [Label](slug.md) or
# [Label](../folder/slug.md). Excludes parens-containing targets (e.g. a slug like
# "project-based_learning_(pbl).md") — a handful of known-good links with literal
# parentheses in the filename aren't matched; a narrower regex isn't worth the risk
# of merging adjacent links on the same line.
LINK_RE   = re.compile(r"\]\(([^)\s]+\.md)\)")
STATUS_RE = re.compile(r"^status:\s*(.+)$", re.MULTILINE)
DESC_RE   = re.compile(r"## Description\s*\n(.+?)(?=\n##|\Z)", re.DOTALL)


def all_pages() -> dict[str, Path]:
    """Return {slug_or_path: Path} for every .md page in the wiki."""
    pages = {}
    for page_type in PAGE_TYPES:
        folder = WIKI_ROOT / page_type
        for p in folder.glob("*.md"):
            pages[p.stem] = p
            pages[f"{page_type}/{p.stem}"] = p
    # Also root-level pages
    for p in WIKI_ROOT.glob("*.md"):
        pages[p.stem] = p
    return pages


DOC_FILES = {"CLAUDE.md", "README.md"}  # contain illustrative example paths, not real links


def check_broken_links(pages: dict[str, Path]) -> list[dict]:
    issues = []
    for slug, path in pages.items():
        if "/" in slug:
            continue  # skip duplicates (folder-qualified keys)
        if path.name in DOC_FILES:
            continue
        text = path.read_text(encoding="utf-8")
        for m in LINK_RE.finditer(text):
            target = m.group(1)
            if target.startswith(("http://", "https://")):
                continue
            target_path = (path.parent / target).resolve()
            if not target_path.exists():
                issues.append({
                    "file": str(path.relative_to(WIKI_ROOT)),
                    "type": "broken_link",
                    "detail": f"{target} (from {path.relative_to(WIKI_ROOT)}) not found",
                })
    return issues


def check_draft_no_description(pages: dict[str, Path]) -> list[dict]:
    issues = []
    for slug, path in pages.items():
        if "/" in slug:
            continue
        text = path.read_text(encoding="utf-8")
        status_m = STATUS_RE.search(text)
        if not status_m or status_m.group(1).strip() != "draft":
            continue
        desc_m = DESC_RE.search(text)
        if not desc_m:
            continue
        desc_body = desc_m.group(1).strip()
        if not desc_body or "<!-- TODO" in desc_body:
            issues.append({
                "file": str(path.relative_to(WIKI_ROOT)),
                "type": "draft_no_description",
                "detail": "status: draft but description is empty or TODO",
            })
    return issues


def check_claims_missing_evidence(pages: dict[str, Path]) -> list[dict]:
    issues = []
    claims_folder = WIKI_ROOT / "claims"
    if not claims_folder.exists():
        return issues
    for path in claims_folder.glob("*.md"):
        if path.stem == "index":
            continue
        text = path.read_text(encoding="utf-8")
        # Check evidence strength in frontmatter
        if not re.search(r"evidence_strength:\s*\S+", text):
            issues.append({
                "file": str(path.relative_to(WIKI_ROOT)),
                "type": "claim_no_evidence_strength",
                "detail": "evidence_strength missing from frontmatter",
            })
        # Check for at least one DOI or URL in evidence table
        evidence_section = ok.get_section(text, "Evidence")
        if evidence_section is not None:
            if not re.search(r"https?://|doi\.org|10\.\d{4}", evidence_section):
                issues.append({
                    "file": str(path.relative_to(WIKI_ROOT)),
                    "type": "claim_no_doi",
                    "detail": "Evidence section has no DOI or URL",
                })
    return issues


def check_principles_missing_claims(pages: dict[str, Path]) -> list[dict]:
    issues = []
    principles_folder = WIKI_ROOT / "principles"
    if not principles_folder.exists():
        return issues
    for path in principles_folder.glob("*.md"):
        if path.stem == "index":
            continue
        text = path.read_text(encoding="utf-8")
        if "### Claims" not in text and "## Claims" not in text:
            continue
        # Find the claims section content
        claims_section = re.search(
            r"#{2,3} Claims\s*\n(.+?)(?=\n#{2,3}|\Z)", text, re.DOTALL
        )
        if not claims_section:
            continue
        body = claims_section.group(1).strip()
        has_real_link = bool(re.search(r"\]\((?:\.\./)?claims/", body))
        has_todo = "<!-- TODO" in body
        if not has_real_link and (has_todo or not body):
            issues.append({
                "file": str(path.relative_to(WIKI_ROOT)),
                "type": "principle_no_claim_link",
                "detail": "Principle has no linked claim pages",
            })
    return issues


def check_unfilled_competing_claims(pages: dict[str, Path]) -> list[dict]:
    issues = []
    claims_folder = WIKI_ROOT / "claims"
    if not claims_folder.exists():
        return issues
    for path in claims_folder.glob("*.md"):
        if path.stem == "index":
            continue
        text = path.read_text(encoding="utf-8")
        section = ok.get_section(text, "Competing Claims")
        if section is None:
            continue
        section = section.strip()
        if not section or "<!-- TODO" in section or section == "-":
            issues.append({
                "file": str(path.relative_to(WIKI_ROOT)),
                "type": "competing_claims_unfilled",
                "detail": "## Competing Claims is empty — check literature for contradicting findings",
            })
    return issues


def check_open_conflicts(pages: dict[str, Path]) -> list[dict]:
    """Find <!-- CONFLICT: ... --> markers anywhere in the wiki."""
    conflicts = []
    conflict_re = re.compile(r"<!--\s*CONFLICT:\s*(.+?)-->", re.DOTALL)
    for slug, path in pages.items():
        if "/" in slug:
            continue
        text = path.read_text(encoding="utf-8")
        for m in conflict_re.finditer(text):
            conflicts.append({
                "file": str(path.relative_to(WIKI_ROOT)),
                "type": "open_conflict",
                "detail": m.group(1).strip(),
            })
    return conflicts


def auto_promote(pages: dict[str, Path], all_issues: list[dict], dry_run: bool = False) -> int:
    """Promote draft pages with no issues to status: review."""
    issue_files = {i["file"] for i in all_issues}
    promoted = 0
    for slug, path in pages.items():
        if "/" in slug:
            continue
        rel = str(path.relative_to(WIKI_ROOT))
        if rel in issue_files:
            continue
        text = path.read_text(encoding="utf-8")
        if "status: draft" not in text:
            continue
        new_text = text.replace("status: draft", "status: review", 1)
        if not dry_run:
            path.write_text(new_text, encoding="utf-8")
        promoted += 1
    return promoted


def main():
    parser = argparse.ArgumentParser(description="Lint the ld-wiki")
    parser.add_argument("--fix", action="store_true", help="Auto-promote clean draft pages to review")
    parser.add_argument("--type", choices=["broken_links", "drafts", "claims", "principles", "conflicts", "all"],
                        default="all", help="Which checks to run")
    args = parser.parse_args()

    print(f"Scanning {WIKI_ROOT} ...\n")
    pages = all_pages()
    print(f"  {len([s for s in pages if '/' not in s])} pages indexed\n")

    all_issues = []
    checks = {
        "broken_links":  check_broken_links,
        "drafts":        check_draft_no_description,
        "claims":        check_claims_missing_evidence,
        "principles":    check_principles_missing_claims,
        "competing":     check_unfilled_competing_claims,
        "conflicts":     check_open_conflicts,
    }

    selected = list(checks.keys()) if args.type == "all" else [args.type]

    for check_name, fn in checks.items():
        if check_name not in selected and args.type != "all":
            continue
        issues = fn(pages)
        all_issues.extend(issues)
        label = check_name.replace("_", " ").title()
        if issues:
            print(f"[{label}] {len(issues)} issues:")
            by_type = defaultdict(list)
            for i in issues:
                by_type[i["type"]].append(i)
            for itype, group in by_type.items():
                print(f"  {itype}: {len(group)}")
                for item in group[:5]:
                    print(f"    {item['file']}: {item['detail']}")
                if len(group) > 5:
                    print(f"    ... and {len(group) - 5} more")
        else:
            print(f"[{label}] OK")
        print()

    print(f"Total issues: {len(all_issues)}")

    if args.fix and all_issues:
        promoted = auto_promote(pages, all_issues)
        print(f"\nAuto-promoted {promoted} clean draft pages → review")
    elif args.fix:
        promoted = auto_promote(pages, all_issues)
        print(f"\nAuto-promoted {promoted} pages → review (all pages were clean!)")

    sys.exit(0 if not all_issues else 1)


if __name__ == "__main__":
    main()
