---
type: claim
title: In the fine-tuning experiments, increasing base model size up to 32B parameters improved performance, and larger LLMs consistently outperformed smaller MLMs
description: In the fine-tuning experiments, increasing base model size up to 32B parameters improved performance, and larger LLMs consistently outperformed smaller MLMs
id: model-size-and-llm-vs-mlm-performance-vocabulary-difficulty
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: adam-nohejl-2026
    resource: "https://doi.org/10.48550/arxiv.2605.14257"
    title: "Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka. (2026). Sakura at BEA 2026 Shared Task 1: What Makes Vocabulary Difficult? https://arxiv.org/abs/2605.14257 [doi:10.48550/arxiv.2605.14257](https://doi.org/10.48550/arxiv.2605.14257)"
    author: Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# In the fine-tuning experiments, increasing base model size up to 32B parameters improved performance, and larger LLMs consistently outperformed smaller MLMs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`

## Subclaims
`q2 i?` Performance improved with base model size up to 32B parameters, and larger LLMs consistently outperformed smaller-sized MLMs, differing from prior LCP findings where smaller MLMs performed comparably to larger LLMs. [→ Adam Nohejl 2026](#adam-nohejl-2026)

## Evidence

### Adam Nohejl 2026

Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka. (2026). Sakura at BEA 2026 Shared Task 1: What Makes Vocabulary Difficult? https://arxiv.org/abs/2605.14257 [doi:10.48550/arxiv.2605.14257](https://doi.org/10.48550/arxiv.2605.14257)

`q2 · i?` · `causal · r?`

Conclusion-level summary of the fine-tuning experiments (Section 5.1, Table 2; Appendix E), where individual LLMs up to 32B (GLM-4-32B, Qwen2.5-32B, Ministral-3-14B) and MLMs were compared. The authors hypothesize the LLM advantage is due to the more complex nature of vocabulary difficulty prediction compared to LCP.

> "increases in base model size up to 32B parameters resulted in performance improvements"

## Discussion


## Related Claims
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — related
- [The domain-specialized 32-billion-parameter model surpasses significantly larger general-purpose models such as Qwen3-235B-A22B-Thinking (86.63%) and Qwen2.5-72B-Instruct (78.60%) on the CDPK Benchmark](domain-specialized-32b-outperforms-larger-models.md) — related
- [Fine-tuning LLMs and MLMs with cross-entropy loss using soft targets outperforms standard discretization and regression-head approaches on vocabulary difficulty prediction](soft-target-finetuning-beats-standard-loss-vocabulary-difficulty.md) — related
