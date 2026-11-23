---
type: claim
title: Logit-gap (confidence margin) curricula consistently outperform the shuffled baseline, with Reverse CL providing the most consistent gains
description: Logit-gap (confidence margin) curricula consistently outperform the shuffled baseline, with Reverse CL providing the most consistent gains
id: logit-gap-curricula-reverse-most-consistent
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

# Logit-gap (confidence margin) curricula consistently outperform the shuffled baseline, with Reverse CL providing the most consistent gains

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` LG-based curricula outperform the shuffled baseline across models, particularly on easier datasets, and Reverse CL (high-confidence first) yields the most consistent gains across benchmarks. [→ Yaning Jia 2025](#yaning-jia-2025)

## Evidence

### Yaning Jia 2025

Yaning Jia, Chunhui Zhang, Xingjian Diao, Xiangchi Yuan, Zhongyu Ouyang, Chiyu Ma, and Soroush Vosoughi. (2025). What Makes a Good Curriculum? Disentangling the Effects of Data Ordering on LLM Mathematical Reasoning. [doi:10.48550/arXiv.2510.19099](https://doi.org/10.48550/arXiv.2510.19099)

`q2 · i?` · `causal · r2`

Section 3.2.3 (Table 3) evaluates curricula built from the logit gap for all three models on five benchmarks. The article reports Llama-8B improving from 74.02 to 77.93% on ASDiv and states Reverse CL provides "the most consistent gains across benchmarks".

> "Across models, LG-based curricula consistently outperform the shuf- fled baseline, particularly on easier datasets such as ASDiv(e.g.,Llama-8B: 74.02 →77.93%)"

## Discussion


## Related Claims
- Curriculum direction systematically shifts model internal states: forward CL yields more cautious internal states than reverse CL for perplexity and logit-gap metrics — related
- [Problem-difficulty-based curricula consistently outperform random shuffling, with gains of up to 3–6% on easier datasets](problem-difficulty-curricula-beat-shuffled-baseline.md) — related
- [Reverse curricula on decision variability outperform forward curricula in most settings, with the gap narrowing on harder benchmarks](decision-variability-reverse-wins-most-settings.md) — related
- [Sorting training paragraphs by length improves over random baselines, but the article reports no clear recipe on whether increasing or decreasing order is preferred](length-sorting-improves-no-clear-recipe.md) — related
