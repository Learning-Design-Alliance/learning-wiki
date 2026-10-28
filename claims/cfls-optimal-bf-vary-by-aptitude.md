---
type: claim
title: "Optimal CFLS b and f settings vary by learner aptitude: higher aptitude benefits from larger values"
description: "Optimal CFLS b and f settings vary by learner aptitude: higher aptitude benefits from larger values"
id: cfls-optimal-bf-vary-by-aptitude
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

# Optimal CFLS b and f settings vary by learner aptitude: higher aptitude benefits from larger values

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the simulation, low aptitude learners achieved highest expertise at b=1, f=1; medium aptitude learners at b=1 or 2, f=2; and high aptitude learners at b=3, f=3 — the higher the aptitude, the higher the optimal b and f values. [→ Stephanie Frost · Gord McCalla 2020](#stephanie-frost-gord-mccalla-2020)

## Evidence

### Stephanie Frost · Gord McCalla 2020

Stephanie Frost · Gord McCalla. (2020). A Planning Algorithm to Support Learning in Open-ended, Unstructured Environments. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00221-3

`q2 · i?` · `causal · r2`

Simulation tuning experiment across 25 b,f combinations. Expertise heatmaps showed dark red (best) cells shifting to higher b,f values as aptitude increased: b=1, f=1 for low aptitude; b=1 or 2, f=2 for medium; b=3, f=3 for high aptitude learners. The authors attribute this to lower-aptitude learners following less coherent paths, making longer neighbourhoods less useful.

> "Another general observation is that different aptitude groups found their best performance with differing values of b and f : the higher the learner's aptitude, the higher values of b and f should be used."

## Discussion


## Learner Variables
- [General Cognitive Ability](../learner-variables/general-cognitive-ability.md) — moderator: an instructional effect differs with it

## Related Claims
- [A diagonal b ≤ f pattern in the CFLS parameter space predicts better learning outcomes](cfls-diagonal-bf-pattern-better-outcomes.md) — related
- [Recommended CFLS settings: b=f with b scaled to aptitude level (1, 2, or 3)](cfls-recommended-settings-b-equals-f.md) — possibly the same claim (merge candidate)
- [Effectiveness of pedagogical tools depends on learners' initial grasp of the object of learning (aptitude–treatment interaction)](tool-effectiveness-depends-initial-grasp.md) — a broader claim this one bears on
- [In the few studies that split by ability, learning techniques helped low-ability students and not high-ability students](learning-techniques-benefit-low-ability-not-high-ability-students.md) — reports the opposite
- [Mastery learning effects are larger for lower-aptitude students, narrowing the spread of achievement in a class](mastery-learning-effects-larger-for-lower-aptitude-students.md) — reports the opposite
- [CFLS planner outperforms the Random planner at nearly all b and f settings](cfls-outperforms-random-planner.md) — related
- [CFLS planner outperforms the SPP for medium and high aptitude learners within the success triangle despite lacking prerequisite knowledge](cfls-outperforms-spp-medium-high-aptitude.md) — related
- [The introduction reports that in a simulation study the CFLS planner, relying only on inferred learner behaviour, worked highly effectively even compared to a planner using external prerequisite metadata](cfls-planner-effective-without-external-metadata.md) — related
