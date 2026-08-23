"""
fetch_article.py — Fetch and cache full text for the eval corpus (arXiv / ERIC / PMC).

Text is cached to eval/corpus/cache/<id>.txt so repeated harness runs (and reruns
against new models) don't re-download or re-parse PDFs. Delete a cache file (or
pass --refresh-cache to eval_harness.py) to force a re-fetch.
"""

import io
import re
import sys
from pathlib import Path
from typing import Optional

import requests

EVAL_ROOT = Path(__file__).parent.parent.parent / "eval"
CACHE_DIR = EVAL_ROOT / "corpus" / "cache"

USER_AGENT = "learning-design-wiki-eval-harness/1.0 (research corpus fetch)"
TIMEOUT = 60


class FetchError(RuntimeError):
    pass


def _get(url: str) -> requests.Response:
    resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp


def _extract_pdf_text(content: bytes) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        raise FetchError("pypdf not installed. Run: pip install -r requirements-eval.txt")
    reader = PdfReader(io.BytesIO(content))
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    text = "\n\n".join(pages)
    if len(text.strip()) < 500:
        raise FetchError("Extracted PDF text is suspiciously short (<500 chars) — "
                          "likely a scanned/image PDF that needs OCR.")
    return text


def _extract_pmc_html(html: str) -> str:
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        raise FetchError("beautifulsoup4 not installed. Run: pip install -r requirements-eval.txt")
    soup = BeautifulSoup(html, "html.parser")
    # PMC article body typically lives in a <div class="jig-ncbiinpagenav"> or article tag;
    # fall back to stripping nav/script/style and taking all visible text.
    for tag in soup(["script", "style", "nav", "header", "footer", "form"]):
        tag.decompose()
    article = soup.find("article") or soup.find(attrs={"class": re.compile("article|body|content", re.I)}) or soup
    text = article.get_text("\n", strip=True)
    if len(text.strip()) < 500:
        raise FetchError("Extracted PMC HTML text is suspiciously short (<500 chars) — "
                          "page may be a landing/paywall page, not the article body.")
    return text


def fetch_article_text(entry: dict, refresh: bool = False) -> str:
    """Fetch (or load from cache) the full text for one manifest entry."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = CACHE_DIR / f"{entry['id']}.txt"

    if cache_path.exists() and not refresh:
        return cache_path.read_text(encoding="utf-8")

    source = entry["source"]
    fetch_url = entry["fetch_url"]

    try:
        if source in ("arxiv", "eric"):
            resp = _get(fetch_url)
            text = _extract_pdf_text(resp.content)
        elif source == "pubmed":
            resp = _get(fetch_url)
            text = _extract_pmc_html(resp.text)
        else:
            raise FetchError(f"Unknown source type: {source}")
    except requests.HTTPError as e:
        raise FetchError(f"HTTP error fetching {fetch_url}: {e}") from e
    except requests.RequestException as e:
        raise FetchError(f"Network error fetching {fetch_url}: {e}") from e

    cache_path.write_text(text, encoding="utf-8")
    return text


def main() -> None:
    """Prefetch/verify the whole manifest without calling any model — run this
    first to confirm every URL in the manifest still resolves before spending
    money on generation calls."""
    import json
    manifest_path = EVAL_ROOT / "corpus" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    refresh = "--refresh-cache" in sys.argv

    ok, failed = 0, []
    for entry in manifest["articles"]:
        try:
            text = fetch_article_text(entry, refresh=refresh)
            print(f"[OK]   {entry['id']:20s} {len(text):>8,} chars — {entry['title'][:60]}")
            ok += 1
        except FetchError as e:
            print(f"[FAIL] {entry['id']:20s} {e}")
            failed.append(entry["id"])

    print(f"\n{ok}/{len(manifest['articles'])} fetched successfully.")
    if failed:
        print(f"Failed: {', '.join(failed)}")
        print("Fix or replace these manifest entries before running the harness.")
        sys.exit(1)


if __name__ == "__main__":
    main()
