---
type: claim
title: "Problem-difficulty-based curricula consistently outperform random shuffling, with gains of up to 3–6% on easier datasets"
description: "Problem-difficulty-based curricula consistently outperform random shuffling, with gains of up to 3–6% on easier datasets"
id: problem-difficulty-curricula-beat-shuffled-baseline
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

# Problem-difficulty-based curricula consistently outperform random shuffling, with gains of up to 3–6% on easier datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Difficulty-aware ordering based on problem-side metrics enhances reasoning performance relative to a randomly shuffled baseline, with the largest gains on easier datasets. [→ Yaning Jia 2025](#yaning-jia-2025)

## Evidence

### Yaning Jia 2025

Yaning Jia, Chunhui Zhang, Xingjian Diao, Xiangchi Yuan, Zhongyu Ouyang, Chiyu Ma, and Soroush Vosoughi. (2025). What Makes a Good Curriculum? Disentangling the Effects of Data Ordering on LLM Mathematical Reasoning. [doi:10.48550/arXiv.2510.19099](https://doi.org/10.48550/arXiv.2510.19099)

`q2 · i?` · `causal · r2`

Results in Section 3.2.1 (Table 1) from fine-tuning three base models on MetaMathQA-40K subsets with curricula built from reasoning steps, symbol complexity, comprehension difficulty, and Acc@K. The article reports "gains of up to 3–6% on easier datasets such asASDivandGSM8K", e.g. Llama-8B +4.7% on ASDiv under RS descending.

> "Cur-ricula based on problem difficulty metrics consis-tently outperform the randomly shuffled baseline, with gains of up to 3–6% on easier datasets such asASDivandGSM8K(e.g.,Llama-8B: +4.7% onASDivunder RS ↓)"

## Discussion


## Related Claims
- Dataset difficulty moderates the benefit of difficulty-based sampling: performance differences are more pronounced on challenging datasets like SST-5 and XNLI than on easier ones — related
- [Reverse curricula on decision variability outperform forward curricula in most settings, with the gap narrowing on harder benchmarks](decision-variability-reverse-wins-most-settings.md) — related
- [Logit-gap (confidence margin) curricula consistently outperform the shuffled baseline, with Reverse CL providing the most consistent gains](logit-gap-curricula-reverse-most-consistent.md) — related
- [Sorting training paragraphs by length improves over random baselines, but the article reports no clear recipe on whether increasing or decreasing order is preferred](length-sorting-improves-no-clear-recipe.md) — related
- [Curriculum learning with easy-to-hard data ordering yields better final performance than shuffled vanilla learning on both benchmarks](yoda-curriculum-learning-improves-robustness.md) — related
- [A fully learned curriculum (deterministic ordering of generator inputs) makes GTN training more effective than other curriculum variants](gtn-full-curriculum-outperforms-other-variants.md) — related
- SEC-2D, with one arm per problem-type × difficulty combination, outperforms random curricula and stabilizes multi-task RL fine-tuning across three reasoning domains — related
