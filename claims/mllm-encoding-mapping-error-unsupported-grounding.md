---
type: claim
title: Some MLLM failures occur when a higher-level SciVis interpretation is grounded in an unsupported visual encoding rather than the encoding specified by the visualization and caption
description: Some MLLM failures occur when a higher-level SciVis interpretation is grounded in an unsupported visual encoding rather than the encoding specified by the visualization and caption
id: mllm-encoding-mapping-error-unsupported-grounding
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

# Some MLLM failures occur when a higher-level SciVis interpretation is grounded in an unsupported visual encoding rather than the encoding specified by the visualization and caption

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In Item 35, Gemini inferred fiber density from opacity and solidness of colored regions, and Claude reached the same wrong conclusion across all 10 runs by invoking anatomical prior knowledge, even though the caption specifies that color encodes fiber orientation. [→ Patrick Phuoc Do 2026](#patrick-phuoc-do-2026)

## Evidence

### Patrick Phuoc Do 2026

Patrick Phuoc Do, Chau M. Ta, Chaoli Wang. (2026). Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy. https://arxiv.org/abs/2607.15176 [doi:10.48550/arxiv.2607.15176](https://doi.org/10.48550/arxiv.2607.15176)

`q2 · i?` · `design · r2`

Qualitative error analysis of a tractography item (Section 4.4, Figure 5). Gemini concluded region C had the highest fiber density because it appeared as a highly opaque, solid red mass; Claude grounded its judgment in imported neuroanatomical knowledge and color variety rather than actual fiber concentration.

> "The error, therefore, is not simply that the model made a higher-level inference, but that it grounded this inference in an unsupported encoding rather than in the actual evidence provided by the visualization and caption."

## Discussion


## Related Claims
- [MLLM performance on SVLAT is highly uneven across SciVis techniques, with Scientific Illustration most accessible and texture-based and integration-based visualizations revealing human-model gaps](mllm-accuracy-uneven-across-scivis-techniques.md) — related
- [MLLMs show recurring failures in fine-grained quantitative estimation, often identifying the encoding and measurement strategy but misestimating precise values](mllm-fine-grained-quantitative-misestimation-scivis.md) — related
- [Texture-based visualizations expose MLLM difficulty in decoding local flow direction from animated vector fields, a difficulty specific to dense texture-based motion rather than directional reasoning generally](mllm-flow-direction-interpretation-error-texture-based.md) — related
- In a contrastive audit, visual misreading is the dominant failure mode for non-reasoning models on items reasoning models solve — a broader claim this one bears on
- [VLMs show a common grounding failure: coarse semantic relevance without precise region-activity binding and entity-evidence alignment](vlm-grounding-failure-region-activity-binding.md) — a broader claim this one bears on
