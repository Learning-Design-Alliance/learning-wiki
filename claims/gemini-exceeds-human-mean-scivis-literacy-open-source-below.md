---
type: claim
title: Gemini-3.1-Pro-Preview is the strongest MLLM on SVLAT, exceeding the human mean, while the three open-source models remain below the human baseline
description: Gemini-3.1-Pro-Preview is the strongest MLLM on SVLAT, exceeding the human mean, while the three open-source models remain below the human baseline
id: gemini-exceeds-human-mean-scivis-literacy-open-source-below
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
    kind: design
    rigour: 2
---

# Gemini-3.1-Pro-Preview is the strongest MLLM on SVLAT, exceeding the human mean, while the three open-source models remain below the human baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Gemini-3.1-Pro-Preview achieves 88.6% overall accuracy on SVLAT, exceeding the human overall accuracy, while Qwen3.5-9B (68.8%), InternVL3.5-8B (64.3%), and LLaVA-OneVision (64.1%) trail humans in combined accuracy. [→ Patrick Phuoc Do 2026](#patrick-phuoc-do-2026)

## Evidence

### Patrick Phuoc Do 2026

Patrick Phuoc Do, Chau M. Ta, Chaoli Wang. (2026). Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy. https://arxiv.org/abs/2607.15176

`q2 · i?` · `design · r2`

Benchmark evaluation of six MLLMs on SVLAT, each model run 10 times with temperature 0, compared against 485 human participants. The results section reports that Gemini achieved "88.6% overall, exceeding human performance" while the open-weight models trail humans in combined accuracy.

> "Gemini is the strongest model by a wide margin, achieving 90.9% on image items, 82.9% on animation items, and 88.6% overall, exceeding human performance of 76.4%, 74.5%, and 75.9%, respectively. The three open-weight models trail humans in combined accuracy"

## Discussion


## Related Claims
- [On animation items, GPT via frame extraction matches human-level accuracy while Claude scores lowest of all models and humans at 59.3%](animation-items-gpt-matches-human-claude-lowest.md) — related
- [In the blind judicial-exam evaluation, Gemini 2.5 Pro scored 21/24, above the top human benchmark of 18/24, while the other LLMs scored substantially lower.](gemini-exceeds-human-judicial-exam-doctrinal-analysis.md) — related
- [MLLM performance on SVLAT is highly uneven across SciVis techniques, with Scientific Illustration most accessible and texture-based and integration-based visualizations revealing human-model gaps](mllm-accuracy-uneven-across-scivis-techniques.md) — related
