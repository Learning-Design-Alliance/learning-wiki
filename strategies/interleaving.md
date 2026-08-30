---
type: strategy
title: Interleaving
description: Interleaving arranges practice so that different but related problem types or categories are mixed within a session rather than blocked, forcing learners to discriminate between them.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Interleaving

## Description
Interleaving sequences practice so that problems from different categories or skills alternate within a session (A, B, C, A, B, C) instead of appearing in blocks (AAA, BBB, CCC). The mixing forces learners to select an appropriate strategy for each problem, not just execute one they have already primed. It is typically combined with [spaced repetition](../claims/distributed-practice-improves-retention.md), since interleaved schedules naturally distribute practice over time.

## Design Implications

Interleaving improves delayed test performance across mathematics, category learning, and motor skills, even though learners often feel it is less effective than blocked practice [Interleaved practice improves delayed test performance more than blocked practice.](../claims/interleaved-practice-improves-retention.md) [+S]. The mechanism is twofold: discriminative contrast — comparing adjacent problems reveals what makes category A different from category B — and retrieval practice, because each item requires reactivating the correct strategy rather than repeating the previous one. Interleaving trades short-term fluency for long-term retention and transfer, which is why learners' preference for blocked practice is a poor design guide [~M].

### Context
#### Requirements
- Problem sets or items drawn from **related** categories that learners confuse or that share surface features — interleaving unrelated topics produces mostly spacing benefits and little discrimination benefit
- Enough items per category to allow repeated revisits across the sequence
- Feedback or answer-checking so learners can correct category misassignments [Practice](../elements/practice.md) with feedback
- Delayed assessment to capture the benefit; immediate post-tests will understate it

#### Constraints
- Interleaving hurts performance **during practice** — learners make more errors and work more slowly, which can be misread as the strategy failing [-S]
- Weakly effective or counterproductive for novices who have not yet mastered any single category; some initial blocked exposure before interleaving may be needed [~M]
- For very distinct, easily discriminated skills (e.g., addition vs. reading comprehension), interleaving adds little beyond spacing [~W]
- Interleaving within a single session is not a substitute for distributed practice across days; the two are complementary [Interleaving's benefits are partly but not wholly attributable to spacing.](../claims/distributed-practice-improves-retention.md) [~M]

#### Implementation Variability
- **Within-topic interleaving**: mixing problem types from one unit (e.g., volume of cones, spheres, cylinders in one set) — the classic Rohrer design
- **Across-topic interleaving**: cycling through several units in review sets, common in adaptive practice platforms
- **Inductive interleaving**: presenting interleaved exemplars of categories before teaching labels or rules, which improves concept induction [~S]
- **Shuffled vs. systematic sequences**: random ordering works; systematic ABCCBA ordering makes discrimination contrasts more reliable

### Target Learners
- Learners past the initial acquisition stage who can execute each category's procedure but confuse *when* to use it [+S]
- Students in domains with confusable categories: mathematics problem types, art-history styles, bird species, grammar rules
- Less suitable for absolute novices, who need some blocked practice to form initial procedures [~M]

### Target Learning Goals
- Discrimination learning: selecting the correct strategy or category, not just executing it
- Long-term retention and transfer of procedures [Interleaved practice improves delayed test performance more than blocked practice.](../claims/interleaved-practice-improves-retention.md) [+S]
- Inductive concept learning from exemplars [~S]

### Instructions
1. Identify the confusable categories or problem types in the unit — the pairs learners typically mix up.
2. Ensure learners have had initial [practice](../elements/practice.md) with each category separately; do not interleave from zero knowledge.
3. Build mixed problem sets that cycle through categories, keeping adjacent items from different categories so contrasts are salient.
4. Require learners to identify the problem type or strategy *before* solving — this makes the discrimination demand explicit.
5. Provide immediate feedback so category errors are corrected, not consolidated.
6. Revisit the mixed set across multiple sessions, pairing interleaving with [distributed practice](../claims/distributed-practice-improves-retention.md).
7. Assess with a delayed, mixed test — never judge the strategy by within-session fluency.

## Related Strategies
- [Spaced practice](../claims/distributed-practice-improves-retention.md) — interleaving's natural companion; mixed schedules distribute retrieval over time
- [Retrieval practice](../claims/distributed-practice-improves-retention.md) — each interleaved item forces re-selection of a strategy, embedding retrieval in the schedule
- [Comparing cases](../elements/case-studies.md) — interleaving enacts comparison at the schedule level; explicit case comparison does it at the task level

## Examples
- **Rohrer's math worksheets** — the "mixed" practice sets in Rohrer & Taylor (2007): volume problems for prisms, cylinders, cones, and spheres shuffled in one assignment, producing large gains on a delayed test despite worse practice performance.
- **[Khan Academy](https://www.khanacademy.org)** — its mastery practice draws exercises from previously learned skills in mixed sets rather than one skill at a time.
- **[Anki](https://apps.ankiweb.net)** — spaced-repetition flashcard software that interleaves cards across decks and topics by default, mixing discrimination-heavy item types.
- **Art and category learning studies** — Kornell & Bjork (2008) showed learners induced painters' styles better from interleaved than blocked exemplar sets, despite confidently believing the opposite.

## Key Sources
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*(6), 481–498. [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8)
- Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the "enemy of induction"? *Psychological Science, 19*(6), 585–592. [doi:10.1111/j.1467-9280.2008.02127.x](https://doi.org/10.1111/j.1467-9280.2008.02127.x)
- Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin, 145*(11), 1029–1052. [doi:10.1037/bul0000209](https://doi.org/10.1037/bul0000209)
- Kang, S. H. K. (2016). Spaced repetition promotes efficient and effective learning: Policy implications of innovations in teaching and learning science. *Policy Insights from the Behavioral and Brain Sciences, 3*(1), 12–19. [doi:10.1177/2372732215624708](https://doi.org/10.1177/2372732215624708)