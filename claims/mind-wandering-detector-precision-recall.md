---
type: claim
title: "SVM-based mind wandering detector achieved 69% precision and 67% recall generalizing to new learners"
description: "SVM-based mind wandering detector achieved 69% precision and 67% recall generalizing to new learners"
id: mind-wandering-detector-precision-recall
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2016
recheck_by: 2019
sources:
  - id: dmello-2016
    resource: "https://doi.org/10.1007/s40593-016-0104-1"
    title: "D’Mello, S. K. (2016). Giving Eyesight to the Blind: Towards Attention-Aware AIED. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-016-0104-1"
    author: D’Mello, S. K.
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# SVM-based mind wandering detector achieved 69% precision and 67% recall generalizing to new learners

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A support vector machine discriminated mind wandering from eye gaze with a precision of 69% and a recall of 67%, designed to generalize to new learners. [→ D’Mello 2016](#dmello-2016)

## Evidence

### D’Mello 2016

D’Mello, S. K. (2016). Giving Eyesight to the Blind: Towards Attention-Aware AIED. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-016-0104-1

`q2 · i?` · `theoretical · r3`

Data from 98 learners reading a 57-page scientific text on surface tension, tracked with a Tobii TX 300 eye tracker, trained a support vector machine to discriminate mind wandering (pages with a self-report — 32%) from normal reading. The article reports "The model had a precision of 69 % and a recall of 67 %".

> "The model had a precision of 69 % and a recall of 67 %, which we deemed to be sufficiently accurate for our purposes"

## Discussion


## Related Claims
- D'Mello proposes attention tracking and management as a new AIED research direction — a broader claim this one bears on
- [Lab-trained mind wandering detectors generalize to in-the-wild lecture viewing across task, setting, and cultural group, with BiLSTM on latent features reaching F1 = 0.352](cross-dataset-generalization-mind-wandering-detection.md) — related
