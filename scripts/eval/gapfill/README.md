# Gap-fill: evidence for claims that have none

`TASK.md` is the contract one in-session agent follows to fill the `## Subclaims` and
`## Evidence` sections of **one** claim page that has no evidence. The claims to work on
come from `python3 scripts/priority_worklist.py --queue gap`, ranked by how many pages
cite them.

## The loop (what a session does)

1. Take the next claims from the gap queue. Skip a page whose claim is a near-duplicate of
   one already filled, and copy that page's verified draft in instead (for example
   `testing-effect-improves-retention` and `retrieval-practice-improves-retention`).
   The duplicate stays in the near-duplicate backlog; it is not merged here.
2. Give each agent its own folder outside the repo, and tell it to write only `output.md`
   there. Agents never edit the wiki.
3. Read every report before applying its draft. The fixes so far:
   - a code read off an abstract's wording ("small to medium") becomes `i?`;
   - an agent's conversion of one metric into another is removed;
   - a truncated Crossref title is restored to the full published one;
   - one study cited on several pages gets the same `q` code everywhere.
4. Apply by replacing the two sections, then run `sync_evidence_codes.py --apply`,
   `add_evidence_summary.py --apply`, `fix_dead_anchors.py --apply`,
   `enrich.verify_page_citations(path, apply=False)` (expect no findings),
   `log_revision.py`, `build_indexes.py` and `lint.py`.
5. If the evidence contradicts the page's own Discussion, correct the Discussion in the
   same commit and say so in the commit message. A title the evidence contradicts is
   flagged in the Discussion, not renamed, because renaming breaks links.

## Headless Chromium through the proxy

The session proxy re-terminates TLS, and Chromium does not read the system trust store,
so it fails with `net_error -202`. Trust only the proxy's own CA keys:

```bash
awk 'BEGIN{n=0} /BEGIN CERT/{n++} {print > ("ca" n ".pem")}' /root/.ccr/ca-bundle.crt
for f in ca*.pem; do openssl x509 -in $f -noout -subject | grep -q Anthropic && \
  openssl x509 -in $f -pubkey -noout | openssl pkey -pubin -outform der | \
  openssl dgst -sha256 -binary | base64; done | sort -u | paste -sd, > proxy_spki.txt
chrome --headless=new --no-sandbox --proxy-server="$HTTPS_PROXY" \
  --ignore-certificate-errors-spki-list="$(cat proxy_spki.txt)" --dump-dom <url>
```

Every other certificate is still verified. Never use `--ignore-certificate-errors`.

## What 81 claims taught

- **Most sources could be read only as abstracts.** Publisher sites block automated
  access. Every entry says which it was, and an abstract without an effect size is `i?`.
- **The evidence qualified the claim more often than it simply supported it**, and in
  several cases contradicted the page: advance organizers, exercise timing, learner-built
  graphic organizers, dialogic reading, checklist evaluation of online sources.
- **Opus and Sonnet agents produce drafts of similar quality**; use Sonnet in the long tail.
- **An agent sent a personal email address to Unpaywall once.** The contract now forbids
  sending any personal identifier to an outside service.
