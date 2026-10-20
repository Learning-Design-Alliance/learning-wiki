---
type: claim
title: MLLMs show recurring failures in fine-grained quantitative estimation, often identifying the encoding and measurement strategy but misestimating precise values
description: MLLMs show recurring failures in fine-grained quantitative estimation, often identifying the encoding and measurement strategy but misestimating precise values
id: mllm-fine-grained-quantitative-misestimation-scivis
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: patrick-phuoc-do-2026
    resource: "https://doi.org/10.48550/arxiv.2607.15176"
    title: "Patrick Phuoc Do, Chau M. Ta, Chaoli Wang. (2026). Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy. https://arxiv.org/abs/2607.15176 [doi:10.48550/arxiv.2607.15176](https://doi.org/10.48550/arxiv.2607.15176)"
    author: Patrick Phuoc Do, Chau M. Ta, Chaoli Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# MLLMs show recurring failures in fine-grained quantitative estimation, often identifying the encoding and measurement strategy but misestimating precise values

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In qualitative error analysis of model rationales, models struggle with precise quantitative judgment when the answer depends on careful visual estimation, as in Item 3 where Gemini misread waypoint A as lying exactly on the 7200 ft contour line, and Item 41 where Gemini and Claude overestimated a lipid envelope radius as 50 nm when the correct radius is about 40 nm. [→ Patrick Phuoc Do 2026](#patrick-phuoc-do-2026)

## Evidence

### Patrick Phuoc Do 2026

Patrick Phuoc Do, Chau M. Ta, Chaoli Wang. (2026). Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy. https://arxiv.org/abs/2607.15176 [doi:10.48550/arxiv.2607.15176](https://doi.org/10.48550/arxiv.2607.15176)

`q2 · i?` · `design · r2`

Qualitative error analysis of model rationales (Section 4.4). In Item 41, Gemini estimated the diameter at approximately five times the 20 nm scale bar yielding a radius of 50 nm; Claude produced the same overestimate across all 10 runs, and GPT in 3 of 10 runs.

> "These examples suggest that the models can often identify the relevant quantitative encoding and coarse measurement strategy, a weakness reflected in the particularly low MLLM scores onQuantitative Estimation–Relative Estimation (Quantitative)."

## Discussion


## Related Claims
- [MLLM performance on SVLAT is highly uneven across SciVis techniques, with Scientific Illustration most accessible and texture-based and integration-based visualizations revealing human-model gaps](mllm-accuracy-uneven-across-scivis-techniques.md) — related
- [Some MLLM failures occur when a higher-level SciVis interpretation is grounded in an unsupported visual encoding rather than the encoding specified by the visualization and caption](mllm-encoding-mapping-error-unsupported-grounding.md) — related
- In a contrastive audit, visual misreading is the dominant failure mode for non-reasoning models on items reasoning models solve — related
- [VLMs show a common grounding failure: coarse semantic relevance without precise region-activity binding and entity-evidence alignment](vlm-grounding-failure-region-activity-binding.md) — a broader claim this one bears on
- [Trained students more often identify and remediate GenAI deficiencies such as visual errors and reasoning flaws](trained-students-remediate-genai-deficiencies.md) — related
- [Embodied teaching actions are spatially accurate across models, but temporal action–speech alignment remains more variable](lecturaagents-taq-spatial-strong-temporal-variable.md) — related
- [Texture-based visualizations expose MLLM difficulty in decoding local flow direction from animated vector fields, a difficulty specific to dense texture-based motion rather than directional reasoning generally](mllm-flow-direction-interpretation-error-texture-based.md) — related
- [Vision-assisted extraction identified chart type in all sampled images but showed ±5–10% numeric estimation error and two failure modes correctable via mandatory review](llm-chart-extraction-accuracy-failure-modes.md) — related
