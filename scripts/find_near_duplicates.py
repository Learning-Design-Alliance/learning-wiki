#!/usr/bin/env python3
"""
find_near_duplicates.py — Two-stage LLM scan for near-duplicate wiki pages
within one content type (principles/elements/patterns/strategies/theories/
claims/learner-variables). Built after finding two pairs of near-identical
pages by hand during a filename cleanup (headings_and_highlight_strategy,
blocks_and_legos-maker_spaces_and_fab_labs) — that doesn't scale past a
handful of pages, let alone strategies/'s ~1,629.

Stage 1 (one cheap call): every page's title in this type, sorted so
lexically similar titles land near each other (near-duplicates usually
share distinctive words, so sorting clusters them for the model's
attention), sent in a single prompt. Asks the model to flag GROUPS of
titles that look like they describe the same underlying practice/concept —
a single read-through pass, not an exhaustive pairwise comparison (which
isn't feasible in one prompt at this scale anyway). This is a first-pass
filter: it won't catch every duplicate, but it's cheap enough to re-run
after every ingest batch.

Stage 2 (one call per flagged group): reads each candidate group's full
page content and asks the model to confirm whether they're genuinely
near-duplicates (not just similarly-titled but substantively different
techniques), and if so, which page should stay canonical and what from the
others is worth folding in — the same judgment call already made by hand
for the two pairs above.

This is a reporting tool, not an auto-merge: per this project's convention
that content mergers are a human call, it writes a markdown report for a
human (or a later Claude turn, on explicit request) to act on.

Usage:
    python3 scripts/find_near_duplicates.py --type strategies
    python3 scripts/find_near_duplicates.py --type strategies --limit 200   # test on a subset
    python3 scripts/find_near_duplicates.py --type principles --out report.md
    python3 scripts/find_near_duplicates.py --type strategies --stage1-only  # just see candidate groups
"""

import argparse
import json
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
PAGE_TYPES = ("principles", "elements", "patterns", "strategies", "theories", "claims", "learner-variables")

MODEL_MAP = {
    "sonnet": "claude-sonnet-5",
    "opus": "claude-opus-5",
    "haiku": "claude-haiku-4-5-20251001",
}


def _extract_json(text: str):
    """Minimal fenced-code-block-aware JSON extractor — this script is
    deliberately independent of scripts/eval/jsonutil.py (a much larger
    module built for the eval harness's own JSON-heavy generation format);
    a small local version keeps this tool as self-contained as enrich.py."""
    fence = re.search(r"```(?:json)?\s*(.*?)```", text, re.DOTALL)
    candidate = fence.group(1) if fence else text
    # Prefer whichever of [ or { appears first, then take to the matching last bracket of that kind.
    first_brace, first_bracket = candidate.find("{"), candidate.find("[")
    if first_bracket != -1 and (first_brace == -1 or first_bracket < first_brace):
        start, end_char = first_bracket, "]"
    else:
        start, end_char = first_brace, "}"
    end = candidate.rfind(end_char)
    if start == -1 or end == -1:
        raise ValueError(f"No JSON object/array found in response:\n{text[:500]}")
    return json.loads(candidate[start:end + 1])


def _get_client():
    try:
        import anthropic
    except ImportError:
        print("[ERROR] anthropic package not installed. Run: pip install anthropic", file=sys.stderr)
        sys.exit(1)
    import os
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("[ERROR] ANTHROPIC_API_KEY not set.", file=sys.stderr)
        sys.exit(1)
    return anthropic.Anthropic(api_key=api_key)


def _call(client, model: str, prompt: str, max_tokens: int = 8000) -> str:
    resp = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(block.text for block in resp.content if block.type == "text")


def load_pages(page_type: str, limit: int = None) -> list:
    """Returns [{"slug": ..., "title": ..., "path": Path}, ...] for every
    content page of this type (excludes index.md)."""
    folder = WIKI_ROOT / page_type
    pages = []
    for path in sorted(folder.glob("*.md")):
        if path.stem == "index":
            continue
        text = path.read_text(encoding="utf-8")
        m = re.search(r"^title:\s*(.+)$", text, re.MULTILINE)
        title = m.group(1).strip().strip('"') if m else path.stem.replace("-", " ").title()
        pages.append({"slug": path.stem, "title": title, "path": path})
    if limit:
        pages = pages[:limit]
    return pages


def stage1_find_candidate_groups(pages: list, client, model: str) -> list:
    """Returns [[slug, slug, ...], ...] — groups of >=2 slugs the model
    thinks might describe the same underlying practice/concept."""
    # Sort by a normalized title so near-duplicates (which usually share
    # distinctive words) land adjacent to each other in the list — this
    # doesn't guarantee every real duplicate is adjacent, but it's a cheap
    # way to help a single read-through catch more of them than a random
    # (here: alphabetical-by-slug) order would.
    def _norm(p):
        return re.sub(r"[^a-z0-9\s]", "", p["title"].lower()).strip()

    sorted_pages = sorted(pages, key=_norm)
    listing = "\n".join(f"{p['slug']}: {p['title']}" for p in sorted_pages)

    prompt = f"""Below is every "{sorted_pages[0]['path'].parent.name}" page title in a learning-design wiki, one per line as `slug: Title`, sorted so similar titles are near each other.

Find groups of 2 or more entries that likely describe the SAME underlying practice or concept — not just a similar topic area, but close enough that they'd probably duplicate content if both pages were fully written out (e.g. "Competency-Based Assessment" and "Competency-Based Learning Assessment" almost certainly describe the same thing; "Direct Instruction: Phonics" and "Direct Instruction: Spelling" do NOT, despite sharing a prefix — different content area).

Read through the whole list once. Respond with ONLY a JSON array, no other text:
[{{"slugs": ["slug-a", "slug-b"], "reason": "one sentence on why these look like the same thing"}}, ...]

If you find no likely duplicates, respond with an empty array: []

Titles:
{listing}"""

    raw = _call(client, model, prompt, max_tokens=8000)
    try:
        groups = _extract_json(raw)
    except (ValueError, json.JSONDecodeError) as e:
        print(f"[ERROR] Could not parse stage-1 response as JSON: {e}\n\nRaw response:\n{raw[:2000]}", file=sys.stderr)
        return []
    by_slug = {p["slug"]: p for p in pages}
    result = []
    for g in groups:
        slugs = [s for s in g.get("slugs", []) if s in by_slug]
        if len(slugs) >= 2:
            result.append({"slugs": slugs, "reason": g.get("reason", "")})
    return result


def stage2_confirm_and_recommend(group: dict, by_slug: dict, client, model: str) -> dict:
    """Reads each candidate's full page content and asks the model to
    confirm true duplication and recommend a merge, or reject the
    candidate as a false positive."""
    pages_block = "\n\n---\n\n".join(
        f"### {slug} ###\n{by_slug[slug]['path'].read_text(encoding='utf-8')}"
        for slug in group["slugs"]
    )
    prompt = f"""These wiki pages were flagged as possible near-duplicates (reason given: "{group['reason']}"). Read their full content and decide.

{pages_block}

Respond with ONLY this JSON, no other text:
{{"is_duplicate": true/false, "canonical_slug": "the slug that should stay as the main page, or null if not a duplicate", "reasoning": "2-3 sentences", "fold_in_notes": "what (if anything) from the non-canonical page(s) is worth pulling into the canonical one before deprecating them, or null"}}"""

    raw = _call(client, model, prompt, max_tokens=2000)
    try:
        return _extract_json(raw)
    except (ValueError, json.JSONDecodeError) as e:
        return {"is_duplicate": None, "canonical_slug": None,
                "reasoning": f"[parse error: {e}]", "fold_in_notes": None}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--type", required=True, choices=PAGE_TYPES)
    parser.add_argument("--model", default="sonnet", choices=list(MODEL_MAP))
    parser.add_argument("--limit", type=int, default=None, help="Only scan the first N pages (alphabetical) — for testing")
    parser.add_argument("--stage1-only", action="store_true", help="Skip stage 2 (full-content confirmation); just print candidate groups")
    parser.add_argument("--out", default=None, help="Write the report to this path instead of stdout")
    args = parser.parse_args()

    model = MODEL_MAP[args.model]
    client = _get_client()

    pages = load_pages(args.type, args.limit)
    print(f"Loaded {len(pages)} {args.type} page(s). Running stage 1 (title scan)...", file=sys.stderr)
    groups = stage1_find_candidate_groups(pages, client, model)
    print(f"Stage 1 flagged {len(groups)} candidate group(s).", file=sys.stderr)

    lines = [f"# Near-duplicate scan: {args.type}", "", f"{len(pages)} pages scanned, {len(groups)} candidate group(s) flagged by title.", ""]

    if not groups:
        lines.append("No candidates found.")
    elif args.stage1_only:
        for g in groups:
            lines.append(f"- **{', '.join(g['slugs'])}** — {g['reason']}")
    else:
        by_slug = {p["slug"]: p for p in pages}
        for i, g in enumerate(groups, 1):
            print(f"Stage 2: confirming group {i}/{len(groups)} ({', '.join(g['slugs'])})...", file=sys.stderr)
            verdict = stage2_confirm_and_recommend(g, by_slug, client, model)
            lines.append(f"## {', '.join(g['slugs'])}")
            lines.append(f"- Flagged because: {g['reason']}")
            lines.append(f"- **Confirmed duplicate: {verdict.get('is_duplicate')}**")
            if verdict.get("is_duplicate"):
                lines.append(f"- Recommended canonical page: `{verdict.get('canonical_slug')}`")
                lines.append(f"- Reasoning: {verdict.get('reasoning')}")
                if verdict.get("fold_in_notes"):
                    lines.append(f"- Fold in before deprecating the rest: {verdict['fold_in_notes']}")
            else:
                lines.append(f"- Reasoning (false positive): {verdict.get('reasoning')}")
            lines.append("")

    report = "\n".join(lines)
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"Wrote report to {args.out}", file=sys.stderr)
    else:
        print(report)


if __name__ == "__main__":
    main()
