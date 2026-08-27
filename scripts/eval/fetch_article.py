"""
fetch_article.py — Fetch and cache full text for the eval corpus (arXiv / ERIC / PMC).

Every request goes through compliance.guard() first (robots.txt + per-domain
rate limiting) — see eval/SOURCES.md for why each source is fetched the way
it is (e.g. PMC via the BioC API rather than scraping article HTML, which
NCBI's usage guidelines don't list as a sanctioned automated-retrieval path).

Text is cached to eval/corpus/cache/<id>.txt so repeated harness runs (and reruns
against new models) don't re-download or re-parse PDFs. Delete a cache file (or
pass --refresh-cache to eval_harness.py) to force a re-fetch.
"""

import io
import sys
from pathlib import Path

import requests

from . import compliance

EVAL_ROOT = Path(__file__).parent.parent.parent / "eval"
CACHE_DIR = EVAL_ROOT / "corpus" / "cache"

TIMEOUT = 60


class FetchError(RuntimeError):
    pass


def _get(url: str) -> requests.Response:
    compliance.guard(url)
    resp = requests.get(url, headers={"User-Agent": compliance.USER_AGENT}, timeout=TIMEOUT)
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


def _extract_pmc_bioc(data) -> str:
    """Parse a BioC-PMC JSON response into plain text. The BioC-PMC API only
    serves the PMC Open Access subset — a 404 here means this PMCID isn't in
    that subset, i.e. it isn't cleared for automated bulk retrieval at all,
    not just via this endpoint. Don't fall back to scraping the HTML page for
    it; swap the manifest entry for one that IS in the OA subset instead."""
    collection = data[0] if isinstance(data, list) and data else data
    documents = collection.get("documents", []) if isinstance(collection, dict) else []

    parts = []
    for doc in documents:
        for passage in doc.get("passages", []):
            text = passage.get("text", "").strip()
            if text:
                parts.append(text)

    text = "\n\n".join(parts)
    if len(text.strip()) < 500:
        raise FetchError("Extracted BioC text is suspiciously short (<500 chars) — "
                          "check the PMCID is correct and actually in the PMC OA subset.")
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
            text = _extract_pmc_bioc(resp.json())
        else:
            raise FetchError(f"Unknown source type: {source}")
    except compliance.ComplianceError:
        raise
    except requests.HTTPError as e:
        if source == "pubmed" and e.response is not None and e.response.status_code == 404:
            raise FetchError(
                f"{entry.get('pmcid', fetch_url)} returned 404 from the BioC-PMC API — "
                f"it's likely not in the PMC Open Access subset, so it isn't cleared for "
                f"automated retrieval. Replace this manifest entry rather than scraping "
                f"the HTML article page as a workaround."
            ) from e
        raise FetchError(f"HTTP error fetching {fetch_url}: {e}") from e
    except ValueError as e:
        # resp.json() raising here (a 200 with an empty/near-empty body) is the
        # same underlying issue as the 404 case above, just a different HTTP
        # status: open access[filter] in search_pmc()'s ESearch query means
        # "flagged OA," not "already processed into the BioC full-text corpus"
        # — very recently published PMCIDs are the ones most likely to hit
        # this. Caught here (ValueError, which requests' own JSONDecodeError
        # and the stdlib json.JSONDecodeError both subclass) rather than
        # falling through to the generic RequestException case below, which
        # would otherwise mislabel this "Network error" and obscure the cause.
        if source == "pubmed":
            raise FetchError(
                f"{entry.get('pmcid', fetch_url)} returned an empty/unparseable body from "
                f"the BioC-PMC API — likely not yet processed into the OA full-text corpus, "
                f"even though it was flagged open access[filter] at search time. Replace "
                f"this manifest entry; it may become fetchable later, but isn't now."
            ) from e
        raise FetchError(f"Unparseable response from {fetch_url}: {e}") from e
    except requests.RequestException as e:
        raise FetchError(f"Network error fetching {fetch_url}: {e}") from e

    cache_path.write_text(text, encoding="utf-8")
    return text


def main() -> None:
    """Prefetch/verify the whole manifest without calling any model — run this
    first to confirm every URL in the manifest still resolves before spending
    money on generation calls. Pass --manifest <path> to check a different
    manifest file (e.g. discover_articles.py's output) instead of the default
    10-article benchmark corpus."""
    import json
    manifest_path = EVAL_ROOT / "corpus" / "manifest.json"
    if "--manifest" in sys.argv:
        manifest_path = Path(sys.argv[sys.argv.index("--manifest") + 1])
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
        except compliance.ComplianceError as e:
            print(f"[BLOCKED] {entry['id']:20s} {e}")
            failed.append(entry["id"])

    print(f"\n{ok}/{len(manifest['articles'])} fetched successfully.")
    if failed:
        print(f"Failed: {', '.join(failed)}")
        print("Fix or replace these manifest entries before running the harness.")
        sys.exit(1)


if __name__ == "__main__":
    main()
