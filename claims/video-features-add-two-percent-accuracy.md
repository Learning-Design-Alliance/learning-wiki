---
type: claim
title: "Adding video-specific features improves pairwise accuracy by approximately 2%, and subject-specific comparison is easier than subject-agnostic"
description: "Adding video-specific features improves pairwise accuracy by approximately 2%, and subject-specific comparison is easier than subject-agnostic"
id: video-features-add-two-percent-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: sahan-bulathwela-2020
    resource: "https://doi.org/10.48550/arXiv.2006.00592"
    title: "Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)"
    author: Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: sahan-bulathwela-2020-2
    resource: "https://doi.org/10.48550/arXiv.2006.00592"
    title: "Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)"
    author: Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Adding video-specific features improves pairwise accuracy by approximately 2%, and subject-specific comparison is easier than subject-agnostic

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For the RF model, adding video-specific features to content-based features raises pairwise accuracy by approximately 2% (e.g. .724 to .744 subject-agnostic). [→ Sahan Bulathwela 2020](#sahan-bulathwela-2020)
`q2 i?` Pairwise accuracy is higher when restricted to lecture pairs from the same subject area (.755 vs .744 with video features). [→ Sahan Bulathwela 2020 (2)](#sahan-bulathwela-2020-2)

## Evidence

### Sahan Bulathwela 2020

Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)

`q2 · i?` · `design · r2`

5-fold cross-validation experiment with the RF model (Table 3) comparing content-based features against content-based plus video-specific features. The authors note a compromise: cross-modal extractors "can be reused in a practical scenario" despite the small performance cost.

> "The addition of video fea- tures increase the performance by approximately 2%. This result shows that there is a compromise in performance when restricting features to cross-modal features although the fea- ture extractors can be reused in a practical scenario."

### Sahan Bulathwela 2020 (2)

Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)

`q2 · i?` · `design · r2`

Same Table 3 experiment comparing subject-agnostic and subject-specific pairwise accuracy columns (.744 vs .755 with video features; .724 vs .733 with content only). The authors call this clearly an advantage for recommender systems choosing among same-subject resources.

> "Table 3 shows how the pairwise accuracy increases when restricted to subject-speciﬁc comparisons (lecture pairs be-longing to the same subject area)."

## Discussion


## Related Claims
- [A common subject-agnostic engagement model can be assumed across knowledge areas, since subject-specific training does not improve accuracy](common-engagement-model-across-knowledge-areas.md) — related
- [Ranking and pairwise comparison reduce graders' cognitive load relative to numeric scoring, with limits when submissions are similar or numerous](ranking-reduces-grader-cognitive-load.md) — related
- [Raw LMNET is the most predictable engagement encoding, and Random Forest with kernelised models performs best, indicating non-linearity](raw-lmnet-rf-best-engagement-prediction.md) — related
