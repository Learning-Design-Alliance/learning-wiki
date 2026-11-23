---
type: claim
title: Larger learner models achieve higher normalized learning gains, with interactive clarification benefits growing as capacity increases
description: Larger learner models achieve higher normalized learning gains, with interactive clarification benefits growing as capacity increases
id: learner-scale-increases-interactive-learning-gains
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

# Larger learner models achieve higher normalized learning gains, with interactive clarification benefits growing as capacity increases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Normalized learning gains increase with learner model scale, and the advantage of interactive clarification over passive consumption becomes more pronounced at larger scale. [→ Zhengyu Hu 2025](#zhengyu-hu-2025)

## Evidence

### Zhengyu Hu 2025

Zhengyu Hu, Jianxun Lian, Zheyuan Xiao, Seraphina Zhang, Tianfu Wang, Nicholas Jing Yuan, Xing Xie, Hui Xiong. (2025). Unveiling the Learning Mind of Language Models: A Cognitive Framework and Empirical Study. NeurIPS 2025. [doi:10.52202/085713-5760](https://doi.org/10.52202/085713-5760)

`q2 · i?` · `causal · r2`

Scaling study fixing the instructor as Qwen2.5-72B and varying the learner across Qwen2.5-1.5B, 7B, and 32B. The article reports a strong positive correlation between learner scale and normalized gains; Qwen2.5-32B reached "+25.7% and +23.8% normalized improvement" interactively versus passive values, with no standardized effect size printed.

> "Qwen2.5-32B demonstrates substantial gains under interactive supervision across all eight math-related benchmarks. For instance, in NUMGLUE and SVAMP, it achieves +25.7% and +23.8% normalized improvement, compared to +18.2% and +16.8% in the passive setting"

## Discussion


## Related Claims
- [Interactive clarification consistently outperforms passive consumption in instructor-based LLM learning across eight math benchmarks](interactive-clarification-beats-passive-consumption-llm.md) — related
- [Interactive clarification degrades learning when the instructor model is too small](weak-instructor-degrades-interactive-learning.md) — related
- [Adaptation gains grow monotonically with model capacity under the same LoRA recipe, though three data points cannot establish a scaling law](adaptation-gains-grow-with-model-capacity.md) — related
