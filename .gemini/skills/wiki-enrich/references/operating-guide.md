# Operating Guide — ld-wiki

Copy of `CLAUDE.md`. Read that file for the authoritative version.

This is a **persistent, LLM-maintained knowledge base** for learning design. The wiki compiles design principles, instructional patterns, elements, strategies, theories, and empirical claims into a structured, cross-linked reference.

**You never write the wiki yourself.** The LLM reads sources, ingests new content, cross-links pages, and keeps schemas consistent. You source materials and ask questions.

The wiki is a bundle in the [Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md): every content page is markdown with YAML frontmatter carrying `type`, `title`, `description`, `status`, `generated`, and (where applicable) `sources`; cross-links are plain bundle-relative markdown links, not Obsidian wikilinks; `index.md` and `log.md` are OKF's reserved directory-listing and change-log filenames.

---

## Three core operations

### 1. Ingest
Process a new source (paper, book chapter, CSV batch, worked example) into wiki pages.

Steps:
1. Identify the page type(s) the source contributes to (principle, element, pattern, strategy, theory, claim)
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

Every content page (principle, element, pattern, strategy, theory, claim) carries this OKF-conformant frontmatter:

| Field | Required | Meaning |
|-------|----------|---------|
| `type` | Yes | `principle` \| `element` \| `pattern` \| `strategy` \| `theory` \| `claim` |
| `title` | Recommended | Display name — normally matches the page's `# H1` |
| `description` | Recommended | One-sentence summary, used in index listings |
| `status` | Recommended | See Status values above |
| `generated` | Recommended | `{ by: <actor>, at: <date> }` — who/what last wrote the page and when, replacing the old `last_edited`/`edited_by` pair |
| `sources` | When applicable | List of `{ id, resource, title, author }` entries parsed from `## Key Sources` (or `## Evidence` for claims) — a structured mirror of the citations already in the body, not a replacement for them |
| `id`, `evidence_strength`, `author`, `grain_size` | Type-specific | Extra scalar fields kept as-is per page type (see templates below); OKF tolerates extra frontmatter keys |

**Actor convention** for `generated.by` (and any other identity field): `<tool>/unspecified` for an agent/tool (e.g. `claude/unspecified`, `codex/unspecified`), `human:<id>` for a person, `process:<id>` for an unattended batch job (e.g. `process:wiki-ingest`). Never invent a specific model version you're not certain of — `unspecified` is fine.

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
  claims/            ← empirical claims with evidence
  sources/           ← bibliographic source pages (optional; most citations live inline in Key Sources / Evidence)
  scripts/
    okf_lib.py         ← shared OKF helpers (frontmatter parse/dump, link conversion, actor formatting)
    ingest.py          ← CSV → wiki pages batch ingest
    enrich.py          ← LLM-based stub enrichment (Claude/Gemini)
    build_indexes.py   ← regenerates index.md and every per-folder index from disk state
    log_revision.py    ← records a revision card + updates a page's `generated` field + appends to log.md
    lint.py            ← health-check (see Lint above)
```

Each folder's `index.md` is itself a reserved OKF filename: no frontmatter (except the bundle-root's `okf_version`), and a plain `* [Title](slug.md) - description` bullet listing grouped by status. Regenerate these with `python3 scripts/build_indexes.py` rather than hand-editing them.

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
