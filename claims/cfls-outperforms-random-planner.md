---
type: claim
title: CFLS planner outperforms the Random planner at nearly all b and f settings
description: CFLS planner outperforms the Random planner at nearly all b and f settings
id: cfls-outperforms-random-planner
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
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

# CFLS planner outperforms the Random planner at nearly all b and f settings

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the simulation comparison, the CFLS planner outperformed the Random planner on both coverage and expertise for all but one b,f setting; the exception was b=2, f=1 for low aptitude learners where it was marginally worse. [→ Stephanie Frost · Gord McCalla 2020](#stephanie-frost-gord-mccalla-2020)

## Evidence

### Stephanie Frost · Gord McCalla 2020

Stephanie Frost · Gord McCalla. (2020). A Planning Algorithm to Support Learning in Open-ended, Unstructured Environments. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00221-3

`q2 · i?` · `causal · r2`

Comparison of the CFLS planner against the Random baseline planner across the b,f heatmap cells. Random planner baselines: 26–29.2% average coverage and 0.107–0.235 average expertise by aptitude group. The one exception was b=2, f=1 for low aptitude learners, where CFLS was marginally worse on both measures.

> "For all but one setting of b and f, the CFLS planner readily outperforms Random on both coverage and expertise measures."

## Discussion


## Related Claims
- [CFLS planner outperforms the SPP for medium and high aptitude learners within the success triangle despite lacking prerequisite knowledge](cfls-outperforms-spp-medium-high-aptitude.md) — related
- [Recommended CFLS settings: b=f with b scaled to aptitude level (1, 2, or 3)](cfls-recommended-settings-b-equals-f.md) — related
- [A diagonal b ≤ f pattern in the CFLS parameter space predicts better learning outcomes](cfls-diagonal-bf-pattern-better-outcomes.md) — related
- [Optimal CFLS b and f settings vary by learner aptitude: higher aptitude benefits from larger values](cfls-optimal-bf-vary-by-aptitude.md) — related
- [The introduction reports that in a simulation study the CFLS planner, relying only on inferred learner behaviour, worked highly effectively even compared to a planner using external prerequisite metadata](cfls-planner-effective-without-external-metadata.md) — related
