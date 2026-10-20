---
type: claim
title: Automated gaming-the-system detectors built with XGBoost reliably recognize gaming in both problem-solving and self-explanation steps
description: Automated gaming-the-system detectors built with XGBoost reliably recognize gaming in both problem-solving and self-explanation steps
id: xgboost-gaming-detectors-decimal-point
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-18
evidence_strength: moderate
sources:
  - id: baker-2025
    resource: "https://doi.org/10.1007/s11251-024-09679-3"
    title: "Baker, R. S., Richey, J. E., Zhang, J., Karumbaiah, S., Andres-Bray, J. M., Nguyen, H. A., Andres, J. M. A. L., & McLaren, B. M. (2025). Gaming the system mediates the relationship between gender and learning outcomes in a digital learning game. Instructional Science, 53, 203–238. https://doi.org/10.1007/s11251-024-09679-3"
    author: "Baker, R. S., Richey, J. E., Zhang, J., Karumbaiah, S., Andres-Bray, J. M., Nguyen, H. A., Andres, J. M. A. L., & McLaren, B. M."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Automated gaming-the-system detectors built with XGBoost reliably recognize gaming in both problem-solving and self-explanation steps

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Tenfold student-level cross-validation showed the detectors reliably predicted gaming in unseen students in the problem-solving (AUC = 0.89, k = 0.50) and self-explanation (AUC = 0.99, k = 0.95) steps. [→ Baker 2025](#baker-2025)

## Evidence

### Baker 2025

Baker, R. S., Richey, J. E., Zhang, J., Karumbaiah, S., Andres-Bray, J. M., Nguyen, H. A., Andres, J. M. A. L., & McLaren, B. M. (2025). Gaming the system mediates the relationship between gender and learning outcomes in a digital learning game. Instructional Science, 53, 203–238. https://doi.org/10.1007/s11251-024-09679-3

`q2 · i?` · `associational · r2`

Detectors were built by hand-labeling log data via text replay coding (800 problem-solving and 1500 self-explanation clips; inter-rater k = 0.74 and 0.88) and training an Extreme Gradient Boosting (XGBoost) classifier for each step type.

> "Based on the cross-validation results, we determined that the models could reliably predict gaming in unseen students in both the problem-solving (AUC = 0.89, k = 0.50) and self-explanation (AUC = 0.99, k = 0.95) steps."

## Discussion


## Related Claims
- [Machine-learned detectors of science inquiry skill made accurate inferences after a student ran a simulation three times](inquiry-detectors-accurate-after-three-runs.md) — related
- [Gaming the system is significantly negatively correlated with test performance in the digital learning game](gaming-negative-correlation-test-performance.md) — related
- [Automated detectors of disengaged behaviors inferred from interaction-log data alone reached AUC over 0.8 for gaming and correlated 0.55 with observed off-task behavior](sensor-free-disengagement-detectors-accuracy.md) — a broader claim this one bears on
- [No significant gender difference in gaming the system appears in the non-game control condition or in the problem-solving step](no-gender-gaming-difference-nongame-and-problem-solving.md) — related
- [Generalizable detectors of students' affective states in DLPs remain an unsolved problem](no-generalizable-affective-detectors.md) — a broader claim this one bears on
- [Male students game the system significantly more than female students in the self-explanation step of a digital learning game, across three studies](males-gaming-more-self-explanation-game-condition.md) — related
