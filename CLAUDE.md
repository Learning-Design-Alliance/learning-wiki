# Learning Design Wiki — Agent Operating Guide

This is a **persistent, LLM-maintained knowledge base** for learning design. The wiki compiles design principles, instructional patterns, elements, strategies, theories, learner variables, and empirical claims into a structured, cross-linked reference.

**You never write the wiki yourself.** The LLM reads sources, ingests new content, cross-links pages, and keeps schemas consistent. You source materials and ask questions.

The wiki is a bundle in the [Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md): every content page is markdown with YAML frontmatter carrying `type`, `title`, `description`, `status`, `generated`, and (where applicable) `sources`; cross-links are plain bundle-relative markdown links, not Obsidian wikilinks; `index.md` and `log.md` are OKF's reserved directory-listing and change-log filenames.

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
| `id`, `evidence_strength`, `author`, `grain_size` | Type-specific | Extra scalar fields kept as-is per page type (see templates below); OKF tolerates extra frontmatter keys |

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
a set of silently broken cross-links — and because a rename is often done on a
branch cut some time ago, they only break once the rename is merged forward into
a tree that has since grown pages linking to the old name.

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
- Claims use semantic slugs: `../claims/worked-examples-reduce-novice-load.md`; the short `id:` in frontmatter is for programmatic reference only
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
  scripts/
    okf_lib.py         ← shared OKF helpers (frontmatter parse/dump, link conversion, actor formatting)
    ingest.py          ← CSV → wiki pages batch ingest
    enrich.py          ← LLM-based stub enrichment (Claude/Gemini)
    build_indexes.py   ← regenerates index.md and every per-folder index from disk state
    log_revision.py    ← records a revision card + updates a page's `generated` field + appends to log.md
    log_source_review.py ← appends one entry to sources/manifest.ndjson (see Source Manifest below)
    add_type_banner.py ← inserts/refreshes the page-type banner under each page's H1 (see below)
    update_links_for_renames.py ← after pages are renamed, re-points every inbound cross-link (see below)
    lint.py            ← health-check (see Lint above)
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

## Page templates

### Principle

```markdown
---
type: principle
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
id: CL-XXXX          # short programmatic ID (e.g. we-4, fi-2)
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
