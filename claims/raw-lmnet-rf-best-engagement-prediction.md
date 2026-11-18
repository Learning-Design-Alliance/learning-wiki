---
type: claim
title: Raw LMNET is the most predictable engagement encoding, and Random Forest with kernelised models performs best, indicating non-linearity
description: Raw LMNET is the most predictable engagement encoding, and Random Forest with kernelised models performs best, indicating non-linearity
id: raw-lmnet-rf-best-engagement-prediction
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
    kind: associational
    rigour: 2
  - id: sahan-bulathwela-2020-2
    resource: "https://doi.org/10.48550/arXiv.2006.00592"
    title: "Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)"
    author: Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Raw LMNET is the most predictable engagement encoding, and Random Forest with kernelised models performs best, indicating non-linearity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Psychometric-inspired transformations (cleaned, standardised, comparative) of the engagement signal do not improve predictive power over raw LMNET with cross-modal features. [→ Sahan Bulathwela 2020](#sahan-bulathwela-2020)
`q2 i?` Pairwise accuracy depends on the engagement gap: pairs with the largest MNET difference are predicted with 0.962 accuracy versus 0.642 for the smallest difference. [→ Sahan Bulathwela 2020 (2)](#sahan-bulathwela-2020-2)

## Evidence

### Sahan Bulathwela 2020

Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)

`q2 · i?` · `associational · r2`

5-fold cross-validation experiment (Table 2) comparing four engagement encodings across RR, SVR, KRR, KSVR and RF with cross-modal features; raw LMNET reaches the highest values (e.g. RF .723 pairwise accuracy, .625 SROCC). The authors report that "RF seems to be the best performing model providing more evidence that non-linearity plays a signiﬁcant role."

> "These results suggest that raw LMNET may be the most ap- propriate target label, particularly since the proposed fea- tures seem to be more useful when building a model for predicting raw LMNET."

### Sahan Bulathwela 2020 (2)

Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)

`q2 · i?` · `associational · r2`

Misranking analysis binning lecture pairs by MNET difference in 0.1 bins from 0 to 1 (Figure 2). Accuracy rises monotonically with the engagement gap between the two named extremes; cumulative pairwise accuracy is 0.816 when ignoring pairs with MNET difference of [0.0, 0.2].

> "the pairs with largest diﬀerence of MNET are predicted correctly with 0.962 accuracy whereas pairs with the smallest diﬀerence are predicted with 0.642 accuracy."

## Discussion


## Related Claims
- [Random forest achieves the highest mean test accuracy (0.9590) of all models compared for predicting exam grade categories from physiological signals](random-forest-highest-accuracy-physiological-exam-prediction.md) — related
- [On the CASED challenge test set, all participating engagement-prediction methods converge near random-chance performance, with the best F1 Macro at 0.52](cased-challenge-methods-near-random-chance.md) — related
- [Engagement, number of views and star ratings carry very different information, with near-zero correlation between engagement and ratings](engagement-decoupled-from-views-and-ratings.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — related
- [Adding video-specific features improves pairwise accuracy by approximately 2%, and subject-specific comparison is easier than subject-agnostic](video-features-add-two-percent-accuracy.md) — related
