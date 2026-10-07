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
