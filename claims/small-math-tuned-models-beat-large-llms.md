---
type: claim
title: Domain-adapted small math models outperform much larger general-purpose LLMs on mathematical reasoning benchmarks
description: Domain-adapted small math models outperform much larger general-purpose LLMs on mathematical reasoning benchmarks
id: small-math-tuned-models-beat-large-llms
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: asghar-ghorbani-2025
    resource: "https://doi.org/10.1364/opn.36.9.000028"
    title: "Asghar Ghorbani, Hanieh Fattahi. (2025). Bridging the Digital Divide: Small Language Models as a Pathway for Physics and Photonics Education in Underdeveloped Regions. arXiv. [doi:10.1364/opn.36.9.000028](https://doi.org/10.1364/opn.36.9.000028)"
    author: Asghar Ghorbani, Hanieh Fattahi
    q: 2
    i: "?"
    kind: review
    rigour: 1
---

# Domain-adapted small math models outperform much larger general-purpose LLMs on mathematical reasoning benchmarks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Qwen2.5-Math-7B surpasses LLaMA3.1-405B on GSM8K (8-shot) and MATH (4-shot), and the 1.5B variant outperforms LLaMA3.1-70B on MATH (4-shot). [→ Asghar Ghorbani 2025](#asghar-ghorbani-2025)

## Evidence

### Asghar Ghorbani 2025

Asghar Ghorbani, Hanieh Fattahi. (2025). Bridging the Digital Divide: Small Language Models as a Pathway for Physics and Photonics Education in Underdeveloped Regions. arXiv. [doi:10.1364/opn.36.9.000028](https://doi.org/10.1364/opn.36.9.000028)

`q2 · i?` · `review · r1`

Benchmark comparison in Table 2 reports few-shot chain-of-thought scores showing "Qwen2.5-Math-7B surpasses LLaMA3.1-405B on GSM8K (8-shot) and MATH (4-shot) benchmarks"; the article presents this as evidence that domain adaptation lets small models rival much larger ones.

> "Qwen2.5-Math-7B surpasses LLaMA3.1-405B on GSM8K (8-shot) and MATH (4-shot) benchmarks, while the 1.5B variant outperforms LLaMA3.1-70B on MATH (4-shot)."

## Discussion


## Related Claims
- [At 30K and 60K data scales, AgenticMath outperforms all compared baselines across four base models on six math benchmarks](agenticmath-sota-at-small-data-scales.md) — related
- [The domain-specialized 32-billion-parameter model surpasses significantly larger general-purpose models such as Qwen3-235B-A22B-Thinking (86.63%) and Qwen2.5-72B-Instruct (78.60%) on the CDPK Benchmark](domain-specialized-32b-outperforms-larger-models.md) — related
- [Fine-tuning LLMs on 30K-90K AgenticMath samples matches or surpasses baselines trained on 400K-2.3M samples on math reasoning benchmarks](agenticmath-small-data-matches-large-scale-baselines.md) — related
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — related
- [In the fine-tuning experiments, increasing base model size up to 32B parameters improved performance, and larger LLMs consistently outperformed smaller MLMs](model-size-and-llm-vs-mlm-performance-vocabulary-difficulty.md) — related
