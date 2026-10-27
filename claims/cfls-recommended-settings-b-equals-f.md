---
type: claim
title: "Recommended CFLS settings: b=f with b scaled to aptitude level (1, 2, or 3)"
description: "Recommended CFLS settings: b=f with b scaled to aptitude level (1, 2, or 3)"
id: cfls-recommended-settings-b-equals-f
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2020
sources:
  - id: stephanie-frost-gord-mccalla-2020
    resource: "https://doi.org/10.1007/s40593-020-00221-3"
    title: "Stephanie Frost · Gord McCalla. (2020). A Planning Algorithm to Support Learning in Open-ended, Unstructured Environments. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00221-3"
    author: Stephanie Frost · Gord McCalla
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Recommended CFLS settings: b=f with b scaled to aptitude level (1, 2, or 3)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Based on the simulation results, the recommended CFLS planner settings are b=1, f=1 for low aptitude; b=1, f=2 for medium; b=3, f=3 for high aptitude — or simply b=f with b=1, 2, or 3 respectively. [→ Stephanie Frost · Gord McCalla 2020](#stephanie-frost-gord-mccalla-2020)

## Evidence

### Stephanie Frost · Gord McCalla 2020

Stephanie Frost · Gord McCalla. (2020). A Planning Algorithm to Support Learning in Open-ended, Unstructured Environments. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00221-3

`q2 · i?` · `causal · r2`

Simulation-based recommendation derived from comparing CFLS heatmap results against the SPP baseline. A simpler near-equivalent metric is b=f with b scaled to aptitude, suggesting that sequence length for planning guides how long the learner should follow the plan, with longer sequences useful for 'better' learners.

> "the recommendation would be for the CFLS planner to use b = 1,f = 1 for low aptitude learners, b = 1,f = 2 for medium aptitude learners, and b = 3,f = 3 for high aptitude learners"

## Discussion


## Learner Variables
- [General Cognitive Ability](../learner-variables/general-cognitive-ability.md) — moderator: an instructional effect differs with it

## Related Claims
- [A diagonal b ≤ f pattern in the CFLS parameter space predicts better learning outcomes](cfls-diagonal-bf-pattern-better-outcomes.md) — related
- [Optimal CFLS b and f settings vary by learner aptitude: higher aptitude benefits from larger values](cfls-optimal-bf-vary-by-aptitude.md) — possibly the same claim (merge candidate)
- [CFLS planner outperforms the Random planner at nearly all b and f settings](cfls-outperforms-random-planner.md) — related
- [CFLS planner outperforms the SPP for medium and high aptitude learners within the success triangle despite lacking prerequisite knowledge](cfls-outperforms-spp-medium-high-aptitude.md) — related
