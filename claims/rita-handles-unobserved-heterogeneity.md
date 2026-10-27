---
type: claim
title: RITA can account for unobserved heterogeneity in treatment effects, while existing frequentist and bandit approaches can only address observed heterogeneity
description: RITA can account for unobserved heterogeneity in treatment effects, while existing frequentist and bandit approaches can only address observed heterogeneity
id: rita-handles-unobserved-heterogeneity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
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

# RITA can account for unobserved heterogeneity in treatment effects, while existing frequentist and bandit approaches can only address observed heterogeneity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The article argues that when heterogeneity is unobserved, no interaction term can be added and no assignment probability can be updated conditionally on an observable, implying RITA outperforms all other models in that scenario. [→ Ilja Cornelisz and Chris van Klaveren 2022](#ilja-cornelisz-and-chris-van-klaveren-2022)

## Evidence

### Ilja Cornelisz and Chris van Klaveren 2022

Ilja Cornelisz and Chris van Klaveren. (2022). Recurrent individual treatment assignment: a treatment policy approach to account for heterogeneous treatment effects. npj Science of Learning 7:3. https://doi.org/10.1038/s41539-021-00117-4

`q2 · i?` · `design · r2`

Theoretical argument in the 'Comparing RITA with more advanced models' section. The authors reason that frequentist interaction models and Bayesian/bandit approaches both condition on observed characteristics and therefore cannot address unobserved heterogeneity.

> "If we would assume that there is only unobserved heterogeneity, then no interaction can be added, and no treatment assignment probability can be updated conditionally on an observable. It implies that RITA outperforms all other models as it is the only model that can handle unobserved heterogeneity."

## Discussion


## Related Claims
- [RITA's advantage is largest when two interventions have equal ATEs but large unobserved individual differences in relative effectiveness (World 4)](rita-largest-advantage-ate-equivalence-world4.md) — a narrower finding that bears on this claim
- [The baseline RCT-derived ATE model outperforms RITA when no heterogeneity exists and one intervention is uniformly more effective](baseline-outperforms-rita-no-heterogeneity.md) — related
- [RITA outperforms an RCT-derived ATE baseline in simulated worlds with heterogeneous treatment effects](rita-outperforms-rct-baseline-under-heterogeneity.md) — a narrower finding that bears on this claim
- [RITA produces an asymmetry: small losses for individuals not benefiting from exploration are offset by large gains for those who do](rita-asymmetry-losses-offset-by-gains.md) — related
- [Bayesian adaptive design benefits study subjects by allocating them to more effective treatment arms](bayesian-adaptive-benefits-study-subjects.md) — related
