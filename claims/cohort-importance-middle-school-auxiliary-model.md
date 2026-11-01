---
type: claim
title: Variable importance from the auxiliary model indicates the student cohort matters most for predicting middle school math passing rates, while demographics matter for high schools
description: Variable importance from the auxiliary model indicates the student cohort matters most for predicting middle school math passing rates, while demographics matter for high schools
id: cohort-importance-middle-school-auxiliary-model
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: weak
newest_evidence: 2024
sources:
  - id: c-z-mann-2024
    resource: "https://github.com/manncz/aeis-aux-rct"
    title: "C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. https://github.com/manncz/aeis-aux-rct"
    author: C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Variable importance from the auxiliary model indicates the student cohort matters most for predicting middle school math passing rates, while demographics matter for high schools

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For middle schools the top predictors were primarily previous-year TAKS passing rates including 7th graders', while for high schools demographic variables such as percent of 9th or 10th graders and special education percentage rose in importance. [→ C. Z. Mann 2024](#c-z-mann-2024)

## Evidence

### C. Z. Mann 2024

C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. https://github.com/manncz/aeis-aux-rct

`q2 · i?` · `causal · r2`

Observational variable-importance analysis of random forest models fit on auxiliary Texas schools (Figures 1 and 2). The article reports the cohort of students was highly important for middle schools, whereas high school predictors included demographic variables from the 2007/8 school year such as the percent of 9th or 10th graders and students in special education.

> "For middle schools, the top 15 predictors are primarily different TAKS passing rates (math or overall), either for all grades or for 7th graders from the previous year (Figure 1)."

## Discussion


## Related Claims
- [In auxiliary Texas school data, a random forest with all predictors predicts math TAKS passing rates better than OLS with the pretest alone](rf-all-predictors-beats-pretest-auxiliary.md) — related
- [Random forest models consistently outperform neural networks for predicting math TAKS passing rates in the auxiliary data](random-forests-outperform-neural-nets-auxiliary.md) — related
