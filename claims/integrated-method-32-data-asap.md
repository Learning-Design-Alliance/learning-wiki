---
type: claim
title: "In the 32-data setting on ASAP++, the integrated LoRA+SA+UST method reaches 91.2% of full-data performance, with statistically significant gains over DualBERT"
description: "In the 32-data setting on ASAP++, the integrated LoRA+SA+UST method reaches 91.2% of full-data performance, with statistically significant gains over DualBERT"
id: integrated-method-32-data-asap
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
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
    rigour: 1
---

# In the 32-data setting on ASAP++, the integrated LoRA+SA+UST method reaches 91.2% of full-data performance, with statistically significant gains over DualBERT

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1`–`r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Training on only 32 rated essays per set, the integrated method reached QWKs of 0.639 (per-trait) and 0.653 (per-prompt), corresponding to 91.2% and 90.7% of DualBERT's full-data performance. [→ Hongseok Choi 2026](#hongseok-choi-2026)
`q3 i?` LoRA+SA+UST improves AVG QWK over DualBERT by 0.046 (per-trait) and 0.054 (per-prompt), both with p < 0.01; LoRA alone is not significant and UST alone only in the per-prompt setting. [→ Hongseok Choi 2026 (2)](#hongseok-choi-2026-2)

## Evidence

### Hongseok Choi 2026

Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177

`q3 · i?` · `causal · r2`

Ablation experiment in the 32-data setting on ASAP++ (Tables 6 and 7) applying Two-Stage fine-tuning, Score Alignment, and UST to DualBERT; total improvement averaged 4.6 (per-trait) and 5.4 (per-prompt) QWK points.

> "The final QWKs reached 0.639 for per-trait and 0.653 for per-prompt, corresponding to 91.2% and 90.7% of the full-data performance of DualBERT, i.e., 0.701 and 0.720, respectively."

### Hongseok Choi 2026 (2)

Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177

`q3 · i?` · `causal · r1`

Paired t-tests over five folds in the 32-data setting; the article attributes LoRA's insignificance to the small development set providing a noisy selection signal for the LoRA configuration sweep.

> "LoRA+SA+UST improves the AVG QWK over DualBERT by 0.046 (per-trait; 95% CI [0.029, 0.063]) and 0.054 (per-prompt; 95% CI [0.038, 0.070]), both with p < 0.01"

## Discussion


## Related Claims
- [Score Alignment and UST generalize to TOEFL11 and ELLIPSE, but LoRA slightly degrades performance on those datasets](technique-generalizability-toefl11-ellipse.md) — related
- [Gains from the integrated method shrink as labeled training data increase, from about 0.133 QWK at K = 16 to about 0.043 at K = 128](integrated-method-gains-shrink-with-data-size.md) — related
- [The proposed techniques combine orthogonally with 5-runs selection and ensembling, adding 7.6 QWK points in the 32-data setting and 2.4 points in the full-data setting](orthogonal-gains-with-runs-and-ensembling.md) — related
- [Score Alignment applied to DualBERT outperforms previous SOTA AES models (ArTS+RMTS and SaMRL) in the full-data setting on ASAP++](score-alignment-sota-full-data-asap.md) — related
