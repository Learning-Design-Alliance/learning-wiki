---
type: claim
title: Off-the-shelf LLMs are systematically misaligned with human item-difficulty judgments and struggle to simulate lower-proficiency states
description: Off-the-shelf LLMs are systematically misaligned with human item-difficulty judgments and struggle to simulate lower-proficiency states
id: off-the-shelf-llms-misaligned-human-difficulty-judgments
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: zhihao-yuan-2026
    resource: "https://doi.org/10.48550/arxiv.2601.05473"
    title: "Zhihao Yuan, Yunze Xiao, Ming Li, Weihao Xuan, Richard Tong, Mona Diab, Tom Mitchell. (2026). Towards Valid Student Simulation with Large Language Models. https://arxiv.org/abs/2601.05473 [doi:10.48550/arxiv.2601.05473](https://doi.org/10.48550/arxiv.2601.05473)"
    author: Zhihao Yuan, Yunze Xiao, Ming Li, Weihao Xuan, Richard Tong, Mona Diab, Tom Mitchell
    q: 2
    i: "?"
    kind: theoretical
    rigour: 2
---

# Off-the-shelf LLMs are systematically misaligned with human item-difficulty judgments and struggle to simulate lower-proficiency states

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Even with difficulty labels grounded in real student field testing, off-the-shelf LLMs can be systematically misaligned with human difficulty judgments and struggle to reliably simulate lower-proficiency cognitive states. [→ Zhihao Yuan 2026](#zhihao-yuan-2026)

## Evidence

### Zhihao Yuan 2026

Zhihao Yuan, Yunze Xiao, Ming Li, Weihao Xuan, Richard Tong, Mona Diab, Tom Mitchell. (2026). Towards Valid Student Simulation with Large Language Models. https://arxiv.org/abs/2601.05473 [doi:10.48550/arxiv.2601.05473](https://doi.org/10.48550/arxiv.2601.05473)

`q2 · i?` · `theoretical · r2`

The review reports this large-scale evidence, citing Li et al. (2025c), in the content-evaluation section, as a caution that substituting an LLM for human pilots does not by itself solve item-difficulty calibration. The cited study's design is not described here.

> "recent large-scale evidence suggests this setting is not solved by simply substituting an LLM for human pilots: even with difficulty labels grounded in real student field testing"

## Discussion


## Related Claims
- [Model and prompt choice account for only a small share of misalignment error, which concentrates in transcript-conditioned higher-order interactions](variance-decomposition-model-prompt-weak-levers.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [Automated metrics and LLM judges can misalign with expert human preferences in non-verifiable educational evaluation](non-verifiability-crisis-llm-judges-misalign.md) — related
- [On structured pedagogical-judgment items, all evaluated models share a systematic style-over-fit deviation, converging on the same non-reference option](llm-style-over-fit-uniform-deviation.md) — related
- [Item complexity is an intrinsic item characteristic while item difficulty describes how hard it is to solve for students](complexity-intrinsic-difficulty-performance.md) — related
