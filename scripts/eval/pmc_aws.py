"""
pmc_aws.py — Shared access to the PMC Article Datasets on AWS Open Data
(bucket `pmc-oa-opendata`, world-readable, no AWS credentials or SDK needed —
see https://pmc.ncbi.nlm.nih.gov/tools/pmcaws/). This replaced NCBI's old
FTP-hosted bulk oa_file_list.csv, which was fully decommissioned the week of
August 24, 2026 (verified live: the file 404s, and the FTP host's readme.txt
confirms the migration) — see eval/SOURCES.md's PMC section.

Every PMC article version has a small JSON metadata object here, keyed by
PMCID + version number (most articles have only version 1), carrying an
authoritative `is_pmc_openaccess` flag plus direct URLs to that version's
XML/text/PDF/media objects. Two callers share this module rather than one
reimplementing the other's logic:
  - discover_articles.search_pmc() checks a candidate's metadata before
    spending a manifest slot on it — the ESearch "open access[filter]" tag
    is best-effort and can lag reality; `is_pmc_openaccess` here is ground
    truth.
  - fetch_article.py fetches the actual full text from the SAME metadata
    object's `text_url`, replacing the old BioC-PMC API call — the same
    source of truth is now used at both discovery and fetch time, closing
    the "flagged OA at search time, 404s at fetch time" gap at its root
    instead of just filtering it out earlier.
"""

import requests

from . import compliance

S3_BASE = "https://pmc-oa-opendata.s3.amazonaws.com"


def metadata_url(pmcid: str, version: int = 1) -> str:
    return f"{S3_BASE}/metadata/{pmcid}.{version}.json"


def fetch_metadata(pmcid: str, version: int = 1):
    """Returns the article version's JSON metadata dict, or None if no
    object exists at this version number (most articles have only version 1
    — see the module docstring; this project doesn't probe higher version
    numbers, since a missing v1 object means "not available via this
    dataset" for our purposes either way). Raises requests.RequestException
    (network failure) or ValueError (unparseable body) on a genuine error —
    callers decide how to handle that: discover_articles.py degrades
    gracefully and keeps the candidate on the ESearch flag alone;
    fetch_article.py lets it surface as a FetchError."""
    url = metadata_url(pmcid, version)
    compliance.guard(url)
    resp = requests.get(url, headers={"User-Agent": compliance.USER_AGENT}, timeout=30)
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json()


def s3_to_https(s3_url: str) -> str:
    """Converts an s3://<bucket>/<key>[?query] URL (the form every URL field
    in an AWS metadata object uses, e.g. text_url) into the equivalent
    https://<bucket>.s3.amazonaws.com/<key>[?query] virtual-hosted-style URL
    — the documented plain-HTTPS access pattern (see
    https://pmc.ncbi.nlm.nih.gov/tools/pmcaws/: "You can also retrieve files
    directly with a browser or curl, using a URL that starts with
    https://pmc-oa-opendata.s3.amazonaws.com/"). Passes through unchanged if
    given something that isn't an s3:// URL."""
    if not s3_url.startswith("s3://"):
        return s3_url
    bucket, _, key_and_query = s3_url[len("s3://"):].partition("/")
    return f"https://{bucket}.s3.amazonaws.com/{key_and_query}"
