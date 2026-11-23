---
type: claim
title: "In metric-tiered training, the most effective difficulty tier depends on task difficulty: high-entropy tiers help easier tasks, low-entropy tiers help harder ones"
description: "In metric-tiered training, the most effective difficulty tier depends on task difficulty: high-entropy tiers help easier tasks, low-entropy tiers help harder ones"
id: metric-tier-effects-depend-task-difficulty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
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

# In metric-tiered training, the most effective difficulty tier depends on task difficulty: high-entropy tiers help easier tasks, low-entropy tiers help harder ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For entropy-based metrics, training on the high-entropy tier yields stronger gains on easier benchmarks while the low-entropy tier performs better on harder benchmarks; for other metrics, gains concentrate in the medium tier. [→ Yaning Jia 2025](#yaning-jia-2025)

## Evidence

### Yaning Jia 2025

Yaning Jia, Chunhui Zhang, Xingjian Diao, Xiangchi Yuan, Zhongyu Ouyang, Chiyu Ma, and Soroush Vosoughi. (2025). What Makes a Good Curriculum? Disentangling the Effects of Data Ordering on LLM Mathematical Reasoning. [doi:10.48550/arXiv.2510.19099](https://doi.org/10.48550/arXiv.2510.19099)

`q2 · i?` · `causal · r2`

Metric-tiered training on Llama3-8B (Section 3.3, Figure 2): the training set is split into three equal-size tiers per metric, models are trained on one tier at a time under a fixed budget, and evaluated on four benchmarks grouped into easy and hard categories.

> "On easier benchmarks (ASDiv,GSM8K), training on thehigh-entropytier yields stronger gains, suggesting that uncertain samples provide valuable learning sig- nals for simpler tasks. In contrast, on harder bench- marks (MBench,MATH), thelow-entropytier per- forms better"

## Discussion


## Related Claims
- [No curriculum strategy dominates universally: the advantage of forward versus reverse ordering depends jointly on model capability, task complexity, and the difficulty metric](no-universal-curriculum-strategy-llm.md) — related
- [Harder practice questions disproportionately benefit students with prior Python skill but do not help beginners (pilot study)](difficulty-interaction-prior-python-pilot.md) — related
- Under tailored curriculum learning, the proportion of harder training data rises from 0% in stage one to 34.6% in stage two and 55.1% in stage three — related
