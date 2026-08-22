#!/usr/bin/env python3
"""
migrate_to_okf.py — One-time conversion of the wiki's content pages to the
Open Knowledge Format (OKF) v0.2 (https://github.com/GoogleCloudPlatform/
knowledge-catalog/blob/main/okf/SPEC.md).

Per page, this:
  - Replaces `last_edited`/`edited_by` with OKF's `generated: {by, at}`
  - Adds `title` and `description` (recommended fields)
  - Parses '## Key Sources' (principles/elements/patterns/strategies/theories)
    or '## Evidence' (claims) into an OKF `sources:` frontmatter list
  - Leaves `status` and any extra existing fields (id, evidence_strength,
    author, grain_size) as-is — OKF tolerates extra frontmatter keys
  - Converts every [[wikilink]] in the body to a standard markdown link
    ([Label](/folder/slug.md)), per OKF's cross-linking convention
  - Leaves all other body content untouched

index.md / log.md are NOT touched here — see build_indexes.py / log_revision.py
and the one-off rewrite done for the initial conversion.

Usage:
    python3 scripts/migrate_to_okf.py [--dry-run] [--type principles|elements|...|all]
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib as ok


def first_sentence(text: str, limit: int = 240) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"^`[^`]*`\s*", "", text)  # strip leading `q3 i2`-style codes
    m = re.match(r"(.{10,}?[.!?])(\s|$)", text)
    sentence = m.group(1) if m else text
    if len(sentence) > limit:
        sentence = sentence[: limit - 1].rsplit(" ", 1)[0] + "…"
    return sentence.strip()


def get_intro_paragraph(body: str) -> str | None:
    """For claim pages: the optional 1-2 sentence clarifier between the H1 and the
    first '##' heading."""
    m = re.search(r"^# .+\n(.*?)(?=\n##\s|\Z)", body, re.MULTILINE | re.DOTALL)
    if not m:
        return None
    text = m.group(1).strip()
    return text or None


def dedupe_ids(sources: list) -> list:
    seen = {}
    for src in sources:
        base = src["id"]
        if base in seen:
            seen[base] += 1
            src["id"] = f"{base}-{seen[base]}"
        else:
            seen[base] = 1
    return sources


def build_description(page_type: str, body: str) -> str | None:
    if page_type == "claim":
        intro = get_intro_paragraph(body)
        return first_sentence(intro) if intro else None
    desc_section = ok.get_section(body, "Description")
    if not desc_section or not desc_section.strip():
        return None
    return first_sentence(desc_section)


def build_sources(page_type: str, body: str) -> list:
    if page_type == "claim":
        evidence = ok.get_section(body, "Evidence")
        if not evidence:
            return []
        return dedupe_ids(ok.parse_evidence_sources(evidence))
    key_sources = ok.get_section(body, "Key Sources")
    if not key_sources:
        return []
    return dedupe_ids(ok.parse_key_sources(key_sources))


def migrate_file(path: Path, title_index: dict, dry_run: bool) -> None:
    text = path.read_text(encoding="utf-8")
    lines, body = ok.split_frontmatter(text)
    if not lines:
        print(f"  SKIP (no frontmatter): {path}")
        return
    fm = ok.parse_frontmatter_scalars(lines)
    page_type = fm.get("type", path.parent.name.rstrip("s"))

    new_fm = {}
    new_fm["type"] = fm.get("type", page_type)
    new_fm["title"] = ok.get_title(body, fm, path.stem)
    description = build_description(page_type, body)
    if description:
        new_fm["description"] = description
    new_fm["status"] = fm.get("status", "draft")
    new_fm["generated"] = {
        "by": ok.actor_for(fm.get("edited_by")),
        "at": fm.get("last_edited", ""),
    }
    sources = build_sources(page_type, body)
    if sources:
        new_fm["sources"] = sources

    # Preserve any other pre-existing fields (id, evidence_strength, author, grain_size...)
    handled = {"type", "status", "last_edited", "edited_by", "title"}
    for k, v in fm.items():
        if k not in handled and k not in new_fm:
            new_fm[k] = v

    new_body = ok.convert_wikilinks(body, title_index)
    new_text = ok.dump_frontmatter(new_fm) + new_body

    if dry_run:
        print(f"--- {path} ---")
        print(new_text[:500])
        print()
    else:
        path.write_text(new_text, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--type", default="all", choices=ok.CONTENT_FOLDERS + ["all"])
    parser.add_argument("--limit", type=int, default=None, help="Only process N files (per type), for spot-checking")
    args = parser.parse_args()

    print("Building title index...")
    title_index = ok.build_title_index()
    print(f"  {len(title_index)} entries\n")

    folders = ok.CONTENT_FOLDERS if args.type == "all" else [args.type]
    total = 0
    for folder in folders:
        d = ok.WIKI_ROOT / folder
        files = sorted(p for p in d.glob("*.md") if p.stem != "index")
        if args.limit:
            files = files[: args.limit]
        print(f"[{folder}] {len(files)} files")
        for p in files:
            migrate_file(p, title_index, args.dry_run)
            total += 1
    print(f"\nDone. {total} files {'previewed' if args.dry_run else 'migrated'}.")


if __name__ == "__main__":
    main()
