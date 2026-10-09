---
type: claim
title: Two distinct feature combinations identify two types of wheel-spinning students in ASSISTments Skill Builders
description: Two distinct feature combinations identify two types of wheel-spinning students in ASSISTments Skill Builders
id: two-types-wheel-spinning-students-assistments
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: kai-2018
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/210"
    title: "Kai, S., Heffernan, C., Almeda, M. V., Heffernan, N., & Baker, R. S. (2018). Decision Tree Modeling of Wheel-Spinning and Productive Persistence in Skill Builders. Journal of Educational Data Mining, Volume 10, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/210"
    author: "Kai, S., Heffernan, C., Almeda, M. V., Heffernan, N., & Baker, R. S."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: kai-2018-2
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/210"
    title: "Kai, S., Heffernan, C., Almeda, M. V., Heffernan, N., & Baker, R. S. (2018). Decision Tree Modeling of Wheel-Spinning and Productive Persistence in Skill Builders. Journal of Educational Data Mining, Volume 10, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/210"
    author: "Kai, S., Heffernan, C., Almeda, M. V., Heffernan, N., & Baker, R. S."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Two distinct feature combinations identify two types of wheel-spinning students in ASSISTments Skill Builders

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` Students who request no hints in at least one problem but more than one bottom-out hint in the last 8 problems are likely wheel-spinning (89.07% of such instances). [→ Kai 2018](#kai-2018)
`q2 i?` Students who request no hints in at least one problem, at most one bottom-out hint in the last 8 problems, and have time-between-problems standard deviation of 2.53 days or less are also likely wheel-spinning, at a lower probability than the first combination. [→ Kai 2018 (2)](#kai-2018-2)

## Evidence

### Kai 2018

Kai, S., Heffernan, C., Almeda, M. V., Heffernan, N., & Baker, R. S. (2018). Decision Tree Modeling of Wheel-Spinning and Productive Persistence in Skill Builders. Journal of Educational Data Mining, Volume 10, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/210

`q2 · i?` · `associational · r2`

Analysis of the top nodes of the J48 decision tree over 8,948 persistent student-problem set pairs; Table 3 reports 2544 out of 2856 student-problem set pairs (89.07%) with this combination labeled wheel-spinning.

> "The first feature combination indicates that students are likely to be wheel -spinning when they do not request any hints in at least one problem within the problem set but request more bottom-out hints in the last 8 problems within the sequence of 10."

### Kai 2018 (2)

Kai, S., Heffernan, C., Almeda, M. V., Heffernan, N., & Baker, R. S. (2018). Decision Tree Modeling of Wheel-Spinning and Productive Persistence in Skill Builders. Journal of Educational Data Mining, Volume 10, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/210

`q2 · i?` · `associational · r2`

Second top-node feature combination in the J48 tree; Table 4 reports 5027 out of 6457 student-problem set pairs (77.85%) labeled wheel-spinning, a lower probability than the first combination.

> "even when the maxim um number of bottom-out hint requests is 1 or 0, students can still wheel-spin if they do not request any hints in at least one problem and the standard deviation value of the amount of time since the current problem set was last seen is less than or equal to 2.53 days."

## Discussion


## Related Claims
- [The relationship between bottom-out hint use and wheel-spinning is nuanced, depending on whether students avoid hints entirely](bottom-out-hint-use-nuanced-wheel-spinning.md) — a broader claim this one bears on
- [Not requesting any hints in at least one problem is related to greater wheel-spinning, consistent with help avoidance](hint-avoidance-related-greater-wheel-spinning.md) — a broader claim this one bears on
- [A 15-feature J48 decision tree model distinguishes wheel-spinning from productive persistence in ASSISTments Skill Builders at AUC ROC 0.684 under student-skill-level cross-validation](j48-model-distinguishes-wheel-spinning-productive-persistence.md) — related
- [A retention-based definition of wheel-spinning classifies a much lower proportion of students as wheel-spinning than Beck and Gong's opportunity-count definition](retention-based-wheel-spinning-definition-lower-proportion.md) — related
- [Consistently short delays between problems of the same skill are associated with greater wheel-spinning](short-consistent-delays-associated-wheel-spinning.md) — related
