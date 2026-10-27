---
type: claim
title: "RITA produces an asymmetry: small losses for individuals not benefiting from exploration are offset by large gains for those who do"
description: "RITA produces an asymmetry: small losses for individuals not benefiting from exploration are offset by large gains for those who do"
id: rita-asymmetry-losses-offset-by-gains
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

# RITA produces an asymmetry: small losses for individuals not benefiting from exploration are offset by large gains for those who do

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In World 4, individuals for whom intervention A is better (n = 520) experience a median loss of -0.71 over 60 periods under RITA, while individuals for whom intervention B is better (n = 480) experience a median gain of 21.91. [→ Ilja Cornelisz and Chris van Klaveren 2022](#ilja-cornelisz-and-chris-van-klaveren-2022)

## Evidence

### Ilja Cornelisz and Chris van Klaveren 2022

Ilja Cornelisz and Chris van Klaveren. (2022). Recurrent individual treatment assignment: a treatment policy approach to account for heterogeneous treatment effects. npj Science of Learning 7:3. https://doi.org/10.1038/s41539-021-00117-4

`q2 · i?` · `design · r2`

Individual-level simulation results in World 4, ordered by RITA rank. The 520 individuals for whom A is better show a median loss of -0.71; the 480 individuals for whom B is better show a median gain of 21.91 over 60 periods.

> "individuals ( n = 520) for whom intervention A is better to experience a small loss when RITA is applied, with a median loss of −0.71 over 60 periods. In contrast, individuals ( n = 480) for whom intervention B is better to experience a potentially huge benefit when RITA is applied, with a median gain of 21.91 over 60 periods."

## Discussion


## Related Claims
- [RITA's advantage is largest when two interventions have equal ATEs but large unobserved individual differences in relative effectiveness (World 4)](rita-largest-advantage-ate-equivalence-world4.md) — related
- [RITA outperforms an RCT-derived ATE baseline in simulated worlds with heterogeneous treatment effects](rita-outperforms-rct-baseline-under-heterogeneity.md) — a broader claim this one bears on
- [RITA can account for unobserved heterogeneity in treatment effects, while existing frequentist and bandit approaches can only address observed heterogeneity](rita-handles-unobserved-heterogeneity.md) — related
