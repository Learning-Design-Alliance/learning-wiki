# Learning Design Wiki — Agent Operating Guide

This is a **persistent, LLM-maintained knowledge base** for learning design. The wiki compiles design principles, instructional patterns, elements, strategies, theories, and empirical claims into a structured, cross-linked reference.

**You never write the wiki yourself.** The LLM reads sources, ingests new content, cross-links pages, and keeps schemas consistent. You source materials and ask questions.

---

## Three core operations

### 1. Ingest
Process a new source (paper, book chapter, CSV batch, worked example) into wiki pages.

Steps:
1. Identify the page type(s) the source contributes to (principle, element, pattern, strategy, theory, claim)
2. Check if a page already exists (`index.md` or `grep` by name)
3. If new: create a page in the correct folder using the template below
4. If existing: merge new content into the right sections; append to `## Key Sources`; log the change
5. Cross-link: add example wikilinks like ``[ [principles/example-page] ]`` to related pages already in the wiki
6. Update `index.md` (add entry under the right type heading)
7. Append an entry to `log.md`: `## [YYYY-MM-DD] ingest | [page name] | [source]`

### 2. Query
Answer a question by reading the wiki.

Steps:
1. Search `index.md` for relevant pages
2. Read those pages; follow example wikilinks like ``[ [principles/example-page] ]`` as needed
3. Synthesize across pages; cite page names and claim IDs
4. Flag gaps: if the answer requires a page that doesn't exist, note it

### 3. Lint
Health-check the wiki.

Checks:
- Broken example wikilinks like ``[ [principles/example-page] ]`` (link target not found in index)
- Pages with `status: draft` and no description
- Claim pages missing an evidence strength rating
- Principles missing at least one claim link
- Source entries missing a DOI or URL

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

Always link the tag to a claim page: ``[ [claims/example-claim] ] [+M]``

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

## Wikilink conventions

- All links use Obsidian-style examples like ``[ [folder/slug] ]`` or ``[ [folder/slug|Display Name] ]``
- Slugs are lowercase, hyphen-separated: `worked-examples`, `cognitive-load-theory`
- Folder-qualified links when disambiguation is needed: ``[ [claims/worked-examples-math-performance] ]``
- Claims use semantic slugs: ``[ [claims/worked-examples-reduce-novice-load] ]``; the short `id:` in frontmatter is for programmatic reference only

---

## Folder map

```
ld-wiki/
  CLAUDE.md          ← this file (schema + operating guide)
  index.md           ← catalog of all pages by type
  log.md             ← append-only ingest/edit log
  principles/        ← design principles (what to do and why)
  elements/          ← instructional components (building blocks)
  patterns/          ← instructional patterns (reusable designs at lesson/unit level)
  strategies/        ← teaching strategies (concrete activity recipes)
  theories/          ← learning theories (explanatory frameworks)
  claims/            ← empirical claims with evidence
  scripts/
    ingest.py        ← CSV → wiki pages batch ingest
```

---

## Page templates

### Principle

```markdown
---
type: principle
status: draft
last_edited: YYYY-MM-DD
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
<!-- Link claims with evidence tags: [ [claims/claim-slug] ] [+M] -->
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
status: draft
last_edited: YYYY-MM-DD
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
<!-- Link to sub-claims: [ [claims/claim-slug] ] -->
- 

### Target Learning Goals
<!-- Link to sub-claims: [ [claims/claim-slug] ] -->
- 

### Affordances
<!-- Link to principles applied: [ [principles/principle-slug] ] -->
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
status: draft
last_edited: YYYY-MM-DD
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
<!-- Link to claims: [ [claims/claim-slug] ] -->
- 

### Target Learners
<!-- Link to claims: [ [claims/claim-slug] ] -->
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
<!-- Steps with links to elements: [ [elements/element-slug] ] -->
1. 

### Affordances
<!-- Links to principles applied: [ [principles/principle-slug] ] -->
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
status: draft
last_edited: YYYY-MM-DD
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
<!-- Link to sub-claims: [ [claims/claim-slug] ] -->
- 

### Target Learning Goals
<!-- Link to sub-claims: [ [claims/claim-slug] ] -->
- 

### Instructions
<!-- Steps with links to elements: [ [elements/element-slug] ] -->
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
status: draft
last_edited: YYYY-MM-DD
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
<!-- Claims that derive from or test this theory: [ [claims/claim-slug] ] [+M] -->
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
id: CL-XXXX          # short programmatic ID (e.g. we-4, fi-2)
status: draft
last_edited: YYYY-MM-DD
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
<!-- One entry per study. Heading slug becomes the anchor target for subclaim links.
     Show full APA citation with DOI as a hyperlink.
     Then: quality · impact · n codes with plain-language explanations.
     Then: 2–4 sentence plain-language description. Link instructional elements to wiki pages.
     Avoid unexplained abbreviations or jargon. -->

### Author Year

Author, A., & Author, B. (Year). Title. *Journal, vol*(issue), pages. [doi:...](https://doi.org/...)

`q? · [e.g. peer-reviewed RCT / quasi-experiment / meta-analysis]` · `i? · [e.g. large effect, d=0.9]` · `n=?`

[2–4 sentences: study design, participants (who, how many, what context), conditions or intervention, and findings in plain language. Link any instructional elements used to their wiki pages, for example ``[ [elements/demonstration|worked examples] ]`` and ``[ [elements/practice|practice tasks] ]``.]

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
- When a field references another page by name (e.g., "Cognitive Load Theory"), convert it to a wikilink using the slugified name
- When research support / impact fields contain citations, extract them into `## Key Sources` and create or link `sources/` pages
- Mark pages `status: draft` on initial ingest; a human or a lint pass can promote to `review` or `stable`
- Never delete content on update — move superseded content to a `<!-- deprecated -->` comment block
