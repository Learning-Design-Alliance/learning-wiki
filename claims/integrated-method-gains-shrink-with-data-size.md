---
type: claim
title: Gains from the integrated method shrink as labeled training data increase, from about 0.133 QWK at K = 16 to about 0.043 at K = 128
description: Gains from the integrated method shrink as labeled training data increase, from about 0.133 QWK at K = 16 to about 0.043 at K = 128
id: integrated-method-gains-shrink-with-data-size
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
---

# Gains from the integrated method shrink as labeled training data increase, from about 0.133 QWK at K = 16 to about 0.043 at K = 128

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` All techniques consistently improved performance across all sample sizes, with Score Alignment showing the most substantial improvement, but the integrated method's boost over DualBERT diminishes as K grows. [→ Hongseok Choi 2026](#hongseok-choi-2026)

## Evidence

### Hongseok Choi 2026

Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177

`q3 · i?` · `causal · r2`

Analysis of performance scaling with training-sample size on ASAP++ (Fig. 3), reporting average QWK across traits in per-prompt performance; the article attributes the shrinking gain to the robust generalization capability of deep learning.

> "Specifically, atK =16, the QWK improves from 0.494 to 0.627, an increase of approximately 0.133. In contrast, at K =128, the QWK improves from 0.675 to 0.718, showing a smaller increase of approximately 0.043."

## Discussion


## Related Claims
- [In the 32-data setting on ASAP++, the integrated LoRA+SA+UST method reaches 91.2% of full-data performance, with statistically significant gains over DualBERT](integrated-method-32-data-asap.md) — related
