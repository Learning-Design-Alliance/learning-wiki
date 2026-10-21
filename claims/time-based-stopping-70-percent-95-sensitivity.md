---
type: claim
title: "A time-based stopping rule requires screening about 70% of abstracts to reach 95% sensitivity, saving on average 0.86 days"
description: "A time-based stopping rule requires screening about 70% of abstracts to reach 95% sensitivity, saving on average 0.86 days"
id: time-based-stopping-70-percent-95-sensitivity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-21
evidence_strength: moderate
sources:
  - id: campos-2024
    resource: "https://doi.org/10.1007/s10648-024-09862-5"
    title: "Campos, D. G., Fütterer, T., Gfrörer, T., Lavelle-Hill, R., Murayama, K., König, L., Hecht, M., Zitzmann, S., & Scherer, R. (2024). Screening Smarter, Not Harder: A Comparative Analysis of Machine Learning Screening Algorithms and Heuristic Stopping Criteria for Systematic Reviews in Educational Research. Educational Psychology Review. https://doi.org/10.1007/s10648-024-09862-5"
    author: "Campos, D. G., Fütterer, T., Gfrörer, T., Lavelle-Hill, R., Murayama, K., König, L., Hecht, M., Zitzmann, S., & Scherer, R."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: campos-2024-2
    resource: "https://doi.org/10.1007/s10648-024-09862-5"
    title: "Campos, D. G., Fütterer, T., Gfrörer, T., Lavelle-Hill, R., Murayama, K., König, L., Hecht, M., Zitzmann, S., & Scherer, R. (2024). Screening Smarter, Not Harder: A Comparative Analysis of Machine Learning Screening Algorithms and Heuristic Stopping Criteria for Systematic Reviews in Educational Research. Educational Psychology Review. https://doi.org/10.1007/s10648-024-09862-5"
    author: "Campos, D. G., Fütterer, T., Gfrörer, T., Lavelle-Hill, R., Murayama, K., König, L., Hecht, M., Zitzmann, S., & Scherer, R."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# A time-based stopping rule requires screening about 70% of abstracts to reach 95% sensitivity, saving on average 0.86 days

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` On average, a reviewer needs to screen 70% of abstracts to find 95% or more of the relevant abstracts using a time-based stopping criterion. [→ Campos 2024](#campos-2024)
`q2 i?` Stopping after classifying 70% of abstracts saved on average 0.86 days (SD = 0.73) by not classifying 36% (SD = 6%) of irrelevant abstracts. [→ Campos 2024 (2)](#campos-2024-2)

## Evidence

### Campos 2024

Campos, D. G., Fütterer, T., Gfrörer, T., Lavelle-Hill, R., Murayama, K., König, L., Hecht, M., Zitzmann, S., & Scherer, R. (2024). Screening Smarter, Not Harder: A Comparative Analysis of Machine Learning Screening Algorithms and Heuristic Stopping Criteria for Systematic Reviews in Educational Research. Educational Psychology Review. https://doi.org/10.1007/s10648-024-09862-5

`q2 · i?` · `causal · r2`

Simulation of time-based stopping in 10% intervals across 27 collections and ten algorithms (Table 4). The article reports screening "an average of 70% of the abstracts" to reach 95% sensitivity.

> "The results indicate that to find 95% or more of the relevant abstracts in an abstract collection, a reviewer needs to screen an average of 70% of the abstracts."

### Campos 2024 (2)

Campos, D. G., Fütterer, T., Gfrörer, T., Lavelle-Hill, R., Murayama, K., König, L., Hecht, M., Zitzmann, S., & Scherer, R. (2024). Screening Smarter, Not Harder: A Comparative Analysis of Machine Learning Screening Algorithms and Heuristic Stopping Criteria for Systematic Reviews in Educational Research. Educational Psychology Review. https://doi.org/10.1007/s10648-024-09862-5

`q2 · i?` · `causal · r2`

Same time-based stopping simulation (Table 4). Stopping at 70% screened yielded mean ETS of 0.86 days (SD = 0.73), leaving "36% (SD = 6%) of irrelevant abstracts" unclassified.

> "if a reviewer decides to stop screening after classifying 70% of the abstracts in an abstract collection, they can save, on average, 0.86 (SD = 0.73) days by not having to classify 36% (SD = 6%) of irrelevant abstracts present in the abstract collection."

## Discussion


## Related Claims
- [A data-driven stopping rule needs about 7% consecutive irrelevant abstracts to reach 95% sensitivity, saving on average 1.04 days](data-driven-stopping-7-percent-consecutive-irrelevant.md) — related
- [The LR+SBERT model achieved the highest specificity and estimated time savings at 95% sensitivity among the tested learning algorithms](lr-sbert-highest-specificity-screening.md) — related
- [Sensitivity under mixed stopping criteria correlated positively with collection length in some strategy groups but not others](mixed-stopping-sensitivity-correlates-with-collection-length.md) — related
- [Active learning algorithms reduce abstract-screening workload in education systematic reviews, saving on average 58% of irrelevant-record screening and 1.66 days at 95% sensitivity](ml-screening-reduces-workload-education-reviews.md) — related
