---
type: claim
title: "No curriculum strategy dominates universally: the advantage of forward versus reverse ordering depends jointly on model capability, task complexity, and the difficulty metric"
description: "No curriculum strategy dominates universally: the advantage of forward versus reverse ordering depends jointly on model capability, task complexity, and the difficulty metric"
id: no-universal-curriculum-strategy-llm
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: yaning-jia-2025
    resource: "https://doi.org/10.48550/arXiv.2510.19099"
    title: "Yaning Jia, Chunhui Zhang, Xingjian Diao, Xiangchi Yuan, Zhongyu Ouyang, Chiyu Ma, and Soroush Vosoughi. (2025). What Makes a Good Curriculum? Disentangling the Effects of Data Ordering on LLM Mathematical Reasoning. [doi:10.48550/arXiv.2510.19099](https://doi.org/10.48550/arXiv.2510.19099)"
    author: Yaning Jia, Chunhui Zhang, Xingjian Diao, Xiangchi Yuan, Zhongyu Ouyang, Chiyu Ma, and Soroush Vosoughi
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# No curriculum strategy dominates universally: the advantage of forward versus reverse ordering depends jointly on model capability, task complexity, and the difficulty metric

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Under distribution shift, Reverse CL generally excels on simpler datasets whereas Forward CL performs better on harder ones, with the pattern varying by model and metric. [→ Yaning Jia 2025](#yaning-jia-2025)

## Evidence

### Yaning Jia 2025

Yaning Jia, Chunhui Zhang, Xingjian Diao, Xiangchi Yuan, Zhongyu Ouyang, Chiyu Ma, and Soroush Vosoughi. (2025). What Makes a Good Curriculum? Disentangling the Effects of Data Ordering on LLM Mathematical Reasoning. [doi:10.48550/arXiv.2510.19099](https://doi.org/10.48550/arXiv.2510.19099)

`q2 · i?` · `causal · r2`

Controlled post-training experiments on Gemma3-4B, Mistral-7B, and Llama3.1-8B across five math benchmarks (512 problems each), reported in Section 3.2.1. The article states "Reverse CL generally excels on simpler datasets, whereas Forward CL performs better on harder ones", e.g. Gemma-4B rising from 19.5 to 24.8% on MATH under SC ascending.

> "Under distri- bution shift, Reverse CL generally excels on sim- pler datasets, whereas Forward CL performs better on harder ones (e.g.,Gemma-4B: 19.5 →24.8% on MATHunder SC ↑)."

## Discussion


## Related Claims
- Curriculum direction systematically shifts model internal states: forward CL yields more cautious internal states than reverse CL for perplexity and logit-gap metrics — related
- [Reverse curricula on decision variability outperform forward curricula in most settings, with the gap narrowing on harder benchmarks](decision-variability-reverse-wins-most-settings.md) — reports the opposite
- [In metric-tiered training, the most effective difficulty tier depends on task difficulty: high-entropy tiers help easier tasks, low-entropy tiers help harder ones](metric-tier-effects-depend-task-difficulty.md) — related
