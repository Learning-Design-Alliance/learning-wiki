---
type: claim
title: The top six models are statistically indistinguishable on overall ELBench score yet differ substantially at the module level, so module profiles are more informative than a single aggregate
description: The top six models are statistically indistinguishable on overall ELBench score yet differ substantially at the module level, so module profiles are more informative than a single aggregate
id: top-six-indistinguishable-overall-module-profile
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: yilin-jiang-2026
    resource: "https://arxiv.org/abs/2608.09548"
    title: "Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou. (2026). ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models. https://arxiv.org/abs/2608.09548"
    author: Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The top six models are statistically indistinguishable on overall ELBench score yet differ substantially at the module level, so module profiles are more informative than a single aggregate

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The top six models lie in overlapping 95% confidence intervals on overall score (roughly 83.1–83.7) and no adjacent pair is distinguishable at the P > 0.95 threshold. [→ Yilin Jiang 2026](#yilin-jiang-2026)
`q2 i?` Among those overall-tied leaders, module scores spread 19.5 points on Safety, 9.7 on Basic Education, and 7.0 on General Capability. [→ Yilin Jiang 2026](#yilin-jiang-2026)

## Evidence

### Yilin Jiang 2026

Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou. (2026). ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models. https://arxiv.org/abs/2608.09548

`q2 · i?` · `design · r2`

Results section of the nine-model evaluation of ELBench, with 95% bootstrap confidence intervals over items (10,000 resamples). The results report that models "indistinguishable on the overall score differ substantially at the module level", with spreads of 19.5 (Safety), 9.7 (Basic Education), and 7.0 (General Capability) points; the printed interval test threshold is P > 0.95.

> "The same six models that are indistinguishable on the overall score differ substantially at the module level, wherethescorespreadamongthemis19.5pointsonSafety, 9.7 on Basic Education, and 7.0 on General Capability."

## Discussion


## Related Claims
- [Within General Capability, model spread concentrates in competition mathematics (AIME), which dominates the aggregate score](aime-dominates-general-capability-spread.md) — related
- [The two education-specialized models lead neither education module, and the improvement from education-specific post-training is small relative to differences in general capability](education-specialized-models-lead-neither-education-module.md) — related
- [Claude Opus 4.8 has the highest overall score (0.803) and is the only model ranking in the top three on all three stages, yet does not saturate situated tutoring (0.773) or workflows (0.704)](claude-opus-48-highest-overall-unsaturated.md) — related
