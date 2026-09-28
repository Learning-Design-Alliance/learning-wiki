# Targeted pass: attach named syntheses to the claims they test

Usage scenario S1 (Italian A1, adults, self-paced mobile) showed that a topic sweep adds one-study
claims but not the handful of syntheses a practitioner would rely on. This pass adds those
syntheses **as evidence on the claims they test**, so existing claims gain a second study, and
creates a claim only where none exists.

Candidates come from two signals: syntheses a model names from memory (a recall aid only) and
OpenAlex's citation-ranked meta-analyses and reviews per topic, which do not depend on memory.
Nothing either signal says about a paper is used: every fact comes from the paper's own record and text.

## For each synthesis you are given

1. **Identify it** with Crossref (`https://api.crossref.org/works/<DOI>` or
   `works?query.bibliographic=...&mailto=contact@learningdesignalliance.org`). Author, year, title
   (Crossref `title` plus `subtitle` after a colon, word for word), journal, volume, issue and pages
   come from that record. If it does not resolve, drop it and say so.
2. **Check whether the wiki already cites it**: `grep -rli "<doi>" claims/`. If it does, read that
   entry and extend rather than duplicate.
3. **Read it**: open-access full text if you can fetch it (Unpaywall
   `https://api.unpaywall.org/v2/<DOI>?email=contact@learningdesignalliance.org`; respect robots.txt
   and 403s, do not work around them), otherwise the abstract (OpenAlex
   `abstract_inverted_index`; run `set -a; . /etc/eval-harness.env; set +a` and add
   `&api_key=$OPENALEX_API_KEY`, never printing the key). Record which you read.
4. **Find the claims it tests**: `python3 scripts/mcp_server.py --call search '{"query": "...", "kind": "claim"}'`
   and grep. Read each candidate claim page. The synthesis bears on a claim only if it tests that
   proposition (same construct, a comparable population); "related topic" is not enough. At most
   four claims per synthesis.
5. **Write the evidence** on each claim it tests, following `scripts/eval/gapfill/TASK.md`'s rules
   exactly (every number from what you read, never computed or rounded; `(abstract only)` in the
   codes line when you read only the abstract, plus a sentence on what the abstract did not
   establish; q codes per its checklist; the same DOI and codes as any page already citing it):
   - append one `### Author Year` entry to `## Evidence` (codes line as the other entries on the
     page; do not add a kind/rigour span, a script codes that);
   - add one subclaim under `## Subclaims` linking to it;
   - if the synthesis qualifies or contradicts the claim, say so in the entry and add a sentence to
     `## Discussion`; never bend it to fit;
   - change nothing else on the page (the title stays; if the synthesis shows the title overstates,
     say so in Discussion and report it).
6. **Only if no claim fits**, create one claim page in the Claim template of CLAUDE.md
   (`status: draft`, `generated: {by: claude/unspecified, at: 2026-09-30}`, `id:` equal to the slug,
   the banner line), after checking the slug is free. At most two new claims per agent.

## Rules

- Edit only `claims/*.md`. Never touch index files, never commit, never add `verified:`.
- Other agents are working on other syntheses at the same time; if a claim page changed since you
  read it, re-read before editing.
- When done, run `python3 scripts/lint.py` and report anything on your pages.
- Report: per synthesis, the DOI, what you read, each claim it was attached to (with the subclaim
  codes) or why none fitted, new claims created, and anything you could not verify.
