---
type: claim
title: Best hedge-detection performance (F1 79.0) came from LightGBM using nearly all feature groups
description: Best hedge-detection performance (F1 79.0) came from LightGBM using nearly all feature groups
id: lightgbm-all-features-best-f1-79
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: yann-raphalen-2022
    resource: "https://doi.org/10.18653/v1/2022.acl-long.153"
    title: "Yann Raphalen, Chloé Clavel, Justine Cassell. (2022). \"You might think about slightly revising the title\": Identifying Hedges in Peer-tutoring Interactions. [doi:10.18653/v1/2022.acl-long.153](https://doi.org/10.18653/v1/2022.acl-long.153)"
    author: Yann Raphalen, Chloé Clavel, Justine Cassell
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Best hedge-detection performance (F1 79.0) came from LightGBM using nearly all feature groups

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across six models on the 4-class task, the highest performance was LightGBM with almost all features, reaching a 3-class weighted F1 of 79.0. [→ Yann Raphalen 2022](#yann-raphalen-2022)

## Evidence

### Yann Raphalen 2022

Yann Raphalen, Chloé Clavel, Justine Cassell. (2022). "You might think about slightly revising the title": Identifying Hedges in Peer-tutoring Interactions. [doi:10.18653/v1/2022.acl-long.153](https://doi.org/10.18653/v1/2022.acl-long.153)

`q2 · i?` · `design · r2`

Overall model comparison across six classifiers (rule-based, MLP, LSTM, Attention-CNN, BERT, LightGBM) on the annotated peer-tutoring corpus, scored by weighted F1 for the three hedge classes and for all four classes. The article reports an "F1- score of 79.0" for the best configuration.

> "Best performance (F1- score of 79.0) is obtained with LightGBM lever- aging almost all the features."

## Discussion


## Related Claims
- [A LightGBM model with knowledge-driven rule-based features outperforms fine-tuned BERT and an Attention-CNN baseline for hedge detection in peer-tutoring conversation](lightgbm-knowledge-driven-features-beat-bert-hedge-detection.md) — possibly the same claim (merge candidate)
- [SHAP analysis identified novel features of hedge classes, including interjections associated with Apologizers and clause length as a class indicator](shap-novel-hedge-features-interjections-clause-length.md) — related
- [Fold-local top-20 feature selection had mixed effects across model families, supporting the complete 166-dimensional representation as the primary analysis](feature-selection-effects-mixed-across-families.md) — related
- [Adding n-gram features significantly improved the hedge classifier, but tutoring moves and nonverbal features did not](ngrams-help-tutoring-moves-nonverbal-do-not.md) — related
