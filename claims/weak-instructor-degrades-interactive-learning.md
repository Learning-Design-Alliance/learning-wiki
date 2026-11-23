---
type: claim
title: Interactive clarification degrades learning when the instructor model is too small
description: Interactive clarification degrades learning when the instructor model is too small
id: weak-instructor-degrades-interactive-learning
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: zhengyu-hu-2025
    resource: "https://doi.org/10.52202/085713-5760"
    title: "Zhengyu Hu, Jianxun Lian, Zheyuan Xiao, Seraphina Zhang, Tianfu Wang, Nicholas Jing Yuan, Xing Xie, Hui Xiong. (2025). Unveiling the Learning Mind of Language Models: A Cognitive Framework and Empirical Study. NeurIPS 2025. [doi:10.52202/085713-5760](https://doi.org/10.52202/085713-5760)"
    author: Zhengyu Hu, Jianxun Lian, Zheyuan Xiao, Seraphina Zhang, Tianfu Wang, Nicholas Jing Yuan, Xing Xie, Hui Xiong
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Interactive clarification degrades learning when the instructor model is too small

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` When the instructor is extremely small (e.g., Qwen2.5-1.5B), learners trained with Interactive Clarification underperform those trained passively on tasks such as GSM8K, MATH, and SAT. [→ Zhengyu Hu 2025](#zhengyu-hu-2025)

## Evidence

### Zhengyu Hu 2025

Zhengyu Hu, Jianxun Lian, Zheyuan Xiao, Seraphina Zhang, Tianfu Wang, Nicholas Jing Yuan, Xing Xie, Hui Xiong. (2025). Unveiling the Learning Mind of Language Models: A Cognitive Framework and Empirical Study. NeurIPS 2025. [doi:10.52202/085713-5760](https://doi.org/10.52202/085713-5760)

`q2 · i?` · `causal · r2`

Instructor-scaling study fixing the learner as Qwen2.5-7B and varying the instructor across Qwen2.5-1.5B, 7B, 32B, and 72B. The article reports that with a too-small instructor "the benefits of interactivity diminish or even become negative"; no effect size is printed.

> "However, when the instructor is too small (e.g., Qwen2.5-1.5B), the benefits of interactivity diminish or even become negative. In tasks such as GSM8K, MATH, and SAT, we observe that learners trained withInteractive Clarificationunderperform compared to those trained passively."

## Discussion


## Related Claims
- [Interactive clarification consistently outperforms passive consumption in instructor-based LLM learning across eight math benchmarks](interactive-clarification-beats-passive-consumption-llm.md) — reports the opposite
- [Larger learner models achieve higher normalized learning gains, with interactive clarification benefits growing as capacity increases](learner-scale-increases-interactive-learning-gains.md) — related
