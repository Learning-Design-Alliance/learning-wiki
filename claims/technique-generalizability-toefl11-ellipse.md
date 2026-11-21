---
type: claim
title: Score Alignment and UST generalize to TOEFL11 and ELLIPSE, but LoRA slightly degrades performance on those datasets
description: Score Alignment and UST generalize to TOEFL11 and ELLIPSE, but LoRA slightly degrades performance on those datasets
id: technique-generalizability-toefl11-ellipse
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: mixed
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: hongseok-choi-2026
    resource: "https://doi.org/10.1109/ACCESS.2026.3718177"
    title: "Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177"
    author: Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: hongseok-choi-2026-2
    resource: "https://doi.org/10.1109/ACCESS.2026.3718177"
    title: "Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177"
    author: Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Score Alignment and UST generalize to TOEFL11 and ELLIPSE, but LoRA slightly degrades performance on those datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` In the 32-data setting, Score Alignment and UST improve over DualBERT on both TOEFL11 and ELLIPSE, with +SA+UST yielding the largest gains (ELLIPSE 0.484 to 0.530; TOEFL11 0.514 to 0.586). [→ Hongseok Choi 2026](#hongseok-choi-2026)
`q3 i?` Unlike on ASAP++, LoRA slightly degrades performance on TOEFL11 and ELLIPSE in both the 32-data and full-data settings. [→ Hongseok Choi 2026 (2)](#hongseok-choi-2026-2)

## Evidence

### Hongseok Choi 2026

Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177

`q3 · i?` · `causal · r2`

Evaluation on TOEFL11 and ELLIPSE (Table 8, average over ten folds, multi-prompt training); per-fold paired t-tests report +SA, +UST, and +SA+UST significantly improve over DualBERT (p < 0.05) in the 32-data setting.

> "In the 32-data setting, Score Alignment and UST improve over DualBERT on both datasets, and the +SA+UST combination yields the largest gains: the ELLIPSE trait average rises from 0.484 to 0.530 and the TOEFL11 overall score from 0.514 to 0.586."

### Hongseok Choi 2026 (2)

Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177

`q3 · i?` · `causal · r2`

The article attributes this to the multi-prompt training configuration, which cannot exploit per-trait, per-prompt loss-weight sweeping, and to homogeneous trait sets leaving little trait-specific structure for LoRA to adapt to.

> "unlike on ASAP++, LoRA slightly degrades performance on TOEFL11 and ELLIPSE in both the 32-data and full-data settings."

## Discussion


## Related Claims
- [In the 32-data setting on ASAP++, the integrated LoRA+SA+UST method reaches 91.2% of full-data performance, with statistically significant gains over DualBERT](integrated-method-32-data-asap.md) — related
- [Score Alignment applied to DualBERT outperforms previous SOTA AES models (ArTS+RMTS and SaMRL) in the full-data setting on ASAP++](score-alignment-sota-full-data-asap.md) — related
