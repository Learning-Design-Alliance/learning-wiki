---
type: claim
title: Variable importance from the auxiliary model indicates the student cohort matters most for predicting middle school math passing rates, while demographics matter for high schools
description: Variable importance from the auxiliary model indicates the student cohort matters most for predicting middle school math passing rates, while demographics matter for high schools
id: cohort-importance-middle-school-auxiliary-model
aliases: [variable-importance-differs-middle-high-schools]
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: weak
newest_evidence: 2024
sources:
  - id: c-z-mann-2024
    resource: "https://doi.org/10.5281/zenodo.12729874"
    title: "C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. [doi:10.5281/zenodo.12729874](https://doi.org/10.5281/zenodo.12729874)"
    author: C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: c-z-mann-2024-2
    resource: "https://doi.org/10.5281/zenodo.12729874"
    title: "C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. [doi:10.5281/zenodo.12729874](https://doi.org/10.5281/zenodo.12729874)"
    author: C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Variable importance from the auxiliary model indicates the student cohort matters most for predicting middle school math passing rates, while demographics matter for high schools

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims

`q2 i?` For middle schools the top predictors were primarily previous-year TAKS passing rates including 7th graders', while for high schools demographic variables such as percent of 9th or 10th graders and special education percentage rose in importance. [→ C. Z. Mann 2024](#c-z-mann-2024)

`q2 i?` For auxiliary middle schools the top predictors are primarily previous-year TAKS passing rates, indicating the student cohort was highly important. [→ C. Z. Mann 2024](#c-z-mann-2024)

`q2 i?` For auxiliary high schools, top predictors included percent of 9th or 10th graders, percent in special education, and numbers of students and staff, in addition to TAKS passing rates. [→ C. Z. Mann 2024 (2)](#c-z-mann-2024-2)

## Evidence

### C. Z. Mann 2024

C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. [doi:10.5281/zenodo.12729874](https://doi.org/10.5281/zenodo.12729874)

`q2 · i?` · `causal · r2`

Observational variable-importance analysis of random forest models fit on auxiliary Texas schools (Figures 1 and 2). The article reports the cohort of students was highly important for middle schools, whereas high school predictors included demographic variables from the 2007/8 school year such as the percent of 9th or 10th graders and students in special education.

> "For middle schools, the top 15 predictors are primarily different TAKS passing rates (math or overall), either for all grades or for 7th graders from the previous year (Figure 1)."

<!-- merged 2026-11-23 from variable-importance-differs-middle-high-schools: that page's entry for this study, which differed from the one above, kept verbatim.
### C. Z. Mann 2024

C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. [doi:10.5281/zenodo.12729874](https://doi.org/10.5281/zenodo.12729874)

`q2 · i?`

Random forest variable importance analysis on auxiliary Texas middle schools (Figure 1, Section 4.3), ranked by percent increase in MSE. The article interprets this as showing "the actual cohort of students ... was highly important" for middle school prediction.

> "For middle schools, the top 15 predictors are primarily different TAKS passing rates (math or overall), either for all grades or for 7th graders from the previous year (Figure 1)."
-->

### C. Z. Mann 2024 (2)

C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. [doi:10.5281/zenodo.12729874](https://doi.org/10.5281/zenodo.12729874)

`q2 · i?` · `causal · r2`

Random forest variable importance analysis on auxiliary Texas high schools (Figure 2, Section 4.3). The article explains the 8th-grade cohort cannot be followed into 9th grade with the given data, "so other types of predictors rise in importance when predicting the outcome for high schools".

> "For high schools, the top predictors included demographic variables from the 2007/8 school year, such as the percent of 9th or 10th graders in a school, the percent of students in special education programs, and the number of students and staff, in addition to TAKS passing rates (Figure 2)."

## Discussion



## Related Claims

- [In auxiliary Texas school data, a random forest with all predictors predicts math TAKS passing rates better than OLS with the pretest alone](rf-all-predictors-beats-pretest-auxiliary.md) — related
- [Random forest models consistently outperform neural networks for predicting math TAKS passing rates in the auxiliary data](random-forests-outperform-neural-nets-auxiliary.md) — related
