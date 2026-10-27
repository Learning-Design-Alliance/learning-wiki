---
type: claim
title: "RITA's advantage is largest when two interventions have equal ATEs but large unobserved individual differences in relative effectiveness (World 4)"
description: "RITA's advantage is largest when two interventions have equal ATEs but large unobserved individual differences in relative effectiveness (World 4)"
id: rita-largest-advantage-ate-equivalence-world4
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

# RITA's advantage is largest when two interventions have equal ATEs but large unobserved individual differences in relative effectiveness (World 4)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In World 4, where both interventions have the same ATE (0.8) but heterogeneous individual responses, RITA's cumulative gain advantage over the baseline averages 11.45 (SD = 21.08). [→ Ilja Cornelisz and Chris van Klaveren 2022](#ilja-cornelisz-and-chris-van-klaveren-2022)

## Evidence

### Ilja Cornelisz and Chris van Klaveren 2022

Ilja Cornelisz and Chris van Klaveren. (2022). Recurrent individual treatment assignment: a treatment policy approach to account for heterogeneous treatment effects. npj Science of Learning 7:3. https://doi.org/10.1038/s41539-021-00117-4

`q2 · i?` · `design · r2`

Simulation result from World 4 (ATE equivalence with unobserved heterogeneity, 60 periods, 1000 individuals). RITA's average cumulative gain advantage over the baseline model is 11.45 (SD = 21.08), the largest across the four worlds.

> "In World 4, when only observing ATE is no longer informative for individual treatment assignment, the relative performance of RITA is even better. The increase in cumulative gains in World 4 by applying RITA -instead of the baseline model approach- is on average 11.45 (SD = 21.08)."

## Discussion


## Related Claims
- [RITA produces an asymmetry: small losses for individuals not benefiting from exploration are offset by large gains for those who do](rita-asymmetry-losses-offset-by-gains.md) — related
- [RITA can account for unobserved heterogeneity in treatment effects, while existing frequentist and bandit approaches can only address observed heterogeneity](rita-handles-unobserved-heterogeneity.md) — a broader claim this one bears on
- [RITA outperforms an RCT-derived ATE baseline in simulated worlds with heterogeneous treatment effects](rita-outperforms-rct-baseline-under-heterogeneity.md) — a broader claim this one bears on
