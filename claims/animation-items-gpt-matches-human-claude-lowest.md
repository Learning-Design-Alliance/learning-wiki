---
type: claim
title: "On animation items, GPT via frame extraction matches human-level accuracy while Claude scores lowest of all models and humans at 59.3%"
description: "On animation items, GPT via frame extraction matches human-level accuracy while Claude scores lowest of all models and humans at 59.3%"
id: animation-items-gpt-matches-human-claude-lowest
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: patrick-phuoc-do-2026
    resource: "https://doi.org/10.48550/arxiv.2607.15176"
    title: "Patrick Phuoc Do, Chau M. Ta, Chaoli Wang. (2026). Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy. https://arxiv.org/abs/2607.15176 [doi:10.48550/arxiv.2607.15176](https://doi.org/10.48550/arxiv.2607.15176)"
    author: Patrick Phuoc Do, Chau M. Ta, Chaoli Wang
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# On animation items, GPT via frame extraction matches human-level accuracy while Claude scores lowest of all models and humans at 59.3%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` On SVLAT animation items, Gemini remains the top-performing model; via frame extraction GPT matches human-level accuracy (73.6% vs. 73.9%), while Claude scores the lowest of all models and humans at 59.3%. [→ Patrick Phuoc Do 2026](#patrick-phuoc-do-2026)

## Evidence

### Patrick Phuoc Do 2026

Patrick Phuoc Do, Chau M. Ta, Chaoli Wang. (2026). Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy. https://arxiv.org/abs/2607.15176 [doi:10.48550/arxiv.2607.15176](https://doi.org/10.48550/arxiv.2607.15176)

`q2 · i?` · `associational · r2`

Overall performance results split by item format (Table 1, Section 4.1). GPT-5.4 and Claude-Opus-4.6 were evaluated on animation items via frame extraction because their APIs did not support direct video input at the time of evaluation.

> "On animation items, Gem- ini remains the top-performing model. Via frame extraction, GPT matches human-level accuracy (73.6% vs. 73.9%), while Claude scores the lowest of all models and humans at 59.3%."

## Discussion


## Related Claims
- [Gemini-3.1-Pro-Preview is the strongest MLLM on SVLAT, exceeding the human mean, while the three open-source models remain below the human baseline](gemini-exceeds-human-mean-scivis-literacy-open-source-below.md) — related
- [MLLM performance on SVLAT is highly uneven across SciVis techniques, with Scientific Illustration most accessible and texture-based and integration-based visualizations revealing human-model gaps](mllm-accuracy-uneven-across-scivis-techniques.md) — related
- [Texture-based visualizations expose MLLM difficulty in decoding local flow direction from animated vector fields, a difficulty specific to dense texture-based motion rather than directional reasoning generally](mllm-flow-direction-interpretation-error-texture-based.md) — related
