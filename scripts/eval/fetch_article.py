"""
fetch_article.py — Fetch and cache full text for the eval corpus (arXiv / ERIC / PMC).

Every request goes through compliance.guard() first (robots.txt + per-domain
rate limiting) — see eval/SOURCES.md for why each source is fetched the way
it is (e.g. PMC via the PMC Article Datasets on AWS, see pmc_aws.py, rather
than scraping article HTML, which NCBI's usage guidelines don't list as a
sanctioned automated-retrieval path).

Text is cached to eval/corpus/cache/<id>.txt so repeated harness runs (and reruns
against new models) don't re-download or re-parse PDFs. Delete a cache file (or
pass --refresh-cache to eval_harness.py) to force a re-fetch.
"""

import io
import sys
import time
from pathlib import Path

import requests

from . import compliance, pmc_aws

EVAL_ROOT = Path(__file__).parent.parent.parent / "eval"
CACHE_DIR = EVAL_ROOT / "corpus" / "cache"

TIMEOUT = 60
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 5  # seconds; doubled each attempt if the server gives no Retry-After


class FetchError(RuntimeError):
    pass


def _get(url: str) -> requests.Response:
    """A bounded, Retry-After-respecting retry on 429/503 — not a hammer,
    just enough to survive a transient rate hiccup. Empirically justified,
    not speculative: a live PMC fetch hit 429 from www.ncbi.nlm.nih.gov while
    this harness was well under NCBI's documented 3 req/s ceiling, most
    likely because their server-side limiting pools traffic by IP across all
    of *.ncbi.nlm.nih.gov rather than per-subdomain the way compliance.py's
    own bookkeeping does. compliance.guard() re-runs on every attempt, so a
    retry still respects our own rate floor on top of any explicit backoff."""
    for attempt in range(MAX_RETRIES + 1):
        compliance.guard(url)
        resp = requests.get(url, headers={"User-Agent": compliance.USER_AGENT}, timeout=TIMEOUT)
        if resp.status_code in (429, 503) and attempt < MAX_RETRIES:
            retry_after = resp.headers.get("Retry-After")
            try:
                delay = float(retry_after) if retry_after else RETRY_BACKOFF_BASE * (2 ** attempt)
            except ValueError:
                delay = RETRY_BACKOFF_BASE * (2 ** attempt)
            print(f"  [WARN] {resp.status_code} from {url}, retrying in {delay:.0f}s "
                  f"(attempt {attempt + 1}/{MAX_RETRIES})...", file=sys.stderr)
            time.sleep(delay)
            continue
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


def _fetch_pmc_via_aws(entry: dict) -> str:
    """Fetches full text via the PMC Article Datasets on AWS (pmc_aws.py)
    instead of the old BioC-PMC API — see that module's docstring. Uses the
    same `is_pmc_openaccess` ground truth discover_articles.search_pmc() now
    checks before adding a manifest entry, so a 404/empty-body surprise here
    should be rare — but a manifest entry can come from a hand-curated
    source (the original 10-article benchmark) that never went through that
    check, so this still verifies rather than assuming. Don't fall back to
    scraping the HTML page for a miss; swap the manifest entry instead."""
    pmcid = entry.get("pmcid") or entry["id"]
    aws_meta = pmc_aws.fetch_metadata(pmcid)
    if aws_meta is None:
        raise FetchError(
            f"{pmcid} has no PMC AWS metadata object (metadata/{pmcid}.1.json not found) — "
            f"not available via the PMC Article Datasets on AWS. Replace this manifest entry."
        )
    if not aws_meta.get("is_pmc_openaccess"):
        raise FetchError(
            f"{pmcid} is not marked is_pmc_openaccess in its PMC AWS metadata — not cleared "
            f"for automated bulk retrieval. Replace this manifest entry rather than scraping "
            f"the HTML article page as a workaround."
        )
    text_url = aws_meta.get("text_url")
    if not text_url:
        raise FetchError(f"{pmcid}'s PMC AWS metadata has no text_url.")
    resp = _get(pmc_aws.s3_to_https(text_url))
    text = resp.text
    if len(text.strip()) < 500:
        raise FetchError("Extracted PMC AWS text is suspiciously short (<500 chars) — "
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
            text = _fetch_pmc_via_aws(entry)
        else:
            raise FetchError(f"Unknown source type: {source}")
    except compliance.ComplianceError:
        raise
    except requests.HTTPError as e:
        raise FetchError(f"HTTP error fetching {fetch_url}: {e}") from e
    except ValueError as e:
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
