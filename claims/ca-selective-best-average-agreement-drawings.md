---
type: claim
title: Confidence-aware selective test-time scoring achieves the best average agreement with expert rubric scoring across six NGSS drawing items
description: Confidence-aware selective test-time scoring achieves the best average agreement with expert rubric scoring across six NGSS drawing items
id: ca-selective-best-average-agreement-drawings
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
recheck_by: 2029
sources:
  - id: fang-2026
    resource: "https://doi.org/10.48550/arxiv.2606.20264"
    title: "Fang, L., Zhang, Y., Park, J., Wang, Z., Ma, P., Zhai, X. (2026). Confidence-Aware Automated Assessment of Student-Drawn Scientific Models. https://arxiv.org/abs/2606.20264 [doi:10.48550/arxiv.2606.20264](https://doi.org/10.48550/arxiv.2606.20264)"
    author: Fang, L., Zhang, Y., Park, J., Wang, Z., Ma, P., Zhai, X.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Confidence-aware selective test-time scoring achieves the best average agreement with expert rubric scoring across six NGSS drawing items

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across six items, the proposed CA-Selective method attains the best overall performance on average across items, suggesting selective aggregation improves scoring quality by reducing the influence of less informative test-time predictions. [→ Fang 2026](#fang-2026)

## Evidence

### Fang 2026

Fang, L., Zhang, Y., Park, J., Wang, Z., Ma, P., Zhai, X. (2026). Confidence-Aware Automated Assessment of Student-Drawn Scientific Models. https://arxiv.org/abs/2606.20264 [doi:10.48550/arxiv.2606.20264](https://doi.org/10.48550/arxiv.2606.20264)

`q2 · i?` · `design · r2`

Numerical evaluation on six NGSS-aligned drawing items (Table 2), comparing ViT Frozen, ViT+LoRA, CA-Uniform, and CA-Selective. CA-Selective shows "the best overall performance on average across items", with the highest average Cohen's kappa (0.760) and F1 (0.727) as printed in Table 2.

> "Comparing the two confidence-aware variants, CA-Selective achieves the best overall performance on average across items, suggesting that selective aggregationcanimprovescoringqualitybyreducingtheinfluenceoflessinformativetest-time predictions."

## Discussion


## Related Claims
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [The framework shows high scoring consistency, with 79% agreement and 81% inter-rater reliability on physics questions](framework-scoring-high-consistency-physics.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts — related
- [A Gemini-based creativity autorater scores real students' complex multimedia creativity tasks on par with human experts (item Kappa 0.66; total-score Pearson r = 0.88)](gemini-autorater-creativity-real-students.md) — related
- [LLM alignment with expert teaching ratings does not predict, and is often negatively associated with, alignment with student learning gains](proxy-alignment-not-impact-alignment-llm-classroom.md) — reports the opposite
- [Multimodal LLMs grading handwritten student work achieved κ = 0.90 on arithmetic but κ ≈ 0.47 on interpreting student illustrations](multimodal-llm-grading-kappa-arithmetic-illustrations.md) — related
- [Hierarchical Acceptance Rate aligns with expert acceptance decisions better than single-dimension and holistic LLM judges](har-outperforms-llm-judge-acceptance-alignment.md) — related
- [Multimodal XGBoost models achieved rubric-aligned scoring comparable to expert ratings, and no single modality approached multimodal performance](multimodal-xgboost-expert-comparable-scoring.md) — related
- [Claude's few-shot scoring behaved erratically across items: best few-shot model on Item 1 but by far the worst model on Item 2](claude-erratic-few-shot-performance-across-items.md) — related
- [LoRA adaptation adds only 0.6M trainable parameters on an 86.4M frozen backbone, keeping methods lightweight relative to LLM-based scoring](lora-parameter-efficiency-drawing-scoring.md) — related
