---
type: claim
title: "The proposed Transformer-based framework achieved first place in the EDM Cup 2023 with an AUC of 78.969% on the private evaluation dataset"
description: "The proposed Transformer-based framework achieved first place in the EDM Cup 2023 with an AUC of 78.969% on the private evaluation dataset"
id: transformer-kt-first-place-edm-cup-2023
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: lu-2024
    resource: "https://doi.org/10.31219/osf.io/3k7z2"
    title: "Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/ [doi:10.31219/osf.io/3k7z2](https://doi.org/10.31219/osf.io/3k7z2)"
    author: "Lu, Y., Tong, L., & Cheng, Y."
    q: 3
    i: 2
    kind: design
    rigour: 2
---

# The proposed Transformer-based framework achieved first place in the EDM Cup 2023 with an AUC of 78.969% on the private evaluation dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3` · `i2` medium
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q3 i?` The framework won first place on the EDM Cup 2023 private leaderboard with a private AUC of 78.969% for predicting end-of-unit test performance. [→ Lu 2024](#lu-2024)

## Evidence

### Lu 2024

Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/ [doi:10.31219/osf.io/3k7z2](https://doi.org/10.31219/osf.io/3k7z2)

`q3 · i2` · `design · r2`

Contest evaluation on the held-out private ASSISTments evaluation set, with predictions scored by AUC on Kaggle. The article reports "the first-place position in the contest with an AUC of 78.969% for the private dataset" and notes overall best performance across public and private leaderboards.

> "Our model has the best prediction accuracy, as exemplified by the first-place position in the contest with an AUC of 78.969% for the private dataset."

## Discussion

## Related Claims

- [The survey states that deep learning knowledge tracing models exhibit superior performance to Bayesian and logistic models but have significant room for improvement in interpretability.](deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability.md) — the general claim this finding bears on, with the studies behind it

- [Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models](learner-models-miscalibrated-outside-data-interval.md) — the general claim this finding bears on, with the studies behind it
- [The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture](model1-outperforms-complex-model2.md) — related
- [Rank-averaged ensembling stabilized predictions but did not outperform the single base model](ensemble-stabilizes-but-not-better-than-model1.md) — related
- Replacing the transformer with a single-layer 2048-unit LSTM drops the average score by 5.6, with the LSTM winning only on MRPC — related
- [Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs](ablation-all-features-maximize-auc.md) — related
