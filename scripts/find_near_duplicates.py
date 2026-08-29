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
    python3 scripts/find_near_duplicates.py --type strategies --provider openrouter  # cheaper (GLM)
    python3 scripts/find_near_duplicates.py --cross-folder --out cross-folder-report.md
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))  # for scripts.eval (openrouter_client, model_catalog)

WIKI_ROOT = Path(__file__).parent.parent
PAGE_TYPES = ("principles", "elements", "patterns", "strategies", "theories", "claims", "learner-variables")

MODEL_MAP = {
    "sonnet": "claude-sonnet-5",
    "opus": "claude-opus-5",
    "haiku": "claude-haiku-4-5-20251001",
}

# --provider openrouter: any OpenRouter model slug works via --model, not just
# this — see enrich.py's OPENROUTER_DEFAULT_MODEL comment for why this is the
# only GLM slug to trust without re-confirming against OpenRouter's own list.
OPENROUTER_DEFAULT_MODEL = "z-ai/glm-5.3-flash"


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


def _get_client(provider: str = "anthropic"):
    """For provider="openrouter", the "client" is just the API key (a plain
    str) — _call() below dispatches on that, so stage1/stage2 don't need to
    know or care which provider they're talking to."""
    import os
    if provider == "openrouter":
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            print("[ERROR] OPENROUTER_API_KEY not set.", file=sys.stderr)
            sys.exit(1)
        return api_key

    try:
        import anthropic
    except ImportError:
        print("[ERROR] anthropic package not installed. Run: pip install anthropic", file=sys.stderr)
        sys.exit(1)
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("[ERROR] ANTHROPIC_API_KEY not set.", file=sys.stderr)
        sys.exit(1)
    return anthropic.Anthropic(api_key=api_key)


def _call(client, model: str, prompt: str, max_tokens: int = 8000) -> str:
    if isinstance(client, str):  # OpenRouter: client is just the API key
        from scripts.eval import openrouter_client, model_catalog
        gen = openrouter_client.generate(
            model, None, prompt, client, max_tokens=max_tokens,
            disable_reasoning=model_catalog.needs_reasoning_disabled(model),
            reasoning_effort=model_catalog.reasoning_effort_for(model),
        )
        return gen.raw_text

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


def stage2_confirm_cross_folder(slug: str, folders: list, client, model: str) -> dict:
    """Same judgment call as stage2_confirm_and_recommend, but for pages that
    share the exact same slug across different OKF type folders (found by
    find_cross_folder_duplicates.py) rather than similar-but-different slugs
    within one folder. This wiki's schema legitimately lets a principle, an
    element, a pattern, and a theory share a name while covering different
    facets of one concept — so an exact-slug match is NOT automatically a
    duplicate the way a title-similarity match usually is; it needs the same
    full-content read before concluding anything."""
    pages_block = "\n\n---\n\n".join(
        f"### {folder}/{slug} ###\n{(WIKI_ROOT / folder / f'{slug}.md').read_text(encoding='utf-8')}"
        for folder in folders
    )
    prompt = f"""These wiki pages share the exact same slug ("{slug}") but are filed under different content types: {', '.join(folders)}.

This wiki's schema allows a principle, element, pattern, strategy, or theory to legitimately share a name while covering a genuinely different facet of one concept — e.g. a theory explaining the mechanism, a principle recommending its use, an element describing the instructional component that enacts it, a pattern showing a lesson-level design built on it. Sharing a slug is not by itself evidence of duplication.

Read the full pages and decide: are these (a) legitimately distinct pages that happen to share a name — different content, different lens, both worth keeping — or (b) actual duplicates, where two or more say substantially the same thing under different type labels and should be merged?

{pages_block}

Respond with ONLY this JSON, no other text:
{{"is_duplicate": true/false, "canonical_folder": "the folder that should stay if duplicate, or null", "reasoning": "2-3 sentences", "fold_in_notes": "what (if anything) from the non-canonical page(s) is worth pulling into the canonical one before deprecating them, or null"}}"""

    raw = _call(client, model, prompt, max_tokens=2000)
    try:
        return _extract_json(raw)
    except (ValueError, json.JSONDecodeError) as e:
        return {"is_duplicate": None, "canonical_folder": None,
                "reasoning": f"[parse error: {e}]", "fold_in_notes": None}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--type", choices=PAGE_TYPES,
                        help="Required unless --cross-folder is given")
    parser.add_argument("--cross-folder", action="store_true",
                        help="Instead of a title scan within one --type, confirm/reject every "
                             "exact-slug collision across type folders (see "
                             "find_cross_folder_duplicates.py) via stage 2's content judgment. "
                             "Skips stage 1 entirely — an exact slug match is already a stronger "
                             "signal than a title-similarity guess.")
    parser.add_argument("--provider", default="anthropic", choices=["anthropic", "openrouter"],
                        help="API provider (default: anthropic)")
    parser.add_argument("--model", default=None,
                        help="anthropic: sonnet (default)|opus|haiku  openrouter: any OpenRouter "
                             f"model slug (default: {OPENROUTER_DEFAULT_MODEL})")
    parser.add_argument("--limit", type=int, default=None, help="Only scan the first N pages (alphabetical) — for testing")
    parser.add_argument("--stage1-only", action="store_true", help="Skip stage 2 (full-content confirmation); just print candidate groups")
    parser.add_argument("--out", default=None, help="Write the report to this path instead of stdout")
    args = parser.parse_args()

    if not args.cross_folder and not args.type:
        parser.error("--type is required unless --cross-folder is given")

    if args.provider == "openrouter":
        model = args.model or OPENROUTER_DEFAULT_MODEL
    else:
        model = MODEL_MAP[args.model or "sonnet"]
    client = _get_client(args.provider)

    if args.cross_folder:
        import find_cross_folder_duplicates as fcfd
        collisions = fcfd.find_collisions()
        if args.limit:
            collisions = dict(list(collisions.items())[:args.limit])
        self_referential = fcfd.find_self_referential(collisions)
        needs_llm = {s: f for s, f in collisions.items() if s not in self_referential}
        print(f"Found {len(collisions)} cross-folder slug collision(s): "
              f"{len(self_referential)} resolved deterministically (self-referential link), "
              f"{len(needs_llm)} need a content judgment.", file=sys.stderr)

        lines = [f"# Cross-folder duplicate scan", "",
                 f"{len(collisions)} slug(s) filed under more than one folder "
                 f"({len(self_referential)} resolved deterministically, {len(needs_llm)} judged by {model}).", ""]

        for slug, links in self_referential.items():
            folders = collisions[slug]
            link_desc = ", ".join(f"{a} links to {b}" for a, b in links)
            lines.append(f"## {slug} ({', '.join(folders)})")
            lines.append(f"- **Confirmed duplicate: True** (deterministic — no LLM call)")
            lines.append(f"- Reasoning: a page here links to another folder's copy of itself ({link_desc}), "
                          f"which is only possible if it's a thin stub restating the other rather than "
                          f"genuinely distinct content.")
            lines.append("")

        for i, (slug, folders) in enumerate(needs_llm.items(), 1):
            print(f"Confirming {i}/{len(needs_llm)}: {slug} ({', '.join(folders)})...", file=sys.stderr)
            verdict = stage2_confirm_cross_folder(slug, folders, client, model)
            lines.append(f"## {slug} ({', '.join(folders)})")
            lines.append(f"- **Confirmed duplicate: {verdict.get('is_duplicate')}**")
            if verdict.get("is_duplicate"):
                lines.append(f"- Recommended canonical folder: `{verdict.get('canonical_folder')}`")
                lines.append(f"- Reasoning: {verdict.get('reasoning')}")
                if verdict.get("fold_in_notes"):
                    lines.append(f"- Fold in before deprecating the rest: {verdict['fold_in_notes']}")
            else:
                lines.append(f"- Reasoning: {verdict.get('reasoning')}")
            lines.append("")

        report = "\n".join(lines)
        if args.out:
            Path(args.out).write_text(report, encoding="utf-8")
            print(f"Wrote report to {args.out}", file=sys.stderr)
        else:
            print(report)
        return

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
