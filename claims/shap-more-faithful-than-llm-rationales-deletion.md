---
type: claim
title: Deletion tests show SHAP sentence rankings are more faithful than LLM-generated rationales for PLM scorers
description: Deletion tests show SHAP sentence rankings are more faithful than LLM-generated rationales for PLM scorers
id: shap-more-faithful-than-llm-rationales-deletion
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
  - id: ivo-bueno-2026-2
    resource: "https://arxiv.org/abs/2606.05180"
    title: "Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci. (2026). From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment. arXiv. https://arxiv.org/abs/2606.05180"
    author: Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Deletion tests show SHAP sentence rankings are more faithful than LLM-generated rationales for PLM scorers

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q2`

## Subclaims
`q2 i?` In single-model deletion tests, SHAP-based sentence rankings produce larger and more coherent prediction shifts than LLM-generated rankings, which induce smaller and often unstable changes. [→ Ivo Bueno 2026](#ivo-bueno-2026)
`q2 i?` A random sentence-deletion baseline matched for sentence length yields near-zero prediction changes, ruling out sentence length or generic perturbation as explanations. [→ Ivo Bueno 2026 (2)](#ivo-bueno-2026-2)

## Evidence

### Ivo Bueno 2026

Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci. (2026). From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment. arXiv. https://arxiv.org/abs/2606.05180 [doi:10.48550/arxiv.2606.05180](https://doi.org/10.48550/arxiv.2606.05180)

`q2 · i?` · `causal · r2`

Deletion-based faithfulness experiment: top-10 ranked sentences were removed stepwise and transcripts re-scored by the same model. Among PLMs BERT large showed the highest average change (Δ = 0.0329); among LLMs Qwen 3 235B showed the largest (Δ = 0.0388), with all other LLMs below 0.02.

> "SHAP-based sentence rankings are more faithful for PLM scorers, whereas LLM-generated rationales induce smaller and often unstable prediction changes, even for the models that produce them."

### Ivo Bueno 2026 (2)

Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci. (2026). From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment. arXiv. https://arxiv.org/abs/2606.05180

`q2 · i?` · `causal · r2`

Ablation study comparing ranked versus random sentence removal matched for sentence length (Table 3). The article concludes the larger ranked-removal effects reflect "the identification of influential content" rather than structural artifacts.

> "This baseline yields near-zero predic- tion changes between consecutive removals, indi- cating that the larger effects observed for SHAP- and LLM-based rankings are not explained by sen- tence length or generic perturbation, but by the identification of influential content."

## Discussion


## Related Claims
- [SHAP and LLM explanation methods show consistently low alignment, with mean top-10 Jaccard similarity of 0.085](low-alignment-shap-llm-sentence-selection.md) — related
- [SHAP explanations transfer robustly across architectures while LLM rationales transfer poorly to PLM predictions](shap-explanations-transfer-across-architectures.md) — possibly the same claim (merge candidate)
