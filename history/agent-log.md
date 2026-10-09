# Agent history

Dated entries moved out of `CLAUDE.md` on 2026-10-09, verbatim, newest first. Each records what
a session changed across the wiki, why, and the numbers that justified it. `CLAUDE.md` keeps the
standing rules these entries produced; read the entry before changing one of them. New entries go
at the top, under this paragraph.

## 2026-10-10 (later) — search for design work: situation index, learner variables canonical, a designer query set

The maintainer's retest asked how well the wiki serves learner analysis, context analysis and
choosing patterns and principles. 30 designer queries found: no learner-variable page in the top
ten even for its own title ("working memory"), no converted page in the top five for any of ten
learner queries, and the best guidance (the 1,117 rows of the 77 `## Fitting the design to a
situation` tables) reachable only from its own page.

- **`situation-index.json`** (`scripts/build_situation_index.py`, run by `build_indexes.py`,
  `--check` in CI) collects every row with its tags from `evidence-dimensions.json` (expertise,
  age, population band, knowledge type, setting, duration), the claims its basis cites with their
  markers, and `basis_kind` (`claim` 543, `untested` 573). 690 rows name their situation in words,
  not tags; conservative patterns read 567 of them as `inferred_tags` (single-session,
  workplace-clinical, classroom, online-self-paced, novice, child, adult), checked against the
  rows they match. `advanced` is never inferred: its patterns caught the teacher ("an
  inexperienced teacher"), and "adult" caught the facilitator ("scarce adult time"). 550 rows
  still carry neither; they name facets the vocabulary has no value for (second language of
  instruction, stakes, class size, scarce facilitator time), which the `text` argument reaches.
- **MCP `situations` tool**: tags and/or words → the matching rows, grouped by page, pages
  covering more of the tags first; no arguments returns the vocabulary.
- **Site: "Design for a Situation"** (`docs_hooks/situations.py`): one generated page per tag
  plus an index, 1,389 links, all resolving. No wiki page is edited.
- **Learner variables are `canonical: true`** (`settle_candidates.py --mark-canonical` now stamps
  every learner-variable page; they are not added to `canonical_keys()`, the ledger's index).
  Agent search also gives +10 to a page whose title *is* the query.
- **`eval/search/designer-queries.json` + `scripts/eval_search.py`**: 38 search queries with
  acceptable answers and 14 situation checks. main → this change: learner hit@5 42% → 67%, all
  68% → 76% (hit@1 37% → 45%); situations 14/14. Goal queries stay at 50%: "improve writing",
  "build conceptual understanding", "long-term retention" land on claims, not the principle,
  which goal-type hub pages would fix (a maintainer decision).
- **Found, not fixed: learner-variable pages are nearly unlinked.** Only 7 of 12 have any inbound
  link, and none links to `prior-knowledge`; claims reporting learner-characteristic findings do
  not link into them, which the learning-design-spec join (`spec/learners.md`) relies on.

## 2026-10-10 — products and research methods; a tighter independence rule; search that finds the main page

- **Two kinds** (maintainer): `products/` for named products and programmes others adopt (a
  programme's own tools, frameworks and indicators are components on its page) and
  `research-methods/` for education-specific research methods (general social-science methods
  are not pages). The ledger's `artifact` outcome became `product` and `research-method`;
  re-settling the open candidates ($0.18) wrote 42 product and 32 method pages, and the
  duplicates it made (To&Through three ways, CRIS three ways, PAI, Freshman On-Track,
  Inclusive Innovation) were folded. The settle prompt now lists existing product and method
  names so later candidates reuse them. An AI-assisted qualitative codebook method was dropped.
- **Independence** (maintainer): two sources promote a cluster only when they share no author
  and no publisher (web domain, the publisher a report names, or a report's DOI prefix, which
  is the registrant's: 10.51388 is Digital Promise's). An unidentifiable source is not
  independent. Promoted clusters 39 → 21.
- **Search on the site** (maintainer's scale retest): Pagefind 1.3.0 dropped results for words
  at chunk boundaries ("retrieval practice" found 3 pages); 1.5.2 finds 884. The main page for
  a topic ranked 34th–70th; the search page's Main pages list now puts it first for retrieval
  practice, worked examples, phonics, growth mindset, cognitive load and spaced practice
  (spaced practice through the alias). Learning styles' key page is a claim, which the list
  does not search. One line per result; a header search box on every page.
- **Agent search** folds titles that differ by word ending, and weights inbound links more;
  99 stem-equal duplicates were folded (53 strategies, 20 elements, 9 theories, 17 claims).
- **Deploys replace the published tree**, keeping open previews, so gh-pages stops growing
  with renamed pages. Not done: moving the long tail off Pages, needed near 85,000 pages.

## 2026-10-09 (later) — the scale fixes: a two-tier site, Pagefind, rotated log, compact indexes, a shorter CLAUDE.md

After batch 47 the maintainer's scale test found the site heading past Pages' 1 GB limit, a 20 MB
lunr index, a 3.4 MB claims listing, a 5.3 MB log page, slow agent search and a 272 KB CLAUDE.md.
Fixed in four PRs (#205 ledger extension, #206 search, #207 generated files, and the site and
guide PR), measured on the same 18,600 pages, before → after:

| | before | after |
|---|---|---|
| built site | 658 MB | 251 MB (60 MB of it the Pagefind index, fetched in chunks) |
| site build | 284 s (mkdocs alone, locally) | 129 s (mkdocs 16 s, long tail 33 s, Pagefind ~80 s) |
| search download | 21 MB `search_index.json` | ~350 KB a query (script, wasm, metadata, one or two chunks) |
| claims listing page | 3.6 MB | 18 KB landing + 41 letter pages of ≤400 |
| log page | 6.3 MB rendered, 5.3 MB file | not on the site; `log.md` 3.0 MB (October only) |
| wiki-index / reverse-index | 11.6 / 9.2 MB | 10.9 / 6.5 MB, one record per line |
| MCP search, first query | stat of every page each query | ~0.1 s; warm ~8 ms |
| CLAUDE.md | 272 KB | 120 KB (history moved here, verbatim) |

- **Two tiers** (`docs_hooks/two_tier.py`, `scripts/build_longtail.py`, `scripts/build_site.sh`): mkdocs
  renders the curated kinds and the canonical elements and theories; the rest is rendered as light pages
  at the same URLs, the evidence-code legend shared rather than repeated (it was 5.7 KB of an 11.6 KB
  claim page). Every internal link in the built site resolves (333,699 checked; mkdocs' own 404 page
  uses absolute paths that resolve once deployed).
- **Search**: Pagefind over both tiers, filterable by kind; MCP search ranks canonical pages and
  well-linked pages first, with a title-only pass for long canonical pages BM25 ranked low.
- **Duplicates**: 158 strategies sharing a normalised title with another were folded
  (`merge_pages.py`, the one with more inbound links kept, the other an alias), and
  `write_design` reuses a programme's existing design page (two pairs folded).
- **Previews** run only for PRs that change the site build, or carry the `preview` label.
- **Still open**: only 17% of claims (1,812 of 10,549) are linked from a curated page; the
  rest are reached by search, listings and other claims. The near-duplicate title backlog
  (`find_title_duplicates.py`, ~943 pairs before these folds) is otherwise untouched. gh-pages keeps the old `search/search_index.json`
  and Material claim pages until overwritten, since the deploy uses `keep_files`.

## 2026-10-09 — batches 16–47 from the hub; elements and theories join the candidate ledger; stopped for scale

- **Batches 16–47 and a Campbell recovery** (PRs #174–#201 and the batch-47 PR) read the hub queue to 1,910 ingested of
  2,584 queued (507 not yet tried, 136 unfetchable). The AIED queue (1,477) is untouched. From batch 39 a batch is 100
  entries at concurrency 10 (about $0.45–0.80, long reports up to $2); one driver, never two batches at once.
- **New fetch routes**: `source_lists.py --campbell` (a Campbell review's DOI by title in Crossref, then its PMC copy, else
  ERIC: 18 of 51 recovered; Wiley 403s automated PDF downloads); `fetch_article` reads DSpace 7 items
  (`digitalpromise.dspacedirect.org`, ~280 hub entries) through the REST API's ORIGINAL bundle, since their pages are
  Angular shells. JavaScript-rendered pages (Campbell, some ESSA) still fail and go to `fetch-failed.ndjson`.
- **A container restart changes the proxy port, and processes started before it keep the old one**: every model call
  then fails. After a restart check `/proc/<pid>/environ` against `$HTTPS_PROXY`; stop, `git stash`, and `--resume`.
- **Elements and theories now go through the candidate ledger** (batches wrote ~0.7 element and ~0.4 theory pages an
  article, mostly products, programmes and one paper's framework). Settle decides them against a canonical index (pages
  no batch wrote, plus batch pages with 10+ inbound links: 387 elements, 208 theories) with a new outcome, **`artifact`**
  (a product, tool, dataset, instrument or one programme's framework: recorded, no page, until the maintainer decides
  on a kind), and resolves the links the article's own pages made to the candidate. Batch 47, the first run: 0 element
  and 0 theory pages (against ~65 and ~35 before); of 130 candidates, 88 artifact, 20 attach, 11 design, 9 drop, 1 new.
- **Stopped for scale (maintainer's scale test, 2026-10-09)**: ~18,800 pages; the published site (702 MB) passes the
  1 GB Pages limit at ~+5,000 articles; generated JSON and `log.md` grow every batch; only 13% of claims are reachable
  from a curated page. Do not restart batches until the site is split (static curated tier, dynamic long tail), search
  moves to Pagefind or the FTS server, generated files are split or rotated, and products/programmes have a kind.
- **Promotion clusters are mostly not independent**: of 17 reported, 9 pair one author or one report across years
  (maintainer: "a research agenda, not independence"). Tightening the rule waits for more clusters; research-methods
  candidates (Schochet, Gill, Kassler) stay open, not pages, until the lists are finished.

## 2026-10-07 (later) — curated lists come before topic search; batches 14 and 15 from the Learning Agency hub

- **Two curated lists come first** (maintainer): the Learning Agency's Renaissance AI and Education Resource Hub (3,927
  published entries) and the AI in Education Knowledge Base (`edtechdev/aied`, 1,647 papers, CC0). Before this the wiki
  had read 14 and 2 of them.
- **`scripts/eval/source_lists.py`** measures coverage (manifest id, DOI or title; or a wiki page citing the DOI or URL)
  and writes a priority queue to `eval/runs/queues/` (ignored). **The hub has no licence, so none of its data is
  committed**: the list is read at run time. Queue order:
  1. the hub's research domain, WWC, ESSA, Campbell, Mathematica, RELs and the two journals first;
  2. learning-engineering practice;
  3. policy;
  4. AIED.
- **robots.txt is checked up front.** It refuses 1,669 hub entries (WestEd, Learning Policy Institute, Education Trust,
  TNTP, some Brookings). **`--eric-fallback`** finds 489 of them in ERIC with full text, by exact title, and queues the
  ERIC copy. Hub queue: 2,584 entries. AIED: 1,477 (668 arXiv, 809 by DOI).
- **`fetch_article` has a `web` source**:
  - It follows a landing page to the work's own PDF. WWC intervention reports, RELs, JEDM, JLA, CREDO and UChicago
    return full reports.
  - ESSA, Mathematica and NWEA return their summary pages.
  - Campbell's pages are JavaScript-rendered and fail.
- **`run_scrape_batch.py --queue <files> --take N`** takes the next N unsettled entries before any `--pmc`/`--eric`
  search. A queue entry that cannot be fetched goes to `eval/runs/queues/fetch-failed.ndjson`, so the next batch moves on.
- **Batches 14 and 15** (100 hub entries, WWC first, all fetched): about 640 new pages each time. Mostly claims; the
  WWC-reviewed programmes were written as `designs/` by the candidate settle step (18 and 16). About $1.90 a batch.
  Generation was $0.20–0.33; evidence coding was most of the rest, because WWC reports are long.
- **Design pages from candidates now resolve their related links across folders**: four links pointed at elements the
  same article produced.

## 2026-10-07 — batches no longer write principle or pattern pages; a candidate ledger decides; batch 13

- **Ingest writes each extracted principle or pattern to `eval/candidates/candidates.ndjson`, not as a page**
  (`candidates_lib.py`; the README there has the process). Batches had written 430 principles and 232 patterns,
  one page per article in that article's words, and the conversion waves spent much of their effort folding them
  back in. **`settle_candidates.py --apply` runs in every batch** after linking. It does three things:
  - **Decides each candidate** against the whole canonical index (the triage's canonical pages plus every converted
    page), as `attach`, `join`, `new`, `design` or `drop`.
  - **Writes an `attach`'s claims** under the canonical page's `## Further evidence, not yet read against this
    model`. Only the claims `link_pages.py`'s verifier keeps are written, and markers are capped.
  - **Reports clusters for promotion**: two independent sources, or one synthesis at q3 or above. Promotion and
    model updates stay with agents, as in the waves, and every page they write must pass
    **`scripts/check_design_page.py`**, the waves' checks as a script.

  `--direct-pages` restores the old behaviour. **Do not re-enable it in the batch.**
- **Batch 13** (47 articles fetched): 44 ingested and 3 rejected, adding 309 pages and **no principle or pattern
  page**. Its 28 candidates settled as 17 attach, 8 new, 2 design and 1 drop. Only 4 of the 13 claims proposed for
  attachment passed the verifier: it refused null results tagged `+` and learning-style subgroups attached to
  cognitive-load management. **Backlog dry run** (`--backlog`, 277 non-canonical batch pages, writes nothing): 220
  would attach, 41 are new. Folding them is the maintainer's call.
- **`code_kind_rigour.py --new` re-coded the whole corpus in a fresh container**, resetting rigour to `r?` on about
  2,000 claims wherever it had no text of the study.
  - **Cause:** it read "has a kind" from a block `units()` had already stripped of its kind span, so every entry
    looked new. Only the ignored decision cache had hidden this.
  - **Fix:** it now reads the span from the page. The 2,485 entries were restored from the committed text, and the
    batch's 158 new entries were coded properly.
  - **A step whose correctness depends on an ignored cache is a bug.** Check a fresh-container batch's claim diff
    before committing.
- **ERIC discovery asks for 25 results per topic** and takes the topic's share. Asking for 2 per topic across 1,400
  wiki topics had cost about 290 queries for 45 articles.
- **The backlog was then folded** (maintainer's go-ahead).
  - **Folded:** 97 of the 220 pages, the ones two independent second reads agreed on (`--fold-backlog`,
    `eval/candidates/backlog-folds.ndjson`). The other 179 are open candidates in the ledger.
  - **Promoted** to canonical pages by agents: the stages-of-concern principle (Hall 1978 folded into Hall &
    Rutherford 1983) and the caregivers-as-self-regulation-coaches principle.
  - **Not promoted:** Bue (1979) with Chorianopoulos (2018), a loose pairing around style matching.
  - **Waiting for the maintainer:** two two-source clusters, industrial-arts career education with value education,
    and Rassaei (2011) with Adamson (1983).
  - **Cost:** batch 13 cost $3.53 all in. $2.00 of it was the kind/rigour bug, so it should have been about $1.53.
- **A fresh container needs `pip install -r requirements-eval.txt`** before a batch. Without pypdf, 45 of 50 PDFs
  failed to fetch.

## 2026-10-05 (late night) — conversion wave 7: the first wave below the core; "no claim here" is not "no research"

- **Fifteen principles converted** (`eval/page-triage/wave-7.md`), each with 3–5 inbound links: sequencing, social
  presence, procedural learning, positive self-talk, observation and shadowing, memory consolidation, explicit
  vocabulary instruction, classroom management plans, developing cultural awareness, criterion- and norm-referenced
  testing, flipped learning, flexible grouping, wise feedback across difference, supporting gifted students and
  text-to-speech. Two are partly tested (vocabulary, classroom management); thirteen keep a labelled default design.
  Seven frontmatter DOIs and one journal (Dudai 2004 is *Annual Review of Psychology*) corrected against Crossref.
- **Tested with 30 briefs (about $5.9): blind pairs 76–44** (sparse 43–17, complete 33–27), the weakest wave;
  accuracy 3.08 → 3.78, decision value 3.57 → 3.95. DeepSeek picked the first-shown answer 48 times in 60.
  Seven briefs lost 1–3; one row each (or one regeneration, for a garbled answer) took five to 3–1 or 4–0 and two to 2–2.
- **New lesson: answers turned "no claim in this wiki compares X" into "X has never been compared"**, and graders
  marked it inaccurate (flipped learning). **A page stating an absence of claims must say it is an absence in the
  wiki, not in the literature.** The other losses were wave 6's lesson again: the brief's own stages, assessment
  criteria and learner (a tutor being trained, not students) must be taken as given.
- Open: the agents' lists (about ten duplicate pairs, ten overstated titles, homepage citations, miscoded kinds, and
  ingest candidates such as Richardson et al. 2017 and Kraft et al. 2018) are in `wave-7.md`.

## 2026-10-05 (late night) — wave 6's claim findings settled

- **Six duplicate claims merged** (`merge_claims.py`): summarization with training into summarization; overjustification
  into `rewards-undermine-intrinsic-motivation`; the Johnson & Johnson digests (`johnson-meta-analysis-…`,
  `cooperative-learning-meta-analysis-…`) into `cooperative-learning-higher-achievement-than-competitive-individualistic`,
  now titled as three second-hand digests; both generative-learning claims into `generative-processing-improves-learning`,
  now titled as self-explanation (Bisra et al. 2018 is its only evidence). **Pages folded**: `elements/debriefing` into
  `elements/debrief`; the principles `multimedia-projects` and `multimedia-literacy-through-production` into
  `patterns/learning-by-producing-pattern` (across kinds, no alias). **Not merged**: the two Benner (2008) PBIS claims and
  the two autonomy claims (distinct findings), and `strategies/debriefing` (a strategy, not a duplicate element).
- **Claim corrections** (three agents, from the pages' own entries): 23 titles rewritten (link text on 162 links), among
  them laptop notes (the replication failed), math anxiety (a correlation), teacher expectations (one associational
  cohort), growth mindset (d = .11), four Miller (2015) TBL claims (two non-randomised cohorts), wait time (associations
  from abstracts), and five testimony or web-essay sources now named as such; stale text on about ten pages; `i` codes
  with no printed effect size set to `i?` on nine; q recodes where the entry shows the design (Blosser's digest q2,
  self-efficacy review q2, math-anxiety meta-analysis of correlations q3, Bangert-Drowns d = .22 → `i1` on both pages);
  bare markers with no claim removed (math anxiety, growth mindset, `strategies/functional-behavior-assessment`, whose
  wrong feedback-levels link is gone too).
- **Citations** (Crossref, DataCite or ERIC): Sturgill & Motley (2014) → `10.20343/teachlearninqu.2.1.81` on three
  pages; Van de Sande (2013) → DataCite `10.5281/zenodo.3554629` on seven; the authorless "Criterion Referenced
  Measurement in Reading (1974)" is Pikulski (1973), ERIC ED085660, on three; Freedle is 2003, `10.17763/haer.73.1.8465k88616hn4757`;
  a second Gaofeng & Yeyu (2007) page. **Rigour is still never re-judged from an entry**; the agents reported, not changed,
  differing `r` on Karpicke (2017), Cameron & Pierce (1994) and Okonofua (2016).
- **Still open**: Miller (2015) is `causal` on two survey claims and `associational` on two; the criterion-referenced
  claims code a non-peer-reviewed recommendation q2; `teacher-expectation-effects-on-achievement` keeps bare markers in
  its merged paragraphs; Sisk et al. (2018) q4 unconfirmed; Bangert-Drowns's d = .22 comes from an earlier full-text
  write-up the abstract cannot confirm.

## 2026-10-05 (late night) — conversion wave 6: the last of the conversion core; complete briefs barely moved

- **Fifteen pages converted** (`eval/page-triage/wave-6.md`): the principles journaling, gamification, debriefing,
  note-taking, functional behavior assessment, multiple methods of assessment, supporting students with intellectual
  disabilities, summative assessment, standardized test fairness and bias, motivation, knowledge organization and
  culturally responsive classroom norms, and the patterns professional development, learning by producing and
  experience with languaging activities. They are ranked by inbound links from content pages; index, log and
  revision links no longer count. **Folded first**: the self-determination-theory and reinforcement-theory principles
  into their theories (across kinds, no alias), and the stub patterns journaling, inquiry-based learning and summative
  assessment into their principles. After this wave, no unconverted canonical page has more than five such links,
  apart from the skipped source-framed stances.
- **Tested with 30 briefs (about $6.7): blind pairs 86–34** (sparse 49–11, **complete only 37–23**); accuracy
  3.18 → 3.80, decision value 3.72 → 3.97; fit up on sparse briefs, slightly down on complete ones. The graders split
  on level: Gemini scores NEW higher everywhere, DeepSeek lower on fit and decision value.
- **Every loss was a row that assumed a setting the brief did not have**: fill-in guided notes for nursing assistants
  who needed a reusable handover grid in their own categories; a memory check for older adults' take-home notes; a
  journal scaffold that ignored the brief's rubric and had the trainer read private entries; three methods crammed into
  two sessions; a whole-task ambulance exam split into paper items. One row each turned all six briefs to 3–1 or 4–0.
  **Rows should take the brief's own categories, routine and privacy terms as given.**
- **Check answer endings before reading a loss**: one answer stopped mid-sentence even with the 16,000-token limit.
- Open: the agents' lists (nine duplicate-claim pairs, about a dozen overstated titles, stale text, `i` codes without
  printed effect sizes, two fold candidates, Kraft et al. 2018 as an ingest candidate) are in `wave-6.md`.

## 2026-10-05 (late night) — wave 5's claim findings settled; the evidence parser stopped reading comments

- **Eleven duplicate claims merged** (`merge_claims.py`): judgments of learning into fluent illusions, teaching others
  into learning by teaching, SRSD writing into strategy instruction, SEL academic achievement into SEL behaviour and
  achievement, phonological into phonemic awareness, learner-centred relationships into teacher–student
  relationships, feedback use into feedback, retrieval-fails-without-encoding into pretesting (its title overstated:
  the studies show a failed attempt enhancing the encoding that follows), both expertise-reversal variants into
  `expertise-reversal-effect`, and the second pretraining claim into `pretraining-improves-transfer`.
  `principles/explicit-instruction-phonics` (adults) folded into `phonics`. **Not merged**: the Frydenberg (2007) and
  Honig (2021) pages, which are distinct findings of one study, not duplicates.
- **`okf_lib.parse_evidence_sources` now ignores HTML comments.** A merge keeps a differing write-up of a shared
  study in a `<!-- merged -->` comment, and the parser read it as a second entry, so six pages merged in #165 and
  this pass said "2 studies (3 entries)" and carried a duplicate `sources[]` item. Same rule as the reverse index.
- **Claim corrections** (three agents, each change from the page's own entries): 16 titles rewritten (slugs kept, old
  titles in comments, link text on 178 links); stale "no evidence" text on about 20 pages; `i` codes with no printed
  effect size set to `i?` (five pages, and two Slezak 2011 pages); `teacher-modeling-internalizes-reading-strategies`
  recoded qualitative q1; Furtak et al. (2012)'s .40 is now said to be the teacher-led minus student-led difference
  between studies; "reports the opposite" labels between claims measuring different outcomes relabelled.
- **Citations, checked against Crossref, DataCite or ERIC**: Sweet & Rupp (2012) → `10.5281/zenodo.3554649` on five
  pages (DataCite); Rupp et al. (2010) has no DOI, now its JTLA article page; the authorless "Relations between
  cognitive resources…" (2015, a Google Scholar link) is Miwa, Terai & Mizuno (2017), CELDA, ERIC ED579478, on five
  pages; "Marjorie Ceballos 2022" is Ceballos & Nutta (2022), ERIC EJ1380081, on six; the ZJNU community report is
  Gaofeng & Yeyu (2007), ERIC ED500172, on three; the primary-evidence links on the worked-examples and contingent
  scaffolding claims were unregistered DOIs, now Sweller & Cooper (1985) and Pratt & Savoy-Levine (1998); Gray et al.
  (2018) on phonics → `10.1007/s11145-017-9774-9`. Eight frontmatter titles with an unquoted `: ` (invalid YAML that
  only the lenient parser read) are quoted.
- **Rigour is not re-judged in a merge**: an agent lowered Cornelius-White (2007) r3 → r2 from the entry text and it
  was reverted, since rigour is coded from the article. Durlak et al. (2011) is still r2, r? and r3 on different pages.
- **Still open**: Van de Sande (2013) cites the JEDM homepage on five BKT claims (JEDM's Zenodo deposits probably carry
  DataCite DOIs); q codes on qualitative pages coded q2 (organization simulation, positioning students as sources) and
  a queue simulation coded `causal`; Ruan Gaofeng's name order; Bernard et al. (2009) and Castles et al. (2018) as
  ingest candidates; self-monitoring's sparse brief.

## 2026-10-05 (night) — conversion wave 5: 15 more pages; the biggest gain in fit so far

- **Fifteen pages converted** (`eval/page-triage/wave-5.md`): strengths-based approach, pre-reading questioning,
  instructor accessibility, feedback loops, validity/reliability/bias in classroom assessment, self-monitoring,
  process-based writing (which had absorbed three writing-response pages), modeling, holistic learning and phonics;
  the patterns fostering communities of learning, epistemic games, structured peer review, social-emotional learning
  and online course design. Only phonics has a claim testing its relationship; every page keeps a labelled default
  design with doses across sessions. Four more frontmatter DOIs corrected against Crossref.
- **Tested with 30 briefs (about $6.8): blind pairs 93–27 for the new pages** (complete 47–13, sparse 46–14);
  accuracy 3.27 → 4.17, decision value 3.72 → 4.53, **brief fit 4.07 → 4.60 and situation fit 3.83 → 4.57**, up on
  complete and sparse briefs alike. No answer was cut off (answer limit 16,000 tokens).
- **Losses came from one missing row, again: scarce facilitator time** (volunteers, busy shifts). Rows added to
  self-monitoring and feedback loops; feedback loops' sparse brief went 1–3 → 2–2 / 3–1. **Self-monitoring lost by
  overriding the brief**: asked for a "know / unsure / next move" pause, answers replaced it with the page's "tests, not
  feelings" rule. A row saying to keep a routine the brief names, with one check on its "know" line, took the complete
  brief 1–3 → 3–1 / 2–2. Its sparse brief still loses 1–3 (open). **When a brief names the routine it wants, a page
  must say how to run it well, not replace it.**
- Open: the agents' lists (13 duplicate-claim pairs, ~15 overstated titles, stale text, mis-coded impacts and kinds,
  two primary-evidence links that disagree with their citations) are in `wave-5.md`.

## 2026-10-05 (evening) — folds, merges and a claim cleanup before wave 5; merge_claims stopped dropping entries

- **Pages folded** (`merge_pages.py`, maintainer's go-ahead): `competency-based-learning-assessment` into
  `competency-based-assessment`; `creating-visual-representations` into `dual-coding`; three small writing-response
  principles (`involve-students-in-revision-process`, `avoid-appropriating-student-writing`, `respond-as-a-reader`)
  into `process-based-writing`; and across kinds `patterns/adaptive-learning` (a stub) into the principle,
  `patterns/reflective-practice` into `principles/reflection`, `principles/debate` and
  `principles/case-studiescase-based-learning` into their patterns, `principles/situated-learning` into the theory.
  Renamed (old slug an alias): `peer-feedbackpeer-review` → `peer-feedback`, `mentoringcoaching` →
  `mentoring-and-coaching`. **Not folded**: `scaffolding`/`scaffolding-and-fading` and
  `assessment-for-learning`/`formative-assessment`, each pair converted with a stated division of labour; and
  `patterns/game-based-mastery-learning`, which is misfiled rather than a duplicate.
- **Eleven duplicate claims merged** (`merge_claims.py`), among them the two dual-coding claims, the two seductive-details
  claims (now six studies), the cooperative free-rider claim into group rewards, the fiction/empathy claim into
  theory of mind, the two contrasting-cases claims, guided inquiry into guided discovery, and the second-hand
  deliberate-practice variance claim into its source's claim. Not merged: clear structure and signaling,
  inquiry and teacher-guided inquiry, the two autonomy claims (different propositions).
- **`merge_claims.py` dropped the folded page's write-up of a study both pages carried.** On nine entries across
  #163's and today's merges the write-ups differed (another finding, another quote): the tutor-background subgroup
  test vanished entirely. They are restored verbatim in `<!-- merged … restored verbatim -->` comments under the
  surviving entry, and the script now keeps a differing write-up that way itself.
- **Claim cleanup** (wave 4's list, three agents, each change grounded in the page's own entries): 27 titles
  rewritten to what their entries show (slugs unchanged, old titles in comments, link text on 500+ links), stale
  "no evidence yet" text on about 25 pages, recodes where the entry prints the statistic or the design (Macnamara
  2014's R² is not an effect size → `i?`, q4 → q3 as a meta-analysis of correlations; Alfieri 2011 is
  `quant-synthesis`; Chi et al. 2001 q2 on both pages; affiliation motive was blocked, not assigned → associational),
  and the CRAAP-checklist claim no longer cited as evidence that rubrics breed compliance.
- **Still open**: `cognitive-disequilibrium-motivates-conceptual-change` asserts a mechanism its own entry says it
  does not isolate (retitle); the germane-load claim's citation has no authors (a Google Scholar link); bare
  `[±]` markers after related-claim links in older claim Discussions; the sibling of
  `computer-based-no-better-than-individual-paper` still labels it "reports the opposite".

## 2026-10-05 (later) — conversion wave 4: 15 more pages; fit rose on sparse briefs for the first time

- **Fifteen pages converted** (`eval/page-triage/wave-4.md`). Principles: evaluating sources, ask experts, cultural
  and life experiences, universal design for learning, social interdependence, engagement, deliberate practice,
  graphic organizers, dual coding, digital learning and transfer of learning. Patterns: experiential learning cycle,
  authentic assessment, develop understanding and collaborative evaluation. No claim tests 11 of the 15 as a whole;
  every page keeps a labelled default design with doses across sessions. Stubs, duplicates and theory-like
  principles in the ranking were skipped for a fold. Six more frontmatter DOIs that disagreed with Key Sources were
  wrong and are corrected against Crossref.
- **Tested with 30 briefs ($6.85): blind pairs 86–34 for the new pages** (complete 40–20, sparse 46–14);
  accuracy 3.33 → 4.08, decision value 4.12 → 4.50, affordances 5.6 → 9.1 of 12. **Situation fit rose on sparse
  briefs (3.60 → 4.20), where waves 2 and 3 moved only complete ones.** The answer prompt now tells the answerer to
  write for a designer who has not seen the page. That fixes wave 3's "page, step 4" bias, but makes the numbers
  not strictly comparable with earlier waves.
- **Set the answerer's token limit high.** At 4,000 tokens the reasoning model cut off three NEW answers and no OLD
  one, because the new pages are longer. Each of those briefs went 0–4 until the answers were regenerated; the raw
  result was 81–39.
- **Two pages lost a complete brief 1–3, each for want of one situation row**: remote learners in a live expert
  consultation, and a product whose audience should not see the reasoning (split it from a decision memo). With the
  rows added: 3–1 and 2–2, and 3–1 and 4–0. **When a page loses, look first for the missing setting row.**
- Open: the agents' lists of overstated claim titles, stale "no evidence" text (including on the self-explanation
  claim #163 folded into), merge candidates and codes to recheck are in `wave-4.md`.

## 2026-10-05 — waves 1–3's open findings settled, before wave 4

- **Citations, Crossref-checked** (first author, year and title): the frontmatter `resource:` disagreed with Key
  Sources on ten converted pages, and the frontmatter side was wrong each time (another paper in the same issue, or
  no record): Jacobson & Spiro (both cognitive-flexibility pages), Numrich, Gellevij, Givens (and its year: 2019, not
  2020), Reigeluth (listed twice), Binder (`…12319` is an "Issue Information" record), Sachs, Hooley, and Vo & Morris,
  whose journal was invented (*Journal of Education for Business* 81(6) 315–320, not *J. Economic Education*).
  Setlhodi (2018)'s Key Sources DOI was a 2021 anthology reprint; it now carries the 2018 handbook chapter's own
  (`10.4018/978-1-5225-5085-3.ch010`). Kulik et al. (1990) has two registered DOIs (JSTOR and SAGE) for one paper;
  the last JSTOR one moved to SAGE's. `principles/social-presence`'s `https://example.org` placeholder link is gone.
- **Claim pages corrected from their own entries**: 16 overstated titles rewritten (slugs unchanged, old titles in
  `<!-- deprecated title -->` comments, link text on 155 pages; text inside comments left verbatim), stale "no
  evidence" text on 16 pages, `erroneous-examples-build-conceptual-knowledge` brought in line with its entry (grades
  4–5, no transfer), four recodes where the entry prints the statistic (community-partner conflict r ≈ −.4 → `q2 i3`,
  syllabus connection r = .569 → `i3`, refutational-text `i1` → `i?`, experimenter-underlining `i0` → `i?`), the
  parliamentary-debate survey `theoretical` → `associational r1`, and two wrong links. **Markers on design pages
  citing a retitled claim were not changed**: `fiction-reading-improves-empathy` now says the evidence is
  theory-of-mind, not empathy, and pages citing it `[+]` for empathy need a reading.
- **Eight duplicate claims folded** (`merge_claims.py`, each slug an alias): lateral reading into civic online
  reasoning; two interleaving pages into `interleaving-improves-inductive-learning` (which took the precise title);
  `self-explanation-prompts-…-worked-examples` and `self-explanation-improves-learning` into
  `self-explanation-improves-conceptual-understanding` (now four studies); `matching-instruction-to-styles-no-effect`
  into the learning-styles claim; `discussion-quality-drives-comprehension` and
  `structured-discussion-approaches-improve-comprehension` into `structured-discussion-methods-improve-comprehension`.
  **Not merged**: `goal-setting-improves-performance` and `specific-difficult-goals-…` (general against specific,
  different studies), and wave 1's principle pairs (`scaffolding`/`scaffolding-and-fading`,
  `assessment-for-learning`/`formative-assessment`), which are the maintainer's call.
- **Still open**: Brewer & Klein (2003)'s sibling claims still say "adult learners" (the entry says undergraduate
  business majors); Gentner et al. (2003) is `r3` on one claim and `r?` on two, which a read of the full article would
  settle; wave 2's Key Sources with no claim page (Patall et al. 2008, Reeve, Richland et al. 2007, Abedini et al.
  2021, Champion 2015); the strategy near-duplicates.

## 2026-10-03 — the four pages wave 3 skipped: two duplicates folded, two theories absorbed

- **`principles/self-regulation` folded into `self-regulated-learning`** (its slug an alias, beside `metacognition`).
- **`principles/explaining-their-thinking` renamed `principles/self-explanation`** (the old slug an alias), so the
  principle carries the name of its element, `elements/self-explanation`, as worked examples does. Its body is
  unchanged and still unconverted.
- **`principles/behaviorism` folded into `theories/behaviorism`, and `principles/social-learning` into
  `theories/sociocultural-theory`** (maintainer's decision): the page described learning through interaction and
  cited sociocultural perspectives, not Bandura's observational learning, so not `social-learning-theory`.
  Cross-kind, so links were repointed and no alias was kept; each body is in a `<!-- merged -->` block.
  `update_links_for_renames.py` stamped an `id:` and the old slug as an alias onto the sociocultural theory; both
  were removed, since theories carry no id and an alias cannot cross kinds.

## 2026-10-02 (late night) — conversion wave 3: a situation table on every page; fit barely moved

- **Fifteen more pages converted** (`eval/page-triage/wave-3.md`): the principles guided practice, error analysis,
  cognitive activation, goal setting and monitoring, cognitive flexibility, multimodal instruction, game-based
  learning, reflection, experiential learning and epistemic cognition, and the patterns blended learning, concept
  attainment, elaboration theory, constructive alignment and structured academic controversy. Behaviorism and
  social learning (theories in all but folder), explaining-their-thinking and self-regulation (duplicates) were skipped.
- **New in the brief: `## Fitting the design to a situation`**, the three facts that most change the decision and a
  `| If the brief says… | Then change… | Basis |` table, each row a claim link or marked untested (153 rows, 94 on a
  claim). Described in `principle-pattern-authoring.md`.
- **Tested with 30 briefs ($4.58): blind pairs 101–19 for the new pages**; accuracy 4.07 → 4.52, decision value
  4.05 → 4.52, affordances 5.8 → 8.8 of 12. **Situation fit rose only on complete briefs** (anchored 4.00 → 4.13,
  brief fit 3.90 → 4.07) and not on sparse ones. Gemini gives fit ≈ 5 to everything, and a pairwise "more fitted"
  question matched the overall pick 118 of 120 times, so **these graders cannot measure fit apart from quality**; a
  real test needs briefs that differ in one fact. **Guided practice lost both briefs 1–3** to the old page's concrete
  plans, the wave 1 lesson again: a default design less concrete than the old guidance loses, and a situation table
  does not make up for it.
- **Reworked the next day** (`wave-3.md`, "Rework"): both losing pages lacked **a dose and a progression across
  sessions**, which the winning old answers had. With those added, error analysis's complete brief went 1–3 → 3–1 and
  guided practice's 1–3 → 4–0 (sparse 1–3 → 2–2); guided practice also stopped deriving a success threshold from a
  retrieval-practice claim, which graders called an import. **Give a default design a multi-session arc, not only a
  lesson.** Answers that cite the page's structure ("page, step 4") are marked down; that is the answer prompt's
  doing, and it biases these tests towards the old pages.

## 2026-10-02 (late night) — conversion wave 2: 15 more pages, and no page lost

- **Fifteen more pages converted** (`eval/page-triage/wave-2.md`): the patterns collaborative learning, competency-
  based learning, Gagné's nine events, debate and anchored instruction; the principles community of inquiry,
  communities of practice, cognitive disequilibrium, community-based learning, inquiry-based learning, autonomy,
  analogical reasoning, adaptive learning, competency-based assessment and immediate feedback (30 to 83 inbound
  links). The brief now requires a **labelled default design** wherever no claim tests the page's relationship;
  13 of the 15 needed one.
- **Tested with 30 briefs ($4.67): blind pairs 113–7 for the new pages, every brief won**, unanimous on 23;
  accuracy 3.88 → 4.72, decision value 4.18 → 4.68, affordances 7.2 → 10.5 of 12. **Brief fit is flat** (3.75 →
  3.68): the format makes answers more accurate and decisive, not more fitted to the brief. Wave 2's open list
  (wrong-claim links on the old adaptive-learning page, overstated titles, stale text, three citation mismatches,
  merge candidates) is in `wave-2.md`.

## 2026-10-02 (late night) — before wave 2: four converted siblings absorb their duplicates

- **Folded** (maintainer's decision): `principles/spaced-practice` into `spaced-learning`, `cognitive-apprenticeship`
  into `scaffolding-and-fading`, `explicit-instruction` into `direct-instruction`, `metacognition` into
  `self-regulated-learning`; each slug an alias. `principles/audiobooks` folded into `elements/audiobooks` and
  `patterns/cognitive-load-theory` into `theories/cognitive-load-theory` (cross-kind: links repointed, no alias),
  and `patterns/cognitive-flexibility-theory` moved to `theories/`. `merge_pages.py` folds across kinds when the
  fold is given as `kind/slug`.

## 2026-10-02 (late night) — conversion wave 1: the 15 most-linked canonical pages

- **Fifteen single pages converted** to the conditional-model format (`eval/page-triage/wave-1.md`): thirteen
  principles (cognitive-load management, annotating, check-ins, chunking, assessment for learning, active
  learning, clear structure, collaborative learning, building empathy, accessible vocabulary, authentic
  audiences, activation, scaffolding) and two patterns (case-based learning, think-pair-share), 113 to 395
  inbound links each. One agent each from a single-page brief; where a converted sibling exists the page owns
  the more general relationship and places the sibling inside it. Checked by script as the pairs were, plus
  every quoted number found on a cited claim page.
- **Tested with 30 briefs ($4.46 with the rework): blind pairs 100–20 for the new pages** (complete 44–16,
  sparse 56–4); accuracy 3.95 → 4.78, decision value 4.15 → 4.78, affordances 7.5 → 10.7 of 12. DeepSeek's
  pairwise picks lean to the first answer shown. **Accessible vocabulary lost its complete brief 0–4** to the old
  page's concrete plan; a default-design section restoring that plan, each step labelled with its evidence,
  brought it to 2–2. **Where no claim tests a page's relationship, keep the old page's concrete design as a
  labelled proposal**: a rewrite that leaves only caveats loses, as PBL did.
- **Most of these pages have no claim that tests their own relationship**, and say so; the wave's list of
  overstated claim titles, stale claim text, two citation mismatches and merge candidates is in `wave-1.md`.

## 2026-10-02 (night) — every principle and pattern triaged; nothing moved yet

- **`eval/page-triage/triage.tsv`** (`scripts/triage_design_pages.py`, README beside it) classes all 837
  principle and pattern pages as canonical, duplicate, variant, design or misfiled, from two model runs
  (GPT 5.6 Luna and DeepSeek V4 Pro, $1.80), each page shown with its ten nearest same-kind pages. They agree
  on 64% of principles and 48% of patterns, systematically: DeepSeek calls single-setting designs "variants"
  and recommendation pages "canonical", GPT draws those lines where the settled rules do, so the verdict is
  agreement, else design-over-variant, else GPT with a review flag. **Writes no page; every move is a
  maintainer decision** (where designs live; merging duplicates; moving misfiled pages).
- **Results**: canonical 197 principles and 64 patterns (64% of inbound links each); 121 patterns are
  designs; 46 duplicates (20 point at a target with fewer inbound links, so direction is decided at merge);
  138 misfiled. **The conversion core is ~100 pages**: 106 canonical pages have 5+ inbound links, 15 already
  converted. **Seven converted pages are classed as variants or duplicates** (`principles/cognitive-load-theory`
  of `cognitive-load-management`, `scaffolding-and-fading`, `self-regulated-learning`, `cooperative-learning`,
  `direct-instruction`, `peer-discussion`, `patterns/team-based-learning`): fold their siblings into them or
  port the conversion before the next wave.

## 2026-10-02 (night) — a `designs/` kind

- **`designs/` is the tenth content kind** (maintainer's decision): a design for one setting, course,
  population or product, which the settled rule says is never a pattern. It carries `id:`, resolves in
  `wiki-index.json` as `design`, takes the Design template below, and Lazuli-generated design
  descriptions go there. Every kind list knows it, and `check_nav_coverage` passes. The triage's design
  pages move in a separate change, by `scripts/move_pages_kind.py`, which repoints their links (a move
  across kinds cannot be carried by an alias).
- **The README's page-count table is generated** (`build_indexes.py`, between `page-counts` markers; CI runs
  `build_indexes.py --check`). It was hand-written, so it listed no designs and carried September's counts. The
  dashboard's editable folders and the MCP search description now include designs (and, for the dashboard,
  processes and methods, which it had never allowed).
- **The triage was applied** (`eval/page-triage/README.md`): a third model settled 270 of the 305 flagged rows;
  188 pages moved to their kind (115 to `designs/`), and 22 duplicate principles and patterns were folded
  into 21 pages by `scripts/merge_pages.py`, each fold's slug an alias of its survivor and its body kept in a
  `<!-- merged -->` block. Not moved, on reading: five general patterns the models called designs, and six
  pages classed as claims.

## 2026-10-02 (evening) — batch 12 landed; the PBL pair reworked and re-tested

- **Batch 12** (`eval/deep-dive/principle-pattern-pairs/topics.txt`): re-run on a new key from the cached
  articles; 63 fetched, 57 ingested, 4 validation failures, 2 out of scope, $0.33 (v136). 276 claims, 852 new
  files. Verify stopped on three generated header lines (below); the post-verify steps were run by hand: 593
  claim links, 150 page links, kind/rigour and dimension cells for the new entries. **The load-bearing check's
  10 failures are settled, 0 open**: Metin (2022)'s prose t = 6.964 is the control SD in its own Table 5
  (t = 6.678), now said on the entry; Blosser (1993) reports Basili & Sanford's (1991) study second-hand;
  Ceballos & Nutta (2022) is a practice-to-theory article, not a review; Clinton et al. (2017)'s "did not
  affect" time is now "no reliable difference". Seven dismissed as judge errors, chiefly **a manuscript's
  "please cite as" line is not the registry**: Crossref records Clinton et al.'s chapter
  (10.4018/978-1-5225-1005-5.ch010) under the title the pages give.
- **#144's three claim pages had no citation or codes line in the body**, so every batch wrote "none recorded
  yet" on them, and `sync_evidence_codes` would have replaced their DOI resources with manuscript links. Each
  entry now opens with a Crossref-checked APA citation and a codes line matching its frontmatter. **An evidence
  entry must open with its citation line**: the tools take the first link in the entry as its resource.
- **The PBL pair is reworked** from batch 12's re-analysis of a PBL meta-analysis (Walker & Leary 2023; 353
  outcomes): as a curriculum format PBL's average effect is modest (g = 0.27), ranges from −1.26 to 1.91, may
  be inflated by publication bias (g = 0.103 after trim-and-fill), and is not predicted by tutor background;
  guidance for novices leads, and productive failure is a narrower configuration. **Re-tested on the same two
  briefs: it beats the old pages 7–1 and #149's version 8–0** (decision value 4.75 → 5.0, brief fit 4.25 →
  5.0, $0.33). Part of the gain is the new evidence rather than the rework: the shared reference now holds the
  Walker & Leary claims, which the earlier versions could not cite.

## 2026-10-02 (later) — the ten new pairs, tested with briefs: they help, except problem-based learning

- **Same design as the 2026-10-01 format study** (scratch only, briefs unseen by the page writers): 20 new
  briefs, one complete and one sparse per pair; Kimi K3 answered each from one version's two pages, with
  frontmatter and HTML comments stripped as a reader sees them (OLD = main before #149, NEW = after); Gemini 3.8
  Flash and DeepSeek V4 Pro graded against every claim either version cites, on the six affordances plus
  accuracy, decision value and brief fit, and blind in pairs, both orders. $4.31.
- **Result.** Affordances 6.8 → 11.1 of 12 (sparse briefs 3.7 → 10.5: the old pages gave nothing to elicit
  from); accuracy 4.30 → 4.80; decision value 4.53 → 4.95; brief fit 4.12 → 4.62, both graders agreeing in
  direction on every measure. **Blind pairs 68–12 for the new pages**, unanimous on 13 of 20 briefs; answers were
  of similar length (median 554 against 593 words), though the new pages are 1.4–6× longer.
- **Problem-based learning lost, 3–5.** The new pair builds its model on the productive-failure and
  minimal-guidance syntheses, and answers followed it into a problem-first design for novice pharmacy students
  and an engineering course; graders called that conflating PBL with productive-failure mathematics studies,
  and preferred the old pages' faded worked examples and explicit routines for novices. **The PBL pair needs
  rework**: lead with guidance for novices and say plainly that no claim here tests PBL curricula.
  Retrieval practice / team-based learning tied 4–4, every judgement favouring whichever answer came first:
  no signal either way.

## 2026-10-02 — ten more principle–pattern pairs in the conditional format; batch 12 blocked on an expired key

- **Ten pairs rewritten as conditional models** (`principle-pattern-authoring.md` lists them): cooperative
  learning, direct instruction, mastery learning, multimedia learning, problem-based learning, self-regulated
  learning, peer discussion / peer instruction, scaffolding and fading / cognitive apprenticeship, cognitive
  load / 4C/ID, retrieval practice / team-based learning. One agent per pair from a brief (scratch, not
  committed): 3–6 core claims read in full and described only from their claim pages, at least one limiting
  claim, markers under `strength_cap`, every claim either page cited kept (in the model or under Further
  evidence, labelled with its current load-bearing status), the old body verbatim in a `<!-- deprecated -->`
  block, and Design Decisions, Related, Examples and Key Sources kept. Checked by script against each old page:
  no old line lost, no frontmatter key changed but description/status/generated, no live claim dropped, no
  marker above cap, no broken link. Not yet tested with briefs as #144's three were; that is the next step.
- **What the agents found, open:** no claim tests 4C/ID, team-based learning or whole PBL curricula as a
  whole; `whole-task-performance-improves-transfer` is a design argument titled as an effect; the
  cooperative-learning free-rider and group-rewards claims share three entries and overstate them; the
  direct-instruction claim's opening still says "particularly for novices"; `self-regulated-learning-improves-
  achievement` pools performance, strategy use and motivation; several claims still say "no evidence yet"
  beside entries; Roediger & Karpicke 2006 is n=180 on one claim and n=300 on another; the #144 claim pages
  (`fading-and-principle-prompts-…`, `worked-example-problem-sequences`) have no parseable codes line, so their
  headers read "none recorded yet" and their cap is W.
- **Links inside HTML comments no longer count.** `build_reverse_index.py` and `check_evidence_markers.py`
  strip `<!-- -->` first, so text kept in a deprecated block is not a citation, an edge or an evidence-profile
  entry (11 edges dropped from two gap-fill pages that already had such blocks).
- **Batch 12** (`eval/deep-dive/principle-pattern-pairs/topics.txt`, 63 articles fetched) **produced nothing:
  the OpenRouter key in `/etc/eval-harness.env` has expired** (HTTP 401 on every call). Its writes were
  reverted. With a new key, re-run generation for `--label batch-12`; the articles are cached.

## 2026-10-01 (evening) — every batch codes its new evidence on the shared dimensions

- **`run_scrape_batch.py` now runs `code_evidence_axes.py --new --code` then `--contrasts`** after kind and
  rigour: each new evidence entry becomes up to four cells (learners, goal, conditions, the contrast, outcome,
  direction, design; `evidence-dimensions.json`), coded from the article the batch fetched, in a call
  separate from extraction (a study record in the same call cost GLM most of its passes). The store is
  `eval/runs/evidence-axes/cells.ndjson` (ignored; the pilot's run `a`, renamed), read by
  `render_evidence_map.py`. Writes no page; about $0.0025 an entry, $3 cap.
- **A cell's quote is checked against the whole article**, not the 30,000 characters the coder sees: the
  entry's own verbatim quote often sits in a Results section past that cut, and the coder reuses it. The cut
  check had failed 35 of the pilot's 528 cells, now 434 verified.
- **Prompt v137 (contrast and direction on every evidence entry) is benchmarked, not adopted; `CURRENT`
  is v136.** Same day, same flags (`eval/runs/bench-axes-v136`, `-v137`): validation 9/10 both, first-attempt
  passes 6 and 5, GPT judge 9/10 (4.28) against 10/10 (4.20), $0.0088 against $0.0095 a passed article,
  output JSON 5–10% longer, all within this benchmark's noise. 65 of 65 entries carry both fields and none
  trips the validator's warnings. Against GPT coding the same entries from the articles: the two agree on
  whether an entry has a contrast in 57 of 65 cases and on direction in 43 of the 57 where both name one. GLM
  wrote `0` never, and 12 of its 13 `ns` were `ns` for the reference too. Most of the 14 disagreements are
  omnibus or interaction results (`+` against `mixed`) or the same finding framed from the other side, not
  errors. The post-batch coder (above) records the same two fields with learners, goal, conditions and
  outcome as well, so v137 adds only having them in the extraction itself, for about $0.0007 an article.
  Adopt it only if they are to be written onto the claim page, which needs an ingest change and a decision
  on where on the page they go.
- **The docs site's search index is one entry per page** (`docs_hooks/search_trim.py`, #147): 91,222
  entries and 66 MB (12.8 MB gzipped) became 8,691 and 9.2 MB (1.7 MB). Section-level search is the MCP
  server's.

## 2026-10-01 (later) — one vocabulary for the evidence and design dimensions; the spec reads the new format

- **`evidence-dimensions.json`** (root, beside `evidence-scales.json`) defines once the dimensions three works
  had named separately: the evidence-axes coder's L, G, C, D and O, the impact comparison record
  (`methods/impact-evidence-comparison.md`, observations' `impact_context`) and the six principle–pattern
  affordances (`principle-pattern-authoring.md`). Nine dimensions (learner state, goal, valued goal,
  conditions, design variable, assignment, outcome, effect, diagnosis), each with its controlled values and its
  name in each work. `scripts/evidence_dimensions.py` is its only reader; `eval/evidence-axes/axes.json` is
  gone. "randomized" is canonical, "randomised" an alias, so cells coded before still read. `lint.py --type
  dimensions` fails on a value defined twice, an alias or crosswalk naming a value that does not exist, or a
  guide affordance no dimension maps (both verified by mutation). Two dimensions have **no evidence side**:
  the learner's valued goal and diagnosis are design-only, since studies rarely report either.
- **learning-design-spec reads the conditional-model format** (that repo's decision 0020, finding 0032):
  `planning-patterns` reads a principle or pattern page by the role of each section, either shape, and takes
  a page's observation-and-adaptation table into its phases. #144 merged after it, and #140–#142 are closed.

## 2026-10-01 — the conditional-model page format, tested independently: it helps, if the evidence stays

- **#144 rewrote three principle–pattern pairs** (worked examples, spaced learning, formative assessment) as
  conditional models (`principle-pattern-authoring.md`): observed response → uncertain state hypotheses →
  discriminating observation → next activity → response at a stated horizon, with the learner's valued goal kept
  apart from the designer's objective. Its own audits were the author scoring known cases. **An independent test**
  (scratch only, not committed, so the briefs stay unseen): 12 new briefs, 4 per topic, half complete and half
  sparse; Kimi K3 answered each from one version's two pages only; Gemini 3.8 Flash and DeepSeek V4 Pro graded
  blind against one shared reference (every claim either version cites), on #144's six affordances plus
  accuracy, decision value and brief fit, and in pairs, both orders. About $5.6 in all.
- **Result.** Affordances 7.0 → 12.0 of 12 (by construction, the rubric is the format's own); accuracy 3.71 →
  4.83; decision value 4.21 → 4.88; blind pairs **38–10 for the new format**, unanimous on worked examples and
  spacing. But it **lost formative assessment 7–9**, the page the rewrite cut from 17 claims to 1: graders called
  its answers abstract, and the old ones concrete and better evidenced.
- **So the removed claims are restored** (maintainer's decision), below each page's own evidence, markers capped,
  each labelled with how far its sources have been checked, and the formative-assessment pattern's Design
  Decisions are back. Re-tested as a third arm: it **beats the old pages 35–13 and wins formative assessment
  9–7**, ties the pruned version 25–23, and lifts brief fit 4.12 → 4.50. Restoring evidence did not dilute the model.
- **The format is the direction, and learning-design-spec must be updated to read it** (maintainer's rule: adopt
  it if it serves the theoretical goals better). These pages no longer carry `### Target Learners`,
  `### Target Learning Goals` or `#### Requirements`/`#### Constraints`, which the spec reads. Caveats: one
  answerer, two graders, 12 briefs; on worked examples part of the gain is #144's source corrections, not format.
  The cleanest format test, formative assessment, is the narrowest win.
## 2026-10-01 — evidence axes, a pilot: what the evidence can say for a given designer's learners

- **`eval/evidence-axes/`** codes evidence entries as **cells** on five axes, learners (L), goal properties
  (G), conditions (C), the design variable changed (D) and outcome (O), each with a result direction and
  design (then `axes.json`, now `evidence-dimensions.json`; ΔO = f(L, G, C, do(D))). `scripts/code_evidence_axes.py` codes from the study's text,
  with a verbatim-checked quote per cell; `--contrasts` names each cell's contrast canonically ("spaced vs
  massed", "longer vs shorter gaps") and flags cells coded the other way round. `scripts/render_evidence_map.py
  <page> --profile <designer>` renders one table per Design Decision: contrasts as rows, outcomes as columns,
  each cell keeping status (known / extrapolated / associational / hypothesized), directions, impact bin,
  experimental count and fit to the designer's learners apart, and **no score or ranking**, so the designer
  makes the outcome weighting and extrapolation calls. Nothing writes to a wiki page.
- **Pilot on the 10 Design Decision pages** (226 entries, 528 cells, $0.56): **learner expertise is not reported
  in 78% of results**, element interactivity in 80%, setting in 60%; only 2 cells are a powered null against
  34 inconclusive `ns`; the commonest outcome is pooled "general achievement". Against S1–S3's learners, 1, 12
  and 15 cells are known and about 300 extrapolated, mostly because the axes are unreported. Known limits:
  verbatim quotes that are not findings, misfiled design variables, fragmented contrast labels, no agreement
  check yet, not yet tried by a designer.
- **Three pieces of work now name the same dimensions**: this pilot's axes, #143's comparison record
  (`methods/impact-evidence-comparison.md`: learner state, assignment, activity and context, objective, outcome
  instrument, effect construction, horizon) and #144's page affordances (`principle-pattern-authoring.md`:
  initial state, transition, target, expectation, diagnosis, significance). **They should become one vocabulary**,
  held once as data like `evidence-scales.json`, before any of them is written into pages at scale.

## 2026-09-30 (late night) — design decisions on 10 canonical pages: more sound decisions, not yet more of them

- **`## Design Decisions`** (brief: `eval/design-decisions/BRIEF.md`) now sits on elements/feedback, practice,
  spaced-repetition, simulation, debrief, worked-examples, principles/retrieval-practice, gamification,
  patterns/direct-instruction and formative-assessment: about 64 decisions, each a designer's question with a
  Default, Changes when, Tested with and Not settled line, every choice citing a claim page, markers under
  `strength_cap`, cited claims added to the page's Claims list. **To extend it, give an agent the brief and
  a list of pages; do not write decisions a claim page does not state.**
- **Measured on S1–S3** (Italian A1, nurse onboarding, algebra), two wiki-only answers before and two after
  on a frozen pre-pilot checkout, one length-matched no-wiki baseline each, a GPT grader (anchored rubric
  ×3, plus a blind decisions-only test over three orders; $0.08; scratch files, not committed).
  Rubric mean before → after (baseline): S1 4.4 → 4.5 (4.33), S2 4.2 → 4.7 (4.33), S3 4.7 → 4.77 (4.4).
  Relevance S2 3.67 → 5; accuracy S2 4.17 → 5 (baseline 3 everywhere). **Share of decisions judged sound,
  blind: S1 77 → 86% (baseline 87), S2 92 → 96% (81), S3 87 → 92% (84).** But the baseline still ranks
  first blind in all three and leads decision value (4.33–5 against 4.0–4.33), because it makes 28–31
  decisions to the wiki's 19–21: **the pages made the wiki's decisions better, not more numerous.** Two
  runs a condition, so differences under ~0.3 are noise. What the after-answers still lacked was a way
  to **select patterns by learning goal and learner conditions**: agents searched by context ("mobile",
  "language", "algebra") and reported "no pattern for this course", while the one answer that did well (S2)
  took 4C/ID, a general pattern, and built the course from it. Domain claims were also missing (medication
  safety, EAL maths). The next measurement is dose: decision sections on ~40 canonical patterns and
  elements, with their Target Goals, Target Learners and Requirements/Constraints backed by claims so a
  pattern can be chosen for a goal, re-run on the same three scenarios. **Not** course- or context-level
  patterns: see the settled item on what a pattern is.
- **Cleanup in the same change.** Nine load-bearing failures fixed (0 open): D'Orazzi & Hajek 2022 is a
  student questionnaire study, not a teacher-and-learner one, so the Italian-motivation page's teacher clause
  is flagged as unconfirmed; Harkins et al. is **2020** (Crossref and ERIC), not 2021, on 9 pages, and a
  non-randomised q2 with `i?`; Ozturk (2023)'s link was the YouTube film it analyses, now its ERIC record;
  Gil's Table 10 contradicts its own prose; KOKU's focus group was staff; three titles retitled
  (Harkins, Ellis 1991, funds-of-knowledge labs). Fourteen other titles that overstated their evidence were
  rewritten in text (interleaving, seductive details, rewards, feedback use, structured peer assessment,
  and others; slugs unchanged, old titles in comments, link text updated). The three van Gog et al. (2011)
  pages now agree (n=96; problem–example pairs did not beat problems only); two unresolvable Gollwitzer &
  Sheeran DOIs in prose now point at the implementation-intentions claim; 17 bare evidence markers with no
  claim behind them were removed on the DragonBox, simulation-based medical training and after-action review
  pages; stale "no evidence yet" text on five claims describes what is recorded.

## 2026-09-30 (night) — named syntheses attached; S1 re-graded properly; where the wiki's value is and is not

- **Targeted pass** (`eval/deep-dive/adult-language-learning/SYNTHESES.md`): candidates from two signals,
  OpenAlex's citation-ranked meta-analyses per topic (`title_and_abstract.search:<topic>` plus a synthesis
  filter; free-text `search=` with a citation sort returns noise) and syntheses a model names (a recall aid
  only). Four agents attached **15 syntheses to 25 claims** (Norris & Ortega 2000, Spada & Tomita 2010, Goo et
  al. 2015, Lyster & Saito 2010, Li 2010, Lee, Jang & Plonsky 2015, Saito & Plonsky 2019, Ngo et al. 2024, Kim &
  Webb 2022, Webb et al. 2023, Uchihara et al. 2019, Nakata 2015, Boers & Lindstromberg 2012, Gollwitzer &
  Sheeran 2006, Kizilcec & Cohen 2017, Wong et al. 2019, Sailer & Homner 2020) and created four claims
  (corrective feedback overall, implementation intentions, gamification, formulaic sequences). Most were read
  as **abstracts only: publishers' robots.txt and 403s block their PDFs**, and the pipeline respects both;
  `fetch_article.py` gained an `oa` source for the open-access copies that are reachable. Five were dropped
  for having no readable text. Several syntheses **contradict or narrow** the claim they joined (ASR practice
  alone vs with peers; reading vs listening; explicit teaching for simple rules), and two titles were
  corrected in text. Uchihara et al. 2019 is q3 (a meta-analysis of correlational studies), not q4.
- **The first S1 grading was not sound, and the numbers above it should not be quoted.** Its "overall" was
  a holistic judgment the rubric never defined, the grader shared a model with the baseline, and the baseline
  answer was 387 words against ~1,050. Re-graded with a GPT grader, anchored criteria, overall as the mean of
  five, three repeats, and a **length-matched baseline** (`scratchpad` only, not committed):
  rubric mean — wiki before the deep dive 4.4, after it 4.6, after the syntheses 4.6, wiki + live search 4.2,
  no-wiki baseline 4.27. The baseline leads on relevance (5 against 4.3) and decision value (4.3 against 4.0);
  the wiki leads on accuracy (5 against 3) and traceability.
- **Blind, decisions only** (citations stripped, six plans, three orders): the length-matched baseline ranks
  first on breadth (30 decisions), but only **70% of its decisions are sound, against 84–89% for the wiki**
  plans, and the syntheses pass cut the wiki's questionable decisions to the fewest of any plan. **Checked
  against registries, the baseline's citations** exist (45 of 47) but 11 of the 29 checkable ones carry a
  detail the abstract lacks or contradicts, and 16 cannot be checked. A short baseline invented two.
- **So the wiki's value is precision and verification, and its gap is breadth of decisions.** The evidence
  exists; the design pages do not turn it into decisions: element/practice (915 inbound links) cites 6 claims,
  element/feedback 4, and no design page links the new syntheses. **Next: a design-decision layer on the
  canonical pattern and element pages**, built from the claims they should cite, and measured with the blind
  decision test. Live search at answer time did not beat the wiki alone (4.2); it is more useful as an
  ingest-queue generator, and its queue overlapped this pass.

## 2026-09-30 (later) — did the deep dive make the wiki more useful? Scenario S1 says: barely

Usage scenario S1 (Italian A1, adults, self-paced mobile) was re-run with the same brief after batches 10
and 11 and the nine hubs, and graded with the same rubric (scratch files, not committed). Overall
usefulness **3 → 3**, against the no-wiki baseline's 3.5; relevance 3 → 3.5; traceability 5, accuracy
4 and gap honesty 5 unchanged; every spot-checked statement matched its page. **The hubs changed no
design decision** (their "input first, then output" is what the baseline already says); two new claims
did (a realistic daily dose, 174 s against the 10 minutes asked; metalinguistic feedback better at once,
recasts more durable), each one study. The ~100 articles mostly added one-study `q2` claims on
mismatched populations (children, EFL cadets, undergraduates) and second-hand claims from reviews.
**What the baseline has and the wiki lacks is a handful of named syntheses** (Norris & Ortega on
explicit instruction, implementation-intention meta-analyses for dropout, ASR pronunciation feedback),
which an ERIC topic sweep does not reach: its open full text in this area is small classroom studies.
So depth by topic sweep adds volume, not decisions. The next test is a targeted pass on named
syntheses, attached to existing claims so they gain second studies. The first S1 run also found
**search ranked each hub below its fragments** (drafts are penalised); hubs now carry
`canonical: true`, rank first when the query names them, and fragments' results carry `canonical_page`.
Also fixed: the Frolli et al. (2023) subclaim still said articles were "disproportionately hard",
which the observation record had already shown the paper never measured.

## 2026-09-30 — the deep dive's theory layer: nine SLA hubs, batch 11, and a stale-verdict bug

- **Theory pages are framed one source at a time**, so the wiki had three fragments of Krashen, three
  of Swain and none that said what either theory claims. **Nine canonical hubs** now exist, each
  linking its source-framed variants (which stay) and the claims that test it, with markers under
  `strength_cap`: `krashen-input-hypothesis-monitor-model`, `swain-output-hypothesis`,
  `long-interaction-hypothesis`, `schmidt-noticing-hypothesis`, `skill-acquisition-theory-second-language`,
  `l2-motivational-self-system`, `willingness-to-communicate-in-l2`,
  `usage-based-second-language-acquisition`, `foreign-language-anxiety`. Descriptions are compiled
  **only from the fetched articles** that discuss each theory (listed in an HTML comment on the page),
  primary works are Crossref-verified but unread, and every hub is `status: draft` for that reason.
  The brief is `eval/deep-dive/adult-language-learning/HUBS.md`; use it for the next area's hubs.
  Variants that are rivals or descendants (Labov's monitor model, Wen's output-driven hypothesis,
  ACT*) are linked as neighbours, not called variants.
- **Batch 11** (`topics-gaps.txt`, ERIC 30): 24 generated, 23 ingested (182 pages), 1 validation
  failure, 14 first time, about $0.11. It supplied skill-acquisition, negotiation and focus-on-form
  sources batch 10 had not reached. **It stopped at verify, falsely**: the hubs had been committed
  mid-batch without their `> **Evidence** ·` lines, and the batch's profile step added them, which
  verify rightly refuses as non-citation edits. **Do not commit hand-written pages while a batch is
  running.** The post-verify steps were run by hand.
- **Adding the kind span in #134 made every load-bearing verdict stale**, so the check re-judged
  entries that had passed and spent its budget doing it. `check_load_bearing.units()` now strips the
  span before judging and hashing, and the earlier verdicts apply again. The re-judge's 9 failures
  were read anyway: 4 real and corrected (Kuhn & Crowell 2011's "do not develop on their own";
  Klahr & Nigam 2004 bears on guidance vs discovery, not guided inquiry; Cornelius-White 2007's
  correlational evidence, so the claim now reads "are associated with"; Wood et al. 1987's "in every
  set"), 5 the judge's (truncated author lists twice, an online-first year, two fair readings). **A
  field added to the codes line must be left out of every digest that keys a verdict.**

## 2026-09-29 (night) — every evidence entry carries a kind and a rigour; `q` is the design tier

- **Maintainer's decision, after the 38-entry pilot**: `q` ranked every study on the causal-design
  ladder and so called a careful qualitative study low quality. Each entry now also carries its
  **kind** (`causal`, `quant-synthesis`, `review`, `associational`, `qualitative`, `design`,
  `theoretical`) and its **rigour 1–3 judged by that kind's own criteria**
  (`eval/kind-rigor/RUBRIC.md`, `evidence-scales.json`), as a span on the codes line
  (`qualitative · r3`) mirrored to `sources[]` as `kind:`/`rigour:`. **`q` is unchanged and kept**,
  read as the design tier, because the design side and `strength_cap` read it.
- **`scripts/code_kind_rigour.py` coded all 3,806 entries, $6.92** (GPT, one pass, on the fetched
  article for 3,176, the abstract for 459, the entry alone for 171). **Rigour is never judged from
  the wiki's own paraphrase**: with no text of the study it is `r?`, and it is `r?` wherever the
  abstract cannot show the kind's criteria. Decisions are in `eval/runs/kind-rigor/coded.ndjson`
  (ignored), keyed by the entry's text, so an edited entry is re-coded and an unchanged one never
  paid for twice. Verified by parse: 3,036 claim pages, 0 source entries added or dropped, 0 other
  keys changed, and the body diff is only codes lines and header lines.
- **Of 1,070 distinct studies**: 37 qualitative studies are `r3` against 6 causal ones (few trials
  here are pre-registered and powered); `r?` is mostly meta-analyses (105 of 147) and trials (96 of
  233), which are known from abstracts. **Fetching those full texts is what would settle them.**
- Claim headers lead with kind and rigour (`1 study · qualitative r3 · q1 · n=10`; q goes bare
  beside kinds so "argument or single case" never sits next to "qualitative r3"), design pages'
  evidence lines count studies by kind, `evidence.md` has a kind × rigour table, and the docs
  legend explains both. **Batches code their new entries** after the verify step (`--new`, $2 cap).
  The extraction prompt does not ask for them: coding from the article afterwards is cheaper than a
  prompt change and a benchmark, and keeps GLM's job unchanged.

## 2026-09-29 (evening) — batch 10, the adult language-learning deep dive

- **75 ERIC articles from `eval/deep-dive/adult-language-learning/topics.txt`, all ingested** (541 pages,
  0 rejected), 55 of 75 first time, about $0.27 billed ($0.0037 an article on v136, Sail Research for
  71). Every source quote passes the grounding rule; 212 of 215 decimal statistics appear in their
  articles. The batch brought SLA theory pages the wiki lacked (output hypothesis, noticing, L2
  motivational self system, usage-based development, willingness to communicate), several in two or
  three near-duplicate versions; Long's interaction hypothesis and skill-acquisition theory are still
  missing. Next: consolidate those, link the design pages, and re-run usage scenario S1 (Italian A1).
- **The claim links of #132 made 434 claims load-bearing** (3+ design pages), so the batch's check
  judged older claims it had never read, and 15 failed. All are settled: 11 corrected (Adesope &
  Nesbit 2012 and Trypke et al. 2023 had been worded as the opposite of their abstracts on the
  redundancy pages; Kulik 1990's "requires added time"; five qualitative, survey or proposal studies
  titled as causal findings, retitled to what was observed with their scope, and recoded q1; two
  citations, Barber et al. (2007, not 2006) and Vongehr (2012, the arXiv paper, not the 2011 blog
  post), corrected on all 19 pages from those sources with DataCite DOIs), 4 dismissed (Alfieri's
  wrong OpenAlex abstract, twice; Furtak's and Williams's titles, which Crossref confirms). Link text
  on 49 pages now matches the retitled claims. A link's marker was not changed with its claim's title:
  one page cites the narrowed `redundancy-principle` `[+S]`, and whether that still fits is a reading.

## 2026-09-29 (later) — v136 is `CURRENT`; q4 errors fixed; design pages linked to claims; a kind-and-rigour pilot

- **`CURRENT` is v136** (maintainer's decision). No quantisation filter and no provider pin: 8-bit
  hosts are not used yet.
- **Ten evidence entries coded q4 were not preregistered trials or well-powered meta-analyses** and are
  recoded: seven narrative reviews and a book (Ryan & Deci 2000, Cowan 2001, Metcalfe 2017, Bandura
  1997, Pajares 1996, Locke & Latham 2002, Eccles & Wigfield 2002) to q2 narrative review; Watts,
  Duncan & Quan 2018 and Chi et al. 1989 (n=10) to q2 observational; Bierman et al. 2026 to q3 (an RCT
  not stated as preregistered). Across the claims, 33 subclaim q codes now equal their entry's, and 18
  subclaim i codes that exceeded their entry's were lowered to it.
- **Every element page has a `### Claims` section** (the template above has it too), and
  **`link_pages.py --claims-for elements patterns principles --verify`** fills them: GLM proposes up
  to 12 BM25 claim candidates for each page that cites no claim, and GPT keeps only links where the
  claim tests or bears directly on the page's own construct (`eval/runs/page-links/verified.ndjson`
  records each decision and its reason). GLM alone proposed 1,700; GPT kept 866 ($0.51), on 314
  pages. Rejections read right: "Cognitive Styles" was refused a Kolb learning-styles claim as a
  different construct. Design pages citing no claim: **671 → 357**. Markers are capped by the claim's
  recorded evidence (`strength_cap`), so most are `[+W]`. A page without a Claims heading gets one
  before its Related/Examples/Key Sources tail.
- **Four wrong-claim links from the usage simulation fixed**: `elements/debrief` →
  simulation-based deliberate practice, `principles/gamification`'s extrinsic-rewards line →
  `rewards-undermine-intrinsic-motivation`, `strategies/comparing_multiple_solution_methods` →
  `comparing-contrasting-cases-improves-learning`, and four timing lines on `strategies/timely_feedback`
  no longer cite the task/process-level feedback claim. A check that link text matches its target is
  still open.
- **Kind and rigour, a pilot, not adopted.** `q` ranks quantitative design, so a rigorous qualitative
  study is q1 or q2 however well done. `eval/kind-rigor/RUBRIC.md` codes an evidence KIND (causal,
  quant-synthesis, review, associational, qualitative, design, theoretical) and a rigour 1–3 judged
  within it; `scripts/kind_rigor_pilot.py` coded 38 stratified entries twice ($0.09): kind agreed
  37/38, rigour 33/38, and the judge said q misrepresents the study's value for 24 of 38 (Beittel
  1972, rigorous qualitative work, sits at q1 with bare design descriptions; Liang 2026's interviews
  score r3 at q2; Guzzetti 1993 is a q4 meta-analysis scoring r1 on its abstract). The whole wiki
  would cost about $4. **The scale is unchanged until the maintainer decides**; do not recode.
- **`--topics-file`** on `discover_articles.py` and `run_scrape_batch.py` replaces the built-in topic
  list. `eval/deep-dive/adult-language-learning/topics.txt` is the first: a deep dive testing whether
  depth in one area makes the wiki useful for a course build (usage simulation S1, Italian A1).

## 2026-09-29 — cost: write the citation once (v136); an output-price ceiling backfires; search and study counts fixed

- **Prompt v136 writes the source's citation once**, as `article.citation`; every `evidence[].citation`
  and `key_sources[]` entry is the token `L0b`, which `source_citation.expand_citation_token` (run inside
  `repair()`, so on every attempt) replaces before validation. Ingest and the validator see what they
  saw before. The repeated citation was a fifth of every output. **Benchmark** (10 articles, same
  routing, `eval/runs/bench-cost-b` v135 against `bench-cost-c` v136): median first-attempt output 5,308
  → 3,892 tokens, $0.0094 → $0.0068 an article billed, first-attempt passes 4 → 7, calls 19 → 15, GPT
  judge 4.10 both (9/10 → 10/10 pass); strict audit 0 non-verbatim quotes, 0 wrong DOIs, 1 missing
  statistic, as v135. `CURRENT` is still v135; moving it is the maintainer's call.
- **`OPENROUTER_MAX_COMPLETION_PRICE` / `OPENROUTER_QUANTIZATIONS` exist and must stay unset for
  batches.** A $0.45/M output ceiling with 4-bit hosts excluded routed most calls to Inceptron, whose
  input ($0.11/M) and cached input ($0.07/M) are dear, and cost rose 30% (bench-cost-a $0.0072, b
  $0.0094). A call here is ~27k tokens in (about half cached) and ~4k out, so input price matters as
  much as output; by list price the cheapest 8-bit host for that shape is GMICloud (~$0.0025 a call)
  and default routing sent it nothing. Routing also moves day to day: arm A, default routing, went to
  Inceptron too, and cost more than batch 9 ($0.0051).
- **Search** (`mcp_server` over `search_index`): when every word finds fewer than the limit, pages
  matching some words fill the rest, ranked by query words in title and description; titles that
  differ only in case or punctuation show once, with the others listed as `duplicates`. A brief-style
  query used to return nothing. Vocabulary is still a gap: "second language" does not find the "L2"
  claims.
- **Claim evidence lines count distinct studies**, with evidence_rollup's key, and show `(N entries)`
  when one study backs several entries: 398 pages said "2 studies" or more for one article.
- **Usage simulation** (six invented scenarios; wiki-only agents, a no-wiki baseline, a grader who
  fetched 18 cited statements; scratch files, not committed). Overall usefulness, wiki against
  baseline: Italian A1 3/3.5, nurse onboarding 3/3.5, algebra 3.5/3.5, retrieval lit review 4/4,
  funder priorities **4.5/3**, feedback-timing gap 3.5/4. The wiki wins traceability everywhere by 2–3
  points and honesty about gaps; the baseline wins relevance except for the funder, because it brings
  domain literature the wiki lacks (medication safety, adult mobile language learning, EAL maths).
  17 of 18 checked statements matched their page, so **where the wiki fails, the pages are why**.
  Ready: evidence audits of practice (`evidence.md`'s citation load against studies), checking a design
  rationale, stating gaps, a first pass at a core-topic lit review. Not ready: domain course builds,
  pattern and element pages as evidence (canonical ones are stubs citing no claims), effect-size
  comparison (most entries `i?`). About half of all searches found something useful. The grader's
  ranked fixes: (1) design-page links that point at the wrong claim — `strategy/timely_feedback`,
  `strategy/comparing_multiple_solution_methods`, `principle/gamification` (x3), `element/debrief`,
  all open, since choosing the right claim is a reading, and a check that link text matches its target;
  (2) study counts (done) and q4 codes on theoretical reviews, a book and Chi 1989 (n=10), open;
  (3) merge duplicate families (expertise reversal x3, spacing x6, `timely_feedback`/`timely-feedback`
  giving different advice) and let search favour claims. A subclaim coded `q4 i3` over its `q2 i?`
  entry and four pages still saying they had no evidence were corrected.

## 2026-09-28 (night) — batch 9, the droplet dress rehearsal

Run exactly as the droplet would: a venv built as `deploy/provision.sh` builds it, `deploy/dashboard_server.py`
on 127.0.0.1:8080, the batch launched from its `/launch-scrape` form (10 PMC, 70 ERIC, GLM, `CURRENT` = v135,
2 corrections, no provider pin), keys from `/etc/eval-harness.env`. 75 of 80 fetched; 67 ingested (501
pages), 6 rejected as out of scope, 3 failed validation after both retries (failed runs, still eligible).
50 of 76 passed first time; $0.386 billed ($0.0051 an article) over nine providers OpenRouter chose, Sail
Research 34 of them. Lint 0, verify clean, DOI problems 0, 0 impact codes without a statistic; strict audit
380 quotes (3 not verbatim, all on the failed record), 504 of 506 decimal statistics present (the 2 on it too).
What the rehearsal found, all fixed:

- **`provision.sh` cloned a dead branch** (`claude/research-scraper-test-setup-i4bh9m`); it clones `main` now.
  `/etc/eval-harness.env` also needs `EVAL_HARNESS_CONTACT_EMAIL`, which the dashboard passes to the batch.
- **An inverted author list cost a correct DOI eight times.** PMC's text prints authors surname first
  ("Husain Waqar"); GLM wrote "Waqar, Husain; ...", and the identity gate stripped `10.1002/brb3.71733` because
  "Waqar" is nowhere in the registry record. `source_citation.swapped_authors` rebuilds the list from the
  PubMed-format catalogue record when most first authors are swapped; the 8 pages carry Husain et al. (2026)
  with the DOI, Crossref-verified. 1 of 752 batch records had it.
- **GLM invents catalogue links.** Armbruster & Anderson (1982), fetched as ED218595, was linked to ED185595,
  which the article never prints. Across every batch, 30 records' source citations linked a neighbouring id,
  an old clearinghouse accession number (`BP006086`, `CE005601`) or an ERIC search URL. `repair` now replaces
  a link into the fetch catalogue that names another record; 458 citation lines and 229 `resource:` mirrors
  on 214+ pages were repointed to the record each source was fetched from, only on that source's own pages,
  and every rewritten `resource:` matches its page's body citation.
- **The gate left a stripped DOI in the `title:` mirror** on pages `sync_evidence_codes` does not rebuild
  (theories, strategies). `enrich.verify_page_citations` strips it there too. Ilhan & Guler (2018)'s
  `10.14689/ejer.2018.75.6` was stripped from all seven pages because Crossref holds only its Turkish title.
  **Restored on the maintainer's decision**, and the check now handles the case:
  `resolve_doi_conflicts.translated_record` verifies a DOI whose registry title is in another language
  (`foreign_title`) only when first author and year agree (the identity check), the registry journal is
  named in the citation, and its volume, issue or first page is printed there. The ingest gate passes the
  citation line (`cited_line=`) and `doi_resolver.check_all` applies the same rule. It was 1 of 2,644 cached
  records here, but ERIC indexes many Turkish, Spanish and Portuguese journals registered that way.
- **The load-bearing check missed the batch's own load-bearing claims**: `--top 200` stopped above the 13 new
  claims three pages from one source cite. `--min-designs 3` adds every claim at the threshold, and the batch
  passes it; only unjudged entries cost anything. One real failure: Armbruster's "most frame-slot questions
  went unanswered" (6 of 12 were), corrected from the article's tables. Load-bearing: 0 open, 0 never judged.

## 2026-09-28 (later) — batch 8 on the default prompt; recorded costs were list prices; providers differ 3×

- **Batch 8, the first on `CURRENT` = v135** (PMC 10, ERIC 70): 76 fetched, 67 ingested, 9 rejected as
  out of scope, every record on v135. Strict audit: 316/316 quotes verbatim, 318/318 decimal
  statistics in their articles, 0 impact codes without a printed statistic, lint 0. Three errors
  corrected by hand: Ebadi (2016) cited as 2014 on seven pages (a year from another Ebadi paper in the
  reference list, which also kept `source_citation.repair` from matching the source); Bautista (2015)
  as "Bautsta" on nine pages, from PDF text that lost its "ti" and "ff" ligatures (the DOI was right);
  a course case study coded as a review.
- **Every cost this pipeline recorded before 2026-09-28 was an estimate, not a bill.**
  `cost_source: list_pricing` means the generation-stats lookup had not settled and the model's
  headline price was applied whatever provider served the call: batch 7 recorded $0.0023 a call where
  Sail Research billed $0.0029, batch 8 $0.0030 where InferenceNet billed $0.0012. GLM's price did not
  double; the estimate moved with the headline listing. `openrouter_client` now records `usage.cost`
  from the response itself (`cost_source: usage`), the billed amount. To audit an older run, look up
  each `generation_id` at `/api/v1/generation`.
- **What an article costs depends on the provider OpenRouter picks**: 33 serve GLM 5.3 Flash, $0.14 to
  $1.00 per million output tokens. Batches 7–8: Sail Research 91 articles, 74% first-attempt pass,
  $0.0034 billed; InferenceNet (4-bit) 38, 71%, $0.0012. The 10-article benchmark pinned to
  InferenceNet: 9/10 validation (one quote still not verbatim after both retries), judge 9/9 and mean
  score 4.28 against 4.22, $0.0017 billed per article against $0.0050 on default routing. InferenceNet
  also caches the 15k-token system prompt ($0.010/M against $0.045/M). `OPENROUTER_PROVIDER_ORDER`
  (comma-separated) sets a preference and `OPENROUTER_ALLOW_FALLBACKS=0` pins it; unset, OpenRouter
  chooses. **The maintainer decided (2026-09-28) not to pin a provider**: a cheaper quantised host
  and upstream rate limits (DeepInfra returned 429s for GLM in testing) were judged not worth the cost
  difference. The batch leaves it unset; the variable applies only to models under
  `OPENROUTER_PROVIDER_ORDER_MODEL` (default `z-ai/glm`), so the GPT judge is never pinned by it.
- **OpenRouter's `:batch` models are unusable here**: the Batch API retains submitted data, which the
  account's zero-data-retention setting refuses (422). At the listed batch prices a first attempt would
  cost about 17% less, not 50%, and retries could not use it.
- **Lean correction retries do not pay** (`--lean-retries`, off by default). A retry is sent without
  the article only when every error is fixable from the output alone; on the 19 batch-8 articles that
  needed corrections, 1 of 13 retries qualified, because retries are driven by quotes that are not
  verbatim and impact codes with no printed statistic, both of which need the article. The system
  prompt alone is ~16k tokens, so even that retry saved under half its input. Records now carry
  `attempts`: each attempt's error fields, tokens and billed cost.

## 2026-09-28 — prompt v135: the extractor stops writing impact codes it cannot back

- **Prompt v135** (from v133) fixes the code table that still read "0 = negligible/unclear/null/
  marginal", requires any `i1`–`i3` to state the printed statistic with its value in the evidence
  description, lists what is not an effect size (p, t/F/χ², raw means, unstandardised β, R²,
  AUC, "large"), and gives bins for r (≥ .37 / .20 / .10) and η² (≥ .14 / .04 / .01) as well as d.
  v134 had only d bins, and GLM nulled printed correlations rather than bin them.
- **The validator enforces it** (`validator.EFFECT_SIZE_RE`, `expected_impact`): a non-zero impact
  with no printed effect size in the description or quote is an error, and so is one whose bin
  disagrees with the statistic it prints, or a "β" above 1 (a raw contrast estimate, not a
  standardised one). Errors go back through the correction retry, so the article fixes the code.
- **Benchmark (10 articles, GLM, same flags as bench-gate)**: v133 10/10 validation and judge, with
  13 of 31 non-zero codes printing no effect size and 17 mis-binned; **v135 10/10 and 10/10, 0 and 0,
  $0.028 against $0.029.** Runs: `eval/runs/bench-v134`, `bench-v135`, `bench-v135b`, `bench-v135c`.
  Two pattern bugs were found on the way and fixed: "SD = 2.56" read as a d, and "η2-values of
  .059" not read at all (it failed an article in v135b).
- **`CURRENT` is v135** (maintainer's decision, 2026-09-27), so a batch launched without
  `--prompt-version`, from the command line or the dashboard, runs on it. It was v99 until then, and
  batches 1–7 were given v133 by flag. Batch 8 was the first run on the default.

## 2026-09-27 (late night) — every `i` code now rests on a printed magnitude: 455 entries recoded

- **`scripts/recode_impact.py`** takes each entry `health_evidence.py` flags (an `i1`–`i3` with no
  effect size or test statistic in the entry), has GPT read the study's text (the fetched article,
  else the OpenAlex abstract) and quote any effect size printed for that finding, and keeps a code
  only when the quote is verbatim in the text **and names its statistic** (a bare ".166" beside
  "variance explained" was offered as η²). The bin is computed from the value, never taken from the
  model; r, η² and odds ratios go through the standard conversions for the bin only, and the page
  shows the statistic as printed. Everything else becomes `i?` with a note saying what was read.
  Subclaims resting on the entry follow it, including through accent-folded anchors.
- **Result, $0.82: 441 of 455 became `i?`, 14 kept a verified statistic** (9 `i2`, 3 `i3`, 2 `i1`).
  Of the `i?`: 311 on full text that prints none for the finding, 77 on abstracts (the note says the
  full text may), 53 with no source text on this machine. Verified by parse: 379 pages, 440
  frontmatter `i` values changed, no source entry added or dropped, no other key touched; all 537
  subclaims on recoded entries agree with their entry. The health report's count is now 0.
- **The extractor produced these** because prompt v133's code table read "0 =
  negligible/unclear/null/marginal"; v135 (above) fixes it. A batch still on v133 needs
  `recode_impact.py --check` then `--apply` afterwards; the health report counts what is left.

## 2026-09-27 (night) — one health report covers evidence and links; the DOI check's 61 problems were 3

- **`python3 scripts/wiki_health_check.py` is the general health report.** Beside lint, citation
  conflicts, DOIs, duplicates and the TODO backlog (now naming the TODO pages), it carries
  `scripts/health_evidence.py`'s section: load-bearing claims (3+ design pages) by what the judge
  has on them at their current text (checked / an abstract could not settle it / not checkable /
  never judged / open failure), how many rest on one study, abstract-only entries, `i1`–`i3` codes
  with no effect size or test statistic in the entry, unmarked claim citations, and pages with no
  link in or out. Offline and model-free (it reads only cached abstracts); every run appends to
  `eval/health/history.ndjson`. Run on its own: `python3 scripts/health_evidence.py`.
- **"DOI resolution problems: 61" was 3.** `doi_resolver.check_all` compared the registry title
  with `check_citations`' 160-character excerpt, which a long author list ends before the title:
  58 "resolves to a different paper" findings, 0 real. It reads `full_line` now, and accepts a
  title that is the other's prefix (Crossref's "Two Strikes" for the page's full title), never
  containment elsewhere, so the Bandura case is still refused. Of the other three, two were
  parser bugs: `check_citations.DOI_RE` stopped at `[` in a SICI DOI, and `resolve_doi` put an
  unencoded `#` into the Crossref URL. One was real: `10.1123/jpah.2017-0457` has no doi.org
  handle; the Brusseau citation now carries Crossref's record, `10.1123/jpah.2016-0028`.
- **The count of `i` codes with nothing behind them is 455, not 250**: the first figure matched
  any stray letter. Raw means with no SD, "significant" with no number and a model's
  "substantially" are what the rule means by an impact with no printed magnitude.

## 2026-09-27 (evening) — the load-bearing check has a runbook and runs in every batch

- **`eval/load-bearing/README.md` is the procedure**: when to run `check_load_bearing.py`, how to
  read each verdict, the judge's known errors, how to fix an entry and what regenerates after, and
  how to dismiss. **Read it before acting on a failure.** `run_scrape_batch.py` runs the check
  (top 200, $0.25 cap) after linking, so a batch reports on the claims it made load-bearing; only
  changed or newly ranked entries are judged, so a routine run costs cents.
- **Every open failure is settled: 0 open.** Across both runs, 30 entries failed or named another
  work; 25 were real and are corrected, 2 were judge errors and 3 were wrong OpenAlex abstracts.
  **`--dismiss` records a checked failure** in `eval/load-bearing/reviewed.ndjson` (committed),
  tied to the entry's text, so any later edit re-opens it. `--claims <slug>` re-judges a fixed page.
- **Five batch-claim titles overstated their source and were corrected in text only; the slugs
  are unchanged**, so every link and design reference still resolves: the LoA "all 20
  technologies", the LVN and STRP cases, the C/I-cycle classes and the BRT course-schedule
  proposal. One `link_claims.py` link joined that proposal to Behavioral Relaxation Training on the
  acronym "BRT" alone and was removed. Acronym collisions are a known risk of BM25 candidates.
- **Fixed the same night (see above): 455 evidence entries coded `i1`–`i3` with
  no effect size or test statistic in the entry** (first counted as 250 with a looser match), and 621 carry a bare `q2 · i1` codes line. Most come from
  batches. The extraction prompt contradicts itself: v133 says `null` when no effect size is
  printed, and its code table two sections later still reads "0 = negligible/unclear/null/marginal".
  Recoding needs each source read, not a regex, and the prompt fix needs a benchmark run.

## 2026-09-27 (later) — every kind is linked; the judge is spent where the wiki leans

- **`scripts/link_pages.py`** does for theories, principles, patterns, elements and strategies what
  `link_claims.py` did for claims: each page outside the main component gets its source's other pages
  (from the manifest) and its BM25 neighbours of any kind, and GLM says `related` (same kind, both
  `## Related <Kind>`), `applies` / `applied_by` (the more abstract page's `## Examples`) or
  `evidence` (a claim, into `### Claims` with a marker). A marker is never stronger than the
  claim's recorded evidence: S needs two studies and a q3, M one study at q2 (`strength_cap`). No
  claim link goes onto a strategy or element, whose claims sit in prose sections. 1,256 pages,
  $0.12: **isolated pages 718 → 90, main component 82% → 96%.** 267 pages got no link because no
  candidate fitted, and were left alone. The batch runs it after `link_claims.py`.
- **The batch runs with no gating judge; `scripts/check_load_bearing.py` is where the judge goes
  instead.** It ranks claims by the design pages citing them and judges each evidence entry against
  its study's text: the cached article when the claim came from a batch, otherwise the OpenAlex
  abstract for its DOI. On an abstract, absence is `unverifiable`, never a failure. It writes nothing
  to any page. **The claims the wiki leans on are not the GLM batches' claims**: of the 137 claims
  three or more design pages cite, 3 came from a batch, so the extractor's ~13% misstatement rate
  sits mostly on pages little rests on. First run, top 200 claims plus their re-ranked neighbours, $0.54:
  366 entries, 168 pass, 178 unverifiable, 19 fail. Ten of the failures were real and are corrected
  (Trypke et al. 2023 and Lively et al. 2023 each read as the opposite of their abstracts' findings;
  Stefanou et al. 2004 is a framework paper cited as an evidence review; van Merriënboer et al. 2006
  is a design argument coded as a q4 experiment with a large effect; Sinha & Kapur's productive-failure
  range; Deci et al. 2001's "modest"; Bowers et al.'s "particular benefit for younger students";
  Sweller & Cooper's same-structure limit; Stokamer's r; Orr's own table). **Read the judge's failures before acting**:
  three were its mistakes (a nine-author list OpenAlex truncates; two online-first years), and
  `claims/loa-pilot-self-reported-increase-all-20-technologies` now contradicts its own title, which
  is the maintainer's call to rename.
- **OpenAlex attaches the wrong abstract to some classics**, under the right DOI and title: a Spanish
  thesis's for Wood, Bruner & Ross (1976) and Deci (1971), an English action-research study's for
  Alfieri et al. (2011). `abstract_usable()` refuses a non-English abstract; `--report` lists a
  `not-this-study` on an abstract as a registry problem, not a page problem.

## 2026-09-27 — claims are linked and merged; search runs on an index

- **`scripts/search_index.py`**: SQLite FTS5 over every content page, in `.cache/` (ignored), rebuilt
  when the content folders change. `mcp_server.py`'s `search` uses it (`"engine": "fts5"`) and falls
  back to the scan when it cannot.
- **`scripts/link_claims.py`**: each claim's eight nearest claims (BM25), labelled by GLM as `same`,
  `general`, `specific`, `contradicts` or `related`, written with `--apply` into BOTH pages'
  `## Related Claims` with the label after the link. Decisions go to `eval/runs/claim-links/` first.
  It moves no evidence. The whole corpus cost $0.14 (2,248 claims); 4,089 pairs were linked on
  2,147 pages. **Claim pages with no link in or out went 1,226 → 10**; pages in the main component
  56% → 82% (718 isolated pages remain, none of them claims: theories, elements, strategies).
- **`scripts/merge_claims.py <keep> <fold>`** moves `<fold>`'s evidence entries (skipping a study
  `<keep>` already carries), subclaims, discussion and related links onto `<keep>`, deletes `<fold>`,
  and runs `update_links_for_renames.py` so every link is repointed and `<fold>` becomes an alias.
  **84 duplicates were merged** (2,248 → 2,164 claims; `eval/runs/claim-links/merges-applied.tsv`).
  GLM proposed 369 `same` pairs and is too loose to trust alone: a merge needed GLM `same` from both
  sides, GPT confirming with both pages' findings and studies in view (219 of 369), and a person's
  read, which dropped 11 of the 95 (broader-vs-narrower pairs such as manipulatives vs hands-on
  learning). Distinct studies stayed 860; 158 evidence entries were the same study on both pages.
  The single-study share rose to 91%, because duplicates mostly shared their one study: **new
  multi-study claims come from new articles attaching to existing claims, not from merging.**
- **Immutable research files keep the old slugs**, and aliases resolve them: `check_research.py --why`
  now follows an alias, and the four `observations/` records naming merged claims were repointed.
- **`run_scrape_batch.py` links each batch's new claims after the verify step** (`--new --apply`)
  and rebuilds the indexes. `same` pairs are listed, never merged automatically.

## 2026-09-26 (late night) — the batch runs without a gating judge; what merging and scale will need

**The unattended batch no longer gates on a judge.** On batch 7 GLM cost $0.0027 an article and the
GPT judge $0.0047 more, which a full ERIC run (170,647 peer-reviewed full-text records) cannot carry.
`run_scrape_batch.py` now passes `--judge-sample 0.05`: a hash-chosen 5% is judged as a spot check
(`record["judge_sample"]`), never read at ingest. `--judge-gate gpt` still exists for a run that can
afford it. The cost is known: GPT failed 9 of 71 validated extractions (13%) for misstatements the
validator cannot see. **No cheap judge replaces it** (71 extractions, GPT with the catalogue-URL note
as reference): GLM 5.3 Flash, Gemma 4 31B and DeepSeek V4 Flash passed nearly everything and caught 0
of 9; gpt-oss-120b caught 3 of 9 with 5 false alarms; GPT shown only the quoted passages caught 6 of
9 with 9 false alarms and saved a third. A regex for null-as-no-effect wording flagged 4 passes and 0
fails. Qwen 3.7 Flash is excluded by the account's zero-data-retention setting.

**Merging, measured.** A replay of batch 7's 313 new claims against the 1,934 before it (TF-IDF top 5,
GLM classifying, $0.011): 2 same proposition, 19 a specific instance of a general claim, 3
contradicting one, 126 related, 163 new. Retrieval is the weak part (median top similarity 0.07–0.08),
so these are floors. Separately, **27% of content pages (1,934) have no link in or out**, 1,226 of them
claims, mostly from batches: extraction writes claims nothing cites. Title near-duplicates at cosine ≥
0.6: 128 claims.

**Scale, measured.** 7.5 pages per source, ~7 KB each; `claims/index.md` is already 654 KB (~160k
tokens, too large for an agent to read), `wiki-index.json` ~520 B and `reverse-index.json` ~340 B per
page, and the MCP server loads both and scans linearly. At ERIC's peer-reviewed size without merging
(~1.3M pages) the flat indexes pass GitHub's 100 MB file limit and the docs site passes Pages' 1 GB.
Search itself scales: SQLite FTS5 over title and body answered in 0.9 ms at 7,024 pages and 14.7 ms
at 140,480 (a 20× synthetic copy, 687 MB), so agents can navigate by search at full size once the
server uses an index rather than a scan.

## 2026-09-26 (night) — the evidence layer: per-page profiles and `evidence.md`

Every page that cites claims (principles, elements, patterns, strategies, processes, methods,
theories, learner variables) now carries a second banner line, like a claim's:

    > **Evidence** · 12 claims (9 for, 2 mixed, 1 against) · 19 studies, `q2`–`q4` · 9 of 19 report an effect size · 3 claims rest on one study

and `evidence.md` (in the nav as *State of the Evidence*) rolls the corpus up: studies by tier,
the studies the most claims rest on, citation load against evidence base, claims cited both for
and against, coverage by kind, and how far `observations/` is from a first pooled estimate.
`scripts/evidence_rollup.py` computes both; `add_evidence_profile.py` writes the lines and
`build_evidence_report.py` the page (regenerated by `build_indexes.py`, `--check` in CI). Both
run in the batch chain. Rules, and why:

- **Count distinct studies, never claims.** One source yields many claims: Karpicke (2017), a
  review chapter from the pre-extractor test's Opus arm, stands behind 34 claims and is the only
  study under every one of them. Entries are one study when they share a DOI or a year and the
  first six title words (union-find); on the corpus that merges 868 keys to 790 with no group
  holding two DOIs.
- **A study's tier is the one most of its entries give, ties to the lower.** The minimum let one
  stray q1 outvote 78 q2 codes on Karpicke.
- **No verdicts, no league table, no averaged `i`.** Ranges and counts only. `i` is a bin and
  `i?` is not 0, so pooling waits for `observations/`, and the page says how far away that is.
- **87% of claims rest on one study, and that is mostly the pipeline**: an extraction makes
  claims from one article, so a claim gains a second study only when a later article is merged
  into it. Merging evidence into existing claims is the growth path this number measures.
## 2026-09-26 (night) — batch 7, the first under the judge gate

77 of 80 fetched; 71 ingested (532 pages), 6 rejected as E2, $0.55 all in. 53 passed validation
first time, 71 after correction; the GPT judge failed 14 of the 71, one revision fixed 6. **Five of
the remaining 8 failures were the judge's mistake**: it saw the ERIC URL `source_citation.repair()`
adds, found it nowhere in the article, and called it fabricated. `run_judges(..., source_url=)` now
tells the judge where that link comes from; re-run as `batch-7b`, all 8 passed (4 after a revision)
and were ingested, each with a later `ingested` manifest line after its `judge-failed` one. Strict
audit: 380/380 quotes verbatim, 714/714 decimal statistics present (a Swedish "7, 5" and an OCR
".4e3" read as .463 aside), 16/17 DOIs right paper; the 17th, PME-NA 2020's proceedings-volume DOI
`10.51272/pmena.42.2020`, was stripped by the gate from 6 pages. **Read a judge's failures before
trusting them**: the judge is a model and can be wrong about the pipeline it sits in.

## 2026-09-26 (evening) — the extractor benchmark is 10/10, and a judge now gates the batch

GLM on v133 through the full new chain (`bench-gate`): **10/10 pass validation, 10/10 pass the GPT
judge**; strict audit: 7/7 DOIs right paper (author and year included), 68/68 quotes verbatim, 192/192
decimal statistics present in the article (one, 76.71, printed "76 .71" by the PDF). About $0.008 per
article with the judge. What changed, and why:

- **`pmc-5932263` left the benchmark**: PMC no longer marks it open access, so it could never pass.
  Replaced by `pmc-11473304` (Huang et al. 2024). Do not scrape the HTML page to get it back.
- **The source's own citation gets its link from the pipeline** (`scripts/eval/source_citation.py`):
  a citation naming the article with no link gets the catalogue URL it was fetched from, and a bare
  homepage standing in for one (GLM wrote `https://www.aera.net`) is replaced. Validator demands for a
  "DOI/URL" on reports with none were 23 of v133's 25 citation errors, and each retry asked for an
  invented DOI.
- **A failed quote's retry is shown the closest article passage** (`ground_truth.nearest_passage`), or
  told none resembles it.
- **A reply that hits max_tokens and does not parse is resampled**, up to twice. All 12 of GLM's
  unusable outputs to date stopped exactly at the cap; one recurred in this benchmark and the
  resample recovered it. `generation.finish_reason` and `runaway_resamples` are recorded.
- **The Gemini judge scored every extraction 5/5 and is not a signal.** The GPT judge, now routed
  through OpenRouter when no OpenAI key is set, found real misstatements the validator cannot see:
  non-significance reported as "no effect", an ANOVA's df read as n, correlations worded as causes.
- **`--judge-gate gpt`**: a validated extraction the judge fails gets one revision with the judge's
  issues, kept only if it re-validates and the judge no longer fails it. 3 of 10 failed; all 3 were
  fixed. Ingest skips a record the gate still fails, as `judge-failed` (a failed run: the article
  stays eligible).
- **`run_scrape_batch.py` now runs generation with `--require-source-quotes --ground-truth
  --judge-gate gpt`.** Before, quotes were checked only at ingest, where a bad one could only be
  dropped (80 entries in batch 2); now the retry fixes it from the article.

## 2026-09-26 (later) — a citation pass checked against author and year

Every DOI-bearing citation was compared with its full Crossref record, **first author and year
included**. The existing tools compare title and journal coordinates only, and that is not enough:
a similar title passed `classify_doi` for Pronovost (2006) on a 2008 AJIC paper, and a first-author
match alone produced hybrids (Mayer & Fiorella cited under Mayer's single-author chapter). The pass
removed 67 DOIs of other works, rewrote about 290 invented or shortened titles, and moved conflicts
33 → 22 and invented-title DOIs 109 → 31. What it could not settle (reprint and edition DOIs,
partial titles with no coordinates) was reported, not written.

- **Who and when are now checked, in code.** `citation_identity.identity_mismatch(key, record)`
  compares the citation's author-year key with the registry's first author, year and record type,
  and `classify_doi(..., key=)` applies it, so the ingest gate, `standardize_citations.py` and
  `resolve_citation_metadata.py` all refuse a DOI of another work however well its title matches:
  a 2008 paper for Pronovost (2006), Bloch's review of *Situated learning* for the book, a PsycEXTRA
  dataset record for the journal article. Author order wrong on the right paper (Dweck 1998 for
  Mueller & Dweck 1998) passes, because the year agrees. On the corpus it rejected 2 of 9,560
  citations the pass judged correct, both PsycEXTRA records. `coauthor_mismatch` is report-only: it
  blocks a title rewrite and a fill, never removes a DOI, since most of its hits were right DOIs
  with invented co-authors.
- **A fill needs more than a plausible title.** `standardize_citations.fill_refusal` requires a
  close title, agreeing co-authors, and no multi-author citation matched to a one-author record;
  the loose test had re-added Mayer's single-author chapter to three Mayer & Fiorella citations.
- **`resolve_doi_conflicts.py --apply` refuses to run** without `--allow-cluster-rewrite`, and its
  Crossref search fallback is off without `--allow-search`. Even with search off it rewrites whole
  author-year clusters without checking each page's own citation.
- **The ingest gate edits only the citation line it checked**, strips bare-URL DOIs
  (`https://doi.org/X`, `doi:X`) as well as linked ones, removes that entry's frontmatter
  `resource:` mirror, and reports prose DOI links it cannot vouch for (unregistered, or just
  removed from the citation) without editing them. It used to replace the link form anywhere on
  the page and could not touch a bare URL, which is why batch 5's manifest records two removals
  that never happened (Harkins et al. 2021's wrong `…0026.203`, since corrected to `…0026.202`; and
  Shvidko 2020's `10.26077/936a-72f7`, which was right).
- **`run_scrape_batch.py` runs `resolve_citation_metadata.py --apply --titles`**, so a title
  corroborated by journal, volume and first page (and by the authors) is corrected in the batch.

## 2026-09-26 — a Crossref 404 now asks DataCite before a DOI is stripped

Batch 5's ingest gate stripped `10.26077/936a-72f7` from eight pages as `not_found`. DataCite
registers it to exactly the cited article (Shvidko 2020, Utah State's digitalcommons); Crossref
simply does not index DataCite. `doi_resolver.resolve_doi()` now falls back to
`resolve_datacite()` on a Crossref 404, so `classify_doi` title-checks a DataCite DOI like any
other, and a wrong DataCite DOI is still `wrong_paper`. **DataCite supplies the title only**:
journal, volume, issue and pages stay `None`, so repository-supplied metadata never rewrites a
page's coordinates. A cached unresolved entry without a `registry` key predates the fallback
and is re-resolved.

## 2026-09-25 (night) — the gap queue is empty: every claim page carries evidence

The gap queue (`priority_worklist.py --queue gap`) went from 304 to 0 across #105–#108. Each
claim was filled by one agent working from `scripts/eval/gapfill/TASK.md`, or, for a
near-duplicate, from a sibling's verified draft after checking the sibling's evidence tests the
duplicate's claim. The process and its lessons are in that folder's README. **Do not re-run
the gap-fill over these pages;** further work is deepening them (full text for abstract-only
entries, more studies), not filling them.

- **Read each agent's report before applying its draft.** The corrections reviewers made
  most often (invented subtitles, rounded or computed numbers, numbers taken from another
  paper's summary, overlap statistics coded as d, one study coded differently on two pages)
  are now rules in `TASK.md`.
- **About a dozen pages now contradict their own titles** (laptop notes, structured peer
  assessment, self-affirmation, learner-built organizers, handwriting-intervention
  equivalence and others): each says so in its Discussion, and renaming is the maintainer's
  call.
- **Abstract-only evidence is admitted as weak evidence with a conditional note** (maintainer
  decision): `(abstract only)` in the codes line and a sentence saying what the abstract could
  not establish. Most entries from this pass rest on abstracts. See
  `eval/abstract-only/PLAN.md`, where the status-cap question is still open.
- **Two pages had bodies about the wrong subject** (peer-assisted learning carried the
  worked-examples claim; self-determination instruction was framed as SDT needs theory). They
  were corrected to match their slug and inbound links, with the old text kept in a
  `<!-- deprecated -->` block. When a page's text and its inbound links disagree, the links say
  what the page is cited for.

## 2026-09-25 (later) — batch 4, a bad provider, and a DOI sweep that nearly deleted good DOIs

- **OpenRouter routed 51 of batch 4's 78 GLM calls to OpenInference, and all 51 failed** (22 said "no
  article text was supplied" to a 28k-token prompt carrying the article). `openrouter_client` now sends
  `provider.ignore` (`OPENROUTER_IGNORE_PROVIDERS`, default `OpenInference`) and every record stores
  `generation.provider`. Check pass rate by provider before blaming a prompt. After the fix: 73/78 pass.
- **ERIC discovery filters on `e_fulltextauth:1`**, ERIC's own "we host the full text" flag: 58/60 fetched,
  against 32/125 under the old ED-prefix rule. **arXiv works without Kaggle credentials**:
  `kagglehub.dataset_download('Cornell-University/arxiv')` downloads anonymously (5.5 GB, cached).
- `run_scrape_batch.py` gained `--resume` (skip discover/fetch, regenerate only missing records) and
  `--concurrency` (default 6; sequential GLM took ~5 min per article).
- **A DOI with no doi.org handle does not exist anywhere**, and `resolve_citation_metadata.py` now removes
  it (`doi_resolver.handle_registered`; a failed lookup is `None` and changes nothing). `--all` extends
  the run to DOIs no divergence check flagged. **Its first version removed correct DOIs from 49
  citations** (Hattie's *Visible Learning* on 16 pages), because `check_citations` stores each citation
  line cut to 160 characters, so a long author list pushes the title past the cut and the title test
  compares against a fragment. Records now carry `full_line`, title reads use it, a title-based removal
  needs the registry title to be mostly absent from the whole line, and title-mismatch removal is never
  done without journal coordinates. On DOIs no other check flagged, metadata and title changes are
  reported, not written. **Audit a removal pass by checking each removed DOI's registry title against the
  full line**, as the second pass did: 161 removals, 0 of them wrong. `check_citations`'s own title-
  divergence check still reads the 160-character excerpt.
- **Evidence-less claims can be filled by in-session agents** from Crossref-verified sources they read;
  five of the most-cited stubs were (active learning, feedback levels, assessment for learning, belonging,
  cognitive overload). Most sources were abstract-only, which the entries say, and three of the five
  qualify rather than simply support their claim.

## 2026-09-25 — the first two in-session GLM batches, and what they changed for the droplet

Two batches through `run_scrape_batch.py` with GLM on **v133 and 2 correction attempts**: 96 articles
ingested, 12 rejected as E2, 3 failed, about $0.45 in generation. Claims with coded evidence 274 → 597
(47% → 66%), lint 0. Four things the droplet needs before it runs another batch:

- **A correction retry used to carry no article.** GLM, asked to fix quotes it could not see, answered
  "no article text was supplied" and rejected the source: 22 of batch 2's 51. It did so even once the
  article was included. `eval_harness` now puts the article back in the retry **and accepts a rejection
  only from the first attempt**; a retry that rejects is discarded. A re-check of batch 1's eight
  rejections confirmed seven and overturned one (`pmc-13600062`, which now has a later `ingested` line).
- **`verify_citation_edits.py` skips folder `index.md` files.** It stopped every batch that added pages,
  so lint, `check_citations` and the health check never ran after one.
- **The quote gate is doing real work.** It dropped 15 evidence entries in batch 1 and 80 in batch 2
  (76 claims with them). Most fail within their first quarter, so they are paraphrases, not OCR noise;
  the rest start verbatim and stitch on text the article does not contain. The decimal statistics on
  the surviving claims check out against the article text, apart from OCR readings of scanned reports
  (`F454=5:17` read as 5.17).
- **Batch 3 (v133, retry fix in place)**: 32 of 125 discovered articles fetched (ERIC PDF 404s), 30 passed
  (23 first attempt), 2 retry rejections discarded by the new guard, 1 correct E2 reject, 1 failure, $0.12.
  The quote gate dropped 8 entries (6 claims), against batch 2's 80; all 91 decimal statistics on the new
  claims appear in their articles. `verify_citation_edits.py` now also accepts the frontmatter
  `resource:`/`title:` mirror lines, so a Crossref-verified DOI fill no longer stops the batch.
- **PMC discovery is mostly off-topic**: 8 of batch 1's 10 PMC hits, and rejected correctly. Keep its
  share small.

## 2026-09-24 — in-session extraction, and what the pre-extractor test found

`eval/pre-extractor-test/` runs one article set through five extractors and scores them with one
scorer. **GLM on v124 ties Opus on quality at about 1/150th of the cost.** GLM's ~10% pass rate
belongs to the v99 lineage, which CURRENT pointed to until 2026-09-27 and v130 descends from. So do not read v130's
collapse as "GLM cannot follow the new criteria". The droplet's next step is porting v128–v130
onto v124, **without the `study_record`**: the ablations (v131–v133, `eval/pre-extractor-test/README.md`) show the small rules are free, the inclusion rule costs a few passes, and asking GLM for a study record in the same call drops it from 16/17 to 7/17. **17 articles were ingested from the Opus-agent arm** (237 pages, 10 study records):
the first batch written by in-session subagents. `scripts/eval/agent_arm.py` is that path's
harness, and the subagent contract is its `TASK.md`. Two ingest bugs it exposed are fixed: the
citation gate matched the frontmatter `resource:` line and called correct DOIs `wrong_paper`,
and typeless `related` slugs were linked into the wrong folder. The manifest lines for this
batch were corrected before commit. **`run_scrape_batch.py` never ran `sync_evidence_codes`, `add_evidence_summary` or `fix_dead_anchors`**, whatever this file said elsewhere, so every batch landed claims whose codes lived only in the body. They are in the chain now. And `okf_lib.parse_evidence_sources` read a DOI only from a `(link)`, so sync would have stripped the resource from the 267 entries whose citation carries a bare URL; it reads that form too now. `scripts/health_scorecard.py` measures any set of commits with today's checkers, and `eval/scorecard.md` is this session's. Run `fix_dead_anchors.py --apply` after an ingest: an
accented author name (Göktürk, Bellhäuser) still produces an anchor that does not match its
heading.

## 2026-09-24 — what a source needs to get in: `INCLUSION.md`

**The default is to include.** Every paradigm is eligible, including theoretical, philosophical and
qualitative small-n work. Evidence may be logical rather than empirical, one argument is enough, and
studies of the design process are in. **Domain or setting is never a reason to exclude**: a narrow
population is a scope qualifier on the claim. There are four exclusions, one per verdict code: E1
`opinion-piece`, E2 `out-of-scope` (not about learning at all), E3 `no-ingestable-content`, E4
`already-covered`. **An opinion cited by five or more wiki pages is ingested, not rejected**, coded
`q1` with an evidence entry saying no evidence or argument was offered, so that citing it visibly
justifies nothing. The `q` scale is unchanged; the maintainer declined a `q0`. Prompt v130 carries
the extraction side, with a claim floor of one and a rule that a reasoned argument is evidence.
`CURRENT` stayed at v99 then (v135 since 2026-09-27). **A research-methods paper is in only when it helps design** (a design
process, a way of building or iterating an intervention, or how one was made). The five earlier
rejections the criteria overturned were re-reviewed and ingested the same day, each with a later
`ingested` manifest line rather than an edit: Osguthorpe et al. (moral dimensions), Christensen &
West (design-based research), Dousay (ID models), Svihla (design thinking and agile) and Ellsworth
(educational change models). The
chapters are JavaScript-rendered, so a plain fetch returns an empty shell; render them with the
preinstalled Chromium (`--headless=new --dump-dom`, through `$HTTPS_PROXY`), not by guessing at
their content.

## 2026-09-24 — the evidence sync tools were half right, and a DOI with a `(` in it was half a DOI

`sync_evidence_codes.py --apply` then `add_evidence_summary.py --apply` looked destructive on nine
claim pages. Parsing the frontmatter before and after showed that **it dropped no entry**. What it did:

- **Renamed 10 hand-written ids** (`adesope-2017`) to the evidence heading's slug
  (`adesope-et-al-2017`). The tool was right here: `parse_evidence_sources` makes the id the heading
  slug on purpose, so it equals the `#anchor` the subclaims link to, and none of the old ids matched
  any anchor.
- **Re-synced the Rey (2012) title** left stale by #95.
- **Truncated two DOIs at their first `)`.** `[^\s)]+` read `10.1016/0010-0285(74)90015-2` as
  `…0285(74`. Two more pages (`contingent-scaffolding`, `part-task-practice`) already carried
  truncated resources on `main`. `okf_lib.LINK_URL` now accepts balanced `(...)` and `<...>`, which
  also covers the Wiley SICI form. It is used by `CITATION_LINE_RE`, `parse_evidence_sources` and
  `ingest_extractions._URL_RE`. No truncated `resource:` remains in the wiki.
- **Overwrote curated headers.** `add_evidence_summary.py` now replaces only a line in its own
  grammar (`generated_re()`) and keeps any other line, flagging a kept line whose study count
  disagrees with the entries. Ten are kept.

Verified by parse: 11 pages, 0 entries dropped or added, 0 other keys, 0 body changes. **A second
run of both tools changes nothing.** The lesson here is the reverse of the usual one. A line-count
summary of the first diff read the renamed `- id:` lines as deletions, and the "damage" report
repeated that. Parse the frontmatter before calling a tool destructive, as well as before trusting it.

## 2026-09-24 — the extraction priority list is generated, never kept

`scripts/priority_worklist.py` answers "what should the next extraction run read". It prints three
queues. `record`: articles the wiki cites with no `observations/` record, SMD-reporting first, then
by reuse. `hub`: WWC/ESSA pages from `smd_worklist.py`. `gap`: claims with no coded evidence, by how
many pages cite them. **Do not replace it with a hand-maintained list.** Every row is derived at run
time from `observations/`, `sources/manifest.ndjson` and the claim pages, so a row drops out on the
next run once its work lands. Work in progress shows up by being pushed: a branch ahead of main that
adds an evidence heading to a claim, or a DOI to `observations/`, marks that row `in-flight`. Nothing
it prints is committed, because the hub queue carries data from a repo with no licence.

## 2026-09-24 — a loose title match cannot rewrite a journal

`resolve_citation_metadata.py --apply` proposed 101 metadata corrections, and **99 of them were one
wrong DOI**. `10.1111/medu.12141` (Larsen, Butler & Roediger 2013, *Medical Education*) sat on 99
citations of Roediger & Karpicke (2006), whose *Psychological Science* 17(3) 249 was correct. The two
titles share "test-enhanced learning ... long-term retention", which clears `_same_paper`'s 0.35
overlap, so `decide()` treated the DOI as right and set out to rewrite every page into the other
paper. **`decide()` now returns `conflict` when the registry contradicts both journal and first page and
the titles are not the same title** (equal, or one a prefix of the other). A `conflict` is reported,
never written. It is the mirror of the `fix_title` rule: three coordinates can outvote a title, and a
word overlap cannot outvote three coordinates. The 99 pages now carry the Crossref-verified
`10.1111/j.1467-9280.2006.01693.x`. Read what `--check` proposes before running `--apply`: a
fix that repeats on 99 pages is one decision, not 99.

## 2026-09-15 — `consent.basis` gained a uniformity condition

`basis` holds one value; a protocol may govern sources held under several. Raised by
`learning-graph-structure` 1.0.0 in learning-engine-ai-frontend, whose three sources sit
under a CC-BY-NC licence, a bilateral undertaking that is none of the four enum values,
and nothing at all. `sources_uniformly_governed` is now **required wherever `basis` is
set**, `additional_bases` is required and non-empty when it is false, and `true` is the
fifth condition of the licence relaxation. Nothing was removed — the guard gained a
condition rather than losing one, and all six fixture mutations were verified to break
the benchmark release. Two protocols in learning-engine-ai-frontend were migrated in the
same change.

## State as of 2026-08-31 — the stack is collapsed

All three open PRs were merged into `main` in dependency order (#21, then #19, then #20).
`main` now carries the link repairs, the citation gates, the corrupted-page repairs *and*
the refilled content for them, the 135-slug normalisation, and the near-duplicate detector.
`lint.py` reports 0 and `mkdocs build --strict` exits 0 on that tree.

These three branches are **fully merged and dead** — do not resume a session onto them, do
not push to them, do not reopen a PR from them:

- `claude/research-scraper-test-setup-i4bh9m`
- `claude/fix-no-h1-pages-240eb2`
- `claude/normalize-slugs-forward-port`

Ten other remote branches are also fully merged into `main` and equally dead:
`brand/top-bar-lazuli-colors`, `claude/edtech-theories-principles-v2ezw5`,
`claude/jls-open-access-scraper-b45d3c`, `claude/learning-wiki-okf-conversion-6t5pjn`,
`claude/open-source-license-strategy-6q4gjc`, `content/merge-headings-and-highlight`,
`docs/scale-index-pages`, `feature/source-manifest`, `fix/log-md-formatting`,
`fix/pages-build-colon-filenames`.

Only four branches still hold unmerged commits — **this table was wrong when it was
written and is wronger now; see the 2026-09-11 audit below before acting on it**:

| Branch | Unmerged | Collision risk |
|---|---|---|
| `claude/standards-design-process-homes-q9qky1` | 4 commits, 54 files | **None** — works entirely in a new `goals/` folder, plus `log.md`, `sources/manifest.ndjson`, and one new script |
| `ci/detect-orphaned-pages-v2` | 1 commit, 2 files | Low — `docs.yml` + a new script |
| `ci/pr-preview-deploys` | contains the above | Low |
| `docs/material-theme-polish` | 1 commit, 6 files | **High and stale** — 3 days old, edits `build_indexes.py` and four `index.md` files that have since been regenerated many times. Re-derive the `mkdocs.yml`/`build_indexes.py` change on a fresh branch rather than merging this one |

## State as of 2026-09-11 — the research layer landed, and the branch table was wrong

`main` carries the research layer, the first real protocol, and #76's three hard observation
designs. **PRs #75, #76 and #77 are merged**, in that order, and `main` at `41427124` is green:
`lint.py` 0, `check_observations` 11 studies / 39 observations 0 issues, `check_research` 0,
`--crosswalk` 0 gaps, both index `--check`s current, `mkdocs build --strict` exit 0.

**All three `Deploy Docs` runs succeeded — checked rather than assumed**, because this file
documents four occasions where a merged change was simply absent from the published site while
`main` said it shipped. The `concurrency` group did its job: the three drained in order.

These three branches are **fully merged and dead** — do not resume a session onto them, do not
push to them, do not reopen a PR from them:

- `fix/logic-model-warrant-and-methods-folder-criterion` (#75)
- `feat/observations-cluster-network-singlecase` (#76)
- `claude/epic-hopper-kxb1a5` (#77)

**The "Only four branches" table above is wrong in both directions, and a hand-maintained
branch table is why.** Three of the four branches it names **no longer exist**
(`ci/detect-orphaned-pages-v2`, `ci/pr-preview-deploys`, `docs/material-theme-polish`), and it
misses six that do. Audited 2026-09-11 by comparing every remote ref against `main`:

```bash
for b in $(git for-each-ref --format='%(refname:short)' refs/remotes/origin); do
  echo "$(git rev-list --count origin/main..$b) $b"; done | sort -rn
```

That takes seconds and settles it. **Do not trust a prose branch list — run the command.**

What actually holds unmerged commits, and what each one is:

| Branch | State |
|---|---|
| `claude/standards-design-process-homes-q9qky1` | **Genuinely pending.** 4 commits, 54 files, 24,929 insertions and **0 deletions** — all new `goals/` content. No collision risk, as the older table said. |
| `enrich/droplet-batch-0831` | **Do not merge as-is.** 115 files, and `claims/acute-exercise-timing-memory.md` carries *committed* conflict markers (`<<<<<<< Updated upstream` / `>>>>>>> Stashed changes`) from an unresolved `git stash pop`. It cannot land silently — `lint.py --type merge_markers` catches it, verified on a trial merge — but the markers must be resolved before anyone tries. |
| `feat/citation-authorities`, `feat/doi-variant-families`, `fix/strip-doi-case-insensitive`, `fix/crossref-strip-and-metadata`, `fix/verify-each-page-before-filling` | **Superseded, almost certainly.** `main` already carries every artifact each one introduces — `authorities.py`, `apply_authorities.py`, `citation_worklist.py`, `log_authority.py`, `authorities.ndjson`, `check_citations.py --variants`, `proven_fabrications()`, case-insensitive DOI stripping. Each still shows a diff because `main`'s implementation differs, and **nobody has confirmed line-by-line equivalence** — so this says "superseded", not "identical". Re-derive on a fresh branch if something turns out to be missing; do not resume onto one. |

## State as of 2026-09-13 — the extraction target changes: depth in one scale, not coverage

Measured from `learning-engine-ai-frontend/experiments/research-evidence/wiki_trajectory.py`, which
reads `observations/` at any ref and is meant to be re-run rather than believed.

`main` holds **9 real studies, 36 observations, 9 measure types** (the two `example-*` records
declare themselves synthetic and are not studies — anything counting 11 is counting fixtures).

**The corpus is no longer diverging, and the old reason for pessimism was wrong.** Earlier notes
reasoned that each new study tends to open a new measure type, so adding studies would never build
depth. That treats a small-sample regime as a property of the corpus. There are only so many ways to
report an effect, and the pool can be estimated rather than assumed: a Chao1 estimate from
singletons and doubletons gives **13.2 against the 9 types already seen**. The measure-type pool is
bounded and nearly enumerated. New studies will start deepening existing families instead of opening
new ones.

**A measure type names an ESTIMATOR. A measure family needs a shared SCALE. These came apart here,
and it inverts the obvious recommendation.** `regression_coefficient` is the deepest label family at
3 studies and is **not poolable at all**:

- `zingaretti-2026` — β = 17.17 **words**, β = 13.33 **accuracy points**
- `rosario-2019` — β = 5.168, three-level growth-curve model, class-level Helmert contrast
- `jemr-lexical-elaboration-2026` — β = −0.17, unitless

Three studies, three incompatible scales. Counting labels overstates the corpus. Counting *scales*
also **understates** it in the other direction: **5 of the 9 studies already sit on a common
standardised-mean-difference axis** once the standard conversions are applied (Borenstein et al.,
ch. 7) — `guo-2026` and `martinengo-2024` are already d, `mantovani-2026` is r → d,
`jemr-lexical-elaboration-2026` is log OR → d, `frolli-2023` is η² → d.

#### What to extract next

**Prefer studies that report — or permit conversion to — a standardised mean difference.** Concrete
ordering when choosing what to ingest:

1. `standardized_mean_difference` / `cohens_d` / `hedges_g` — already on the axis. **2 studies now;
   the target is 30.**
2. `correlation`, `odds_ratio`, `risk_ratio`, `partial_eta_squared` — convertible. Record the
   ingredients a conversion needs (group sizes, baseline risk, df) or it cannot be made later.
3. Everything else — still worth recording as evidence beside a claim, but it does **not** build the
   family, so do not count it as progress toward depth.

Do not target `regression_coefficient` merely because it is currently deepest. An unstandardised β
adds a row and no comparability. A study reporting a **standardised** β does belong in tier 1 — note
which it is, because the schema's `measure_type` alone cannot tell them apart. That ambiguity is
itself worth fixing in `observations/SCHEMA.md` when someone next touches it.

**Why this axis and not another.** It is the metric every external corpus this programme can reach
already uses — What Works Clearinghouse (6,631 independent findings), `metadat`'s education subset
(303), Ma et al. 2014 on intelligent tutoring (107). Depth in standardised mean difference buys
comparability *outward* to those, not only statistical power *inward*.

**Where to find candidates: `scripts/smd_worklist.py`.** It ranks the WWC intervention reports and
Evidence for ESSA program pages that the Renaissance AI and Education Resource Hub catalogues (347
SMD-format pages and 30 practice guides as of 2026-09-24). It ranks by URLs the wiki already cites,
then by whether both publishers reviewed the programme, then by name mentions. It reads the hub's
published `data.json` at run time and **commits nothing from it**: that repo has no licence yet, so
its data stays out of this one until the maintainer says otherwise. It also copies no hub
description, and some of those quote effect sizes from model-written summaries. Take the numbers
from the WWC or ESSA page itself.

**The size of the prize.** Reaching 30 studies in one family at the corpus's current extraction
habit takes roughly **90 studies** (95% CI 45–270, wide because it rests on a 3-study family — read
the order of magnitude, not the point estimate). Extracting deliberately at one scale takes **28
more**. Same target, roughly a third of the work, and the difference is a choice about *what* to
extract rather than *how much*.

Re-measure rather than trusting this paragraph:

```bash
python3 experiments/research-evidence/wiki_trajectory.py --wiki /path/to/learning-wiki
```

## The health dashboard refreshes itself

`eval/runs/health.html` used to regenerate only on an enrichment batch, a scraper ingest,
the nightly timer, or a service restart — and a `git pull` is none of those. So the board
showed numbers from the last pipeline event while its own "last scanned" timestamp said a
minute ago, which makes a stale page look current. That cost a real debugging session.

`dashboard_server.py` now compares a cheap tree fingerprint (file count + newest mtime over
the content folders and `scripts/`, ~13ms) against the one stamped when the page was
written, and rescans (~6s) only when they differ. Pull, reload, correct numbers — no
restart. The fingerprint is deliberately **not** a git revision: the droplet's working tree
routinely holds real uncommitted work, and keying on HEAD would call all of it invisible.

## State as of 2026-09-02 — the design-spec `realizes:` targets exist

learning-design-spec's profiles and methods carry `realizes: <wiki-slug>`, with the kind
fixed by what carries the field: a profile realizes a **pattern**, a method realizes a
**strategy**. Eleven of them named nothing. These are the slugs they now resolve to:

| spec object | kind | slug |
|---|---|---|
| `dschool-design-thinking` | process | `design-thinking` |
| `gagne-systematic` | process | `systematic-instructional-design` |
| `sam-agile` | process | `successive-approximation-model` |
| `continuous-improvement` | process | `continuous-improvement-of-learning-materials` |
| `lxd-user-centred` | process | `learner-experience-design` |
| `faculty-course-design` | process | `faculty-course-design` |
| `goals/standards-crosswalk` | method | `standards-crosswalk` |
| `goals/cognitive-task-analysis` | method | `cognitive-task-analysis` |
| `personas/activity-system` | method | `activity-system-personas` |

**The kinds in that table were `pattern` and `strategy` for one day.** See *Two kinds for
the designer's side* below: design work is not instruction, and it now has its own two
kinds. A profile resolves in `process`, a method in `method`.

**Design thinking was two objects under one name.** `strategies/design-thinking.md`
describes learners running the cycle; a profile realizing it needs the *designer's*
process. That process is now `processes/design-thinking.md`, and the strategy page is
restored to `review` — the deprecation existed only because the process briefly needed
the `pattern` namespace, and it no longer does. Ids are unique *per kind*, which is what
makes the same slug in two folders safe.

**Two duplicate pattern pairs are collapsed, canonical page keeping the substance:**
`patterns/4cid.md` (1.2 KB stub) folded into `4cid-four-component-instructional-design`
(73 inbound links), and `gagnés-9-events.md` into the of-instruction page. Both stubs were
pure subsets — the long pages already carried every claim link, element and source. The
retired slugs are recorded as `aliases:`, so `realizes: 4cid` — which the spec and two
pattern plans already write — still resolves.

**Gagné's page is now ASCII: `patterns/gagnes-9-events-of-instruction.md`.** A non-ASCII
`id:` is an NFC/NFD normalisation trap for a repo that resolves it by string equality, and
untypeable besides; `é` survives in the title, the H1 and the author field, where it
belongs. Both former spellings are aliases. 62 inbound links were repointed by
`update_links_for_renames.py --map`, which also stamped the aliases.

**`deprecated` is now its own index bucket.** It used to fall through to `draft` in
`build_indexes.py`, and `strategies/` omits drafts from its listing — so the wiki's first
deprecated page was counted as a draft and then hidden. The two statuses mean opposite
things (draft: nobody has reviewed this; deprecated: reviewed and superseded), and a
superseded page has to stay findable, since being findable by an old reference is the
entire reason for keeping it. Deprecated entries are always listed, never elided.

**`learner-variables/` was invisible for weeks, and nothing could have caught it.**
`build_indexes.py`'s `PAGE_TYPES` never had an entry for the folder, and a folder absent
from that table is simply not iterated — so its `index.md` kept whatever it was last
written with (**"1 entries"**, beside twelve pages) and `ROOT_INDEX_TYPES` left the type
off the front page entirely, while the mkdocs sidebar listed it. Every check passed the
whole time, because every check reads *pages* and the defect was in which pages a
generator visited. `lint.py`'s `check_nav_coverage` now compares the three lists —
`mkdocs.yml`'s nav, the root hub's Knowledge Types, and `build_indexes.PAGE_TYPES` —
against the content folders on disk. `--type`'s choices are also derived from the check
registry now rather than repeated beside it; the hand-written copy had already fallen
behind and was missing `competing`.

**The nine new pages are `status: review`, not `draft`.** Draft means "skeleton or stub;
content not reviewed" and these are complete pages, so `draft` was simply the wrong value —
and it had a visible cost: `strategies/index.md` omits drafts, so all three new strategies
were absent from their own index. Status describes whether the content is written. Whether
anyone has checked it is the `verified` axis, and whether its citations resolve is recorded
in the manifest and in the per-page comments — not in `status`.

**Four `realizes:` fields are unset on purpose — do not write pages for them.**
`lightweight-default`, `elicited-default`, `personas/edge-coverage` and
`context/author-brief` are that repo's own baselines and named null cases. A wiki page for
them would be inventing a literature.

**`competency-based` stays unset, and a page for it is warranted but not writable yet.**
`patterns/competency-based-learning` is a pedagogical pattern; the profile is programme
governance — unbundling credit from seat time, assessment on demand, a competency
framework as the transcript. That is a distinct object at `grain_size: programme`, not a
rename of the existing page. It needs a source before anyone writes it; this sandbox has
no network for one, and guessing at a literature is the failure mode this whole file is
about.

**The nine new pages cite only what could be established.** This sandbox's egress proxy
blocks `edtechbooks.org` and `colorado.edu`, so none of the commissioning brief's sources
could be read. Their `## Key Sources` therefore carry exactly what the brief stated —
surnames, chapter number, book, URL — plus primary works already in this corpus, copied
verbatim. **No initials, chapter titles, years, journals, volumes or pages were inferred**,
including where inference felt safe: a chapter title read off a URL slug is a guess wearing
a citation's clothes. Each affected page carries an HTML comment saying which fields are
absent and why. They are `status: draft` and belong in `citation_worklist.py`'s book
backlog — a person with the chapters in hand can complete them in minutes, and nothing
automated ever will.

## State as of 2026-09-03 — Crossref is reachable from the sandbox, and the wiki has SLA claims

**This file said in four places that this sandbox cannot reach Crossref. As of 2026-09-03 it can.**
`api.crossref.org` answers, and so do `pmc.ncbi.nlm.nih.gov`, its ID converter, and the publisher
sites. Seven DOIs were resolved and put through `resolve_doi_conflicts.classify_doi` with the
cluster's own title words — the same call the pipeline makes — and all seven returned `verified`.

That unblocks work this file has been deferring to the droplet for days: the 97/64 citation
conflicts, the 21 DOI collisions, the 317 metadata disagreements, the 120 invented titles, the 15
variant families, and `proven_fabrications()`. **Check before assuming, in either direction** — an
allowlist can change back, and `classify_doi`'s `error` status still means "the lookup failed", not
"the DOI is wrong". Call it once at the start of a citation task and act on what it says.

**The wiki now has second-language-acquisition claims: six of them**, converted from drafts written
by a Lazuli Studio session against an Italian A1–B1 course. They are the first pages in this repo
whose citations were **Crossref-verified at authoring time** rather than written and deferred.

Their slugs are cited already by six course documents in that repo, so **do not rename them**:
`l1-predicts-l2-phoneme-perception-more-than-proficiency`,
`italian-l2-motivation-is-ideal-self-not-instrumental`,
`strategy-use-correlates-with-l2-proficiency-in-adolescents`,
`italian-gender-stays-incomplete-for-l2-and-heritage-speakers`,
`l2-fluency-gains-persist-weeks-without-practice`,
`game-based-practice-outperforms-traditional-l2-vocabulary-instruction`.

**The handoff said "no SLA coverage at all"; that was overstated and worth correcting**, because a
new page that believes it has no neighbours lands isolated. `heritage-language-preservation-supports-english-acquisition`,
`bilingual-fluency-enhances-metalinguistic-awareness`, `incidental-vocabulary-exposure-limited`,
`learning-strategy-instruction-contextualized-more-effective`,
`conversational-turns-predict-language-development` and
`phoneme-awareness-stronger-predictor-than-rhyme` were all already here, and the six new pages link
into them. Three also join a learner variable's `## Claims`: L1 background and heritage/L2 gender to
`reading-and-language`, strategy use to `self-regulation`, motivation to `motivation`.

**One citation in the handoff named the wrong journal**, and the resolution caught it: the
game-based study was given as "Frontiers / PMC10443373". PMC's own ID converter maps that id to
`10.3390/pediatric15030046` — *Pediatric Reports* 15(3), 502–511, **2023**, Frolli et al. Exactly the
invented-journal shape this file documents at length, stopped before it landed because the DOI was
resolved rather than the URL copied.

**`yaml_escape` did not quote a leading `?`, so a `q?`/`i?` code could never reach frontmatter.**
`dump_frontmatter`'s comment claimed it did. In value position YAML reads a bare `?` as the
complex-mapping-key indicator, so `i: ?` raises *"mapping keys are not allowed here"*, and
`sync_evidence_codes`' write gate correctly refused three of these six pages rather than shipping
broken YAML. The corpus had no `?` codes before now, so nothing was ever silently lost — but the
schema is explicit that `q?` means "somebody looked and could not establish it" and must be
preserved, which made this a bug waiting for its first page. Fixed in `okf_lib.yaml_escape`; a `?`
anywhere but the first character still stays bare.

**Evidence codes on the six are readings of the reported design, not of the authors' ratings.** The
handoff's `evidence_strength` values are kept as it set them — the field is vestigial and the design
side does not read it — while `q`/`i`/`n` come from what each paper actually did. Where a study
reports a composition or a correlation and no effect size, the code is `i?` rather than a number
invented to fill the slot.

## State as of 2026-09-03 (later) — two frontmatter bugs that masked each other are fixed

Running the ordinary ingest pipeline over a new source turned up a **duplicate-key defect on 86
claim pages**, and then a second bug that had been hiding it.

`sync_evidence_codes.SOURCES_BLOCK_RE` required a trailing newline on every line of the `sources:`
block. `okf_lib.FRONTMATTER_RE` captures frontmatter as `(.*?)\n---`, so the block's **last** line
arrives without one — and on a claim page `sources:` is normally the last key. The match therefore
stopped one line short, and `sub` replaced everything up to there while leaving that final line
standing: the rendered block, plus an orphaned copy of its own last key. `n: 157` twice. Valid YAML,
last-one-wins, `lint.py` reporting zero the whole time. **Visible only in a diff** — the same shape
as `strip_doi_from_line`, `apply_authorities` and `fix_title` before it, and the fourth time this
repo has shipped "a tool edited a line it had no business editing".

`okf_lib._derive_id_and_author` did `citation[:year].strip().rstrip(".")`. In APA the period before
`(2022)` usually belongs to the final initial, so **every author list ending in an initial was
recorded one character short** — `& Freeman, S` for `& Freeman, S.` It had been that way long enough
that nobody could see it, because the orphaned duplicate happened to carry the *correct* spelling
and won the last-key race. The corpus read correctly while both bugs were live.

**That is why they had to be fixed together.** Repairing only the regex removes the orphan and
promotes the truncated spelling — a silent rewrite of `author` on 70 pages, dressed as a cleanup.
Both fixed, 115 pages rewritten, and the result verified by parsing each page's frontmatter before
and after: 0 source entries added or dropped, 0 keys other than `author` changed, 0 lines touched
outside frontmatter. **Verify a repair pass this way rather than by reading the diff** — 115 files is
past the point where reading works, and "the parsed value is unchanged except where I intended it to
change" is checkable.

`scripts/log_source_review.py` also gained `--citations`. `okf_lib.append_manifest_entry` has
accepted it since Gate 3 landed, but the CLI never exposed it — so **every manually ingested source
wrote a bare `ingested`**, which this file is explicit must not be read as "the citations were
checked". The automated path calls the library directly and was never affected, which is exactly why
the gap survived unnoticed.

**The wiki now covers game mechanics as a design object.** `elements/learning-mechanic`,
`elements/assessment-mechanic`, `principles/learning-embedded-in-the-core-mechanic` and
`methods/evidence-centered-design`, from the G4LI white paper (Plass et al., 2011). No claim pages
were written from it: it is a conceptual argument that borrows its empirical support, and writing
claims from studies nobody here has read is the failure mode this file is largely about. ECD is
`status: draft` on purpose — it is described from the white paper's summary of Mislevy, Steinberg &
Almond (2003), not from the 60-page primary, and its page says so.

## Known open work

- **Sweep existing pages onto the current conventions and schemas.** Most of the ~3,900
  content pages predate some of: `INCLUSION.md`'s q1 coding for argument and opinion, `i: null`
  (not `i0`) for "no effect size reported", the evidence header line, per-citation `[±~][SMW]`
  markers, `observations/` records for the studies they cite, the processes/methods split, and
  `id:`/`aliases:`. Start from `priority_worklist.py` and `check_evidence_markers.py`, which
  already rank most of it. Batch by page type, one PR each, merged the same day. Verify each
  batch by parsing frontmatter before and after, not by reading the diff. Queued 2026-09-24,
  not started.

- **`scripts/resolve_citation_metadata.py` settles the three citation backlogs against
  Crossref.** Run it from a machine with network — the harness droplet, and as of 2026-09-03 this
  sandbox too (see the state note above; verify, do not assume):
  `--check` to report, `--apply` to write. It corrects a journal/volume/issue/page to the
  registry's values and strips a DOI whose registry title matches no citation of it. It
  never invents or searches for a replacement DOI, never touches anything when the lookup
  fails (an outage is not a verdict), and never fills a field Crossref left empty — absent
  means "the registry did not say", not "the wiki is wrong". The decision function
  `decide()` is pure and unit-tested offline, including the containment trap that put a
  Springer chapter's DOI on 69 pages.
- **64 of the 97 citation conflicts are one agreed DOI plus pages that omit it** — 211
  citations to fill in. `scripts/standardize_citations.py` writes the DOI onto the pages
  missing it, **but only where Crossref confirms it resolves to the paper being cited**.
  Never fill these in by consensus: the same shape covers `bandura-1977`, where exactly ONE
  of 68 citations asserts `10.1037/12256-000` and 67 assert nothing, so copying the majority
  would propagate a single unverified DOI onto 67 pages — which is how the 69-page Bandura
  error happened. The direction of the majority is the only thing separating that case from
  `collins-1989` (22 assert, 1 omits), and direction is not evidence.
- **A DOI asserted on only one page is invisible to the divergence checks.** Metadata,
  title and collision detection all need two *variants* of something to compare, so a lone
  wrong DOI disagrees with nothing and is flagged by nothing — the `bandura-1977` shape,
  where one page carries `10.1037/12256-000` and 67 carry none.
  `resolve_citation_metadata.py` therefore also pulls in every DOI named in a citation
  conflict, which covers 142 DOIs the three checks cannot reach.
- **A title mismatch does not say which side is wrong.** When the registry's title differs
  but journal, volume **and first page** all agree, the DOI is right and the *title* is the
  fabrication — `strategies/student-shadowing-...` cites Cook-Sather (2006) as "Sound,
  presence, and silence in education" at exactly the Curriculum Inquiry 36(4) 359 the
  registry gives for "Sound, Presence, and Power". Stripping there deletes a correct DOI
  and keeps the invented title. **Two of three is not enough** — the pair that satisfies it
  is almost always journal + volume, and two articles in one volume of one journal is the
  normal case, not evidence. At 2/3 the check proposed rewriting "Reading aloud improves
  memory" to "Why are background telephone conversations distracting?". The first page is
  what identifies an article within a volume. And a registry title that is merely a
  *prefix* of the page's is a truncated record, not a correction — Crossref gives Okonofua
  & Eberhardt (2015) as just "Two Strikes" while the page carries the full "Two strikes:
  Race and the disciplining of young students". The registry is not automatically the
  fuller source. `resolve_citation_metadata.py` fixes the title in that case
  and strips only when nothing corroborates the DOI.
- **Crossref returns HTML-escaped strings** — `Youth &amp; Society`. `doi_resolver` unescapes
  once at the boundary; writing the raw value puts the entity on the page.
- **A Crossref 404 is not proof a DOI is fabricated.** Crossref indexes only DOIs
  registered through Crossref, so a DataCite dataset, mEDRA or JaLC registration is
  legitimately absent. `resolve_citation_metadata.py` never strips on a 404; it reports
  them, ranked by whether the *prefix's* other DOIs resolve. A 404 on a prefix that
  otherwise resolves fine means that registrant IS in Crossref and the absence is about
  this DOI — that is the strong case. A 404 on a prefix with no resolving siblings is
  probably just coverage.
- **21 DOI collisions are open — one DOI asserted for two different papers.** Both
  directions are now detected: `check_citations.py` for one paper with two DOIs (97 open),
  and `check_citations.py --collisions` for one DOI on two papers (21 open). The second is
  the Bandura direction, and it is reported rather than auto-fixed on purpose — deciding
  which side of a pair is wrong needs Crossref, and picking blind is how the wrong one
  becomes canonical. Worst live case: `10.1177/001440290707300301` is on Konrad et al.
  (2007) self-determination *and* Bellini & Akullian (2007) video modelling, two unrelated
  papers. Resolve these from a machine that can reach Crossref — check whether this one does.
- **The 13 refilled strategy pages assert DOIs written before the Crossref gate existed.**
  `#19` states it corroborated DOIs against existing repo usage rather than against Crossref,
  because that worktree had no network. Re-run `scripts/check_citations.py` over
  `strategies/{classroom-design-for-engagement,contrasting-cases,formative-assessment-cycles,
  formative-feedback,multisensory-phonics-instruction,sketchnoting,teaching-as-learning}.md`
  and the six underscore-named siblings from a machine that can reach Crossref — check whether
  this one does before deferring it.
- **317 citations carry journal metadata that disagrees with their DOI.** The enrichment
  model copies a title and DOI reliably and then invents the journal, volume and pages
  around them — Graham & Perin (2007) accumulated seven different journals under one DOI.
  `check_citations.py --metadata` reports them; `fix_citation_metadata.py --apply` repairs
  only the ones the DOI itself settles (its suffix encodes volume/issue/page) and defers
  the rest. Do not "fix" the deferred ones by majority vote — where the DOI is opaque,
  picking the popular journal is the same guess as picking a DOI.
- **On 12 of those, the *majority* reading is the fabrication.** `10.17763/haer.81.4...`
  is cited 32 times as *Journal of Educational Research* 104(6) and never once as what its
  own DOI says — Harvard Educational Review 81(4), which is how the other five `haer` DOIs
  are cited. Never resolve a metadata conflict by making the stragglers match the majority
  without checking `leading_contradicted()` first; on these it converts the last correct
  citations into copies of the error. `check_citations.py --metadata` ranks them first as
  `contra`, and both the repair script and the enrichment gate refuse to act on them.
- **120 DOIs are cited with an invented title.** The same defect one layer deeper: the
  model reproduces the DOI and the title's stem, then makes up whatever follows the colon.
  `10.37016/mr-2020-56` carries ten different subtitles across 37 citations. Neither
  title-overlap clustering nor the metadata check can see it — a shared stem carries every
  variant past any similarity threshold. `check_citations.py --titles` reports them; a
  further 105 are mere truncations (one variant is a prefix of another), reported
  separately. **Never repaired automatically** — a subtitle is exactly the kind of
  plausible detail that is worth nothing unless it came from the registry, and the majority
  spelling is evidence, not proof. Resolve from a machine that can reach Crossref — check whether
  this one does before deferring it.
- **15 papers are cited with a *family* of near-identical DOIs** — same registrant,
  suffixes a few characters apart: 43 distinct DOIs over 90 citations, so at least 28 of
  them are wrong, since at most one spelling of a suffix can be the article. Worst is
  `okonofua-2016` with **nine** `10.1177/1745691615*` variants (alongside 27 pages citing
  `10.1073/pnas.1523698113`, a different registrant and almost certainly the real one);
  then `rosenshine-2012` with four `10.1080/00098655.2012.*`. `check_citations.py
  --variants` reports them. This is the fourth defect shape and the other three checks are
  structurally blind to it — `find_conflicts` says only "this paper carries N DOIs" and
  treats nine digit-permutations of one suffix exactly like two unrelated publishers.
- **A variant family is a signal, not a verdict — never strip on family membership alone.**
  `ehri-2001` carries `10.1598/rrq.36.3.2` and `10.1598/rrq.36.3.3`: one character apart
  and *both real*, consecutive articles in the same Reading Research Quarterly issue.
  Nothing in the shape of a suffix separates that from a fabricated neighbour.
- **The family does make one case actionable, and it is the case a bare 404 could not
  settle.** When Crossref resolves one member of a family to the paper being cited and has
  no record of another, the second is not "a registrar Crossref does not index" — its own
  sibling proves the article *is* in Crossref, under a different suffix.
  `resolve_citation_metadata.proven_fabrications()` (pure, tested offline) is the only
  place that upgrades a 404 to a removal, and it requires the near-identical sibling
  specifically: a preprint and its published version legitimately carry two DOIs from two
  registrants, one of which may sit outside Crossref, so "some other DOI for this paper
  resolves" is *not* sufficient. Run it wherever Crossref answers — the droplet, and as of
  2026-09-03 this sandbox as well.
- **Run `scripts/verify_citation_edits.py` after any citation tool writes, before you
  commit.** Every data-corruption bug this pipeline has had was the same shape — a script
  matching a *DOI* instead of a *citation*, and editing whatever line the DOI happened to
  appear on. It has now happened three times: `strip_doi_from_line` removed a correct DOI
  from a page that cited two works under one DOI; `apply_authorities` did the same
  file-wide; and `fix_title` overwrote a frontmatter YAML key with a paper's title
  (leaving a `sources` entry keyed `DeFT` and no `resource` field) and replaced a whole
  prose paragraph on `strategies/explicit_instruction-spelling.md` with a registry title,
  taking the sentence and the opening of a markdown link with it. **All three shipped, and
  `lint.py` reported zero on all three** — the results are valid YAML, valid markdown and
  plausible prose. The damage is only visible as "this edit landed somewhere an edit had
  no business landing", which is a property of the *diff*, so no page-level check can see
  it. `verify_citation_edits.py` reports every changed line that is not a citation line
  and exits 1. It is a guard for tool runs, not a lint check — editing prose by hand will
  and should trip it.
- **Never branch a droplet run off whatever branch happens to be checked out.** A run on
  `fix/fill-agreed-dois` was branched from `fix/crossref-citation-corrections` rather than
  `main`, so every script executed at its pre-#45 version: no case-insensitive DOI
  stripping, `have[0]` sampling instead of majority-title, and no `log_authority.py` at
  all. The results looked plausible and the PR diff looked clean, because the missing
  commits were already merged into `main` and so did not appear in a three-dot diff.
  `git checkout main && git pull` first, every time, and check `git merge-base` if a run's
  numbers look unexpectedly small.
- **`run_scrape_batch.py` is the one command for a whole batch — launchable from
  `/scrape.html`.** With `--model` it chains discover → prefetch → generate → ingest →
  rebuild indexes and banners → fill agreed DOIs → resolve against Crossref → apply
  human authorities → **verify** → lint → check_citations → health check. Started and
  left alone, it takes hours; progress and the live console render at `/scrape.html`.
  arXiv comes from the Kaggle snapshot (`export.arxiv.org` disallows automated access,
  so `--arxiv > 0` needs `KAGGLE_USERNAME`/`KAGGLE_KEY` or `--arxiv-snapshot`); **PMC
  and ERIC are live APIs** — NCBI E-utilities and the IES API — not Kaggle.
- **A failing `verify_citation_edits.py` marks the whole batch `error`, deliberately.**
  It is the only step in the chain that stops the run. Every corruption this pipeline
  has shipped passed `lint.py`, because the damage is a property of the diff rather than
  of any page, and an unattended batch is exactly where that gets committed and
  forgotten. The working tree is left untouched so the offending lines can be read.
  A lint failure, by contrast, is reported and not fatal — lint findings are the normal
  state of a fresh batch.
- **`ingest_extractions.py --model` takes the DIRECTORY name, not the slug.**
  `safe_model_dirname` maps `/` to `__`, so `z-ai/glm-5.3-flash` is
  `z-ai__glm-5.3-flash`. `run_scrape_batch.py` passed the raw slug, which made
  ingest look in `eval/runs/<label>/z-ai/glm-5.3-flash` — a path that never exists — so
  every dashboard scrape launched *with* a model completed discover, fetch and generate,
  paid for the generation, and then failed at ingest. Only a slug containing no `/`
  would have worked, and OpenRouter slugs all contain one.
- **`Deploy Docs` is serialized with a `concurrency` group, because it raced itself four
  times.** Two merges close together each start a deploy, each builds from its own commit,
  and both push to `gh-pages`; the loser is rejected with *"the remote contains work that
  you do not have locally"*. The site then stays on whichever build won, so a merged change
  is simply **absent from the published site while `main` says it shipped** — and the PR is
  green, because the failure is in the deploy run, not the PR's checks. Runs 37, 39, 45 and
  60 all died this way; #60 (the page-metadata panel) merged at 02:57:40, eighteen seconds
  after #59, and its deploy lost. `cancel-in-progress: false`: the newest run is built from
  the newest commit and supersedes the older one, so draining the queue in order publishes
  the same final tree without throwing away a build most of the way through mkdocs.
  **If something merged and the site does not show it, check the `Deploy Docs` run before
  suspecting the change.**
- **All twelve learner dimensions now resolve.** `spec/learners.md` requires every dimension
  slug to be a `learner-variables/` slug, and eleven of the twelve resolved to nothing — an
  agent writing for a course varying on `belonging` had this repo's own table and no
  interventions. The eleven are written, at `status: draft`, in the shape
  `prior-knowledge` established.
- **The granularity question in `findings/0007` is settled: twelve pages, one per
  dimension** — not the ~34 LVN factors with the twelve as a grouping layer. A dimension
  resolves to exactly one page, which is what `spec/learners.md`'s join rule already assumes
  (`belonging → learner-variables/belonging.md → ## Examples`), and no change is needed in
  the spec repo. The cost is real and worth knowing: `reading-and-language` bundles five LVN
  factors whose evidence bases differ, so its `## Claims` mixes them and a decision keyed on
  vocabulary alone cannot select just that. Splitting later is cheap now that `aliases:`
  exists — the factor name becomes an alias until it earns its own page.
- **Every link on those pages was verified to exist before it was written.** 99 candidate
  slugs checked against disk, 0 missing; all 49 claim citations carry a `[±~][SMW]` marker,
  so `check_evidence_markers.py` is unchanged at 244. **Their `## Key Sources` deliberately
  carry no new citations** — the evidence sits on the linked claim pages, which have been
  through the Crossref pipeline. Adding eleven pages' worth of fresh unverified references
  to a corpus this session spent days cleaning would have been the wrong trade, and this
  sandbox could not reach Crossref to check them at the time. It can now, so that trade is
  reversible: the eleven pages could take citations that verify.
- **Third-party Actions are pinned to commit SHAs, with the tag in a trailing comment.**
  A tag is mutable — whoever owns that repo can repoint `@v4` at anything — and `docs.yml`
  runs with `contents: write` on every push to `main`. When bumping one, resolve the new
  tag with `git ls-remote https://github.com/<owner>/<repo> refs/tags/<tag>` and paste the
  SHA it prints. Do not write a SHA from memory or from a changelog.
- **Gate 3 is built.** `sources/manifest.ndjson` entries now carry a `citations` object —
  `{checked, crossref_reachable, removed, flagged}` — so `ingested` no longer means only
  "structurally valid", which was the weakest of the three gates and the one least likely
  to catch what actually goes wrong. `crossref_reachable: false` is recorded separately
  from `flagged` on purpose: an outage is not a finding, and conflating them would both
  fill the manifest with noise during a blip and make a clean ingest during an outage
  indistinguishable from a dirty one.


