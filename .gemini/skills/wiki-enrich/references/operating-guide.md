# Operating Guide — ld-wiki

Condensed from `CLAUDE.md`. Read that file for the authoritative version.

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
[Evidence-grounded paragraph with inline claim tags.]

### Context
#### Requirements
- 
#### Constraints
- [Use [-] or [~] tags here, never [+]]

### Target Learners
- 

### Target Learning Objectives
- 

### Theory
#### Supporting
- [[theories/slug|Theory Name]] — brief explanation
#### Contradicting / Qualifying
- 

### Claims
- [[claims/slug]] [+M]

## Related Principles
- [[principles/slug|Name]] — one-line explanation

## Examples
- [[elements/slug|Element]] or [[patterns/slug|Pattern]] — how it applies

## Key Sources
- APA citation. [doi:...](https://doi.org/...)
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
[What this element is; how it functions.]

## Design Implications
[Evidence paragraph with inline claim tags.]

### Context
#### Requirements
- 
#### Constraints
- [Use [-] or [~] tags here]

### Target Learners
- 

### Target Learning Goals
- 

### Affordances
- [[principles/slug|Principle]] — how this element enacts that principle

## Related Elements
- [[elements/slug|Element]] — one-line explanation

## Examples
- [Real platform with URL] — description

## Key Sources
- APA citation. [doi:...](https://doi.org/...)
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
[Evidence paragraph with inline claim tags.]

### Context
#### Requirements
- 
#### Constraints
- [Use [-] or [~] tags here]
#### Grain Size
[program / course / unit / lesson]

### Target Goals
- 

### Target Learners
- 

### Theory
#### Supporting
- [[theories/slug|Theory]] — explanation
#### Contradicting / Qualifying
- 

### Claims
#### Supporting
- [[claims/slug]] [+S]
#### Contradicting
- [[claims/slug]] [~M]

## Design

### Sequence
1. **Step name** — [[elements/slug|Element]] description

### Affordances
- [[principles/slug|Principle]] — how the pattern applies it

### Personalization
- [Adaptation for different learner profiles]

## Related Patterns
- [[patterns/slug|Pattern]] — one-line explanation

## Examples
- [Real-world example with context]

## Key Sources
- APA citation. [doi:...](https://doi.org/...)
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
[What this theory proposes; core mechanism.]

## Implications

### Context
- 

### Target Learners
- 

### Target Learning Objectives
- 

## Claims
- [[claims/slug]] [+M]

## Related Theories
- [[theories/slug|Theory]] — relationship

## Examples
- [[patterns/slug|Pattern]] or [[principles/slug|Principle]] that applies this theory

## Key Sources
- APA citation. [doi:...](https://doi.org/...)
```

---

### Claim

```markdown
---
type: claim
id: CL-XXXX
status: draft
last_edited: YYYY-MM-DD
evidence_strength: strong | moderate | weak | mixed
---

# [Claim statement — one sentence, present tense]

[1–2 sentence clarification of scope or mechanism.]

## Subclaims

`q? i?` [One-sentence finding summary.] [→ Author Year](#author-year)

## Evidence

### Author Year

Author, A. (Year). Title. *Journal, vol*(issue), pages. [doi:...](https://doi.org/...)

`q? · [study type]` · `i? · [effect size]` · `n=?`

[2–4 sentences: design, participants, conditions, findings in plain language.]

## Discussion
[Contradictions, moderators, boundary conditions, open questions.]

## Related Claims
- [[claims/slug]]
```

**Evidence quality (q):** 4 = pre-registered RCT or well-powered meta-analysis · 3 = peer-reviewed experiment or systematic review · 2 = quasi-experiment or narrative review · 1 = case study or theoretical argument

**Impact magnitude (i):** 3 = large (d ≥ 0.8) · 2 = medium (d 0.4–0.79) · 1 = small (d 0.2–0.39) · 0 = negligible/unclear

---

## Status values

| Status | Meaning |
|--------|---------|
| `draft` | Skeleton or stub; content not reviewed |
| `review` | Content present; needs expert review |
| `stable` | Reviewed and considered reliable |
| `deprecated` | Superseded or discredited; kept for history |

## log.md entry format

```
## [YYYY-MM-DD] enrich | [page name] | enriched via wiki-enrich skill
```
