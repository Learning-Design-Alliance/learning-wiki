---
type: claim
title: MLLM performance on SVLAT is highly uneven across SciVis techniques, with Scientific Illustration most accessible and texture-based and integration-based visualizations revealing human-model gaps
description: MLLM performance on SVLAT is highly uneven across SciVis techniques, with Scientific Illustration most accessible and texture-based and integration-based visualizations revealing human-model gaps
id: mllm-accuracy-uneven-across-scivis-techniques
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: patrick-phuoc-do-2026
    resource: "https://arxiv.org/abs/2607.15176"
    title: "Patrick Phuoc Do, Chau M. Ta, Chaoli Wang. (2026). Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy. https://arxiv.org/abs/2607.15176"
    author: Patrick Phuoc Do, Chau M. Ta, Chaoli Wang
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# MLLM performance on SVLAT is highly uneven across SciVis techniques, with Scientific Illustration most accessible and texture-based and integration-based visualizations revealing human-model gaps

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Across SVLAT techniques, Scientific Illustration is the most accessible to humans and all models, while texture-based and integration-based visualizations show a clearer gap between human and model performance. [→ Patrick Phuoc Do 2026](#patrick-phuoc-do-2026)

## Evidence

### Patrick Phuoc Do 2026

Patrick Phuoc Do, Chau M. Ta, Chaoli Wang. (2026). Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy. https://arxiv.org/abs/2607.15176

`q2 · i?` · `associational · r2`

Technique-level analysis of the SVLAT benchmark results (Figure 1 and Section 4.2). Humans achieve 82.0% on texture-based and 88.8% on integration-based visualization, while model accuracy on these techniques fluctuates much more than the human range of 68.9% to 88.8%.

> "Across all techniques,Scientific Illustrationis the most accessible to humans and all models. Human accuracy reaches 79.5%, while all models perform strongly, ranging from 81.4% to 95.7%. In contrast,Texture-Based VisualizationandIntegration-Based Visualizationreveal a clearer gap between human and model performance."

## Discussion


## Related Claims
- [Gemini-3.1-Pro-Preview is the strongest MLLM on SVLAT, exceeding the human mean, while the three open-source models remain below the human baseline](gemini-exceeds-human-mean-scivis-literacy-open-source-below.md) — related
- [Some MLLM failures occur when a higher-level SciVis interpretation is grounded in an unsupported visual encoding rather than the encoding specified by the visualization and caption](mllm-encoding-mapping-error-unsupported-grounding.md) — related
- [Texture-based visualizations expose MLLM difficulty in decoding local flow direction from animated vector fields, a difficulty specific to dense texture-based motion rather than directional reasoning generally](mllm-flow-direction-interpretation-error-texture-based.md) — a narrower finding that bears on this claim
- [MLLMs show recurring failures in fine-grained quantitative estimation, often identifying the encoding and measurement strategy but misestimating precise values](mllm-fine-grained-quantitative-misestimation-scivis.md) — related
- [On animation items, GPT via frame extraction matches human-level accuracy while Claude scores lowest of all models and humans at 59.3%](animation-items-gpt-matches-human-claude-lowest.md) — related
