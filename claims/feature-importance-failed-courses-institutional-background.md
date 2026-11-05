---
type: claim
title: Feature importance analyses rank failed courses first for predicting academic performance, followed by institutional and academic background variables, with some regression-specific differences
description: Feature importance analyses rank failed courses first for predicting academic performance, followed by institutional and academic background variables, with some regression-specific differences
id: feature-importance-failed-courses-institutional-background
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: sayed-2025
    resource: "https://doi.org/10.1038/s41598-025-31023-z"
    title: "Sayed, A. F. A., Arafa, M. A., El-Nimr, N. A., Banawan, K. A. S., & Abdou, M. S. (2025). Comparison of machine learning classification and regression models for prediction of academic performance among postgraduate public health students. Scientific Reports, 15, 44056. [doi:10.1038/s41598-025-31023-z](https://doi.org/10.1038/s41598-025-31023-z)"
    author: "Sayed, A. F. A., Arafa, M. A., El-Nimr, N. A., Banawan, K. A. S., & Abdou, M. S."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: sayed-2025-2
    resource: "https://doi.org/10.1038/s41598-025-31023-z"
    title: "Sayed, A. F. A., Arafa, M. A., El-Nimr, N. A., Banawan, K. A. S., & Abdou, M. S. (2025). Comparison of machine learning classification and regression models for prediction of academic performance among postgraduate public health students. Scientific Reports, 15, 44056. [doi:10.1038/s41598-025-31023-z](https://doi.org/10.1038/s41598-025-31023-z)"
    author: "Sayed, A. F. A., Arafa, M. A., El-Nimr, N. A., Banawan, K. A. S., & Abdou, M. S."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Feature importance analyses rank failed courses first for predicting academic performance, followed by institutional and academic background variables, with some regression-specific differences

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In decision-tree feature importance analysis, the number of F courses ranked first in both classification and regression models, followed by bachelor's university and major (classification) and forced-withdrawal courses and bachelor major (regression). [→ Sayed 2025](#sayed-2025)
`q2 i?` Regression-specific features such as specialty and forced-withdrawal courses gained prominence, suggesting feature selection should be tailored to the modeling approach. [→ Sayed 2025 (2)](#sayed-2025-2)

## Evidence

### Sayed 2025

Sayed, A. F. A., Arafa, M. A., El-Nimr, N. A., Banawan, K. A. S., & Abdou, M. S. (2025). Comparison of machine learning classification and regression models for prediction of academic performance among postgraduate public health students. Scientific Reports, 15, 44056. [doi:10.1038/s41598-025-31023-z](https://doi.org/10.1038/s41598-025-31023-z)

`q2 · i?` · `associational · r2`

Decision-tree feature importance from the classification models (Fig. 3) on the 922-student dataset. Failed courses ranked first, then bachelor's university, bachelor's major, department, and pre-enrollment GPA; registration semester, working field and bachelor university affiliation had less impact.

> "“no. of F courses” was the most important feature that correlated with prediction, followed by the university from which the bachelor’s degree was obtained and bachelor’s major. Department and pre-enrollment GPA ranked 4th and 5th, respectively."

### Sayed 2025 (2)

Sayed, A. F. A., Arafa, M. A., El-Nimr, N. A., Banawan, K. A. S., & Abdou, M. S. (2025). Comparison of machine learning classification and regression models for prediction of academic performance among postgraduate public health students. Scientific Reports, 15, 44056. [doi:10.1038/s41598-025-31023-z](https://doi.org/10.1038/s41598-025-31023-z)

`q2 · i?` · `associational · r2`

Authors' discussion of the regression feature importance results (Fig. 4), where number of F courses ranked first, followed by number of forced withdrawal courses and bachelor major. The authors attribute the differing rankings to regression's sensitivity to continuous relationships.

> "Regression-specific features like “specialty” and “FW courses” (forced withdrawn courses) gained prominence, likely due to regression’s sensitivity to continuous relationships. This highlights the need for tailored feature selection based on the modeling approach"

## Discussion


## Related Claims
- [The number of failed courses is the strongest correlate of postgraduate public health students' CGPA, with a negative correlation of r = −0.37](failed-courses-strongest-negative-correlate-cgpa.md) — a broader claim this one bears on
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — related
- [SHAP analysis identifies undergraduate GPA rank as the most influential predictor, followed by gender, confidence, undergraduate score average, and CET-4 performance](shap-undergrad-gpa-rank-strongest-predictor.md) — related
- [Engineered practice-balance features outperform raw activity counts: the Intensity Ratio ranks third among Codeforces predictors, and upsolving habit dominates the survey model](intensity-ratio-and-upsolving-habit-top-feature-importance.md) — related
