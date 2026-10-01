"""
search_trim.py — keep the docs site's search index small enough to load.

mkdocs-material's search downloads search/search_index.json and builds a lunr
index from it in the reader's browser, on every visit. With one entry per
heading that file had grown to 91,222 entries and 66 MB (12.8 MB gzipped) by
2026-10-01, most of it the template sections every strategy repeats
("Requirements", "Constraints", "Instructions") and the dated sections of
log.md. Building that index is what made search slow.

After the build this rewrites the file to one entry per content page: its
title, its frontmatter description, its section headings and the opening of
its body, so a query still finds a page by what it is about. log.md, CLAUDE.md
and the generated index pages are left out: they list other pages, and a hit
on them is a hit on a list. Full-text search over every section stays
available from the MCP server's FTS5 index (scripts/search_index.py), which
does not run in a browser.
"""

from __future__ import annotations

import json
import os

BODY_CHARS = 600

_descriptions: dict[str, str] = {}


def on_page_context(context, page, config, nav):
    desc = (page.meta or {}).get("description")
    if isinstance(desc, str):
        _descriptions[page.url] = desc.strip()
    return context


def _skip(location: str, folders: set) -> bool:
    # "" is the bundle index and "claims/" a folder index (listings); log/ and
    # CLAUDE/ are the change log and the guide. Other root pages are kept.
    path = location.split("#", 1)[0]
    return path in ("", "log/", "CLAUDE/") or path.rstrip("/") in folders


def on_post_build(config):
    path = os.path.join(config["site_dir"], "search", "search_index.json")
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    folders = {d["location"].split("/", 1)[0] for d in data["docs"] if d["location"].split("#", 1)[0].count("/") >= 2}
    pages, order = {}, []
    for doc in data["docs"]:
        loc = doc["location"]
        if _skip(loc, folders):
            continue
        base = loc.split("#", 1)[0]
        if base not in pages:
            pages[base] = {"location": base, "title": "", "heads": [], "body": []}
            order.append(base)
        p = pages[base]
        if "#" in loc:
            p["heads"].append(doc.get("title", ""))
            if sum(map(len, p["body"])) < BODY_CHARS:
                p["body"].append(doc.get("text", ""))
        else:
            p["title"] = doc.get("title", "")
            p["body"].insert(0, doc.get("text", ""))
    docs = []
    for base in order:
        p = pages[base]
        parts = [_descriptions.get(base, ""), " ".join(dict.fromkeys(h for h in p["heads"] if h)),
                 " ".join(p["body"])[:BODY_CHARS]]
        docs.append({"location": base, "title": p["title"], "text": " ".join(x for x in parts if x)})
    data["docs"] = docs
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, separators=(",", ":"))
