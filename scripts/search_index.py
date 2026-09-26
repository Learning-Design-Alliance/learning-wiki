#!/usr/bin/env python3
"""
search_index.py — a full-text index of the wiki, so search stays fast at any size.

The MCP server used to score every page on every query, and claim linking needs
the same "which pages are about this" lookup for thousands of claims. Both work at
7,000 pages and stop working at a million: measured 2026-09-26, SQLite FTS5 over
title, description and body answered in 0.9 ms at 7,024 pages and 14.7 ms at
140,480 (a 20x synthetic copy), where a scan grows with every page.

The index is a cache, not a record: it lives in `.cache/wiki-search.db`, which is
ignored, and `ensure()` rebuilds it whenever the content folders change (file
count and newest mtime, the fingerprint dashboard_server.py already uses). Nothing
reads it that could not rebuild it.

    python3 scripts/search_index.py --build
    python3 scripts/search_index.py "worked examples novices" [--kind claim]
"""
import argparse
import re
import sqlite3
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import okf_lib  # noqa: E402

DB_PATH = WIKI_ROOT / ".cache" / "wiki-search.db"
SCHEMA_VERSION = "1"
_WORD = re.compile(r"[A-Za-z0-9]+")
_STOP = {"the", "a", "an", "of", "and", "or", "in", "on", "for", "to", "with", "by", "at", "from",
         "as", "is", "are", "was", "were", "be", "that", "this", "than", "their", "its", "it", "not"}


def _fingerprint(root: Path) -> str:
    n, newest = 0, 0.0
    for folder in okf_lib.CONTENT_FOLDERS:
        for p in (root / folder).glob("*.md"):
            n += 1
            newest = max(newest, p.stat().st_mtime)
    return f"{SCHEMA_VERSION}:{n}:{newest:.3f}"


def _pages(root: Path):
    for folder in okf_lib.CONTENT_FOLDERS:
        for p in sorted((root / folder).glob("*.md")):
            if p.stem == "index":
                continue
            text = p.read_text(encoding="utf-8")
            fm_lines, body = okf_lib.split_frontmatter(text)
            fm = okf_lib.parse_frontmatter_scalars(fm_lines)
            title = str(fm.get("title") or "")
            if not title:
                m = re.search(r"^# (.+)$", body, re.M)
                title = m.group(1) if m else p.stem
            yield (f"{folder}/{p.stem}", folder, p.stem, title, str(fm.get("description") or ""),
                   str(fm.get("status") or ""), body)


def build(root: Path = WIKI_ROOT, path: Path = None) -> Path:
    path = path or (DB_PATH if root == WIKI_ROOT else root / ".cache" / "wiki-search.db")
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    if tmp.exists():
        tmp.unlink()
    db = sqlite3.connect(tmp)
    db.execute("create table meta (key text primary key, value text)")
    db.execute("create virtual table pages using fts5(pid unindexed, folder unindexed, slug, title, "
               "description, status unindexed, body, tokenize='porter unicode61')")
    db.executemany("insert into pages values (?,?,?,?,?,?,?)", _pages(root))
    db.execute("insert into meta values ('fingerprint', ?)", (_fingerprint(root),))
    db.commit()
    db.close()
    tmp.replace(path)
    return path


def ensure(root: Path = WIKI_ROOT) -> sqlite3.Connection:
    """An open connection to a current index, rebuilding it first if the wiki changed."""
    path = DB_PATH if root == WIKI_ROOT else root / ".cache" / "wiki-search.db"
    want = _fingerprint(root)
    have = None
    if path.exists():
        try:
            db = sqlite3.connect(path)
            row = db.execute("select value from meta where key='fingerprint'").fetchone()
            have = row[0] if row else None
            if have == want:
                return db
            db.close()
        except sqlite3.DatabaseError:
            pass
    build(root, path)
    return sqlite3.connect(path)


def match_expr(text: str, max_terms: int = 24, mode: str = "OR") -> str | None:
    """An FTS5 query from free text: every word quoted, so a hyphen or a column
    name in the text ("long-term", "title") cannot turn into query syntax."""
    words = []
    for w in _WORD.findall(text.lower()):
        if len(w) > 1 and w not in _STOP and w not in words:
            words.append(w)
    if not words:
        return None
    return f" {mode} ".join(f'"{w}"' for w in words[:max_terms])


def query(db: sqlite3.Connection, text: str, folder: str = None, limit: int = 10, mode: str = "AND"):
    """[(pid, folder, slug, title, description, status, score)], best first. `mode`
    AND needs every word (a search box); OR ranks by how many match (retrieval)."""
    expr = match_expr(text, mode=mode)
    if not expr:
        return []
    sql = ("select pid, folder, slug, title, description, status, "
           "bm25(pages, 0, 0, 4.0, 10.0, 3.0, 0, 1.0) as s from pages where pages match ?")
    args = [expr]
    if folder:
        sql += " and folder = ?"
        args.append(folder)
    sql += " order by s limit ?"
    args.append(limit)
    return [(*r[:6], -r[6]) for r in db.execute(sql, args).fetchall()]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("text", nargs="?")
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--kind", help="folder name, e.g. claims")
    ap.add_argument("--limit", type=int, default=10)
    args = ap.parse_args()
    if args.build:
        print(f"wrote {build()}")
        return
    db = ensure()
    for r in query(db, args.text or "", args.kind, args.limit):
        print(f"{r[6]:7.2f}  {r[0]:70.70}  {r[3][:70]}")


if __name__ == "__main__":
    main()
