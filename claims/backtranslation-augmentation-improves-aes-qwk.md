---
type: claim
title: "Training AES models on back-translation-augmented data improves QWK performance by 0.2% on average for both tested models"
description: "Training AES models on back-translation-augmented data improves QWK performance by 0.2% on average for both tested models"
id: backtranslation-augmentation-improves-aes-qwk
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: you-jin-jong-2022
    resource: "https://doi.org/10.1155/2022/6906587"
    title: "You-Jin Jong, Yong-Jin Kim, Ok-Chol Ri. (2022). Improving Performance of Automated Essay Scoring by using back-translation essays and adjusted scores. [doi:10.1155/2022/6906587](https://doi.org/10.1155/2022/6906587)"
    author: You-Jin Jong, Yong-Jin Kim, Ok-Chol Ri
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Training AES models on back-translation-augmented data improves QWK performance by 0.2% on average for both tested models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using back-translation essays with adjusted scores to train two neural AES models improved performance by 0.2% on average. [→ You-Jin Jong 2022](#you-jin-jong-2022)

## Evidence

### You-Jin Jong 2022

You-Jin Jong, Yong-Jin Kim, Ok-Chol Ri. (2022). Improving Performance of Automated Essay Scoring by using back-translation essays and adjusted scores. [doi:10.1155/2022/6906587](https://doi.org/10.1155/2022/6906587)

`q2 · i?` · `design · r2`

Numerical evaluation (Tables 4-6) training 'Manipulating-Length-GRU' and 'Considering-Content-LSTM' models on original plus augmented ASAP data, evaluated with QWK under cross-validation. The article reports "The performance was improved by 0.2% on average"; no effect size or significance test is printed.

> "The performance was improved by 0.2% on average for both models using the augmented data."

## Discussion


## Related Claims
- [In the Overview dimension, augmentation produced a marginal QWK decrease (ΔQWK = −0.006) despite improving macro-F1, the only dimension with this trade-off](overview-augmentation-qwk-tradeoff.md) — related
- [Data augmentation was critical for ordinal discriminability, with QWK dropping to near-zero without it in the Focus dimension and gains up to +0.346 in severely imbalanced dimensions](augmentation-critical-ordinal-qwk-gains.md) — related
- [For large score-range prompts, raising scores of high-score back-translation essays (Equation 4) outperforms keeping original scores](equation4-score-adjustment-large-range-prompts.md) — related
- [For prompts with a small score range, keeping the original essay score for back-translation essays is effective, but prompt 1 did not improve](small-score-range-keep-original-scores.md) — a narrower finding that bears on this claim
