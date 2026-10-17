---
type: claim
title: Conventional regression models cannot consistently estimate effects of time-varying treatments when time-varying confounders are affected by past treatment
description: Conventional regression models cannot consistently estimate effects of time-varying treatments when time-varying confounders are affected by past treatment
id: regression-fails-time-varying-confounders-affected-by-treatment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-17
evidence_strength: moderate
sources:
  - id: wodtke-2011
    resource: "https://doi.org/10.1177/0003122411420816"
    title: "Wodtke, Geoffrey T.; Harding, David J.; Elwert, Felix. (2011). Neighborhood Effects in Temporal Perspective. American Sociological Review. https://doi.org/10.1177/0003122411420816"
    author: Wodtke, Geoffrey T.; Harding, David J.; Elwert, Felix
    q: 1
    i: "?"
    kind: associational
    rigour: 3
---

# Conventional regression models cannot consistently estimate effects of time-varying treatments when time-varying confounders are affected by past treatment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r3` · `q1`

## Subclaims
`q1 i?` A directed acyclic graph analysis shows regression adjustment for a time-varying confounder both removes indirect effects of past treatment (over-control) and induces collider-stratification bias. [→ Wodtke 2011](#wodtke-2011)

## Evidence

### Wodtke 2011

Wodtke, Geoffrey T.; Harding, David J.; Elwert, Felix. (2011). Neighborhood Effects in Temporal Perspective. American Sociological Review. https://doi.org/10.1177/0003122411420816

`q1 · i?` · `associational · r3`

Analytical demonstration using a two-wave directed acyclic graph (Figure 1). Conditioning on L2 removes the indirect effect of past treatment and, because L2 is a "collider" variable, creates a new biasing path between unobserved factors and prior treatment.

> "This two-wave example demonstrates that conventional regression models cannot consistently estimate the effects of a time-varying treatment when time-varying confounders are affected by past treatments, even if there is no unobserved confounding"

## Discussion


## Related Claims
- [IPT-weighted estimates of neighborhood effects on high school graduation are substantially larger than conventional regression-adjusted estimates](ipt-estimates-larger-than-regression-estimates.md) — related
- [Confounding may explain the large retention effects reported for the Course Signals early warning system](course-signals-confounding-number-of-classes.md) — related
- [Propensity score matching produced baseline-equivalent treatment and comparison groups on all measured variables](psm-baseline-equivalence-mtss-study.md) — related
