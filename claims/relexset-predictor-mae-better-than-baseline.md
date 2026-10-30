---
type: claim
title: A fine-tuned DistilRoBERTa recipe-quality predictor achieves a test-set MAE of 0.39, slightly better than but not significantly different from a mean-prediction baseline of 0.42.
description: A fine-tuned DistilRoBERTa recipe-quality predictor achieves a test-set MAE of 0.39, slightly better than but not significantly different from a mean-prediction baseline of 0.42.
id: relexset-predictor-mae-better-than-baseline
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: mejia-domenzain-2025
    resource: "https://doi.org/10.1007/s40593-024-00405-1"
    title: "Mejia-Domenzain, P., Frej, J., Neshaei, S. P., Mouchel, L., Nazaretsky, T., Wambsganss, T., Bosselut, A., & Käser, T. (2025). Enhancing Procedural Writing Through Personalized Example Retrieval: A Case Study on Cooking Recipes. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00405-1"
    author: "Mejia-Domenzain, P., Frej, J., Neshaei, S. P., Mouchel, L., Nazaretsky, T., Wambsganss, T., Bosselut, A., & Käser, T."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# A fine-tuned DistilRoBERTa recipe-quality predictor achieves a test-set MAE of 0.39, slightly better than but not significantly different from a mean-prediction baseline of 0.42.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` RELEXset-Predictor achieved a mean absolute error of 0.39 on the hold-out test set, slightly better than the 0.42 baseline MAE, with the difference not significant. [→ Mejia-Domenzain 2025](#mejia-domenzain-2025)

## Evidence

### Mejia-Domenzain 2025

Mejia-Domenzain, P., Frej, J., Neshaei, S. P., Mouchel, L., Nazaretsky, T., Wambsganss, T., Bosselut, A., & Käser, T. (2025). Enhancing Procedural Writing Through Personalized Example Retrieval: A Case Study on Cooking Recipes. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00405-1

`q2 · i?` · `causal · r2`

Numerical evaluation of the fine-tuned DistilRoBERTa regression model (RELEXset-Predictor) on a held-out test split of the rated-recipe database. As printed, "slightly better than the baseline MAE of 0.42 (simply predicting the mean)", with the article noting the difference was not significant. No effect size is printed.

> "RELEXset-Predictor achieved a mean absolute error (MAE) of 0 .39 on the test set, which is slightly better than the baseline MAE of 0.42 (simply predicting the mean)."

## Discussion


## Related Claims
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — related
- [Jointly predicting courses and grades reduces grade-prediction MAE by 46.4% versus an identical Transformer that predicts grades only](joint-course-grade-prediction-halves-mae.md) — related
