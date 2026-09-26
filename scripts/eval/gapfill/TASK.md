# Gap-fill: evidence for one evidence-less claim page

You are filling the `## Subclaims` and `## Evidence` sections of ONE claim page in the
learning-wiki at /home/user/learning-wiki (read-only for you: do NOT edit any file in that repo).
Read /home/user/learning-wiki/CLAUDE.md sections "Claim" template, "Evidence quality tiers (q)",
"Impact magnitude (i)" and INCLUSION.md for conventions.

## Steps
1. Read the claim page. Identify 1–3 studies that directly test the claim: prefer a
   well-powered meta-analysis or systematic review, then a strong primary study.
   Prefer the canonical source the page's own TODO comment points to.
2. For each candidate, get its DOI and confirm it against Crossref:
   `curl -s https://api.crossref.org/works/<DOI>` — title, authors, journal, volume, issue,
   pages and year in your citation MUST come from that record. Never write a DOI you have
   not resolved this way. No DOI? Use a stable URL and say so.
   The title is Crossref's `title` plus its `subtitle` after a colon, word for word. If
   Crossref has no subtitle, write none: a subtitle from memory is an invented title.
3. READ the article itself: open-access full text (PMC, publisher OA page, ERIC PDF,
   author manuscript) or, failing that, at minimum the publisher abstract. Outbound HTTPS
   goes through $HTTPS_PROXY; `curl` works. JS-rendered pages: `/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless=new --no-sandbox --proxy-server="$HTTPS_PROXY" --ignore-certificate-errors-spki-list="<SPKI hashes of the session proxy CA keys; see README.md>" --dump-dom <url>`. The SPKI list trusts ONLY the session proxy's CA keys (it re-terminates TLS); every other certificate is still verified. Never use --ignore-certificate-errors or any flag that disables verification wholesale. Record which you read (full text / abstract only).
4. Every number you write (effect size, k, n, CI) must appear in what you read. A number
   another paper reports ABOUT your study does not count: cite it only from the study itself.
   Never compute a difference, midpoint, average or conversion, and never round (0.198 is
   0.198, and it is below 0.2). `i` codes only a reported standardized effect (d, g, r, OR):
   never raw units such as GPA points, never a word like "moderate", and never a single-case
   overlap statistic (Phi, Tau-U, PND, LRR), which are `i?` with the value in the prose.
   When effects are reported as a range, code the lower bound. Copy one
   short verbatim quote per study supporting the finding.
5. If the evidence actually contradicts or heavily qualifies the claim, say so — do not
   bend it. If you cannot find a readable source, write NOTHING rather than guess.

## Coding checklist (the corrections reviewers made most often)

- `q4` only for a pre-registered RCT or a meta-analysis whose power is established; do not
  write "well-powered" otherwise. A systematic review or a meta-analysis of correlational
  studies is `q3`; a narrative review, survey or quasi-experiment is `q2`; a single-case
  design with a handful of participants, or a theoretical paper, is `q1`.
- Before coding a study, `grep -rl <doi> /home/user/learning-wiki/claims/` (read only). If it
  is already cited, use the same DOI and the same `q`/`i` codes unless you read more of it
  than that page did, and say so. If a paper has two DOIs (a JSTOR one and the publisher's),
  use the publisher's.
- If you read a conference version, a dissertation chapter or a companion chapter instead of
  the cited article, say so in the entry, and take numbers only from what the cited article's
  own abstract or text states.
- Link only to wiki pages that exist: check with `ls` before writing a link.
- If you read only the abstract, put `(abstract only)` in the entry's codes line, as in
  `` `q3 · meta-analysis (abstract only)` ``, and say in the entry what the abstract did not
  establish. Abstract-only evidence is admitted as weak evidence (maintainer decision,
  2026-09-25); the note is what tells a reader so.

## Output: write exactly one file, <your folder>/output.md, containing:

```
## Subclaims

`q4 i2` One-sentence summary of the finding and its scope. [→ Author Year](#author-year)

## Evidence

### Author Year

Full APA citation from the Crossref record. [doi:10.xxxx/yyyy](https://doi.org/10.xxxx/yyyy)

`q4 · pre-registered RCT / meta-analysis / ...` · `i2 · medium effect, d=0.47` · `n=225 studies`

2–4 plain-language sentences: design, participants, conditions, findings.
```

then, after a line `---PROVENANCE---`, one line per study:
`<DOI> | read: full text|abstract | <url read> | "verbatim quote"`

Heading anchors: `### Freeman et al. 2014` -> anchor `#freeman-et-al-2014`. Codes follow
CLAUDE.md: q 1–4; i 0–3 or `i?` when no effect size is reported (never i0 for "unreported").
To find an open-access copy, use the Unpaywall API with the organisation's contact address and no other: `curl -s "https://api.unpaywall.org/v2/<DOI>?email=contact@learningdesignalliance.org"` (read `best_oa_location.url_for_pdf` / `url`). Never send any other email address or personal identifier to any external service. Start every shell command with `cd <your folder> &&` so relative writes (curl -o, python open()) never land in the repo. Keep helper scripts in your own folder. Report back in 3 lines: studies used, what you read,
anything you could not verify.
