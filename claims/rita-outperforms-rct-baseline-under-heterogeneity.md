---
type: claim
title: RITA outperforms an RCT-derived ATE baseline in simulated worlds with heterogeneous treatment effects
description: RITA outperforms an RCT-derived ATE baseline in simulated worlds with heterogeneous treatment effects
id: rita-outperforms-rct-baseline-under-heterogeneity
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

# RITA outperforms an RCT-derived ATE baseline in simulated worlds with heterogeneous treatment effects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In multi-period simulations across four worlds, RITA achieves better average cumulative outcome gains than a baseline model assigning individuals based on RCT-derived ATEs in Worlds 2–4 (where heterogeneous treatment effects exist), but not in World 1 (no heterogeneity). [→ Ilja Cornelisz and Chris van Klaveren 2022](#ilja-cornelisz-and-chris-van-klaveren-2022)

## Evidence

### Ilja Cornelisz and Chris van Klaveren 2022

Ilja Cornelisz and Chris van Klaveren. (2022). Recurrent individual treatment assignment: a treatment policy approach to account for heterogeneous treatment effects. npj Science of Learning 7:3. https://doi.org/10.1038/s41539-021-00117-4

`q2 · i?` · `design · r2`

Multi-period simulation (60 periods, 1000 individuals) comparing RITA to an RCT-derived ATE baseline across four treatment-effect worlds. Simulation results show RITA performs better than the baseline model in all worlds except World 1, which lacks heterogeneity.

> "Figure 4 visualizes the average cumulative outcome gains over periods for both assignment strategies. These results indicate that RITA performs better than the baseline model in all worlds, except in World 1."

## Discussion


## Related Claims
- [The baseline RCT-derived ATE model outperforms RITA when no heterogeneity exists and one intervention is uniformly more effective](baseline-outperforms-rita-no-heterogeneity.md) — possibly the same claim (merge candidate)
- [RITA produces an asymmetry: small losses for individuals not benefiting from exploration are offset by large gains for those who do](rita-asymmetry-losses-offset-by-gains.md) — a narrower finding that bears on this claim
- [RITA can account for unobserved heterogeneity in treatment effects, while existing frequentist and bandit approaches can only address observed heterogeneity](rita-handles-unobserved-heterogeneity.md) — a broader claim this one bears on
- [RITA's advantage is largest when two interventions have equal ATEs but large unobserved individual differences in relative effectiveness (World 4)](rita-largest-advantage-ate-equivalence-world4.md) — a narrower finding that bears on this claim
