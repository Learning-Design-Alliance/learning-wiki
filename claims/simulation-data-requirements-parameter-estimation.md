---
type: claim
title: Simulated-data study shows difficulty and skill are estimated from few data, while discrimination and variance require far more (at least 30 solvers; 50 problems and 150 students)
description: Simulated-data study shows difficulty and skill are estimated from few data, while discrimination and variance require far more (at least 30 solvers; 50 problems and 150 students)
id: simulation-data-requirements-parameter-estimation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2015
recheck_by: 2018
sources:
  - id: pelánek-2015
    resource: "https://doi.org/10.1007/s40593-015-0048-x"
    title: "Pelánek, R., & Jarušek, P. (2015). Student Modeling Based on Problem Solving Times. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0048-x"
    author: "Pelánek, R., & Jarušek, P."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Simulated-data study shows difficulty and skill are estimated from few data, while discrimination and variance require far more (at least 30 solvers; 50 problems and 150 students)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2015 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2018**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Basic difficulty b and student skill θ are estimated well from relatively few data, but estimating discrimination a needs data from at least 30 solvers and variance parameters need data from at least 50 problems and 150 students. [→ Pelánek 2015](#pelanek-2015)

## Evidence

### Pelánek 2015

Pelánek, R., & Jarušek, P. (2015). Student Modeling Based on Problem Solving Times. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0048-x

`q1 · i?` · `design · r2`

Numerical simulation with data generated to match Problem Solving Tutor meta-parameters (skill SD 0.7, difficulty mean 7); Fig. 5 reports Spearman correlations between true and estimated parameters averaged over 10 runs. "to get a good estimate we need data from at least 30 solvers".

> "Estimating problem discrimination a is more difficult – to get a good estimate we need data from at least 30 solvers and even with more data the further improvement of the estimates is slow."

## Discussion


## Related Claims
- [Estimated parameters show lower-skill students have more variable performance (correlations typically from r = -0.2 to r = -0.4) and harder problems are more discriminating (r = 0.17)](parameter-correlations-skill-variability-difficulty-discrimination.md) — related
- [The general polytomous testlet model recovers true item parameters well in simulation, with average correlations of 0.9680, 0.8608, and 0.9982 for discrimination and difficulty parameters](polytomous-testlet-model-good-parameter-recovery.md) — related
- [Discrimination parameter recovery is weak (Pearson 0.31 for Qwen3.5-9B, below MathBERT's 0.35), with slope information partially lost through ability discretization](weak-discrimination-parameter-recovery.md) — related
