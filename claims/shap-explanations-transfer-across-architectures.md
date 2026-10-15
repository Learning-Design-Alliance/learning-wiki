---
type: claim
title: SHAP explanations transfer robustly across architectures while LLM rationales transfer poorly to PLM predictions
description: SHAP explanations transfer robustly across architectures while LLM rationales transfer poorly to PLM predictions
id: shap-explanations-transfer-across-architectures
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: ivo-bueno-2026
    resource: "https://doi.org/10.48550/arxiv.2606.05180"
    title: "Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci. (2026). From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment. arXiv. https://arxiv.org/abs/2606.05180 [doi:10.48550/arxiv.2606.05180](https://doi.org/10.48550/arxiv.2606.05180)"
    author: Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# SHAP explanations transfer robustly across architectures while LLM rationales transfer poorly to PLM predictions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Removing LLM-ranked sentences produces substantially smaller PLM prediction shifts than removing SHAP-ranked sentences, while SHAP-ranked removal causes large immediate shifts in LLM predictions. [→ Ivo Bueno 2026](#ivo-bueno-2026)

## Evidence

### Ivo Bueno 2026

Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci. (2026). From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment. arXiv. https://arxiv.org/abs/2606.05180 [doi:10.48550/arxiv.2606.05180](https://doi.org/10.48550/arxiv.2606.05180)

`q2 · i?` · `causal · r2`

Cross-model evaluation applying explanations from one model family to perturb the other (BERT large, DeBERTaV3 large, ALBERT base; Qwen3 235B, Llama 3.1 8B, Mistral Small). LLM deletion trajectories on PLMs were often non-monotonic; SHAP removal showed a consistent first-step jump on LLMs.

> "In contrast, SHAP explanations consis- tently induce larger, more stable, and more coher- ent prediction shifts both within PLMs and when transferred to LLMs, demonstrating superior faith- fulness for sentence-level interpretability."

## Discussion


## Related Claims
- [SHAP and LLM explanation methods show consistently low alignment, with mean top-10 Jaccard similarity of 0.085](low-alignment-shap-llm-sentence-selection.md) — related
- [Deletion tests show SHAP sentence rankings are more faithful than LLM-generated rationales for PLM scorers](shap-more-faithful-than-llm-rationales-deletion.md) — possibly the same claim (merge candidate)
