# Learning Design Wiki — Agent Operating Guide

This is a **persistent, LLM-maintained knowledge base** for learning design. The wiki compiles design principles, instructional patterns, elements, strategies, theories, learner variables, and empirical claims into a structured, cross-linked reference.

**You never write the wiki yourself.** The LLM reads sources, ingests new content, cross-links pages, and keeps schemas consistent. You source materials and ask questions.

The wiki is a bundle in the [Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md): every content page is markdown with YAML frontmatter carrying `type`, `title`, `description`, `status`, `generated`, and (where applicable) `sources`; cross-links are plain bundle-relative markdown links, not Obsidian wikilinks; `index.md` and `log.md` are OKF's reserved directory-listing and change-log filenames.

---

## Working alongside other sessions — read this before starting

This repo has one human maintainer and many Claude Code sessions — nine open at the time
of writing, each in its own worktree. A session that has been idle for a day still holds
its old plan and its old view of `main`, and resuming it will happily redo work that has
already landed. Sessions cannot message each other (an idle one is disconnected), so
**this file is the coordination channel** — it is loaded into every session's context
automatically. Anything a future session must not undo belongs here.

**Keep the number of live sessions small.** Most of the duplication below came from
parallel sessions, not from parallel people. One session per open task, closed when the
task merges.

**Branch from `main`, merge to `main` the same day, never stack.** A wiki-wide fix is a
wiki-wide diff: a typical task here changes 200+ files. Two branches living longer than a
day *will* collide on hundreds of them. This is not hypothetical — on 2026-08-31 three
branches were open at once, each changing ~200 of the same files, arranged in a stack
(`normalize-slugs` → `fix-no-h1-pages` → `research-scraper-test-setup`) whose base kept
moving. Two sessions independently fixed the same 13 corrupted pages, independently wrote
a link-repair tool, and independently shipped the *same* `[^)\s]+` parenthesis bug in it.
One merge cost 41 conflict resolutions. Do not open a PR whose base is another feature
branch.

**Before starting any wiki-wide pass, check whether it is already done.** Run
`python3 scripts/lint.py` and `python3 scripts/wiki_health_check.py --skip-doi` first, and
`git log --oneline -20 origin/main` to see what landed recently. A count of zero means the
work is done, not that the check is broken.

**Things that are settled — do not re-litigate or revert:**

- **Never assert a DOI that has not been resolved against Crossref.** A DOI that resolves
  to the *wrong* paper is worse than none, because it reads as verified. `10.1007/978-1-4684-7562-3_3`
  ("Model of Causality in Social Learning Theory") was auto-applied to 69 pages as Bandura
  (1977); it took a manual audit to catch. `cc.titles_align()` guards the containment case
  that let it through, and `enrich.verify_page_citations()` gates every newly written page.
- **`classify_doi`'s `error` status is not `wrong_paper`.** A failed lookup means Crossref
  was unreachable. Stripping on `error` deletes good DOIs from every page touched during an
  outage.
- **Unenriched claim pages are `status: draft`, and lint's DOI check skips drafts.** This is
  deliberate, and matches how `check_draft_no_description` and `check_stable_unverified`
  already work. Do not "fix" it by promoting those pages to `review`.
- **Links to filenames containing parentheses need the `<...>` form.** A bare destination
  closes at the first `)`. `scripts/fix_links.py --apply` repairs them; lint's
  `link_needs_angle_brackets` catches new ones.
- **`scripts/find_title_duplicates.py` reports ~943 near-duplicate title pairs.** That is a
  known backlog, mostly hyphen-vs-underscore variants of one page. It is reported, not
  lint-failing, on purpose.

**When you finish something wiki-wide, add a line here.** That is how the next session
finds out.

### State as of 2026-08-31 — the stack is collapsed

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

Only four branches still hold unmerged commits:

| Branch | Unmerged | Collision risk |
|---|---|---|
| `claude/standards-design-process-homes-q9qky1` | 4 commits, 54 files | **None** — works entirely in a new `goals/` folder, plus `log.md`, `sources/manifest.ndjson`, and one new script |
| `ci/detect-orphaned-pages-v2` | 1 commit, 2 files | Low — `docs.yml` + a new script |
| `ci/pr-preview-deploys` | contains the above | Low |
| `docs/material-theme-polish` | 1 commit, 6 files | **High and stale** — 3 days old, edits `build_indexes.py` and four `index.md` files that have since been regenerated many times. Re-derive the `mkdocs.yml`/`build_indexes.py` change on a fresh branch rather than merging this one |

### The health dashboard refreshes itself

`eval/runs/health.html` used to regenerate only on an enrichment batch, a scraper ingest,
the nightly timer, or a service restart — and a `git pull` is none of those. So the board
showed numbers from the last pipeline event while its own "last scanned" timestamp said a
minute ago, which makes a stale page look current. That cost a real debugging session.

`dashboard_server.py` now compares a cheap tree fingerprint (file count + newest mtime over
the content folders and `scripts/`, ~13ms) against the one stamped when the page was
written, and rescans (~6s) only when they differ. Pull, reload, correct numbers — no
restart. The fingerprint is deliberately **not** a git revision: the droplet's working tree
routinely holds real uncommitted work, and keying on HEAD would call all of it invisible.

### Known open work

- **`scripts/resolve_citation_metadata.py` settles the three citation backlogs against
  Crossref.** Run it from a machine with network (the harness droplet):
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
  papers. Resolve these from a machine that can reach Crossref.
- **The 13 refilled strategy pages assert DOIs written before the Crossref gate existed.**
  `#19` states it corroborated DOIs against existing repo usage rather than against Crossref,
  because that worktree had no network. Re-run `scripts/check_citations.py` over
  `strategies/{classroom-design-for-engagement,contrasting-cases,formative-assessment-cycles,
  formative-feedback,multisensory-phonics-instruction,sketchnoting,teaching-as-learning}.md`
  and the six underscore-named siblings from a machine that can reach Crossref.
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
  spelling is evidence, not proof. Resolve from a machine that can reach Crossref.
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
  resolves" is *not* sufficient. Run it from the droplet; this sandbox cannot reach
  Crossref.
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

---

## Page identity — `id:` and `aliases:`

The [learning-design-spec](https://github.com/Learning-Design-Alliance/learning-design-spec)
pipeline resolves design documents against this wiki: a pattern plan names
`element: <slug>`, a principle names `Realizes: <principle-slug>`, a design section cites
`research:<claim-slug>`, and `spec/learners.md` requires every learner dimension to be a
`learner-variables/` slug. Its contract (that repo's `findings/0008`) opens with **every
page's id is stable and unique within its kind** — because a rename breaks a course that
has already shipped, silently, outside this repo.

So the six kinds a design document can point at carry `id:` equal to their filename:
**elements, principles, patterns, claims, learner-variables, strategies**. Theories stay
out — nothing in the spec addresses one. A page type gains an id when something *outside*
the wiki depends on pointing at it.

**Strategies were nearly left out, and that would have been wrong.** `findings/0008`'s
contract names only claim, pattern, element and principle slugs, and the reverse index
reaches strategies without anyone naming them — so the first cut excluded all 2,557.
`spec/patterns.md` then makes a phase name one outright:

```yaml
phases:
  - phase: Read the case
    element: case-based-learning
    strategy: chunked-reading-with-embedded-questions   # a learning-wiki strategy slug
```

whose `### Instructions` become that phase's authored brief. So a strategy rename breaks a
shipped course exactly the way an element rename does.

- `python3 scripts/page_identity.py --check` — report; `--apply` — stamp missing ids
- `python3 scripts/lint.py --type identity` — id present, equal to the slug, and unique
  across ids **and** aliases within a kind

**The claims `id:` was repurposed, deliberately.** CLAUDE.md used to document it as a short
programmatic code (`we-4`, `fi-2`). Measured before the change: present on all 422 pages and
useless as identity — 56 blank, only 183 of the 366 non-empty equal to the slug, and six
values shared by two pages each. `enrich.py` stamped an empty `id: ` into every new claim,
which is where the blanks came from. The short code was referenced nowhere in the wiki's
12,893 citations while the design spec addresses claims by slug throughout, so it was
vestigial.

**`aliases:` is what makes a rename non-breaking, and it is never stamped empty.** It
appears when a page is actually renamed: `update_links_for_renames.py` sets `id:` to the new
slug and records the old one in `aliases:`, so a course document written against the old
name still resolves. Empty fields on a thousand pages train a reader to skip the block.

Ids and aliases share one namespace per kind. A document saying `element: foo` cannot tell
whether `foo` is a current slug or a retired one, so two pages answering to it is ambiguous
however that came about — which is the case lint catches that filename-uniqueness never
could, filenames being unique by construction.

Both YAML spellings are read (`aliases: [a, b]` and the block form), because both are
written here — `page_identity.py` edits raw frontmatter text inline, while
`ingest_extractions.py` builds pages through `okf_lib.dump_frontmatter`, which emits a
block. A reader understanding only one would see no aliases on half the pages that have
them: the rename would look recorded and still not resolve.

**The spec reads exactly two things from wiki frontmatter: `id` and `type:`.** Everything
else it resolves is a *body section* — `### Instructions` for a phase's brief,
`### Target Learners` and `### Target Learning Goals` for matching personas and goals,
`#### Requirements`/`#### Constraints` as the applicability filter, `## Claims` with their
inline markers, `## Examples` on a learner-variable. Those are at 100% and ~99.8% already,
and `findings/0008` is explicit that they must stay prose: structuring them into YAML would
lose the qualifications that make them useful. So there is no further frontmatter work for
the pattern-building process — a `pattern` doc's `pedagogy:` block and a `pack`'s
`elements:` live in those documents, not here.

**Note:** `verify_citation_edits.py` will trip on an id/alias pass — those are frontmatter
edits, not citation edits, and it is a guard for citation tool runs only.

---

## Three core operations

### 1. Ingest
Process a new source (paper, book chapter, CSV batch, worked example) into wiki pages.

Steps:
1. Identify the page type(s) the source contributes to (principle, element, pattern, strategy, theory, learner-variable, claim). `learner-variable` is schema-ready but not yet part of the automated single-pass extraction prompt (deliberately deferred to a dedicated future sweep, so the extraction agent isn't juggling a fourth job on top of claims/omission/fabrication) — for now, factor a learner-variable page out by hand when a claim reports a finding about a learner characteristic (e.g. "X predicts/moderates Y outcome"), rather than leaving it as a bare, unlinked claim.
2. Check if a page already exists (`index.md` or `grep` by name)
3. If new: create a page in the correct folder using the template below
4. If existing: merge new content into the right sections; append to `## Key Sources` (or `## Evidence` for claims); log the change
5. Cross-link: add markdown links like `[Example Page](../principles/example-page.md)` to related pages already in the wiki
6. Update `index.md` — run `python3 scripts/build_indexes.py` to regenerate it and every per-folder index from disk state
7. Append an entry to `log.md` under today's `## YYYY-MM-DD` heading: `* **Ingest**: [page](folder/page.md) — [source]` (or run `python3 scripts/log_revision.py <page> --by <actor> --type ingest --desc "..."`, which updates the page's `generated` field, its revision card, and `log.md` in one step)

### 2. Query
Answer a question by reading the wiki.

Steps:
1. Search `index.md` for relevant pages
2. Read those pages; follow the markdown links (`slug.md` / `../folder/slug.md`) as needed
3. Synthesize across pages; cite page names and claim IDs
4. Flag gaps: if the answer requires a page that doesn't exist, note it

### 3. Lint
Health-check the wiki: `python3 scripts/lint.py [--fix]`.

Checks:
- Broken cross-links (`slug.md` / `../folder/slug.md` link target not found)
- Pages with `status: draft` and no description
- Claim pages missing an evidence strength rating
- Principles missing at least one claim link
- Claim evidence entries missing a DOI or URL

---

## Evidence tags

Used inline in principle, pattern, element, and strategy pages when citing claims. The tag describes the **direction of the claim's effect on the page's topic**, not just evidence strength.

| Tag | Meaning |
|-----|---------|
| **[+S]** | Supports — strong (consistent experimental/meta-analytic) |
| **[+M]** | Supports — moderate |
| **[+W]** | Supports — weak / emerging |
| **[~S]**, **[~M]**, **[~W]** | Contextual / mixed — effect depends on conditions (e.g. expertise reversal: works for novices, not experts) |
| **[-S]**, **[-M]**, **[-W]** | Contradicts or reduces effectiveness — strength varies |
| **[X]** | Contradicted / discredited |

**Rule:** Claims cited in a Constraints section should use `[-]` (negative effect) or `[~]` (contextual/mixed), never `[+]`. A constraint describes a condition where the approach fails or causes harm — the tag should reflect that direction, even if the underlying claim is phrased positively (e.g., "practice improves transfer" cited as evidence that *lack of practice* hurts outcomes → `[-S]`).

Always link the tag to a claim page: `[Claim statement](../claims/example-claim.md) [+M]`

---

## Relation symbols (cross-link annotations)

- `+` supports / reinforces
- `~` contextual / mixed / depends on conditions
- `–` contradicts / undermines

---

## Status values

| Status | Meaning |
|--------|---------|
| `draft` | Skeleton or stub; content not reviewed |
| `review` | Content present; needs expert review |
| `stable` | Reviewed and considered reliable |
| `deprecated` | Superseded or discredited; kept for history |

---

## Frontmatter fields

Every content page (principle, element, pattern, strategy, theory, learner-variable, claim) carries this OKF-conformant frontmatter:

| Field | Required | Meaning |
|-------|----------|---------|
| `type` | Yes | `principle` \| `element` \| `pattern` \| `strategy` \| `theory` \| `learner-variable` \| `claim` |
| `title` | Recommended | Display name — normally matches the page's `# H1` |
| `description` | Recommended | One-sentence summary, used in index listings |
| `status` | Recommended | See Status values above |
| `generated` | Recommended | `{ by: <actor>, at: <date> }` — who/what last wrote the page and when, replacing the old `last_edited`/`edited_by` pair |
| `sources` | When applicable | List of `{ id, resource, title, author }` entries parsed from `## Key Sources` (or `## Evidence` for claims) — a structured mirror of the citations already in the body, not a replacement for them |
| `verified` | Optional | List of `{ by: <actor>, at: <date> }` confirmation events — see Trust tiers below. Absent on every page until someone explicitly reviews it; never set this yourself just because a page looks complete |
| `id` | On identified kinds | Equal to the filename slug, on elements/principles/patterns/claims/learner-variables — the stable name design documents resolve by (see Page identity below) |
| `aliases` | After a rename | Every former slug of this page, retained forever, so a document naming the old one still resolves |
| `evidence_strength`, `author`, `grain_size` | Type-specific | Extra scalar fields kept as-is per page type (see templates below); OKF tolerates extra frontmatter keys |

**Actor convention** for `generated.by` (and any other identity field): `<tool>/unspecified` for an agent/tool (e.g. `claude/unspecified`, `codex/unspecified`), `human:<id>` for a person, `process:<id>` for an unattended batch job (e.g. `process:wiki-ingest`). Never invent a specific model version you're not certain of — `unspecified` is fine.

---

## Trust tiers (`verified`)

`verified` is a **different axis from `evidence_strength`**, and the two should never be conflated:

- `evidence_strength` (and the per-study `q`/`i` codes in a claim's `## Evidence` section) describe how strong the *underlying research* is — is this a meta-analysis or a single case study.
- `verified` describes whether a **human has actually checked that this wiki page** faithfully represents that research — a claim can have `evidence_strength: strong` and still be completely unverified, because the LLM that wrote the page could have paraphrased a finding wrong, mistagged an effect's direction, or introduced a citation error that nothing has caught yet.

OKF derives three trust tiers from the `verified` field:

| Tier | Condition |
|------|-----------|
| **unverified** | No `verified` key present (the default for every freshly ingested or LLM-edited page) |
| **machine-confirmed** | `verified` present, but only by non-`human:` actors (e.g. a lint pass) |
| **human-reviewed** | `verified` present with at least one `human:<id>` actor |

Format (a list, so repeated reviews over time each add an entry — OKF also tolerates a bare single mapping):

```yaml
verified:
  - by: human:david
    at: 2026-08-22
```

Add a `verified` entry when a human substantively reviews a page's content for accuracy — not on every procedural PR approval. The easiest way is:

```bash
python3 scripts/log_revision.py <page> --by human:<id> --type status --desc "Reviewed for accuracy" --verify
```

which appends the `verified` entry alongside its normal `generated`/log-update work. Never add a `verified` entry yourself (as an agent) just because a page looks complete or well-sourced — that defeats the point of the tier. `python3 scripts/lint.py` flags any `status: stable` page that has no `verified` entry, since "stable" should mean someone actually checked it, not just that it looks finished.

---

## Page-type banner

Every content page carries a one-line banner directly under its `# H1`, naming
the page's type and linking back to its section index:

```markdown
# Cooperative Learning

> **Principle** · [All principles](index.md)
```

This exists because 73 slugs live in more than one type folder — `cooperative-learning`
and `direct-instruction` each exist in **all four** of principles/elements/patterns/strategies,
with near-identical titles. Frontmatter carries `type`, but mkdocs strips frontmatter out
of the rendered page entirely, so on the docs site, in GitHub's file view, in the dashboard's
edit box, and in whatever an agent reads during an ingest, the folder in the URL was the only
thing distinguishing them. A blockquote renders as a visible callout in both GitHub and
mkdocs-material.

The banner's label follows the **folder the page is in**, which is what actually determines
its section — so where frontmatter `type` and the folder disagree, that's a real data bug
(the page is either misfiled or mislabelled) and a human decides which. `lint.py`'s
`check_type_banner` verifies all three agree — banner present, label matches folder, and
frontmatter `type` matches folder — on every health run.

Run `python3 scripts/add_type_banner.py --apply` after any batch that creates pages; it's
idempotent (updates an existing banner in place rather than stacking a second one), so it's
safe to re-run at any time. `--check` reports without writing.

Yes, this duplicates `type:` from frontmatter into the body — the same tradeoff this schema
already accepts for `sources:` mirroring the citations in `## Key Sources`: a structured field
and a human-readable rendering of the same fact, kept in sync by a lint check rather than by
dropping one.

---

## Renaming a page

Renaming a page is two jobs, and `git mv` only does the first. Nothing else in
the wiki updates the pages that link to the one you moved, so a rename lands as
a set of silently broken cross-links.

The dangerous version is a rename that is correct in its own tree and breaks
links only when merged forward, because the branch was cut before the linking
pages existed. That has already happened once here: merging the scraper branch
orphaned 17 links to `a_finder's_guide_to_facts.md`, renamed there to
`a_finders_guide_to_facts.md`.

After renaming, always run:

```bash
python3 scripts/update_links_for_renames.py --from-git --dry-run
python3 scripts/update_links_for_renames.py --from-git --apply
```

It reads the renames staged in git (so `git mv` first, or `git add` the rename),
and re-points every inbound link — same-folder, `../folder/`, bundle-absolute,
and the percent-encoded spellings models emit for slugs containing `'`, `"`, `?`,
`,`, `(`, `)`, `&`, `+`. Every rewrite is checked to resolve on disk before it is
kept, so the pass cannot turn a working link into a broken one. Pass `--map
<file>` instead of `--from-git` to drive it from an explicit `old<TAB>new` list.

Then confirm with `python3 scripts/lint.py --type broken_links` and regenerate
indexes with `python3 scripts/build_indexes.py`.

---

## Cross-link conventions

- Cross-links are standard markdown links, relative to the linking page: `slug.md` for another page in the same folder, `../folder/slug.md` for a page in a different folder (every content folder sits exactly one level under the wiki root, so `../folder/` always resolves correctly regardless of which folder you're linking from)
- OKF also permits absolute bundle-relative paths (`/folder/slug.md`) — this wiki uses the relative form instead because it works with plain `mkdocs` (the docs site's builder) with no extra plugin, whereas an absolute path renders as a literal domain-root URL once the site is hosted under a subpath
- Slugs are lowercase, hyphen-separated: `worked-examples`, `cognitive-load-theory`
- Always include the folder in a cross-folder link so the target is unambiguous: `[Worked examples reduce novice search](../claims/worked-examples-reduce-novice-search.md)`
- Claims use semantic slugs: `../claims/worked-examples-reduce-novice-load.md`, and `id:` in frontmatter equals that slug (see Page identity)
- A link to a page that doesn't exist yet is tolerated (OKF requires consumers to tolerate broken links) — write the link anyway rather than leaving a bare TODO if you know the target slug, but don't invent slugs you haven't verified exist or are about to create

---

## Folder map

```
ld-wiki/
  CLAUDE.md          ← this file (schema + operating guide)
  index.md           ← OKF bundle-root index; carries okf_version in frontmatter
  log.md             ← reserved OKF filename: append-only, date-grouped change log
  principles/        ← design principles (what to do and why)
  elements/          ← instructional components (building blocks)
  patterns/          ← instructional patterns (reusable designs at lesson/unit level)
  strategies/        ← teaching strategies (concrete activity recipes)
  theories/          ← learning theories (explanatory frameworks)
  learner-variables/ ← canonical learner characteristics (prior knowledge, self-efficacy, ...) claims link into
  claims/            ← empirical claims with evidence
  sources/           ← bibliographic source pages (optional; most citations live inline in Key Sources / Evidence)
    manifest.ndjson    ← append-only log of every source reviewed, ingested or rejected (see Source Manifest below)
    authorities.ndjson ← append-only log of citations a HUMAN verified against the real source (see Citation Authorities below)
  scripts/
    okf_lib.py         ← shared OKF helpers (frontmatter parse/dump, link conversion, actor formatting)
    ingest.py          ← CSV → wiki pages batch ingest
    enrich.py          ← LLM-based stub enrichment (Claude/Gemini)
    build_indexes.py   ← regenerates index.md and every per-folder index from disk state
    log_revision.py    ← records a revision card + updates a page's `generated` field + appends to log.md
    log_source_review.py ← appends one entry to sources/manifest.ndjson (see Source Manifest below)
    add_type_banner.py ← inserts/refreshes the page-type banner under each page's H1 (see below)
    update_links_for_renames.py ← after pages are renamed, re-points every inbound cross-link (see below)
    page_identity.py   ← stable `id:`/`aliases:` for the kinds design docs point at (see below)
    lint.py            ← health-check (see Lint above)
    verify_citation_edits.py ← after a citation tool writes: did it edit only citations? (see above)
```

Each folder's `index.md` is itself a reserved OKF filename: no frontmatter (except the bundle-root's `okf_version`), and a plain `* [Title](slug.md) - description` bullet listing grouped by status. Regenerate these with `python3 scripts/build_indexes.py` rather than hand-editing them.

---

## Source Manifest

`sources/manifest.ndjson` is an append-only record of every source article the ingest pipeline has *reviewed* — whether it contributed pages or was rejected as out of scope. It exists so anyone (including people outside this project) can check whether a specific article has already been covered, or audit the whole scan, at a scale (eventually tens of thousands of articles) where a rendered list or one page per source stops being practical. It is not meant to be human-browsed — it's a data file, not a wiki page.

**Format:** one JSON object per line (NDJSON), never rewritten or reordered — only appended to.

```json
{"id": "eric-ed265520", "title": "The Effects of High and Low Relevant Text Underlining on Test Performance.", "doi": null, "reviewed_at": "2026-08-27", "status": "ingested", "pages": ["elements/text-underlining-and-annotating.md", "theories/von-restorff-effect-text-marking.md"]}
{"id": "eric-ed616622", "title": "A Bibliography of Cognitive Information Processing Theory, Research, and Practice", "doi": null, "reviewed_at": "2026-08-27", "status": "rejected", "reason": "matched the search topic on keyword overlap only, but the source is a career/vocational-counseling bibliography, not a learning-science theory; out of scope for this wiki"}
```

Fields: `id` (source identifier — the ERIC/PMC/arXiv id from the automated pipeline, or `doi:<doi>` / a URL for manually-ingested articles), `title`, `doi` (nullable), `reviewed_at` (ISO date), `status` (`"ingested"` or `"rejected"`), and either `pages` (bundle-relative paths the source contributed to, for `"ingested"`) or `reason` (why it didn't contribute, for `"rejected"`).

`"ingested"` entries also carry `citations`: `{checked, crossref_reachable, removed, flagged}` — what the citation gate found on the pages that source wrote. `removed` lists DOIs stripped because they resolved to the wrong paper; `flagged` lists findings left for a human (a DOI on two papers, invented journal metadata, an invented title). `crossref_reachable: false` means the network check could not run, so that line is an *unverified* ingest rather than a clean one — never read a bare `"ingested"` as "citations were checked".

**Always append via the helper, never hand-edit the file:**

```bash
python3 scripts/log_source_review.py --id "doi:10.1234/example" --title "Article Title" \
  --status ingested --pages claims/foo.md elements/bar.md

python3 scripts/log_source_review.py --id "doi:10.1234/other" --title "Other Article" \
  --status rejected --reason "not learning-science, out of scope"
```

(`scripts/ingest_extractions.py`, the automated eval-pipeline ingest path, calls `okf_lib.append_manifest_entry()` directly instead of shelling out to this script — same effect.)

**Looking something up** (no need for a script — it's just NDJSON):

```bash
grep '"id": "eric-ed265520"' sources/manifest.ndjson
grep -i '"title":.*underlining' sources/manifest.ndjson
python3 -c "import json,sys; [print(l) for l in map(json.loads, open('sources/manifest.ndjson')) if l['status']=='rejected']"
```

Known gap: the CSV batch-import path (`scripts/ingest.py`, reading external `~/research_briefs/*.csv` files) doesn't write to the manifest — those rows have no natural per-article identity to key an entry on.

---

## Citation Authorities — the human's side of the record

`sources/authorities.ndjson` is where a **person** records what they checked against
the real source: the publisher's page, the book in hand, the article's own PDF. It is
append-only NDJSON like `manifest.ndjson`, keyed by the same author-year key
`check_citations.py` uses.

It exists because every automated check in this repo verifies against Crossref, and
Crossref can only see what it indexes. **2,493 of the wiki's 12,893 citations — 1,232
distinct author-year keys — carry no DOI and no journal metadata at all.** They are
books, and all five checks are structurally blind to them: every one needs two variants
of something to compare, and a book citation offers nothing to compare. Nothing has ever
verified that Ambrose et al. (2010) is *How Learning Works*, Jossey-Bass,
ISBN 978-0-470-61760-1. No lookup would say so. A person can.

```bash
python3 scripts/log_authority.py --key ambrose-2010 --by human:david \
  --title "How Learning Works: Seven Research-Based Principles for Smart Teaching" \
  --publisher "Jossey-Bass" --isbn 978-0-470-61760-1 --url https://www.wiley.com/... \
  --note "Verified against the Wiley product page."

python3 scripts/apply_authorities.py --check     # then --apply
python3 scripts/citation_worklist.py             # what to look at next, ranked
```

Four things about it that are deliberate:

- **An agent must never author one.** `append_authority()` refuses any `verified.by` that
  is not `human:<id>`, for the same reason CLAUDE.md forbids an agent adding a page's
  `verified:` entry because the page looks complete. A machine-written "authority" is
  just another unverified assertion wearing a badge that says otherwise.
- **`"doi": null` is a verdict; an absent `doi` field is not.** The first says a human
  established that no DOI is registered, which makes any DOI a later batch invents for
  that key provably wrong and strippable without a lookup. The second says only "not
  established", and nothing may act on it. Same discipline as `crossref_reachable: false`
  vs `flagged`, and as `error` vs `wrong_paper`.
- **It ratchets.** `lint.py`'s `check_authority_conflicts` fails on any citation that
  contradicts a recorded verdict, so a settled decision survives the next enrichment
  batch. Repairing the pages alone does not: the model that invented a DOI for a book
  once will invent one again, and nothing in the corpus remembers otherwise.
- **Only the no-DOI verdict is auto-repaired.** `apply_authorities.py` reports a wrong
  ISBN, a differing DOI or a mismatched title rather than rewriting it — the page may be
  citing a different edition, a chapter rather than the book, or a reprint, and only the
  person who checked can say which. The tooling has been confidently wrong about exactly
  this kind of "obvious" correction before (the Cook-Sather title case above).

`scripts/citation_worklist.py` is the reading end. It collapses all five checks onto the
author-year key — so several report lines about one source appear once — ranks by how
many citations ride on it, ranks the book backlog separately (different work: a person
and a publisher page, not a lookup), and drops keys already settled, so the list shrinks
as you work.

---

## Page templates

### Principle

```markdown
---
type: principle
id: [principle-slug]      # equal to the filename
title: [Principle Name]
description: [One-sentence summary of the recommendation]
status: draft
generated:
  by: <actor>
  at: YYYY-MM-DD
---

# [Principle Name]

> **Principle** · [All principles](index.md)

## Description
[What this principle is and what it recommends.]

## Implications

### Context
#### Requirements
- 
#### Constraints
- 

### Target Learners
- 

### Target Learning Objectives
- 

### Theory
#### Supporting
- 
#### Contradicting / Qualifying
- 

### Claims
<!-- Link claims with evidence tags: [Claim statement](../claims/claim-slug.md) [+M] -->
- 

## Related Principles
- 

## Examples
<!-- Links to elements or patterns that apply this principle -->
- 

## Key Sources
- 
```

---

### Element

```markdown
---
type: element
id: [element-slug]      # equal to the filename
title: [Element Name]
description: [One-sentence summary of what this element is]
status: draft
generated:
  by: <actor>
  at: YYYY-MM-DD
---

# [Element Name]

> **Element** · [All elements](index.md)

## Description
[What this instructional element is; how it functions.]

## Design Implications

### Context
#### Requirements
- 
#### Constraints
- 

### Target Learners
<!-- Link to sub-claims: [Claim statement](../claims/claim-slug.md) -->
- 

### Target Learning Goals
<!-- Link to sub-claims: [Claim statement](../claims/claim-slug.md) -->
- 

### Affordances
<!-- Link to principles applied: [Principle Name](../principles/principle-slug.md) -->
- 

## Related Elements
- 

## Examples
<!-- Links to strategies that use this element, with ratings -->
- 

## Key Sources
- 
```

---

### Pattern

```markdown
---
type: pattern
id: [pattern-slug]      # equal to the filename
title: [Pattern Name]
description: [One-sentence summary of what this pattern is]
status: draft
generated:
  by: <actor>
  at: YYYY-MM-DD
author: 
grain_size: 
---

# [Pattern Name]

> **Pattern** · [All patterns](index.md)

## Description
[What this pattern is; how it works; what problem it solves.]

## Implications

### Context
#### Requirements
- 
#### Constraints
- 
#### Grain Size
[program / course / unit / lesson]

### Target Goals
<!-- Link to claims: [Claim statement](../claims/claim-slug.md) -->
- 

### Target Learners
<!-- Link to claims: [Claim statement](../claims/claim-slug.md) -->
- 

### Theory
#### Supporting
- 
#### Contradicting / Qualifying
- 

### Claims
<!-- Link claims with evidence tags -->
#### Supporting
- 
#### Contradicting
- 

## Design

### Sequence
<!-- Steps with links to elements: [Element Name](../elements/element-slug.md) -->
1. 

### Affordances
<!-- Links to principles applied: [Principle Name](../principles/principle-slug.md) -->
- 

### Personalization
<!-- How to adapt for non-target learners -->
- 

## Related Patterns
- 

## Examples
<!-- Links to products / lessons / courses with ratings -->
- 

## Key Sources
- 
```

---

### Strategy

```markdown
---
type: strategy
id: [strategy-slug]      # equal to the filename
title: [Strategy Name]
description: [One-sentence summary of what this strategy is]
status: draft
generated:
  by: <actor>
  at: YYYY-MM-DD
---

# [Strategy Name]

> **Strategy** · [All strategies](index.md)

## Description
[What this strategy is and how it is carried out.]

## Design Implications

### Context
#### Requirements
- 
#### Constraints
- 
#### Implementation Variability
- 

### Target Learners
<!-- Link to sub-claims: [Claim statement](../claims/claim-slug.md) -->
- 

### Target Learning Goals
<!-- Link to sub-claims: [Claim statement](../claims/claim-slug.md) -->
- 

### Instructions
<!-- Steps with links to elements: [Element Name](../elements/element-slug.md) -->
1. 

## Related Strategies
- 

## Examples
<!-- Links to products with ratings -->
- 

## Key Sources
- 
```

---

### Theory

```markdown
---
type: theory
title: [Theory Name]
description: [One-sentence summary of what this theory proposes]
status: draft
generated:
  by: <actor>
  at: YYYY-MM-DD
---

# [Theory Name]

> **Theory** · [All theories](index.md)

## Description
[What this theory proposes; its core mechanism or claim.]

## Implications

### Context
- 

### Target Learners
- 

### Target Learning Objectives
- 

## Claims
<!-- Claims that derive from or test this theory: [Claim statement](../claims/claim-slug.md) [+M] -->
- 

## Related Theories
- 

## Examples
<!-- Links to patterns and principles that apply this theory -->
- 

## Key Sources
- 
```

---

### Learner Variable

A canonical page per distinct learner characteristic/variable (prior knowledge, self-efficacy,
working memory capacity, spatial ability, ...). Claims that report a finding about the variable
link *into* it, the same way claims link into theories — this keeps "prior knowledge," "prior
domain knowledge," and "background knowledge" from three different articles as one page instead
of three fragmented, undiscoverable mentions. Schema-ready but not yet part of the automated
single-pass extraction prompt — see the Ingest section above for why, and factor these out by
hand for now when a claim clearly reports a learner-characteristic finding.

```markdown
---
type: learner-variable
id: [variable-slug]   # equal to the filename
title: [Variable Name]
description: [One-sentence definition of this learner characteristic]
status: draft
generated:
  by: <actor>
  at: YYYY-MM-DD
---

# [Variable Name]

> **Learner Variable** · [All learner variables](index.md)

## Description
[What this learner variable is; how it's typically measured or operationalized.]

## Implications

### Context
- 

### Target Learners
- 

### Target Learning Objectives
<!-- Learning outcomes this variable has been shown to affect -->
- 

## Claims
<!-- Claims reporting findings about this variable, with evidence tags: [Claim statement](../claims/claim-slug.md) [+M] -->
- 

## Related Learner Variables
- 

## Examples
<!-- Links to principles/elements/patterns/strategies that account for this variable -->
- 

## Key Sources
- 
```

---

### Claim

```markdown
---
type: claim
title: [Claim statement — one sentence, present tense]
id: [claim-slug]     # equal to the filename — what a design doc cites
status: draft
generated:
  by: <actor>
  at: YYYY-MM-DD
evidence_strength:   # strong / moderate / weak / mixed
---

# [Claim statement — one sentence, present tense]

> **Claim** · [All claims](index.md)

[Optional 1–2 sentence clarification of scope or mechanism.]

## Subclaims
<!-- Each subclaim is a 1-sentence lit-review summary.
     Prefix with quality and impact scores drawn from the supporting evidence.
     Link to the evidence anchor using standard markdown: [→ Author Year](#author-year) -->

`q? i?` [One-sentence summary of the finding and scope.] [→ Author Year](#author-year)

## Evidence
<!-- One entry per study. Heading slug becomes the anchor target for subclaim links,
     and (via scripts/migrate_to_okf.py's parser) the `id` of the matching entry in
     the frontmatter `sources:` list.
     Show full APA citation with DOI as a hyperlink.
     Then: quality · impact · n codes with plain-language explanations.
     Then: 2–4 sentence plain-language description. Link instructional elements to wiki pages.
     Avoid unexplained abbreviations or jargon. -->

### Author Year

Author, A., & Author, B. (Year). Title. *Journal, vol*(issue), pages. [doi:...](https://doi.org/...)

`q? · [e.g. peer-reviewed RCT / quasi-experiment / meta-analysis]` · `i? · [e.g. large effect, d=0.9]` · `n=?`

[2–4 sentences: study design, participants (who, how many, what context), conditions or intervention, and findings in plain language. Link any instructional elements used to their wiki pages, for example `[worked examples](../elements/demonstration.md)` and `[practice tasks](../elements/practice.md)`.]

## Discussion
<!-- Prose section covering: contradictions, moderators, boundary conditions, open questions.
     Link to related claim pages where relevant. -->

## Related Claims
- 
```

**Evidence quality tiers (q):**
| q | Criteria |
|---|----------|
| 4 | Pre-registered RCT or well-powered meta-analysis |
| 3 | Peer-reviewed experiment (not pre-registered) or systematic review |
| 2 | Quasi-experiment, observational with controls, or narrative review |
| 1 | Case study, expert opinion, or theoretical argument |

**Impact magnitude (i):**
| i | Rough effect size |
|---|-------------------|
| 3 | Large (d ≥ 0.8 or equivalent) |
| 2 | Medium (d 0.4–0.79) |
| 1 | Small (d 0.2–0.39) |
| 0 | Negligible / unclear |

---

## Ingest notes for agents

- When a CSV field lists multiple items separated by commas or semicolons, expand each into a list item
- When a field references another page by name (e.g., "Cognitive Load Theory"), convert it to a markdown link using the slugified name: `[Cognitive Load Theory](../theories/cognitive-load-theory.md)`
- When research support / impact fields contain citations, extract them into `## Key Sources` (and, once parsed, the frontmatter `sources:` list) and create or link `sources/` pages
- Mark pages `status: draft` on initial ingest; a human or a lint pass can promote to `review` or `stable`
- Never delete content on update — move superseded content to a `<!-- deprecated -->` comment block
- Never write a raw, un-slugified name straight into a file path — a name containing `/` (e.g. "Stand Up / Sit Down") will be interpreted as a subdirectory separator. Always pass names through `slugify()` before joining them into a path.
