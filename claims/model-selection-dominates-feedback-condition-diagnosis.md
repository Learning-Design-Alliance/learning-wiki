---
type: claim
title: Model selection, not feedback condition, explains LLM diagnostic accuracy in three-way logic proof classification
description: Model selection, not feedback condition, explains LLM diagnostic accuracy in three-way logic proof classification
id: model-selection-dominates-feedback-condition-diagnosis
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: tahreem-yasir-2026
    resource: "https://doi.org/10.48550/arxiv.2605.16207"
    title: "Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes. (2026). Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most. arXiv:2605.16207. https://arxiv.org/abs/2605.16207 [doi:10.48550/arxiv.2605.16207](https://doi.org/10.48550/arxiv.2605.16207)"
    author: Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Model selection, not feedback condition, explains LLM diagnostic accuracy in three-way logic proof classification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Model selection explained most variance in classification performance (η² > 0.95, p < .001) while feedback conditions had negligible effect (η² < .01). [→ Tahreem Yasir 2026](#tahreem-yasir-2026)

## Evidence

### Tahreem Yasir 2026

Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes. (2026). Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most. arXiv:2605.16207. https://arxiv.org/abs/2605.16207 [doi:10.48550/arxiv.2605.16207](https://doi.org/10.48550/arxiv.2605.16207)

`q2 · i?` · `causal · r2`

Variance decomposition analysis (RQ2) comparing η² explained by model selection versus feedback condition across the 10,836-pair benchmark. The article concludes additional information access "did not improve classification when student solutions diverged from the expected path"; η² is variance explained, not an effect size.

> "Model selection explained most of the variance in classification performance (η2 >0.95 ,p<.001 ), while feedback conditions had negligible effect (η2 < .01)."

## Discussion


## Related Claims
- [LLM feedback agents classify optimal logic proof steps near-ceiling but perform poorly on valid-alternative and incorrect solutions](llm-tutors-near-ceiling-optimal-poor-valid-alternative-incorrect.md) — related
- [Step complexity, distance to conclusion, and inference rule explain negligible diagnostic variance, with complexity predicting misdiagnosis only for optimal steps](problem-level-factors-negligible-diagnostic-variance.md) — related
- [Misspecification of theoretical diagnostic classification models and inaccurate Q-matrices impact classification accuracy](tdcm-qmatrix-misspecification-hurts-classification.md) — related
- [A semi-supervised ANN method combining DINA and DINO achieves appreciated classification performance across test conditions, especially when diagnostic quality is not high or the Q-matrix contains misspecified elements](semi-supervised-ann-cdm-robust-classification.md) — related
