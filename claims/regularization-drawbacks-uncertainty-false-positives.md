---
type: claim
title: Regularization-based graphical modeling has key drawbacks, including difficulty obtaining valid parameter uncertainty and inflated false positive rates
description: Regularization-based graphical modeling has key drawbacks, including difficulty obtaining valid parameter uncertainty and inflated false positive rates
id: regularization-drawbacks-uncertainty-false-positives
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: weak
sources:
  - id: donald-williams-2021
    resource: "https://doi.org/10.21105/joss.03308"
    title: "Donald Williams. (2021). GGMnonreg: Non-regularized Gaussian graphical models in R. Journal of Open Source Software, 6(67), 3308. https://doi.org/10.21105/joss.03308"
    author: Donald Williams
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# Regularization-based graphical modeling has key drawbacks, including difficulty obtaining valid parameter uncertainty and inflated false positive rates

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q1`

## Subclaims
`q1 i?` Obtaining a valid measure of parameter uncertainty is very difficult with regularization-based graphical modeling. [→ Donald Williams 2021](#donald-williams-2021)
`q1 i?` Regularization can produce an inflated false positive rate in graphical modeling. [→ Donald Williams 2021](#donald-williams-2021)

## Evidence

### Donald Williams 2021

Donald Williams. (2021). GGMnonreg: Non-regularized Gaussian graphical models in R. Journal of Open Source Software, 6(67), 3308. https://doi.org/10.21105/joss.03308

`q1 · i?` · `design · r1`

The article asserts, citing prior literature (Bühlmann et al., 2014; Donald R. Williams et al., 2019), that "there can be an inflated false positive rate" and that valid parameter uncertainty is very difficult to obtain under regularization. No new empirical test of these drawbacks is reported in this article.

> "There are key drawbacks of regularization, including, but not limited to, the fact that obtaining a valid measure of parameter uncertainty is very (very) difficult (Bühlmann et al., 2014) and there can be an inflated false positive rate"

## Discussion


## Related Claims
- [The frequentist graphical LASSO has difficulty estimating centrality indices and uncertainty in these measures in symptom networks](frequentist-glasso-difficulty-uncertainty-centrality.md) — a narrower finding that bears on this claim
- [Non-regularized graphical model methods are specifically designed for low-dimensional data common in the social-behavioral sciences](ggmnonreg-designed-for-low-dimensional-data.md) — related
