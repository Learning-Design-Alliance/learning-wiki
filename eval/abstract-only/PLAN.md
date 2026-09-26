# Plan: ingesting ERIC records we can read only as abstracts

**Status:** decisions 1 and 2 taken by the maintainer, 2026-09-25; decision 3 open. Nothing below is built yet.

## Why

Most ERIC journal records have no hosted full text (`e_fulltextauth: 0`). For four topics alone,
retrieval practice, worked examples, formative assessment and peer tutoring, there are **3,228
peer-reviewed** such records. Many abstracts state a design, a sample and a result. For example,
EJ1007216 (a peer-tutoring meta-analysis) reports 26 experiments, 938 students and Tau-U = 0.75,
CI 0.71–0.78. That is a citable claim, and today discovery skips the record entirely.

The risk is that an abstract is the author's summary, not the finding. It leaves out moderators and
null results, and it rounds. So the plan has three parts. First, prefer full text whenever it can be
found. Second, when it can't, ingest from the abstract only in a form that says so on every page and
record. Third, measure how often abstract-only claims turn out wrong before scaling up.

## What the sample showed (200 records, `peerreviewed:T AND e_fulltextauth:0`)

| signal | records |
|---|---:|
| has a URL (publisher landing page) | 134 |
| has a results sentence ("results showed…", "findings indicate…") | 49 |
| states a sample size ("938 students") | 19 |
| reports a statistic (d, g, r, p, F, CI, effect size) | 13 |
| median abstract length | 136 words |

Roughly **a quarter of the abstracts carry a result**, and about **1 in 15 carries a number**. Most of
these would be coded `i?`.

## Pipeline

1. **Discover.** Query ERIC with `e_fulltextauth:0 AND peerreviewed:T`, restricted to
   `publicationtype` "Reports - Research" or "Information Analyses" and `abstractor: "As Provided"`,
   which means the author wrote the abstract rather than an ERIC indexer. The discovery cache key gets
   its own version (`SEARCH_VERSIONS`), so these results never mix with the full-text source.

2. **Screen, free and deterministic.** Keep an abstract only if it has at least 100 words, names a
   design (randomized, quasi-experimental, meta-analysis, participants, sample) and has a results
   sentence. Anything else is recorded as E3 `no-ingestable-content` with the reason "abstract states
   no finding". Recording it matters: it keeps the record from being rediscovered.

3. **Try for the full text first.** Most of these papers are published somewhere.
   - Establish the DOI. ERIC gives `source` (the journal) and `sourceid` (`v42 n1 p39-55 2013`).
     Search Crossref by title and journal, and accept a hit only when **journal, volume and first
     page all match**. This is the same three-coordinate rule `resolve_citation_metadata.decide()`
     uses before trusting a title. Tested on EJ1007216: exact match, `10.1080/02796015.2013.12087490`.
     No match means no DOI; the tool never takes the nearest hit.
   - Look for an open-access copy through the Crossref `link` field, PMC's ID converter and Europe
     PMC. OpenAlex's open-access locations would help, but its free, keyless quota ran out today on
     this network. A free OpenAlex API key, stored in `/etc/eval-harness.env`, fixes that. Unpaywall
     needs an email address with every request, so it is out unless you decide otherwise.
   - If full text is found, the record goes through the normal full-text path and none of the steps
     below apply.

4. **Extract from the abstract.** Use a prompt variant, `v134-abstract`, which is v133 with these
   changes:
   - one to three claims at most, with no elements, patterns or principles, since an abstract rarely
     describes a design in enough detail;
   - `i` coded only when the abstract prints an effect size, otherwise `null` (rendered `i?`);
   - `q` taken from the design the abstract states and nothing stronger (the observations rule:
     never infer a stronger design than the source states);
   - no `study_record`.

   The existing quote gate works unchanged, because the cached "article text" is the abstract, so
   every quote has to appear in it.

5. **Mark it everywhere.** Readers and agents must never mistake an abstract-only reading for a full
   one:
   - Evidence entry: the codes line gains `abstract only`, for example
     `` `q3 · meta-analysis (abstract only)` · `i2 · Tau-U 0.75` · `n=26 experiments, 938 students` ``.
   - Manifest: the `ingested` line gains `"basis": "abstract"`. It is additive and append-only, and
     `lint.py`'s manifest check learns the field.
   - Scorecard: a new row, "Claims resting only on abstract-only evidence".
   - Upgrade path: when full text for the same record is ingested later, the full-text entry replaces
     the abstract entry and a later manifest line records `"basis": "full-text"`.

6. **Ingest** through the normal chain (DOI gates, verify, lint), unchanged.

## Pilot before scaling: is an abstract a safe basis?

Take **40 records** that pass the screen and **also** have an open-access full text, so the answer
can be checked.
- Extract each one from its abstract only (GLM on `v134-abstract`, about $0.003 per record).
- Have an Opus agent check every abstract-only claim against the full text: supported, overstated,
  missing a qualifier, or wrong.
- **Decision rule:** go ahead if at least 90% of claims are supported and none is wrong in direction.
  If the pilot misses that bar, abstract-only claims stay out of the wiki. The records then go to
  `priority_worklist.py` as "needs full text" instead.

Cost: about $0.15 for GLM on 40 records, plus 40 agent checks in session (around 1–2 minutes each).

## Decisions for the maintainer

1. **Is an abstract an acceptable basis?** *Decided 2026-09-25: yes, as weak evidence with a
   conditional note.* An abstract-only entry is admitted, but it must say so where a reader
   will see it: `(abstract only)` in its codes line, and a sentence in the page's Discussion
   saying what the abstract could not establish (typically the effect size, the sample, or the
   moderators). The `q` code still reflects the design the abstract states, never a stronger
   one; the note is what carries the weakness. The pilot below still decides whether the
   pipeline runs at scale.
2. **An OpenAlex API key.** *Decided: the maintainer is getting one.* Store it in
   `/etc/eval-harness.env` as `OPENALEX_API_KEY` (never in the repo); step 3 uses it for
   open-access locations.
3. **Should abstract-only evidence cap a claim's status**, for example never above `draft` until
   a full-text entry exists? *Open.* The plan marks the evidence but leaves `status` alone,
   because status describes whether a page is written, not how it was sourced.

## Work to build (after the decisions)

| change | where |
|---|---|
| `search_eric_abstracts()` and the screen | `scripts/eval/discover_articles.py` |
| DOI by three-coordinate Crossref match | `scripts/doi_resolver.py` (pure match function, tested offline) |
| open-access lookup, abstract as article text | `scripts/eval/fetch_article.py` |
| `v134-abstract` prompt | `prompt_versions/` |
| `basis` on manifest lines and evidence codes | `scripts/ingest_extractions.py`, `okf_lib`, `lint.py` |
| scorecard row | `scripts/health_scorecard.py` |
