---
type: claim
title: Texture-based visualizations expose MLLM difficulty in decoding local flow direction from animated vector fields, a difficulty specific to dense texture-based motion rather than directional reasoning generally
description: Texture-based visualizations expose MLLM difficulty in decoding local flow direction from animated vector fields, a difficulty specific to dense texture-based motion rather than directional reasoning generally
id: mllm-flow-direction-interpretation-error-texture-based
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

# Texture-based visualizations expose MLLM difficulty in decoding local flow direction from animated vector fields, a difficulty specific to dense texture-based motion rather than directional reasoning generally

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In Item 20, Gemini and Qwen incorrectly concluded that winds near Chicago and Houston flow in different directions, and even models that answered correctly misread or avoided the specific direction, suggesting models misread local motion in the animated flow field. [→ Patrick Phuoc Do 2026](#patrick-phuoc-do-2026)

## Evidence

### Patrick Phuoc Do 2026

Patrick Phuoc Do, Chau M. Ta, Chaoli Wang. (2026). Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy. https://arxiv.org/abs/2607.15176 [doi:10.48550/arxiv.2607.15176](https://doi.org/10.48550/arxiv.2607.15176)

`q2 · i?` · `design · r2`

Qualitative error analysis of model rationales on a texture-based wind map item (Section 4.4, Figure 4). The winds in both regions actually flow in roughly the same direction, approximately from northwest to southeast, but Gemini and Qwen concluded the directions differed.

> "This suggests that the model misread local motion in the animated flow field, possibly by confusing streak orientation with the actual flow direction. Because most models correctly identified the hurricane's direction in Item 9 (refer to Ap- pendix A), the difficulty appears specific to dense texture-based motion decoding rather than to directional reasoning more generally."

## Discussion


## Related Claims
- [MLLM performance on SVLAT is highly uneven across SciVis techniques, with Scientific Illustration most accessible and texture-based and integration-based visualizations revealing human-model gaps](mllm-accuracy-uneven-across-scivis-techniques.md) — a broader claim this one bears on
- [Some MLLM failures occur when a higher-level SciVis interpretation is grounded in an unsupported visual encoding rather than the encoding specified by the visualization and caption](mllm-encoding-mapping-error-unsupported-grounding.md) — related
- [On animation items, GPT via frame extraction matches human-level accuracy while Claude scores lowest of all models and humans at 59.3%](animation-items-gpt-matches-human-claude-lowest.md) — related
- [MLLMs show recurring failures in fine-grained quantitative estimation, often identifying the encoding and measurement strategy but misestimating precise values](mllm-fine-grained-quantitative-misestimation-scivis.md) — related
