---
type: claim
title: SMART outperforms direct item difficulty prediction methods on both datasets, largely maintaining the advantage with a 1B base LLM
description: SMART outperforms direct item difficulty prediction methods on both datasets, largely maintaining the advantage with a 1B base LLM
id: smart-outperforms-direct-difficulty-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: alexander-scarlatos-2025
    resource: "https://doi.org/10.18653/v1/2025.emnlp-main.1274"
    title: "Alexander Scarlatos, Nigel Fernandez, Christopher Ormerod, Susan Lottridge, Andrew Lan. (2025). SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction. [doi:10.18653/v1/2025.emnlp-main.1274](https://doi.org/10.18653/v1/2025.emnlp-main.1274)"
    author: Alexander Scarlatos, Nigel Fernandez, Christopher Ormerod, Susan Lottridge, Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SMART outperforms direct item difficulty prediction methods on both datasets, largely maintaining the advantage with a 1B base LLM

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` SMART achieves higher PCC, SCC, and lower RMSE than all direct prediction baselines on Smarter Balanced and CodeWorkout, including with the 1B base model. [→ Alexander Scarlatos 2025](#alexander-scarlatos-2025)

## Evidence

### Alexander Scarlatos 2025

Alexander Scarlatos, Nigel Fernandez, Christopher Ormerod, Susan Lottridge, Andrew Lan. (2025). SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction. [doi:10.18653/v1/2025.emnlp-main.1274](https://doi.org/10.18653/v1/2025.emnlp-main.1274)

`q2 · i?` · `design · r2`

Cross-validation experiments on two real-world open-ended response datasets (49 reading comprehension items; 50 Java coding items) report PCC, SCC, and RMSE in Table 1; the authors state that "SMART, outperforms all direct prediction methods on all metrics". No effect sizes are printed.

> "Our approach, SMART, outperforms all direct prediction methods on all metrics, even largely maintaining this advantage when using the small 1B base LLM."

## Discussion


## Related Claims
- [Student simulation is key for item difficulty prediction in low-resource settings with few training items](simulation-key-few-training-items.md) — related
- [A fine-tuned Qwen3.5-9B simulated-respondent model predicts item difficulty with Pearson correlation 0.85, exceeding MathBERT (0.68) and MetaMath (0.75) baselines](llm-simulated-respondents-predict-item-difficulty-above-regression-baselines.md) — related
- [Epi2Diff achieves the best performance across all four item-difficulty test sets and all reported metrics, outperforming SLM fine-tuning, LLM prompting, and supervised LLM adaptation baselines](epi2diff-best-across-four-difficulty-benchmarks.md) — related
- [SMART's difficulty estimates are item-dependent: accurate for recall and narrative items but overestimated for higher-order thinking items](smart-overestimates-higher-order-item-difficulty.md) — related
