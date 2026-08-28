# Source compliance notes

What each source actually allows for automated access, what this harness does
about it, and where to go instead if a source turns out to be off-limits at
the volume the real batch needs. Researched via each source's own published
robots.txt/API docs/usage guidelines — re-verify before a large batch if this
has aged, since policies do change.

`scripts/eval/compliance.py` enforces the mechanical parts of this
automatically (robots.txt + rate limiting) for every fetch — this document
covers the parts a robots.txt check can't: which retrieval *channel* is
actually sanctioned, and what to do if a source blocks bulk access outright.

## arXiv

- **Two different hosts, two different robots.txt — don't conflate them.**
  `arxiv.org` (the main site, used for `/pdf/<id>` fetches) has
  `Crawl-delay: 15`; `/abs` and `/pdf` are explicitly `Allow`ed, but the
  file's own header states "Indiscriminate automated downloads from this
  site are not permitted." `export.arxiv.org` (the legacy **API** host,
  what `discover_articles.py`'s `search_arxiv()` queries) is a **separate
  domain with its own robots.txt** — verified live: a real HTTP 200 with
  body `User-agent: * / Disallow: /`, i.e. a deliberate, total block, not an
  infrastructure artifact (contrast the `eutils.ncbi.nlm.nih.gov` and
  `api.ies.ed.gov` findings above, which *were* artifacts and got a cited
  override in `compliance.py`). This one is real and is respected as-is —
  **no override**. Earlier versions of this doc described the legacy
  API/OAI-PMH's *rate terms* without having verified `export.arxiv.org`'s
  own robots.txt separately; that gap is closed now. Practical effect:
  `discover_articles.py` cannot query arXiv live at all (defaults `--arxiv`
  to 0) — only the S3/Kaggle bulk channels below are viable for arXiv
  candidate discovery.
- **API Terms of Use**: the legacy API and OAI-PMH cap requests at one every
  3 seconds, one connection at a time, across *all* machines you control —
  i.e. you can't parallelize around the limit with more IPs. (Moot for live
  querying per the robots.txt finding above; kept here in case a future
  bulk-harvest approach needs it.)
- **What this harness does**: fetches `/pdf/<id>` directly from `arxiv.org`
  (not `export.arxiv.org`), gated by `compliance.py`'s 15s-per-request floor
  (arXiv's own robots.txt value for that host). Fine for a 10-article smoke
  test with manually-curated IDs; **not** the right approach past a few
  dozen — at 15s/request, 1,000 papers is >4 hours of pure waiting, and it's
  explicitly discouraged for "indiscriminate" volume. This path still works;
  what's blocked is *discovering* new arXiv IDs via the live search API.
- **Bulk alternative for scale**: [arXiv Bulk Data Access via S3](https://info.arxiv.org/help/bulk_data_s3.html) —
  the complete set of processed PDFs/source files in a *requester-pays* S3
  bucket (you pay AWS's transfer cost, not arXiv's bandwidth). This is the
  officially sanctioned path for "give me everything," not repeated
  `/pdf/<id>` requests. [OAI-PMH](https://info.arxiv.org/help/oa/index.html)
  is the equivalent for bulk *metadata* harvesting.
- **Third-party mirror**: [Cornell's official arXiv dataset on Kaggle](https://www.kaggle.com/datasets/Cornell-University/arxiv) —
  metadata (titles/authors/categories/abstracts) for all ~2.7M papers, with
  full PDFs available from the companion `gs://arxiv-dataset` Google Cloud
  Storage bucket. This is arXiv's own maintained export, not a scrape by a
  third party — a good starting point for candidate selection before
  fetching only the PDFs you actually need. This harness fetches it
  automatically: `discover_articles.resolve_arxiv_snapshot()` calls
  `kagglehub.dataset_download()` the first time a batch requests `--arxiv >
  0` with no explicit `--arxiv-snapshot`, authenticating from
  `KAGGLE_USERNAME`/`KAGGLE_KEY` (see `deploy/eval-harness.env.example`) and
  caching the result on disk — no manual download step needed.
- **Attribution**: if you build an index/tool on the full text, link back to
  the arXiv abstract page for downloads (their license term, not just courtesy).

## PubMed Central (PMC) / NCBI

- **This is the one place the original design was wrong, and has been fixed
  twice**: NCBI's own documentation states that automated retrieval of PMC
  content must go through one of their own sanctioned channels — scraping
  the rendered `/pmc/articles/PMC.../` HTML page (what an earlier version of
  `fetch_article.py` did) isn't one of them, independent of what robots.txt
  says. `fetch_article.py` first moved to the BioC-PMC API, then (August
  2026) to the **PMC Article Datasets on AWS** described below, after NCBI
  fully decommissioned the old FTP-based bulk distribution — see the dated
  entry below.
- **Discovery (`discover_articles.search_pmc()`)**: runs ESearch against
  `db=pmc` with the `open access[filter]` tag, same as always — but that tag
  is best-effort, not a guarantee: a very recently published PMCID can be
  flagged OA before it's actually been processed and made available. Every
  ESearch hit is now cross-checked against its own PMC AWS metadata object
  (see below) before an ESummary call or a manifest slot is spent on it —
  ground truth (`is_pmc_openaccess`) instead of a search-time flag. A hit
  this check can't verify (network hiccup) is kept, not dropped — this is a
  safety net on top of the ESearch flag, not a hard dependency.
- **Fetch (`fetch_article.py`, via `pmc_aws.py`)**: pulls full text from the
  **PMC Article Datasets on AWS** — see the next section — using the exact
  same metadata object discovery already checked, so "flagged OA at search
  time, unfetchable at fetch time" is closed at its root rather than just
  filtered out earlier.
- **Rate limits (E-utilities, still used for ESearch/ESummary)**: 3
  requests/second without an API key, 10/second with a free one (NCBI
  account → Settings → API keys); higher on request to
  `eutilities@ncbi.nlm.nih.gov`. `compliance.py` defaults to a much more
  conservative 1 req/s since this harness processes articles one at a time
  anyway.
- **`eutils.ncbi.nlm.nih.gov`'s own robots.txt is a blanket `Disallow: /`**
  (verified live: `# robots.txt - robot exclusion file - back-end server
  version - no robots!` followed by `User-agent: *` / `Disallow: /`, no
  exceptions) — a backend-server default telling generic crawlers "there is
  nothing here to index," not a rescission of the E-Utilities channel NCBI's
  own usage guidelines sanction for automated PMC retrieval. `compliance.py`
  carries a narrow, cited `API_TERMS_OVERRIDE` for this exact host so
  `check_allowed()` skips the robots.txt disallow for it specifically; rate
  limiting and the contact-email `User-Agent` still apply in full. Don't
  extend that override to any other host without the same kind of citation.
- **Courtesy guidance for large jobs**: NCBI asks that big jobs run on
  weekends or 9pm-5am Eastern on weekdays, and that requests carry a `tool` +
  `email` identifier so they can contact you before blocking your IP if
  something misbehaves — hence `EVAL_HARNESS_CONTACT_EMAIL` in
  `compliance.py`'s `User-Agent`. Set it for real.

### PMC Article Datasets on AWS (August 2026 — replaces the BioC API + FTP bulk files)

NCBI fully removed the legacy FTP-hosted bulk files (including the old
`oa_file_list.csv` bulk manifest this document used to point at) the week of
August 24, 2026, migrating bulk/programmatic PMC access to a single new
channel: the **PMC Article Datasets on AWS**
(<https://pmc.ncbi.nlm.nih.gov/tools/pmcaws/>, cited via
<https://registry.opendata.aws/ncbi-pmc>). Verified live against the actual
endpoints, not just the docs, after the old `oa_file_list.csv` URL started
404ing in production.

- **Bucket**: `pmc-oa-opendata` — public, world-readable, `us-east-1`, no AWS
  account or credentials needed for read access. Fetchable over plain HTTPS
  (no AWS SDK required): `https://pmc-oa-opendata.s3.amazonaws.com/<key>`.
- **Per-article-version JSON metadata** at `metadata/<PMCID>.<version>.json`
  (most articles have only version 1) — fields include `is_pmc_openaccess`
  (the ground-truth flag this harness now checks), `is_retracted`,
  `license_code`, and direct URLs (`xml_url`, `pdf_url`, `text_url`,
  `media_urls`) to that version's objects, each as an `s3://` URL.
  `pmc_aws.s3_to_https()` converts these to the plain-HTTPS form above before
  fetching (`pmc-oa-opendata.s3.amazonaws.com` isn't a signed/authenticated
  URL, so this conversion is all that's needed).
- **No robots.txt at this host** (a request for it 404s, same as any other
  missing object) — Python's `robotparser` treats a 404 as "allow all," so no
  `API_TERMS_OVERRIDE` entry was needed here, unlike the eutils/ERIC cases
  above.
- **Rate limiting**: `compliance.py` gives this host its own low floor (0.1s)
  rather than the generic 3s fallback — it's a public, high-volume AWS Open
  Data bucket under the AWS Open Data Sponsorship Program, not one of NCBI's
  own modest research servers, and there's no published per-request ceiling
  to be conservative against.
- **Bulk inventory exists too, but this harness doesn't use it**: a daily
  S3 Inventory (gzip-compressed CSV parts, discovered via a dated
  `manifest.json`) lists every metadata object in the bucket. It's real S3
  API machinery (anonymous unsigned requests still work, but need list/get
  semantics beyond a flat file), and per-candidate metadata checks already
  cover this harness's actual need (confirm one candidate, get its URLs) —
  see `pmc_aws.py`'s module docstring if a future bulk-scan use case
  actually needs the inventory.

## ERIC (Institute of Education Sciences / U.S. Dept. of Education)

- **robots.txt**: couldn't be verified from this sandbox (its egress proxy
  blocks `eric.ed.gov`) — `compliance.py` checks it live at fetch time
  instead of relying on a policy hardcoded here, and fails safe (warns, not
  silently proceeds) if it can't be reached.
- **What this harness does**: fetches `files.eric.ed.gov/fulltext/<id>.pdf`
  directly, gated by `compliance.py`'s conservative 2s-per-request default
  (no published rate-limit guidance was found, so this is a courtesy floor,
  not a confirmed minimum).
- **Bulk alternative for scale**: ERIC publishes its own
  [API](https://eric.ed.gov/pdf/Using_ERIC_API_for_Research_Topics.pdf) (JSON,
  20-200 records per page) and a full **bulk XML export** at
  `https://eric.ed.gov/?download` — both are first-party, sanctioned channels
  for metadata at volume. Full-text PDFs still come from `files.eric.ed.gov`
  per document; there's no bulk full-text package equivalent to arXiv's S3
  bucket or PMC's OA Subset as far as this research found.
- **`api.ies.ed.gov`'s `/robots.txt` returns HTTP 403 with body
  `{"message":"Missing Authentication Token"}`** (verified live) — that's the
  standard AWS API Gateway response for a path that matches no configured
  route, meaning this host doesn't actually publish a robots.txt; it's an
  infrastructure artifact, not a policy. Python's `robotparser` reads any 403
  as "disallow everything," which would otherwise block the exact API
  endpoint named above as ERIC's own sanctioned metadata channel.
  `compliance.py` carries a narrow, cited `API_TERMS_OVERRIDE` for this host
  so `check_allowed()` skips that false disallow; rate limiting still
  applies in full. (`eric.ed.gov`'s own robots.txt, used for the
  `files.eric.ed.gov` full-text PDF fetch above, is a separate host and
  still hasn't been verified from any environment this project has run in —
  re-check it before scaling ERIC's full-text volume up.)
- **Third-party mirror**: none found. Unlike arXiv and PMC, ERIC doesn't
  appear to have an official Kaggle/Hugging Face mirror — the ERIC API/bulk
  XML export is the closest thing to a "backup source" here.

## What to actually do for the first real batch

1. Keep the 10-article smoke test as-is (arXiv PDF + ERIC PDF + PMC BioC, all
   through `compliance.py`) — a dozen requests spread across three domains at
   these rates is indistinguishable from a human downloading papers by hand.
2. Before scaling past ~50-100 articles, stop hitting `arxiv.org` and
   `ncbi.nlm.nih.gov` per-article and switch to their bulk channels above —
   pull candidate metadata from the Kaggle arXiv dataset / PMC OA Subset (or
   its Hugging Face mirror), then fetch full text from the bulk package
   rather than one request per paper. This isn't just politeness — at 15s/req
   arXiv's rate limit alone makes a large per-article batch impractical.
3. ERIC has no bulk full-text equivalent found, so a real ERIC batch will
   still mean one PDF request per article — lean harder on `compliance.py`'s
   rate limiting there, and consider running it during off-peak hours as a
   courtesy even though no explicit guidance was found requiring it.
4. Set `EVAL_HARNESS_CONTACT_EMAIL` to a real address before any run larger
   than the smoke test — it's the only way a source could reach you before
   blocking your IP if something about the batch misbehaves.
