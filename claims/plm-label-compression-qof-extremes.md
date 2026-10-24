---
type: claim
title: Fine-tuned PLMs exhibit label compression toward mid-scale QoF scores, never predicting extreme labels 1 and 7
description: Fine-tuned PLMs exhibit label compression toward mid-scale QoF scores, never predicting extreme labels 1 and 7
id: plm-label-compression-qof-extremes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: ivo-bueno-2026
    resource: "https://doi.org/10.48550/arxiv.2606.05180"
    title: "Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci. (2026). From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment. arXiv. https://arxiv.org/abs/2606.05180 [doi:10.48550/arxiv.2606.05180](https://doi.org/10.48550/arxiv.2606.05180)"
    author: Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned PLMs exhibit label compression toward mid-scale QoF scores, never predicting extreme labels 1 and 7

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Fine-tuned PLM predictions compress toward mid-scale values; for DeBERTaV3 large, predictions never fall below 2.03 or exceed 5.89, so extreme labels are never predicted. [→ Ivo Bueno 2026](#ivo-bueno-2026)

## Evidence

### Ivo Bueno 2026

Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci. (2026). From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment. arXiv. https://arxiv.org/abs/2606.05180 [doi:10.48550/arxiv.2606.05180](https://doi.org/10.48550/arxiv.2606.05180)

`q2 · i?` · `design · r2`

Prediction statistics analysis of fine-tuned PLMs on the NCTE test split. For DeBERTaV3 large the mean predicted score is 4.14 (σ = 0.16), close to the dataset average of 4.22, and the article states "extreme labels (1 and 7) are never predicted". Some ALBERT and RoBERTa variants collapse to the 3–5 range.

> "predictions never fall below 2.03 or exceed 5.89, meaning that extreme labels (1 and 7) are never predicted"

## Discussion


## Related Claims
- [Fine-tuned PLMs outperform prompted LLMs in rubric-based teaching quality scoring accuracy, while LLMs better preserve score variability](plms-outperform-llms-qof-scoring-accuracy.md) — related
- [LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth](llama-prediction-range-compression.md) — related
- [Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict](score-wise-bias-regression-to-mean-awe.md) — related
