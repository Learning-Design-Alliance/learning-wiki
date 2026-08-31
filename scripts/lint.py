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
  8. status: stable pages with no `verified` entry — "stable" should mean a human
     actually checked it, not just that it looks finished

Usage:
    python3 scripts/lint.py [--fix] [--type <page_type>]
    --fix   : auto-promote pages that pass all checks from draft → review
"""

import json
import re
import sys
import argparse
import unicodedata
import urllib.parse
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
        # ok.iter_markdown_links matches the destination by paren BALANCE, so
        # a link to a page whose filename contains parentheses is seen. LINK_RE
        # could not see those at all (it stops at the first ')'), and this
        # check openly skipped them — while mkdocs could not resolve them
        # either, so they rendered as dead literal text. 58 such links were
        # live when this was changed, every one pointing at a real file.
        for _, _, target, is_angle in ok.iter_markdown_links(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            # A destination containing parens only parses inside <...>. It may
            # resolve on disk and still be broken in the rendered page, so flag
            # it separately rather than calling it fine.
            if ok.link_needs_angle_brackets(target) and not is_angle:
                issues.append({
                    "file": str(path.relative_to(WIKI_ROOT)),
                    "type": "link_needs_angle_brackets",
                    "detail": f"{target} contains parentheses and must be written as "
                              f"<{target}> to parse — run scripts/fix_links.py --apply",
                })
                continue
            # Percent-decode before hitting the filesystem. A markdown link to
            # a page whose filename contains an apostrophe, a question mark, a
            # comma or a quote MUST encode those characters to be a valid link
            # target, and mkdocs resolves the encoded form correctly — but this
            # check compared the still-encoded string against real filenames and
            # reported every one of them broken. Nine of this wiki's twenty
            # "broken" links were this false positive (the '%27what%27s_my_
            # emotion%3F%27_game_check-in.md' family), all of them links that
            # build fine under `mkdocs build --strict`.
            target_path = (path.parent / urllib.parse.unquote(target)).resolve()
            if not target_path.exists():
                issues.append({
                    "file": str(path.relative_to(WIKI_ROOT)),
                    "type": "broken_link",
                    "detail": f"{target} (from {path.relative_to(WIKI_ROOT)}) not found",
                })
    return issues


# python-markdown's toc extension turns each heading into an anchor with this
# transform, and mkdocs.yml enables `toc` with no custom slugify — so this is
# the id an `### Author Year` heading actually gets in the built site. Kept as
# a local copy rather than importing markdown, because lint.py runs in CI
# *before* the docs dependencies are installed.
def _heading_anchor(heading: str, separator: str = "-") -> str:
    v = unicodedata.normalize("NFKD", heading).encode("ascii", "ignore").decode("ascii")
    v = re.sub(r"[^\w\s-]", "", v).strip().lower()
    return re.sub(r"[%s\s]+" % separator, separator, v)


HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.M)


# attr_list (enabled in mkdocs.yml) lets a heading name its own id:
#     #### A {: #letter-a }
# which overrides the slugified one. build_indexes.py uses this for the A-Z
# jump bars on large section indexes, so a check that ignored it would call
# every one of those jump links dead.
ATTR_ID_RE = re.compile(r"\{:?\s*#([^\s}]+)[^}]*\}\s*$")


def page_anchors(text: str) -> set[str]:
    """Every anchor the built page will expose: explicit attr_list ids, plus
    slugified headings with toc's duplicate suffixes (`foo`, `foo_1`, ...)."""
    anchors, counts = set(), defaultdict(int)
    for h in HEADING_RE.findall(text):
        explicit = ATTR_ID_RE.search(h)
        if explicit:
            anchors.add(explicit.group(1))
            continue
        base = _heading_anchor(h)
        if not base:
            continue
        n = counts[base]
        counts[base] += 1
        anchors.add(base if n == 0 else f"{base}_{n}")
    return anchors


def check_dead_anchors(pages: dict[str, Path]) -> list[dict]:
    """A link's fragment is as capable of being dead as its path, and nothing
    was looking at it. check_broken_links splits the destination at '#' and
    tests only the file; `mkdocs build --strict` downgrades a missing anchor to
    INFO and so does not fail on it either. That is the same blind spot that
    let 118 dead parenthesis links render as literal text for weeks.

    It matters most for claim pages, whose whole subclaim convention is
    `[-> Author Year](#author-year)` pointing at an `### Author Year` heading in
    the same page's ## Evidence section. A subclaim whose anchor does not
    resolve silently stops being traceable to its study."""
    issues, anchor_cache = [], {}

    def anchors_for(path: Path) -> set[str]:
        key = str(path)
        if key not in anchor_cache:
            try:
                anchor_cache[key] = page_anchors(path.read_text(encoding="utf-8"))
            except OSError:
                anchor_cache[key] = set()
        return anchor_cache[key]

    for slug, path in pages.items():
        if "/" in slug or path.name in DOC_FILES:
            continue
        text = path.read_text(encoding="utf-8")
        anchor_cache[str(path)] = page_anchors(text)
        for _, _, target, _ in ok.iter_markdown_links(text):
            if target.startswith(("http://", "https://", "mailto:")) or "#" not in target:
                continue
            file_part, _, frag = target.partition("#")
            if not frag:
                continue
            frag = urllib.parse.unquote(frag)
            if file_part:
                target_path = (path.parent / urllib.parse.unquote(file_part)).resolve()
                if not target_path.exists():
                    continue          # already reported as a broken_link
            else:
                target_path = path
            if frag not in anchors_for(target_path):
                issues.append({
                    "file": str(path.relative_to(WIKI_ROOT)),
                    "type": "dead_anchor",
                    "detail": f"#{frag} -> no such heading in "
                              f"{target_path.name if file_part else 'this page'}",
                })
    return issues


# A conflicted merge leaves these at the start of a line. Anchored to line
# start so a page that legitimately discusses the markers in prose or inside
# a fenced code block (this wiki documents git workflow in places) is not
# flagged for mentioning them mid-sentence.
MERGE_MARKER_RE = re.compile(r"^(<{7}|={7}|>{7})(\s|$)", re.M)


def check_merge_markers(pages: dict[str, Path]) -> list[dict]:
    """Unresolved VCS conflict markers left in a page.

    Nothing was looking for these, and the gap is not theoretical: a
    `git stash pop` on the droplet conflicted in one claim page, and this
    script then reported "Total issues: 0" with `<<<<<<<` sitting in the file.
    A page in that state renders the markers as literal text on the site and
    silently carries both versions of whatever was in conflict.

    The `[Conflicts]` check next door is about competing claims between pages,
    not merge conflicts, which makes its OK line actively misleading here."""
    issues = []
    for slug, path in pages.items():
        if "/" in slug:
            continue
        text = path.read_text(encoding="utf-8")
        hits = MERGE_MARKER_RE.findall(text)
        if hits:
            first = MERGE_MARKER_RE.search(text)
            line_no = text[:first.start()].count("\n") + 1
            issues.append({
                "file": str(path.relative_to(WIKI_ROOT)),
                "type": "merge_conflict_markers",
                "detail": f"{len(hits)} unresolved conflict marker(s), first at line {line_no} "
                          f"— resolve the merge before committing",
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
        # Check for at least one DOI or URL in evidence table.
        #
        # Skipped for status: draft, which CLAUDE.md defines as "skeleton or
        # stub; content not reviewed" — a draft claim having no evidence yet
        # is the expected state, not a defect, and the status field exists to
        # say so. This mirrors the rest of this module:
        # check_draft_no_description only fires on drafts and
        # check_stable_unverified only on stable. The unenriched backlog stays
        # visible — wiki_health_check.py counts every draft and TODO page for
        # the health dashboard — it just doesn't fail CI for pages that are
        # honestly labelled unfinished. A claim promoted to review or stable
        # is held to the full standard again.
        status_m = STATUS_RE.search(text)
        if status_m and status_m.group(1).strip() == "draft":
            continue
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


def check_stable_unverified(pages: dict[str, Path]) -> list[dict]:
    """Flag status: stable pages with no `verified` entry in frontmatter. `evidence_strength`
    is a separate axis (strength of the underlying research) from `verified` (whether a human
    has actually checked THIS page) — a page can be evidence_strength: strong and still be
    entirely unverified."""
    issues = []
    for slug, path in pages.items():
        if "/" in slug:
            continue
        text = path.read_text(encoding="utf-8")
        status_m = STATUS_RE.search(text)
        if not status_m or status_m.group(1).strip() != "stable":
            continue
        if not re.search(r"^verified:\s*$", text, re.MULTILINE):
            issues.append({
                "file": str(path.relative_to(WIKI_ROOT)),
                "type": "stable_unverified",
                "detail": "status: stable but no verified entry — add one via "
                          "log_revision.py --verify once a human has actually checked it",
            })
    return issues


BANNER_LINE_RE = re.compile(r"^>\s*\*\*([^*]+)\*\*\s*·\s*\[[^\]]*\]\(index\.md\)\s*$")

# folder -> (banner label, frontmatter `type` value). Kept in step with
# scripts/add_type_banner.py's TYPE_LABELS, which is what writes them.
BANNER_TYPES = {
    "principles": ("Principle", "principle"),
    "elements": ("Element", "element"),
    "patterns": ("Pattern", "pattern"),
    "strategies": ("Strategy", "strategy"),
    "theories": ("Theory", "theory"),
    "learner-variables": ("Learner Variable", "learner-variable"),
    "claims": ("Claim", "claim"),
}


def check_type_banner(pages: dict[str, Path]) -> list[dict]:
    """Every content page carries a visible page-type banner under its H1
    (see scripts/add_type_banner.py for why: 73 slugs exist in more than
    one type folder, and mkdocs strips frontmatter out of the rendered
    page, so `type:` alone can't tell a reader which section they're in).

    Because that banner duplicates the frontmatter `type` into the body,
    the two can drift — so check all three agree: the banner exists, its
    label matches the folder the page actually lives in, and frontmatter
    `type` matches that folder too. Run
    `python3 scripts/add_type_banner.py --apply` to fix a missing or
    stale banner; a frontmatter/folder mismatch needs a human to decide
    which one is wrong (is this page misfiled, or mislabelled?)."""
    issues = []
    seen = set()
    for slug, path in pages.items():
        if "/" not in slug:
            continue
        folder = slug.split("/", 1)[0]
        if folder not in BANNER_TYPES or path.stem == "index" or path in seen:
            continue
        seen.add(path)
        label, expected_type = BANNER_TYPES[folder]
        rel = str(path.relative_to(WIKI_ROOT))
        text = path.read_text(encoding="utf-8")
        fm_lines, body = ok.split_frontmatter(text)
        declared = (ok.parse_frontmatter_scalars(fm_lines).get("type") or "").strip()

        if declared and declared != expected_type:
            issues.append({"type": "type_folder_mismatch", "file": rel,
                            "detail": f"frontmatter says type: {declared}, but the page is in "
                                      f"{folder}/ — expected {expected_type}"})

        lines = body.split("\n")
        h1_idx = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
        if h1_idx is None:
            issues.append({"type": "no_h1", "file": rel,
                            "detail": "page has no H1 heading, so it carries no type banner either"})
            continue
        scan = h1_idx + 1
        while scan < len(lines) and not lines[scan].strip():
            scan += 1
        m = BANNER_LINE_RE.match(lines[scan].strip()) if scan < len(lines) else None
        if not m:
            issues.append({"type": "missing_type_banner", "file": rel,
                            "detail": "no page-type banner under the H1 — run "
                                      "scripts/add_type_banner.py --apply"})
        elif m.group(1).strip() != label:
            issues.append({"type": "wrong_type_banner", "file": rel,
                            "detail": f"banner says '{m.group(1).strip()}' but the page is in "
                                      f"{folder}/ — expected '{label}'"})
    return issues


def check_manifest_integrity(pages: dict[str, Path]) -> list[dict]:
    """Validate sources/manifest.ndjson — every line must parse as JSON with the
    required fields for its status, per CLAUDE.md's Source Manifest schema."""
    issues = []
    manifest_path = WIKI_ROOT / "sources" / "manifest.ndjson"
    if not manifest_path.exists():
        return issues
    rel = str(manifest_path.relative_to(WIKI_ROOT))
    for lineno, line in enumerate(manifest_path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError as e:
            issues.append({"file": rel, "type": "manifest_invalid_json", "detail": f"line {lineno}: {e}"})
            continue
        missing = [k for k in ("id", "title", "status", "reviewed_at") if k not in entry]
        if missing:
            issues.append({"file": rel, "type": "manifest_missing_field",
                            "detail": f"line {lineno} ({entry.get('id', '?')}): missing {missing}"})
        if entry.get("status") not in ("ingested", "rejected"):
            issues.append({"file": rel, "type": "manifest_bad_status",
                            "detail": f"line {lineno} ({entry.get('id', '?')}): status={entry.get('status')!r}"})
        elif entry["status"] == "ingested" and not entry.get("pages"):
            issues.append({"file": rel, "type": "manifest_ingested_no_pages",
                            "detail": f"line {lineno} ({entry.get('id', '?')}): status=ingested but no pages"})
        elif entry["status"] == "rejected" and not entry.get("reason"):
            issues.append({"file": rel, "type": "manifest_rejected_no_reason",
                            "detail": f"line {lineno} ({entry.get('id', '?')}): status=rejected but no reason"})
    return issues


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


def check_authority_conflicts(pages: dict[str, Path]) -> list[dict]:
    """Citations that contradict a verdict a human recorded in
    sources/authorities.ndjson.

    This is the ratchet. Repairing the pages alone does not survive the next
    enrichment batch — the model that invented a DOI for a book once will
    invent one again, and nothing in the corpus remembers that a person
    already established there is none. An authority is that memory, and this
    check is what gives it teeth: once ambrose-2010 is recorded, a
    reintroduced DOI fails CI rather than sitting on the page looking
    verified."""
    issues = []
    try:
        import authorities as au
        import check_citations as cc
    except Exception:
        return issues
    try:
        auth = au.load_authorities()
    except ValueError as e:
        return [{"type": "malformed_authority", "file": "sources/authorities.ndjson",
                 "detail": str(e)}]
    if not auth:
        return issues
    by_key = cc.load_all_citations()
    for key, entry in auth.items():
        for c in by_key.get(key, []):
            for why in au.contradictions(entry, c):
                issues.append({"type": "contradicts_authority", "file": c["source"],
                               "detail": why})
    return issues


def main():
    parser = argparse.ArgumentParser(description="Lint the ld-wiki")
    parser.add_argument("--fix", action="store_true", help="Auto-promote clean draft pages to review")
    parser.add_argument("--type", choices=["broken_links", "dead_anchors", "merge_markers", "drafts", "claims", "principles", "conflicts", "trust", "manifest", "type_banner", "authorities", "all"],
                        default="all", help="Which checks to run")
    args = parser.parse_args()

    print(f"Scanning {WIKI_ROOT} ...\n")
    pages = all_pages()
    print(f"  {len([s for s in pages if '/' not in s])} pages indexed\n")

    all_issues = []
    checks = {
        "broken_links":  check_broken_links,
        "dead_anchors":  check_dead_anchors,
        "merge_markers": check_merge_markers,
        "drafts":        check_draft_no_description,
        "claims":        check_claims_missing_evidence,
        "principles":    check_principles_missing_claims,
        "competing":     check_unfilled_competing_claims,
        "conflicts":     check_open_conflicts,
        "trust":         check_stable_unverified,
        "manifest":      check_manifest_integrity,
        "type_banner":   check_type_banner,
        "authorities":   check_authority_conflicts,
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
