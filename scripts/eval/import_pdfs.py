#!/usr/bin/env python3
"""
import_pdfs.py — bring PDFs a person downloaded by hand into the batch queue.

Some queue entries cannot be fetched automatically: the publisher's robots.txt disallows
crawlers (ScienceDirect, MDPI), or its site refuses them (Taylor & Francis, Wiley, ACM),
and no open copy exists elsewhere. A person can still open those papers in a browser. This
matches each PDF to its queue entry, by the DOI printed in it or else by its title, writes
the text to the fetch cache under that entry's id, and takes the entry off
eval/runs/queues/fetch-failed.ndjson, so the next batch ingests it from the cache.

The PDFs themselves are never copied into the repository: it is public, and only the wiki
pages written from a paper are committed.

    python3 scripts/eval/import_pdfs.py <pdf> [<pdf> ...] [--queue <file> ...] [--dry-run]
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.eval import fetch_article as fa  # noqa: E402

QUEUES = [ROOT / "eval/runs/queues/hub.ndjson", ROOT / "eval/runs/queues/aied.ndjson"]
FAILED = ROOT / "eval/runs/queues/fetch-failed.ndjson"
DOI_RE = re.compile(r"\b(10\.\d{4,9}/[^\s\"<>]+)", re.I)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def match(text: str, entries: list) -> "dict | None":
    by_doi = {(e.get("doi") or "").lower().rstrip("."): e for e in entries if e.get("doi")}
    head = text[:6000]
    for m in DOI_RE.finditer(head):
        d = m.group(1).lower().rstrip(".,;)")
        if d in by_doi:
            return by_doi[d]
    flat = norm(head)
    hits = [e for e in entries if len(norm(e.get("title", ""))) > 25 and norm(e["title"]) in flat]
    return hits[0] if len(hits) == 1 else None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdfs", nargs="+")
    ap.add_argument("--queue", nargs="+", default=[str(q) for q in QUEUES])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    entries = [json.loads(l) for q in args.queue for l in Path(q).read_text(encoding="utf-8").splitlines() if l.strip()]
    imported = set()
    for p in args.pdfs:
        try:
            text = fa._extract_pdf_text(Path(p).read_bytes())
        except Exception as e:  # noqa: BLE001
            print(f"  unreadable  {Path(p).name}: {e}")
            continue
        e = match(text, entries)
        if not e:
            print(f"  no match    {Path(p).name} ({len(text):,} chars)")
            continue
        print(f"  matched     {Path(p).name} -> {e['id']}  {e.get('title', '')[:70]}")
        if not args.dry_run:
            fa.CACHE_DIR.mkdir(parents=True, exist_ok=True)
            (fa.CACHE_DIR / f"{e['id']}.txt").write_text(text, encoding="utf-8")
            imported.add(e["id"])
    if imported and FAILED.exists():
        rows = [l for l in FAILED.read_text(encoding="utf-8").splitlines() if l.strip()]
        keep = [l for l in rows if json.loads(l)["id"] not in imported]
        FAILED.write_text("".join(l + "\n" for l in keep), encoding="utf-8")
    print(f"imported {len(imported)} of {len(args.pdfs)}")


if __name__ == "__main__":
    main()
