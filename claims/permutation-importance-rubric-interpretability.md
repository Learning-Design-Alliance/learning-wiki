---
type: claim
title: Permutation importance analysis identifies which writing features drive each rubric scoring model, supporting interpretability of the deep learning black box
description: Permutation importance analysis identifies which writing features drive each rubric scoring model, supporting interpretability of the deep learning black box
id: permutation-importance-rubric-interpretability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: kumar-2020
    resource: "https://doi.org/10.1007/s40593-020-00211-5"
    title: "Kumar, V. S., & Boulanger, D. (2020). Automated Essay Scoring and the Deep Learning Black Box: How Are Rubric Scores Determined? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00211-5"
    author: "Kumar, V. S., & Boulanger, D."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Permutation importance analysis identifies which writing features drive each rubric scoring model, supporting interpretability of the deep learning black box

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Permutation importance was applied to rank writing features by their average impact on exact-match accuracy for each trained rubric model, exposing the linguistic basis of rubric score predictions. [→ Kumar 2020](#kumar-2020)

## Evidence

### Kumar 2020

Kumar, V. S., & Boulanger, D. (2020). Automated Essay Scoring and the Deep Learning Black Box: How Are Rubric Scores Determined? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00211-5

`q2 · i?` · `design · r2`

Methodological/interpretive step in the Results section: five randomized permutations per feature were run on the testing set, and features were ranked by average impact on exact-match percentage with standard deviations, per rubric model.

> "A technique called permutation importance (Breiman 2001) randomizes the values of a feature in the testing set multiple times, one feature at a time, measures the average change (called the weight) in the model's predictive power (e.g., percentage of accurate predictions), and ranks features by weight in descending order."

## Discussion


## Related Claims
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — a broader claim this one bears on
- [MetaForest identifies worked-out examples, intervention duration, intervention condition, learning outcome type, and immediate measurement as the most important moderators](metaforest-top-moderators-its-effects.md) — related
