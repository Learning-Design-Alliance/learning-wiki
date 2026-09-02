#!/usr/bin/env python3
"""
build_wiki_index.py — the resolution table the design-spec side reads.

learning-design-spec now points at this wiki instead of restating it: a profile
carries `realizes: <pattern-slug>`, a method carries `realizes: <strategy-slug>`,
a pattern plan names `element: <slug>`, a design section cites
`research:<claim-slug>`, and `spec/learners.md` requires every learner dimension
to be a `learner-variables/` slug.

That repo checks the *shape* of those fields and cannot check what they name,
because it has to stay usable without a wiki checkout. So today a typo'd
`realizes:` passes CI, ships, and fails silently in front of a course author.
This file is what closes that: id, type and title for every content page,
committed, so the spec repo can resolve a slug in its own CI with no wiki
present — the same arrangement as `reverse-index.json`, and the same reason.

Two things it carries that a naive dump would not:

**Aliases.** A rename is only non-breaking if the retired slug still resolves,
and this file is where the spec side learns that `4cid` means
`4cid-four-component-instructional-design`. An index of current slugs only
would make every rename a silent break on the consuming side — precisely the
failure `aliases:` exists to prevent, reintroduced one repo over.

**A precomputed `resolve` map, per kind.** `pages` already carries id and
aliases, so the map is derivable — but derivable by each consumer, separately,
possibly differently. Ids and aliases share one namespace *per kind*
(CLAUDE.md, "Page identity"), which is a rule a second implementation can get
wrong. Emitting the resolution once means every consumer resolves identically,
and a collision is caught here, at build time, by the side that can fix it.
Both halves come out of one pass, so they cannot drift from each other.

Every content kind is included, theories among them, even though the spec
addresses no theory today: a consumer filters by `type` for free, and a kind
left out is a kind nobody can point at until somebody notices.

    python3 scripts/build_wiki_index.py            # write wiki-index.json
    python3 scripts/build_wiki_index.py --check    # is the committed copy current?
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib
import page_identity as pid

WIKI_ROOT = Path(__file__).parent.parent
OUT_PATH = WIKI_ROOT / "wiki-index.json"

# folder -> the `type:` value a page in it carries. The folder is what actually
# determines a page's kind (see add_type_banner.py); frontmatter `type` is the
# mirror, and lint's check_type_banner fails when the two disagree.
KINDS = {
    "principles": "principle",
    "elements": "element",
    "patterns": "pattern",
    "strategies": "strategy",
    "processes": "process",
    "methods": "method",
    "theories": "theory",
    "learner-variables": "learner-variable",
    "claims": "claim",
}

# Kept per page when present. Deliberately short: this is a resolution table,
# not a mirror of the wiki. `grain_size` earns its place because a profile
# realizing a pattern cares whether that pattern is a lesson or a course.
EXTRA_FIELDS = ("status", "grain_size", "evidence_strength")


def build() -> tuple[dict, list]:
    """Returns (index, collisions). A collision is a slug claimed twice within
    one kind — by two ids, an id and an alias, or two aliases. Filenames are
    unique by construction, so only the alias namespace can produce one, which
    is exactly the case lint's identity check exists for."""
    pages, resolve, collisions = [], {}, []

    for folder, kind in KINDS.items():
        directory = WIKI_ROOT / folder
        if not directory.is_dir():
            continue
        resolve[kind] = {}
        for path in sorted(directory.glob("*.md")):
            if path.stem == "index":
                continue
            text = path.read_text(encoding="utf-8")
            fm_text, _ = pid.split_fm(text)
            fm_lines, body = okf_lib.split_frontmatter(text)
            fm = okf_lib.parse_frontmatter_scalars(fm_lines)

            # The id follows the filename. `id:` in frontmatter is the declared
            # copy and lint requires the two to agree; where they somehow do
            # not, the filename is what a link and a URL actually resolve to.
            slug = path.stem
            aliases = pid.read_aliases(fm_text or "")

            entry = {
                "id": slug,
                "type": kind,
                "title": okf_lib.get_title(body, fm, slug),
                "description": fm.get("description", ""),
                "path": f"{folder}/{path.name}",
            }
            if aliases:
                entry["aliases"] = aliases
            for key in EXTRA_FIELDS:
                if fm.get(key):
                    entry[key] = fm[key]
            pages.append(entry)

            for name in [slug, *aliases]:
                if name in resolve[kind] and resolve[kind][name] != slug:
                    collisions.append(
                        f"{kind}: {name!r} is claimed by both "
                        f"{resolve[kind][name]!r} and {slug!r}")
                    continue
                resolve[kind][name] = slug

    index = {
        "note": ("Resolution table for learning-design-spec: every content page's "
                 "id, kind and title, plus every retired slug that still resolves. "
                 "Built by scripts/build_wiki_index.py; committed because the "
                 "consuming repo has no wiki checkout."),
        "okf_version": "0.2",
        "kinds": sorted(set(KINDS.values())),
        "counts": {kind: sum(1 for p in pages if p["type"] == kind)
                   for kind in sorted(set(KINDS.values()))},
        "resolve": {k: dict(sorted(v.items())) for k, v in sorted(resolve.items())},
        "pages": sorted(pages, key=lambda p: (p["type"], p["id"])),
    }
    return index, collisions


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if the committed wiki-index.json is not what a "
                         "rebuild would produce")
    args = ap.parse_args()

    index, collisions = build()
    if collisions:
        # Never write a table that resolves one slug two ways: a consumer would
        # pick whichever it saw last and be confidently wrong.
        print(f"{len(collisions)} slug collision(s) — refusing to write "
              f"{OUT_PATH.name}:", file=sys.stderr)
        for c in collisions:
            print(f"  {c}", file=sys.stderr)
        print("Run: python3 scripts/lint.py --type identity", file=sys.stderr)
        sys.exit(1)

    rendered = json.dumps(index, indent=1, sort_keys=True) + "\n"

    if args.check:
        if not OUT_PATH.exists():
            print(f"{OUT_PATH.name} is missing — run scripts/build_wiki_index.py")
            sys.exit(1)
        if OUT_PATH.read_text(encoding="utf-8") != rendered:
            print(f"{OUT_PATH.name} is stale — run scripts/build_wiki_index.py")
            sys.exit(1)
        print(f"{OUT_PATH.name} is current.")
        return

    OUT_PATH.write_text(rendered, encoding="utf-8")
    n_aliases = sum(len(p.get("aliases", [])) for p in index["pages"])
    print(f"Wrote {OUT_PATH.name}: {len(index['pages'])} page(s), "
          f"{n_aliases} retired slug(s) still resolving.")
    for kind, n in index["counts"].items():
        print(f"  {kind:<18} {n:>5}")


if __name__ == "__main__":
    main()
