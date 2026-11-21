---
type: claim
title: The proposed techniques combine orthogonally with 5-runs selection and ensembling, adding 7.6 QWK points in the 32-data setting and 2.4 points in the full-data setting
description: The proposed techniques combine orthogonally with 5-runs selection and ensembling, adding 7.6 QWK points in the 32-data setting and 2.4 points in the full-data setting
id: orthogonal-gains-with-runs-and-ensembling
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

# The proposed techniques combine orthogonally with 5-runs selection and ensembling, adding 7.6 QWK points in the 32-data setting and 2.4 points in the full-data setting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Combining the proposed methods with 5-runs (best-of-five model selection) and bagging ensembles of four bootstrapped models improved total QWK by 7.6 points in the 32-data setting and 2.4 points in the full-data setting. [→ Hongseok Choi 2026](#hongseok-choi-2026)

## Evidence

### Hongseok Choi 2026

Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177

`q3 · i?` · `causal · r2`

Upper-bound estimation experiment on ASAP++ (Tables 9 and 10) applying 5-runs selection and a four-model bagging ensemble on top of the proposed methods; the article states the methods "can be applied orthogonally" to such performance-improving methods.

> "In the 32-data setting, the total QWK score improved by 7.6 points, and even in the full-data setting, where performance is already strong, it improved by 2.4 points."

## Discussion


## Related Claims
- [Cross-validated ensemble models performed better on the test set than hold-out models on internal evaluation, suggesting cross-validation leverages data more effectively](cross-validation-ensemble-outperformed-hold-out-internal-evaluation.md) — related
- [Ensemble modeling of multiple LLM scorers yields performance gains in automated divergent thinking scoring](ensemble-models-performance-gains-llm-scoring.md) — a broader claim this one bears on
- [Rank-averaged ensembling stabilized predictions but did not outperform the single base model](ensemble-stabilizes-but-not-better-than-model1.md) — related
- [In the 32-data setting on ASAP++, the integrated LoRA+SA+UST method reaches 91.2% of full-data performance, with statistically significant gains over DualBERT](integrated-method-32-data-asap.md) — related
