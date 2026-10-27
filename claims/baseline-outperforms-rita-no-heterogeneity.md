---
type: claim
title: The baseline RCT-derived ATE model outperforms RITA when no heterogeneity exists and one intervention is uniformly more effective
description: The baseline RCT-derived ATE model outperforms RITA when no heterogeneity exists and one intervention is uniformly more effective
id: baseline-outperforms-rita-no-heterogeneity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: ilja-cornelisz-and-chris-van-klaveren-2022
    resource: "https://doi.org/10.1038/s41539-021-00117-4"
    title: "Ilja Cornelisz and Chris van Klaveren. (2022). Recurrent individual treatment assignment: a treatment policy approach to account for heterogeneous treatment effects. npj Science of Learning 7:3. https://doi.org/10.1038/s41539-021-00117-4"
    author: Ilja Cornelisz and Chris van Klaveren
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The baseline RCT-derived ATE model outperforms RITA when no heterogeneity exists and one intervention is uniformly more effective

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In World 1 (no heterogeneous treatment effects, intervention A more effective by 0.2), the baseline model reacts optimally in the first period and outperforms RITA, which incurs a median loss of -1.00 due to exploration. [→ Ilja Cornelisz and Chris van Klaveren 2022](#ilja-cornelisz-and-chris-van-klaveren-2022)

## Evidence

### Ilja Cornelisz and Chris van Klaveren 2022

Ilja Cornelisz and Chris van Klaveren. (2022). Recurrent individual treatment assignment: a treatment policy approach to account for heterogeneous treatment effects. npj Science of Learning 7:3. https://doi.org/10.1038/s41539-021-00117-4

`q2 · i?` · `design · r2`

Simulation result for World 1 (constant treatment effects, no heterogeneity). Under RITA, the median individual loss is -1.00, meaning the typical individual was assigned the wrong intervention 5 times in 60 periods due to exploration.

> "overall outcomes are generally small, with a median loss of −1.00, indicating that the typical individual has been assigned the wrong intervention — here intervention B— 5 times in the total sequence of 60 periods."

## Discussion


## Related Claims
- [RITA outperforms an RCT-derived ATE baseline in simulated worlds with heterogeneous treatment effects](rita-outperforms-rct-baseline-under-heterogeneity.md) — possibly the same claim (merge candidate)
- [RITA can account for unobserved heterogeneity in treatment effects, while existing frequentist and bandit approaches can only address observed heterogeneity](rita-handles-unobserved-heterogeneity.md) — related
