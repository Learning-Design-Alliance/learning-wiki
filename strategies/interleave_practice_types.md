---
type: strategy
title: Interleave Practice Types
description: Mix different problem or task types within a practice session rather than blocking them by type, forcing learners to discriminate which approach each problem requires.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Interleave Practice Types

## Description
Interleaving arranges practice so that different problem categories, skills, or task types are mixed within a session (ABCBCA) instead of blocked (AAABBBCCC). Learners must first identify *which kind* of problem they face before selecting a solution strategy, rather than applying the same procedure repeatedly. It is typically combined with [Spaced Practice](../principles/spaced-practice.md), since interleaved schedules naturally distribute exposure over time.

## Design Implications

Interleaving works because it trains problem *identification* alongside problem *solving* — the discrimination step that blocked practice skips entirely [~S]. Blocked practice often produces strong short-term performance but weaker delayed test performance, an effect documented across mathematics, category learning, and motor skills [~S]. Interleaving feels harder and yields worse immediate performance, so learners frequently prefer it less even when it produces better retention [~S].

### Context
#### Requirements
- A set of problem or task types that are *confusable* — interleaving helps most when categories are similar enough to be mistaken for one another
- Learners who have at least minimal initial exposure to each type (interleaving from zero knowledge adds confusion without benefit)
- Feedback or answer keys that let learners verify which strategy was correct after each item
- Sufficient total practice volume; interleaving redistributes practice rather than replacing it

#### Constraints
- For highly distinct, non-confusable task types, interleaving adds little and can impose unnecessary switching costs [~S]
- Novices with no prior instruction on any category may be unable to benefit — discrimination requires something to discriminate [~M]
- Learners' preference for blocked practice can depress engagement and completion in self-paced settings [~M]
- Very rapid switching between unrelated topics can overload working memory [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M]

#### Implementation Variability
- **Within-session interleaving** — mixing problem types inside a single worksheet or quiz
- **Between-session interleaving** — rotating topics across successive sessions (a scheduling decision rather than a materials decision)
- **Faded interleaving** — beginning with blocked practice on each new type, then mixing once basic procedures are established
- **Interleaved retrieval** — combining mixing with [Retrieval Practice](retrieval-practice.md), so each item also functions as a spaced retrieval attempt

### Target Learners
- Learners past the initial acquisition stage who can execute procedures but confuse *when* to apply them [~S]
- Students in categorization-heavy domains: mathematics (choosing the right formula), science (classifying phenomena), clinical diagnosis, grammar
- Less suitable for absolute novices on brand-new material, who need blocked practice to build initial procedure fluency [~M]

### Target Learning Goals
- Discrimination and conditional knowledge: knowing which strategy fits which situation
- Long-term retention and transfer rather than immediate performance
- Preparation for mixed assessment formats, where problem types are never labeled in advance

### Instructions
1. Identify the confusable problem or task types in the unit — the pairs learners typically mix up.
2. Teach each type initially with focused instruction and a short blocked run so basic procedures exist ([Practice](../elements/practice.md)).
3. Reorder subsequent practice so types alternate unpredictably; never signal the type in the item header.
4. Require learners to name the problem type and justify the strategy choice *before* solving — this makes the discrimination step explicit ([Comparing contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+S]).
5. Provide immediate feedback keyed to type identification, not just the final answer.
6. Return to each type repeatedly across sessions, spacing exposure over days or weeks.

## Related Strategies
- [Spaced Practice](../principles/spaced-practice.md) — interleaving's natural companion; both trade short-term fluency for long-term retention
- [Retrieval Practice](retrieval-practice.md) — interleaved items double as spaced retrieval attempts
- [Comparing Cases](../elements/comparing-cases.md) — side-by-side contrast trains the same discrimination skill with more scaffolding
- [Scaffolded Difficulty Progression](scaffolded-difficulty-progression.md) — sequencing within a type, complementary to sequencing across types

## Examples
- **Rohrer's interleaved math workbooks** — Algebra and geometry problem sets rewritten so each page mixes previously taught problem types; delayed test scores roughly doubled relative to blocked versions of the same problems (https://sites.usf.edu/rohrer/).
- **Diagnostic radiology training** — Residency programs interleave chest X-ray cases across disease categories so trainees learn to distinguish look-alike pathologies rather than reading blocks of one diagnosis.
- **Music practice** — Alternating scales, etudes, and repertoire excerpts within a session rather than drilling one piece for the full hour.

## Key Sources
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*(6), 481–498. [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8)
- Rohrer, D., Dedrick, R. F., & Stershic, S. (2015). Interleaved practice improves mathematics learning. *Journal of Educational Psychology, 107*(3), 900–908. [doi:10.1037/edu0000001](https://doi.org/10.1037/edu0000001)
- Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the "enemy of induction"? *Psychological Science, 19*(6), 585–592. [doi:10.1111/j.1467-9280.2008.02127.x](https://doi.org/10.1111/j.1467-9280.2008.02127.x)
- Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press.