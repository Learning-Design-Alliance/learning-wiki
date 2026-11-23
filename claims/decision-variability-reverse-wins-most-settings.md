---
type: claim
title: Reverse curricula on decision variability outperform forward curricula in most settings, with the gap narrowing on harder benchmarks
description: Reverse curricula on decision variability outperform forward curricula in most settings, with the gap narrowing on harder benchmarks
id: decision-variability-reverse-wins-most-settings
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

# Reverse curricula on decision variability outperform forward curricula in most settings, with the gap narrowing on harder benchmarks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Reverse CL beginning with high-variability problems wins 12 of 15 comparisons against Forward CL, with notable gains on easier datasets, but the directional gap narrows as task difficulty increases. [→ Yaning Jia 2025](#yaning-jia-2025)

## Evidence

### Yaning Jia 2025

Yaning Jia, Chunhui Zhang, Xingjian Diao, Xiangchi Yuan, Zhongyu Ouyang, Chiyu Ma, and Soroush Vosoughi. (2025). What Makes a Good Curriculum? Disentangling the Effects of Data Ordering on LLM Mathematical Reasoning. [doi:10.48550/arXiv.2510.19099](https://doi.org/10.48550/arXiv.2510.19099)

`q2 · i?` · `causal · r2`

Section 3.2.5 (Table 5) evaluates Variance of Acc@K curricula for three models on five benchmarks. The article reports Reverse CL "winning 12 of 15 comparisons", with Llama-8B gains of +5.9% on MMQA and +4.9% on ASDiv.

> "Reverse CL, which begins with high-variability (less sta- ble) problems, consistently outperforms Forward CL across most settings—winning 12 of 15 com- parisons—with notable gains on easier datasets (MMQA: +5.9%,ASDiv: +4.9% forLlama-8B)."

## Discussion


## Related Claims
- Curriculum direction systematically shifts model internal states: forward CL yields more cautious internal states than reverse CL for perplexity and logit-gap metrics — related
- [No curriculum strategy dominates universally: the advantage of forward versus reverse ordering depends jointly on model capability, task complexity, and the difficulty metric](no-universal-curriculum-strategy-llm.md) — reports the opposite
- [Problem-difficulty-based curricula consistently outperform random shuffling, with gains of up to 3–6% on easier datasets](problem-difficulty-curricula-beat-shuffled-baseline.md) — related
- [Logit-gap (confidence margin) curricula consistently outperform the shuffled baseline, with Reverse CL providing the most consistent gains](logit-gap-curricula-reverse-most-consistent.md) — related
