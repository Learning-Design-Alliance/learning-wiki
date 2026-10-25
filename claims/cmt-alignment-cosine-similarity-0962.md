---
type: claim
title: "The system's generated practice trajectories align with learner skill levels at a peak cosine similarity of 0.962 ± 0.014 at the primary difficulty level"
description: "The system's generated practice trajectories align with learner skill levels at a peak cosine similarity of 0.962 ± 0.014 at the primary difficulty level"
id: cmt-alignment-cosine-similarity-0962
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: zhu-z-2026
    title: Zhu Z 2026
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# The system's generated practice trajectories align with learner skill levels at a peak cosine similarity of 0.962 ± 0.014 at the primary difficulty level

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Design limits** · Zhu Z 2026: no comparison group (read from the study by two models, 2026-10-25)

## Subclaims
`q2 i?` Peak cosine similarity between generated practice trajectory and learner skill level at the primary difficulty level was 0.962 ± 0.014. [→ Zhu Z 2026](#zhu-z-2026)

## Evidence

### Zhu Z 2026

Zhu Z, Luo C and Li L (2026) Adaptive teaching assistance model combining generative AI and big data analytics. Front. Psychol. 17:1844703. https://doi.org/10.3389/fpsyg.2026.1844703

`q2 · i?` · `causal · r1`

Technical validation of the model's alignment performance, reported as a mean ± SD metric for the generated practice trajectory against learner skill level. The article reports the "peak cosine similarity" reached "0.962 ± 0.014" at the primary difficulty level; no effect size is printed for this metric.

> "the peak cosine similarity between the generated practice trajectory and the skill level of learners at the primary difficulty level was 0.962 ± 0.014"

## Discussion


## Related Claims
- [In pairwise WD analyses, learner trajectory similarity dominates variation in percentage-overlap values (57.90% of variation) while remaining design factors are essentially zero](trajectory-similarity-dominates-wd-pair-overlap.md) — related
- [In simulated epistemic games, the weighted density statistic distinguishes simulated learner types with distinct mastery trajectories, with the expert trajectory showing the largest WD values](wd-detects-simulated-learner-trajectory-differences.md) — related
- [In the simulation, task complexity and task difficulty explain the majority of variance in the individual-learner WD statistic, with some effect of task specificity](task-complexity-and-difficulty-dominate-wd-variance.md) — related
