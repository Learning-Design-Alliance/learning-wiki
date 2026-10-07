# Principle and pattern candidates

Before 2026-10-07, ingest wrote every principle and pattern an extraction proposed straight into `principles/`
or `patterns/`, as one page per article, named in that article's words. Batches wrote 430 principles and 232
patterns that way. Most of them restated a canonical page from one source, and the conversion waves spent much of
their effort folding them back in. A principle stated by one essay is a proposal, not a page.

So the extraction proposes and a second pass decides. Rationale: `scripts/candidates_lib.py`.

## The three passes

1. **Extract (no change to the prompt).** `ingest_extractions.py` writes claims, elements, strategies and
   theories as before. Each principle or pattern goes to `candidates.ndjson` instead, with:
   - its fields, the claims it cites and its source's citation;
   - in `sources/manifest.ndjson`, the source's entry lists the candidate ids under `candidates`.

   `--direct-pages` restores the old behaviour.
2. **Settle.** `settle_candidates.py --apply` runs in every batch, after the claims are linked. One model call
   per open candidate (GPT 5.6 Luna, about $0.001). The model sees the candidate, the claims it cites, the 10
   nearest canonical pages (BM25) and the 5 nearest open candidates from other sources. It answers:

   | Outcome | What `--apply` does |
   |---|---|
   | `attach` | Each of its claims that bears on the canonical page is listed under the page's `## Further evidence, not yet read against this model`, or under `### Claims` on a page not yet converted. The marker is capped by `strength_cap`. The source and the candidate's title go beside it, and the claim is flagged if it **tests** the page's relationship. |
   | `join` | Clusters the candidate with another source's candidate. |
   | `new` | A general idea nothing covers; it waits. |
   | `design` | A draft page in `designs/`. |
   | `drop` | Nothing: the candidate restates one finding or is an opinion. |

   Every claim an `attach` would write is then read again by `link_pages.py`'s verifier, and only the ones it keeps
   with the direction confirmed are written. The deciding call judges all of a candidate's claims at once. On batch
   13 it attached null results as `+`, and learning-style subgroup results to cognitive-load management, and the
   verifier kept 4 of 13. A null or non-significant result is never `+`.

   `new` and `join` stay open and are asked again on each run.
3. **Promote and update (agents, as in the conversion waves).** `settle_candidates.py --report` lists:
   - **promoted clusters**: two independent sources, or one claim whose evidence is a quant-synthesis or review
     coded q3 or above. Each is written as a canonical page in the conditional-model format
     (`principle-pattern-authoring.md`), from the cluster's claims and, where those are not enough, its cached
     articles;
   - **canonical pages whose attached claims test their relationship.** These are the pages whose model new
     evidence should change.

   Every page an agent writes or updates passes `scripts/check_design_page.py` before it is merged.

## Files

- `candidates.ndjson`: append-only, one line per candidate as extracted. Its id is `<article>:<type>:<slug>`.
- `decisions.ndjson`: append-only, one line per settling decision. The latest line for an id is its state.

Both are committed, so the next batch, on any machine, sees what the last one left waiting.

## Canonical pages

The canonical pages are those the 2026-10-02 triage classed as canonical (`eval/page-triage/triage.tsv`), plus every
converted page, each of which has a `Further evidence` section. A page promoted from a cluster becomes canonical when it is
converted.

## The backlog

`settle_candidates.py --backlog` settles the 277 non-canonical principle and pattern pages that batches wrote before
the ledger, as if they were candidates. It writes nothing: it measures what folding them would do.

**Applied 2026-10-07 (maintainer's go-ahead).** Of the 220 pages the backlog run would attach, `--fold-backlog`
asked a second model, twice and independently, whether each page really is the canonical page's idea or a narrower
case of it.
- **The two reads agreed on 97, and only those were folded** by `merge_pages.py`. On the folded-into pages, 15
  markers above their claim's cap were lowered, and 10 aliases stamped across kinds were removed.
- **The refusals read right**: Hunter's model is not Direct Instruction, and JiTT is not generic just-in-time
  support.
- **Every decision and refusal is in `backlog-folds.ndjson`.**
- **The 179 pages not folded are open candidates in the ledger** (`origin: page`), so a later batch can join a
  second source to them.

**A synthesis promotes only an extracted candidate.** An existing page's claim links include every claim later
linking added, so for a page only two independent sources promote.

**Promoted:**
- `principles/match-interventions-to-stages-of-concern`: Hall & Rutherford (1983), with Hall (1978) folded in;
- `principles/include-caregivers-as-self-regulation-coaches`: Murray & Rosanbalm (2017).

Both were converted by agents and pass `check_design_page.py`, and neither has a claim that tests its relationship.

**Not promoted:** Bue (1979) with Chorianopoulos (2018). The pairing is loose, and teaching- and learning-style
compatibility is the matching idea that `learning-styles-matching-does-not-improve-learning` counts against.

## First runs (2026-10-07)

| Run | Candidates | attach | new | join | design | drop | Cost |
|---|---|---|---|---|---|---|---|
| Backlog, BM25 neighbours only | 277 | 148 | 109 | 6 | 4 | 10 | $0.24 |
| Backlog, whole canonical index | 277 | 220 | 41 | 5 | 2 | 8 | $0.28 |
| Batch 13 (47 articles) | 28 | 17 | 8 | 0 | 2 | 1 | $0.03 |

- **The canonical index matters.** With only BM25's ten neighbours, the model called a support-fading progression
  `new` because Scaffolding and Fading was not among them.
- **Batch 13 wrote no principle or pattern page.** Before the ledger it would have written 28. Of the 13 claims its
  attachments proposed, the verifier kept 4. No cluster has a second source yet.
- **Backlog clusters reported for promotion:**
  - Hall (1978) with Hall & Rutherford (1983): stages of concern;
  - Murray & Rosanbalm (2017): adults in self-regulation interventions;
  - Bue (1979) with Chorianopoulos (2018). This join looks loose, so whoever promotes it must judge it first.
