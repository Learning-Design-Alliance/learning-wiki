---
type: strategy
id: rita-caliper-oscillation-mitigation
title: Build in a caliper (minimum ranking distance) to prevent undesirable oscillating assignment behavior in RITA
description: When two interventions have approximately similar rankings for an individual, RITA may assign that person back and forth between them.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: ilja-cornelisz-and-chris-van-klaveren-2022
    resource: "https://doi.org/10.1038/s41539-021-00117-4"
    title: "Ilja Cornelisz and Chris van Klaveren. (2022). Recurrent individual treatment assignment: a treatment policy approach to account for heterogeneous treatment effects. npj Science of Learning 7:3. https://doi.org/10.1038/s41539-021-00117-4"
    author: Ilja Cornelisz and Chris van Klaveren
---

# Build in a caliper (minimum ranking distance) to prevent undesirable oscillating assignment behavior in RITA

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
When two interventions have approximately similar rankings for an individual, RITA may assign that person back and forth between them. The article proposes 'a solution within the RITA environment would be to built-in a caliper (i.e., a ranking space is defined such that switches can occur only if the ranking differs by more than, for example, a certain number), such that undesirable oscillating behavior is mitigated.' This is relevant when switching carries mental or logistical costs.

## Design Implications

### Context
#### Requirements
- RITA environment with rank-based updating
- A defined ranking-space threshold below which no switch occurs
#### Constraints
- In online adaptive practicing software or clinical medication settings, oscillation may not be problematic because the assigned intervention is not visible to the student or doctors update monthly anyway

### Target Learners
- students assigned to different learning methods
- individuals in settings with high switching costs

### Target Learning Goals
- maintaining stable intervention assignment while preserving RITA's adaptivity

## Claims

- [The baseline RCT-derived ATE model outperforms RITA when no heterogeneity exists and one intervention is uniformly more effective](../claims/baseline-outperforms-rita-no-heterogeneity.md) [+W]
- [RITA produces an asymmetry: small losses for individuals not benefiting from exploration are offset by large gains for those who do](../claims/rita-asymmetry-losses-offset-by-gains.md) [+W]
- [RITA can account for unobserved heterogeneity in treatment effects, while existing frequentist and bandit approaches can only address observed heterogeneity](../claims/rita-handles-unobserved-heterogeneity.md) [+W]
- [RITA's advantage is largest when two interventions have equal ATEs but large unobserved individual differences in relative effectiveness (World 4)](../claims/rita-largest-advantage-ate-equivalence-world4.md) [+W]
- [RITA outperforms an RCT-derived ATE baseline in simulated worlds with heterogeneous treatment effects](../claims/rita-outperforms-rct-baseline-under-heterogeneity.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Ilja Cornelisz and Chris van Klaveren. (2022). Recurrent individual treatment assignment: a treatment policy approach to account for heterogeneous treatment effects. npj Science of Learning 7:3. https://doi.org/10.1038/s41539-021-00117-4
