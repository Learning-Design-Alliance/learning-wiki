---
type: claim
title: "The LR+SBERT model achieved the highest specificity and estimated time savings at 95% sensitivity among the tested learning algorithms"
description: "The LR+SBERT model achieved the highest specificity and estimated time savings at 95% sensitivity among the tested learning algorithms"
id: lr-sbert-highest-specificity-screening
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
---

# The LR+SBERT model achieved the highest specificity and estimated time savings at 95% sensitivity among the tested learning algorithms

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` LR+SBERT outperformed the other nine tested algorithms, allowing reviewers to locate 95% of relevant studies without screening 65% (SD = 18%) of irrelevant abstracts, saving 1.80 days on average. [→ Campos 2024](#campos-2024)

## Evidence

### Campos 2024

Campos, D. G., Fütterer, T., Gfrörer, T., Lavelle-Hill, R., Murayama, K., König, L., Hecht, M., Zitzmann, S., & Scherer, R. (2024). Screening Smarter, Not Harder: A Comparative Analysis of Machine Learning Screening Algorithms and Heuristic Stopping Criteria for Systematic Reviews in Educational Research. Educational Psychology Review. https://doi.org/10.1007/s10648-024-09862-5

`q2 · i?` · `causal · r2`

Simulation comparison of ten learning algorithms across 27 abstract collections at 95% sensitivity. LR+SBERT reached "the highest specificity and estimated time savings", with mean ETS of 1.80 days (SD = 1.94); the lowest was SVM+Doc2Vec at 53% specificity.

> "The model with the highest specificity and estimated time savings was the LR+SBERT model. Using this model, a reviewer could, on average, locate 95% of all relevant studies in an abstract collection without having to screen 65% (SD = 18%) of the irrelevant abstracts."

## Discussion


## Related Claims
- [A data-driven stopping rule needs about 7% consecutive irrelevant abstracts to reach 95% sensitivity, saving on average 1.04 days](data-driven-stopping-7-percent-consecutive-irrelevant.md) — related
- [Active learning algorithms reduce abstract-screening workload in education systematic reviews, saving on average 58% of irrelevant-record screening and 1.66 days at 95% sensitivity](ml-screening-reduces-workload-education-reviews.md) — a broader claim this one bears on
- [A time-based stopping rule requires screening about 70% of abstracts to reach 95% sensitivity, saving on average 0.86 days](time-based-stopping-70-percent-95-sensitivity.md) — related
- [Sensitivity under mixed stopping criteria correlated positively with collection length in some strategy groups but not others](mixed-stopping-sensitivity-correlates-with-collection-length.md) — related
