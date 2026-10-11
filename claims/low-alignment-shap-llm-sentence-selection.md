---
type: claim
title: SHAP and LLM explanation methods show consistently low alignment, with mean top-10 Jaccard similarity of 0.085
description: SHAP and LLM explanation methods show consistently low alignment, with mean top-10 Jaccard similarity of 0.085
id: low-alignment-shap-llm-sentence-selection
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: ivo-bueno-2026
    resource: "https://arxiv.org/abs/2606.05180"
    title: "Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci. (2026). From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment. arXiv. https://arxiv.org/abs/2606.05180"
    author: Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SHAP and LLM explanation methods show consistently low alignment, with mean top-10 Jaccard similarity of 0.085

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across nine LLMs, overlap between SHAP- and LLM-selected top-10 sentence sets is roughly one to two sentences per transcript, with weak rank-order agreement. [→ Ivo Bueno 2026](#ivo-bueno-2026)

## Evidence

### Ivo Bueno 2026

Ivo Bueno, Babette Bühler, Philipp Stark, Tim Fütterer, Ulrich Trautwein, Dorottya Demszky, Heather Hill, Enkelejda Kasneci. (2026). From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment. arXiv. https://arxiv.org/abs/2606.05180

`q2 · i?` · `design · r2`

Alignment analysis computing Jaccard similarity and Spearman rank correlation between SHAP and LLM top-10 sentence selections per transcript. The article reports these trends are consistent across model families and sizes, suggesting alignment is driven by the explanation method rather than model scale.

> "Across nine LLMs, the mean Jaccard similarity between the indices of the top-10 sentence sets is 0.085, corresponding to an overlap of roughly one to two sentences per transcript, while the mean Spearman rank correlation is 0.062"

## Discussion


## Related Claims
- [Deletion tests show SHAP sentence rankings are more faithful than LLM-generated rationales for PLM scorers](shap-more-faithful-than-llm-rationales-deletion.md) — related
- [SHAP explanations transfer robustly across architectures while LLM rationales transfer poorly to PLM predictions](shap-explanations-transfer-across-architectures.md) — related
- [LLMs and instructors agree broadly on where feedback belongs but diverge on exact sentence spans, with span overlap strongly goal-dependent and LLMs highlighting more of each essay](llm-instructor-span-overlap-goal-dependent.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
