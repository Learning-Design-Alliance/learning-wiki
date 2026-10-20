#!/usr/bin/env python3
"""link_inline_citations.py — give an unlinked inline citation, "(Mayer 2008)" or "[Bandura, 1997]",
the link to the work it names, where the wiki can say which work that is.

Pages written from briefs and older ingests cite in running prose by author and year with no link,
so a reader cannot get from "(Noetel et al. 2022)" to the paper. An author and a year do not
identify a paper on their own: the wiki cites several different Mayer (2008)s. So a citation is
linked only when one target is certain, tried in this order:

1. the page's own `## Key Sources` (or `## Evidence`) lists that author-year with a DOI or URL,
   and every such entry on the page agrees;
2. a claim the page links to carries a study of that author-year in its frontmatter `sources`,
   and every such study agrees on its resource;
3. across the whole wiki, that author-year key has exactly one DOI and one title cluster
   (check_citations.py's own clustering), so it names one paper.

Anything else is left as it is and listed, never guessed. Text inside existing links, code spans,
headings, frontmatter and HTML comments (kept old bodies) is not touched. Claims are skipped: their
citations live in `## Evidence`, which carries its own links.

    python3 scripts/link_inline_citations.py --check     # what would be linked, and what cannot be
    python3 scripts/link_inline_citations.py --apply
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_citations as cc  # noqa: E402
import okf_lib  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
NAME = r"[A-Z][A-Za-z'’\-]+"
# One citation inside a parenthetical or bracketed group: "Mayer 2008", "Mayer, 2008",
# "Noetel et al. 2022", "Clark & Paivio, 1991", "Clark and Paivio 1991a".
ITEM_RE = re.compile(rf"(?P<cite>(?P<first>{NAME})(?:\s+(?:&|and)\s+{NAME}|\s+et\s+al\.?)?,?\s+(?P<year>(?:19|20)\d\d)[a-z]?)")
GROUP_RE = re.compile(r"(?<![\]\w])([(\[])([^()\[\]\n]{4,200}?)([)\]])(?!\()")
LINK_RE = re.compile(r"\[[^\]\n]*\]\([^)\n]*\)|`[^`\n]*`")
CLAIM_LINK_RE = re.compile(r"\]\((?:\.\./claims/)?([a-z0-9][a-z0-9._-]*)\.md(?:#[^)]*)?\)")
URL_RE = re.compile(r"\((https?://[^)\s]+)\)")


def key_of(first: str, year: str) -> str:
    return f"{first.lower()}-{year}"


def page_sources(text: str) -> dict:
    """{key: set of URLs} from the page's own Key Sources / Evidence lines."""
    out = collections.defaultdict(set)
    for c in cc.extract_citations(text, ""):
        m = URL_RE.search(c["full_line"])
        url = f"https://doi.org/{c['doi']}" if c["doi"] else (m.group(1) if m else None)
        out[c["key"]].add(url)
    return out


_claim_cache: dict = {}


def claim_sources(slug: str) -> dict:
    """{key: set of resource URLs} from one claim's frontmatter sources."""
    if slug in _claim_cache:
        return _claim_cache[slug]
    res = collections.defaultdict(set)
    p = ROOT / "claims" / f"{slug}.md"
    if p.exists():
        fm, _ = okf_lib.split_frontmatter(p.read_text(encoding="utf-8"))
        try:
            meta = okf_lib.parse_frontmatter("\n".join(fm)) if hasattr(okf_lib, "parse_frontmatter") else None
        except Exception:
            meta = None
        if meta is None:
            import yaml
            try:
                meta = yaml.safe_load("\n".join(fm).strip().strip("-")) or {}
            except Exception:
                meta = {}
        for s in meta.get("sources") or []:
            title, resource = str(s.get("title") or ""), s.get("resource")
            m = cc.CITATION_KEY_RE.search(title)
            if m and resource:
                res[f"{m.group(1).lower()}-{m.group(2)[:4]}"].add(str(resource))
    _claim_cache[slug] = res
    return res


def wiki_unique(by_key: dict) -> dict:
    """{key: doi URL} for author-year keys naming exactly one paper with one DOI wiki-wide."""
    out = {}
    for key, entries in by_key.items():
        dois = {e["doi"] for e in entries if e["doi"]}
        if len(dois) == 1 and len(cc._cluster_by_title(entries)) == 1:
            out[key] = f"https://doi.org/{next(iter(dois))}"
    return out


def _norm(url: str) -> str:
    """One spelling per resource: DOIs are case-insensitive and come as dx.doi.org or doi.org."""
    u = url.strip().rstrip("/.")
    m = re.search(r"doi\.org/(10\..+)$", u, re.I)
    return f"https://doi.org/{m.group(1).lower()}" if m else u


def resolve(key: str, own: dict, cited: list, unique: dict):
    """A link only when one source settles it; an entry with no URL settles nothing and the
    next source is tried."""
    for urls in (own.get(key) or set(),
                 set().union(*(claim_sources(s).get(key, set()) for s in cited)) if cited else set()):
        urls = {_norm(u) for u in urls if u}
        if len(urls) == 1:
            return next(iter(urls)), None
        if len(urls) > 1:
            return None, "several works"
    if key in unique:
        return unique[key], None
    return None, "no source"


def process(text: str, unique: dict):
    head, body = ("", text)
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        head, body = text[: end + 4], text[end + 4:]
    own = page_sources(text)
    cited = sorted(set(CLAIM_LINK_RE.findall(body)))
    linked, skipped = [], []
    out, in_comment = [], False
    for line in body.split("\n"):
        if in_comment or line.lstrip().startswith("#") or "<!--" in line:
            in_comment = (in_comment or "<!--" in line) and "-->" not in line.split("<!--")[-1]
            out.append(line)
            continue
        protected = [(m.start(), m.end()) for m in LINK_RE.finditer(line)]

        def group(m):
            if any(a <= m.start() < b for a, b in protected):
                return m.group(0)
            inner, changed = m.group(2), False

            def item(im):
                nonlocal changed
                key = key_of(im.group("first"), im.group("year"))
                url, why = resolve(key, own, cited, unique)
                if url:
                    changed = True
                    linked.append(im.group("cite"))
                    return f"[{im.group('cite')}]({url})"
                skipped.append((im.group("cite"), why))
                return im.group(0)

            parts = re.split(r"(;\s*)", inner)
            if not any(ITEM_RE.fullmatch(p.strip()) for p in parts[::2]):
                return m.group(0)
            new = "".join(ITEM_RE.sub(item, p) if ITEM_RE.fullmatch(p.strip()) else p for p in parts)
            if not changed:
                return m.group(0)
            open_, close = ("(", ")") if m.group(1) == "(" else ("(", ")")
            return f"{open_}{new}{close}"

        out.append(GROUP_RE.sub(group, line))
    return head + "\n".join(out), linked, skipped


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    unique = wiki_unique(cc.load_all_citations())
    n_link = n_pages = 0
    reasons = collections.Counter()
    left = collections.Counter()
    for folder in okf_lib.CONTENT_FOLDERS:
        if folder == "claims":
            continue
        for p in sorted((ROOT / folder).glob("*.md")):
            if p.name == "index.md":
                continue
            text = p.read_text(encoding="utf-8")
            new, linked, skipped = process(text, unique)
            for cite, why in skipped:
                reasons[why] += 1
                left[cite] += 1
            if linked:
                n_link += len(linked)
                n_pages += 1
                if args.apply:
                    p.write_text(new, encoding="utf-8")
    verb = "linked" if args.apply else "would link"
    print(f"{verb} {n_link} inline citation(s) on {n_pages} page(s); left unlinked: {dict(reasons)}")
    print("most frequent left unlinked:", ", ".join(f"{c} ({n})" for c, n in left.most_common(15)))


if __name__ == "__main__":
    main()
