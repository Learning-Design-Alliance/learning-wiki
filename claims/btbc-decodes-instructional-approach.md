---
type: claim
title: Directional leader–follower BtBC patterns decode instructional approach better than individual motion, with peak performance at non-zero time lags
description: Directional leader–follower BtBC patterns decode instructional approach better than individual motion, with peak performance at non-zero time lags
id: btbc-decodes-instructional-approach
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: yafeng-pan-2022
    resource: "https://doi.org/10.1038/s41539-022-00131-0"
    title: "Yafeng Pan, Suzanne Dikker, Yi Zhu, Cuirong Yang, Yi Hu and Pavel Goldstein. (2022). Instructor-learner body coupling reflects instruction and learning. npj Science of Learning. https://doi.org/10.1038/s41539-022-00131-0"
    author: Yafeng Pan, Suzanne Dikker, Yi Zhu, Cuirong Yang, Yi Hu and Pavel Goldstein
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Directional leader–follower BtBC patterns decode instructional approach better than individual motion, with peak performance at non-zero time lags

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Logistic regression decoded scaffolding vs explanation from time-lagged BtBC, peaking at AUC 0.79 for learner-leading (2.68 s) and instructor-leading (2.32 s) lags; individual motion failed (AUC = 0.62, p = 0.13). [→ Yafeng Pan 2022](#yafeng-pan-2022)

## Evidence

### Yafeng Pan 2022

Yafeng Pan, Suzanne Dikker, Yi Zhu, Cuirong Yang, Yi Hu and Pavel Goldstein. (2022). Instructor-learner body coupling reflects instruction and learning. npj Science of Learning. https://doi.org/10.1038/s41539-022-00131-0

`q2 · i?` · `causal · r2`

Logistic-regression decoding with FDR-corrected permutation tests at 251 lags; both leader–follower directions significantly predicted the instructional approach (FDR corrected ps < 0.05). Individual motion energy "as the classification feature was insufficient to discriminate between scaffolding and explanation approaches".

> "reached the highest level when the learners' body motion preceded that of the instructors by 2.68 s (AUC = 0.79, p = 6.92 * 10−4), and when the instructors' body motion preceded that of the learners by 2.32 s (AUC = 0.79, p = 6.59 * 10−4)"

## Discussion


## Related Claims
- [Learner-leading BtBC is larger under scaffolding; instructor-leading BtBC shows only a trending effect, and instructor-leading BtBC fails to predict learning under explanation](directional-btbc-exploratory-findings.md) — related
- [Instructor motion is positively associated with BtBC only during scaffolding, not explanation](instructor-motion-btbc-scaffolding-only.md) — related
- [Body-to-body coupling between instructor and learner is greater during scaffolding than explanation instruction](btbc-greater-scaffolding-than-explanation.md) — related
- [Learning outcome can be predicted from overall BtBC via support vector regression](btbc-predicts-learning-outcome.md) — related
- [Instructors moved more when using an explanation approach than a scaffolding approach, but dyad and learner motion did not differ between approaches](instructor-motion-greater-explanation.md) — related
- [Learners acquire concepts better under a scaffolding approach than an explanation approach](scaffolding-beats-explanation-concept-learning.md) — related
