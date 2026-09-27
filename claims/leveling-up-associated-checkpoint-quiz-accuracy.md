---
type: claim
title: Completing more skill levels is associated with higher Checkpoint Quiz post-test accuracy, with positive coefficients for Levels 1, 2, and 4
description: Completing more skill levels is associated with higher Checkpoint Quiz post-test accuracy, with positive coefficients for Levels 1, 2, and 4
id: leveling-up-associated-checkpoint-quiz-accuracy
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
evidence_strength: moderate
sources:
  - id: lucy-portnoff-2021
    resource: "https://educationaldatamining.org/edm2021/"
    title: "Lucy Portnoff, Erin Gustafson, Klinton Bicknell and Joseph Rollinson. (2021). Methods for Language Learning Assessment at Scale: Duolingo Case Study. Proceedings of The 14th International Conference on Educational Data Mining (EDM21). https://educationaldatamining.org/edm2021/"
    author: Lucy Portnoff, Erin Gustafson, Klinton Bicknell and Joseph Rollinson
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Completing more skill levels is associated with higher Checkpoint Quiz post-test accuracy, with positive coefficients for Levels 1, 2, and 4

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Average post-test item accuracy increases linearly with every skill-level completed, and the logistic regression shows the probability of answering a post-test item correctly increases with every additional lesson in Levels 1, 2, and 4. [→ Lucy Portnoff 2021](#lucy-portnoff-2021)

## Evidence

### Lucy Portnoff 2021

Lucy Portnoff, Erin Gustafson, Klinton Bicknell and Joseph Rollinson. (2021). Methods for Language Learning Assessment at Scale: Duolingo Case Study. Proceedings of The 14th International Conference on Educational Data Mining (EDM21). https://educationaldatamining.org/edm2021/

`q2 · i?` · `causal · r2`

Logistic regression on four months of Checkpoint Quiz data predicted post-test accuracy on pre-test-incorrect items, controlling for item, user, course, other session types, prior proficiency, and subscriber status. The article reports "the probability of answering a post-test item correctly increases with every additional lesson in Levels 1, 2, and 4"; no effect sizes are printed.

> "We observed that the probability of answering a post-test item correctly increases with every additional lesson in Levels 1, 2, and 4. Level 3 has a negative coefficient, but this is likely an artifact of variable suppression"

## Discussion


## Related Claims
- [A regression discontinuity design on Review Exercise data supports a causal link between leveling up and higher assessment accuracy, at least for the first level-up](rdd-review-exercises-causal-leveling-up.md) — related
- [Leveling up lessons preceding the source lesson improves Review Exercise accuracy, indicating transfer of learning benefits across lessons within a skill](leveling-up-benefit-transfers-across-lessons.md) — a narrower finding that bears on this claim
