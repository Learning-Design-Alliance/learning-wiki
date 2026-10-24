---
type: claim
title: Demographic MAE-gap regularization reduces targeted subgroup gaps on validation data, but these fairness gains do not consistently transfer to held-out test subjects
description: Demographic MAE-gap regularization reduces targeted subgroup gaps on validation data, but these fairness gains do not consistently transfer to held-out test subjects
id: mae-gap-regularization-validation-gains-do-not-generalize
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: christoforos-fragkiadakis-2026
    resource: "https://doi.org/10.48550/arxiv.2609.02232"
    title: "Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag. (2026). Fairness-Aware Multimodal Transformer Modeling for Real-Time Student Attention Estimation. https://arxiv.org/abs/2609.02232 [doi:10.48550/arxiv.2609.02232](https://doi.org/10.48550/arxiv.2609.02232)"
    author: Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: christoforos-fragkiadakis-2026-2
    resource: "https://arxiv.org/abs/2609.02232"
    title: "Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag. (2026). Fairness-Aware Multimodal Transformer Modeling for Real-Time Student Attention Estimation. https://arxiv.org/abs/2609.02232"
    author: Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Demographic MAE-gap regularization reduces targeted subgroup gaps on validation data, but these fairness gains do not consistently transfer to held-out test subjects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Gender-regularized training (λ=0.7) reduced the validation gender MAE gap from 0.02 to 0.005, but on the test set both the gender gap and worst-group MAE increased, and the gap was reduced in only 4 of 10 runs. [→ Christoforos Fragkiadakis 2026](#christoforos-fragkiadakis-2026)
`q2 i?` Age-regularized training (λ=0.8) reduced the validation age MAE gap from 0.105 to 0.093 and worst-group MAE from 0.352 to 0.345, but on the test set overall performance and demographic disparities worsened relative to the unregularized model. [→ Christoforos Fragkiadakis 2026 (2)](#christoforos-fragkiadakis-2026-2)

## Evidence

### Christoforos Fragkiadakis 2026

Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag. (2026). Fairness-Aware Multimodal Transformer Modeling for Real-Time Student Attention Estimation. https://arxiv.org/abs/2609.02232 [doi:10.48550/arxiv.2609.02232](https://doi.org/10.48550/arxiv.2609.02232)

`q2 · i?` · `causal · r2`

Gender MAE-gap regularized Residual Fusion Transformer (λ=0.7) versus unregularized baseline, each across 10 seeds (Table 5). On test, the regularized model showed MAE 0.288 and gender gap 0.022 versus 0.283 and 0.015 unregularized.

> "During validation, this configuration reduced the gender MAE gap from 0.02 to 0.005, while also slightly improving worst-group MAE, with a very small trade-off in overall predictive performance. However, these improvements did not generalize to the held-out test subjects."

### Christoforos Fragkiadakis 2026 (2)

Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag. (2026). Fairness-Aware Multimodal Transformer Modeling for Real-Time Student Attention Estimation. https://arxiv.org/abs/2609.02232

`q2 · i?` · `design · r2`

Age MAE-gap regularized model (λ=0.8) versus unregularized baseline across 10 seeds (Table 6). On test, the regularized model showed MAE 0.292 and age gap 0.150 versus 0.283 and 0.126 unregularized.

> "During validation, the age-regularized model reduced the age MAE gap from 0.105 to 0.093 and improved worst-group performance from 0.352 to 0.345, while incurring only a minor increase in overall MAE. However, these improvements did not generalize to unseen data."

## Discussion


## Related Claims
- [The Residual Fusion Transformer shows the lowest worst-group MAE and smallest gender gap among baselines, while the Sensor GRU shows the smallest age gap alongside the weakest overall performance](fusion-transformer-lowest-worst-group-mae-smallest-gender-gap.md) — related
- [Repeated subject-level split experiments confirm that validation-level fairness improvements from MAE-gap regularization do not correspond to consistent generalization to unseen subjects](repeated-subject-splits-confirm-fairness-non-generalization.md) — possibly the same claim (merge candidate)
- [Facial visual dynamics provide the most informative cues for attention estimation: the Visual GRU outperforms both the train-mean baseline and the Sensor GRU](visual-gru-outperforms-sensor-gru-attention-estimation.md) — related
