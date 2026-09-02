#!/usr/bin/env python3
"""
sync_evidence_codes.py — mirror each evidence entry's q/i/n into frontmatter.

The `q3 i2` shorthand was designed so an *agent* could weigh a study at a
glance. Until now it existed only in prose, so an agent had to parse a code
span out of a markdown body to get at it — which is the one thing frontmatter
exists to avoid.

`sources[]` already mirrors the `## Evidence` section one entry per study,
keyed by the same anchor slug the subclaim links use. So the codes go there,
beside the citation they describe, rather than into a parallel structure that
could fall out of step with it:

    sources:
      - id: haak-et-al-2011
        resource: https://doi.org/10.1126/science.1204820
        title: "Haak, D. C., … (2011). Increased structure and active learning…"
        author: Haak, D. C.
        q: 3
        i: 2
        n: large (multiple course sections at a research university)

What the codes *mean* is in `evidence-scales.json` at the bundle root — said
once, as data, rather than 143 times. That file is also what
`docs_hooks/page_metadata.py` renders for human readers, so the agent's
definition and the reader's cannot drift apart.

Subclaim prefixes are deliberately not mirrored. A subclaim's `q3 i2` is a
*reading* of the evidence entry it links to, and that entry already carries
the codes; duplicating them into frontmatter would create a second place for
them to disagree with no way to tell which was right.

    python3 scripts/sync_evidence_codes.py --check
    python3 scripts/sync_evidence_codes.py --apply
"""

import argparse
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import okf_lib as ok


def frontmatter_parses(text: str) -> bool:
    """Would this page's frontmatter load as YAML? Used as a write gate."""
    m = ok.FRONTMATTER_RE.match(text)
    if not m:
        return False
    try:
        import yaml
        return isinstance(yaml.safe_load(m.group(1)), dict)
    except Exception:
        return False


SOURCES_BLOCK_RE = re.compile(r"^sources:\n(?:[ \t]+[^\n]*\n)*", re.M)


def render_sources(srcs: list) -> str:
    """Just the `sources:` block, borrowing dump_frontmatter's own renderer.

    Reusing it rather than re-implementing keeps one spelling of the block, so
    a field added there appears here without a second edit."""
    block = ok.dump_frontmatter({"sources": srcs})
    return "\n".join(block.split("\n")[1:-2]) + "\n"


def replace_sources_block(text: str, srcs: list):
    """Swap the page's `sources:` block, leaving every other byte untouched.

    A surgical edit, not a rebuild. The obvious implementation —
    parse_frontmatter_scalars, add sources, dump_frontmatter — silently
    destroys the page: that parser is scalar-only, so it flattens
    `generated:` (a nested by/at mapping) to an empty string and drops
    `verified:` entirely, and rewriting from it would erase the provenance of
    103 pages. It happens to raise a TypeError instead, which is luck rather
    than safety.

    So the only thing this touches is the block it owns."""
    m = ok.FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm, rest = m.group(1), text[m.end():]
    rendered = render_sources(srcs)
    if SOURCES_BLOCK_RE.search(fm):
        fm_new = SOURCES_BLOCK_RE.sub(rendered, fm, count=1)
    else:
        fm_new = fm.rstrip("\n") + "\n" + rendered
    # FRONTMATTER_RE's group excludes the closing newline, so a block replaced
    # anywhere but the end leaves fm_new without one and the closing `---`
    # glues onto the last key: `evidence_strength: moderate---`. That broke 92
    # pages, and the single-page test missed it because that page happened to
    # take the append branch, which ends in a newline by construction.
    fm_new = fm_new.rstrip("\n") + "\n"
    return f"---\n{fm_new}---\n{rest}"


def page_codes(path: Path):
    """[(anchor_id, {q,i,n}), ...] read from the page's ## Evidence section."""
    fm_lines, body = ok.split_frontmatter(path.read_text(encoding="utf-8"))
    section = ok.get_section(body, "Evidence")
    if not section:
        return []
    return [(s["id"], {k: s[k] for k in ("q", "i", "n") if k in s})
            for s in ok.parse_evidence_sources(section)]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    pages = [p for p in sorted((WIKI_ROOT / "claims").glob("*.md")) if p.stem != "index"]
    entries = coded = pages_touched = 0
    for path in pages:
        codes = page_codes(path)
        if not codes:
            continue
        entries += len(codes)
        n = sum(1 for _, c in codes if c)
        coded += n
        if n:
            pages_touched += 1

    print(f"{len(pages)} claim page(s); {entries} evidence entr(y/ies); "
          f"{coded} carry q/i/n ({100 * coded / entries:.0f}%) across "
          f"{pages_touched} page(s).")

    if args.check:
        print("\nRewriting frontmatter is done by the ingest/enrich path that owns "
              "these pages\n(okf_lib.parse_evidence_sources now captures the codes, so "
              "any page rebuilt\nthrough dump_frontmatter carries them). --apply "
              "backfills the pages that\nalready exist.")
        return

    written = 0
    skipped: list = []
    for path in pages:
        text = path.read_text(encoding="utf-8")
        _, body = ok.split_frontmatter(text)
        section = ok.get_section(body, "Evidence")
        if not section:
            continue
        srcs = ok.parse_evidence_sources(section)
        if not any(any(k in s for k in ("q", "i", "n")) for s in srcs):
            continue
        new_text = replace_sources_block(text, srcs)
        if not new_text or new_text == text:
            continue
        # Never write frontmatter that does not parse. This edits YAML by
        # string surgery, which is the right call — rebuilding through
        # parse_frontmatter_scalars silently flattens `generated:` and drops
        # `verified:` — but string surgery on YAML earns a parse check, not
        # trust. The first version of this shipped a glued closing delimiter to
        # 92 pages; lint caught it only because it also broke the type banner.
        if not frontmatter_parses(new_text):
            skipped.append(str(path.relative_to(WIKI_ROOT)))
            continue
        path.write_text(new_text, encoding="utf-8")
        written += 1
    print(f"\nWrote codes into frontmatter on {written} page(s).")
    if skipped:
        print(f"{len(skipped)} page(s) NOT written — the result would not have parsed "
              f"as YAML:")
        for rel in skipped[:10]:
            print(f"      {rel}")


if __name__ == "__main__":
    main()
