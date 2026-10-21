---
type: claim
title: "A data-driven stopping rule needs about 7% consecutive irrelevant abstracts to reach 95% sensitivity, saving on average 1.04 days"
description: "A data-driven stopping rule needs about 7% consecutive irrelevant abstracts to reach 95% sensitivity, saving on average 1.04 days"
id: data-driven-stopping-7-percent-consecutive-irrelevant
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

# A data-driven stopping rule needs about 7% consecutive irrelevant abstracts to reach 95% sensitivity, saving on average 1.04 days

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` To identify 95% of relevant abstracts, a reviewer would need to classify on average 7% of consecutive irrelevant abstracts under a data-driven stopping criterion. [→ Campos 2024](#campos-2024)
`q2 i?` This left on average 38% (SD = 27%) of irrelevant abstracts unclassified, saving an estimated 1.04 days (SD = 1.47). [→ Campos 2024 (2)](#campos-2024-2)

## Evidence

### Campos 2024

Campos, D. G., Fütterer, T., Gfrörer, T., Lavelle-Hill, R., Murayama, K., König, L., Hecht, M., Zitzmann, S., & Scherer, R. (2024). Screening Smarter, Not Harder: A Comparative Analysis of Machine Learning Screening Algorithms and Heuristic Stopping Criteria for Systematic Reviews in Educational Research. Educational Psychology Review. https://doi.org/10.1007/s10648-024-09862-5

`q2 · i?` · `causal · r2`

Simulation of data-driven stopping criteria (1–10% consecutive irrelevant records) across 27 collections and ten algorithms (Table 5). The article reports a mean threshold of "7% of consecutive irrelevant abstracts" for 95% sensitivity.

> "The results indicate that to identify 95% of the relevant abstracts in an abstract collection, a reviewer would need to classify, on average, 7% of consecutive irrelevant abstracts."

### Campos 2024 (2)

Campos, D. G., Fütterer, T., Gfrörer, T., Lavelle-Hill, R., Murayama, K., König, L., Hecht, M., Zitzmann, S., & Scherer, R. (2024). Screening Smarter, Not Harder: A Comparative Analysis of Machine Learning Screening Algorithms and Heuristic Stopping Criteria for Systematic Reviews in Educational Research. Educational Psychology Review. https://doi.org/10.1007/s10648-024-09862-5

`q2 · i?` · `causal · r2`

Same data-driven stopping simulation (Table 5). At the 7% criterion, mean specificity corresponded to 38% (SD = 27%) of irrelevant abstracts not screened and mean ETS of 1.04 days (SD = 1.47).

> "This means that, on average, the reviewer would not have to classify 38% (SD = 27%) of the irrelevant abstracts in an abstract collection, resulting in an estimated time saving of 1.04 (SD = 1.47) days."

## Discussion


## Related Claims
- [A time-based stopping rule requires screening about 70% of abstracts to reach 95% sensitivity, saving on average 0.86 days](time-based-stopping-70-percent-95-sensitivity.md) — related
- [The LR+SBERT model achieved the highest specificity and estimated time savings at 95% sensitivity among the tested learning algorithms](lr-sbert-highest-specificity-screening.md) — related
- [Active learning algorithms reduce abstract-screening workload in education systematic reviews, saving on average 58% of irrelevant-record screening and 1.66 days at 95% sensitivity](ml-screening-reduces-workload-education-reviews.md) — related
- [Sensitivity under mixed stopping criteria correlated positively with collection length in some strategy groups but not others](mixed-stopping-sensitivity-correlates-with-collection-length.md) — related
