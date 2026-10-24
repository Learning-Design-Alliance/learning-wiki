---
type: claim
title: Safety and Trustworthiness is strongly anti-correlated with Basic Education across the nine evaluated models (r = −0.83)
description: Safety and Trustworthiness is strongly anti-correlated with Basic Education across the nine evaluated models (r = −0.83)
id: safety-basic-education-anticorrelation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yilin-jiang-2026
    resource: "https://doi.org/10.48550/arxiv.2608.09548"
    title: "Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou. (2026). ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models. https://arxiv.org/abs/2608.09548 [doi:10.48550/arxiv.2608.09548](https://doi.org/10.48550/arxiv.2608.09548)"
    author: Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou
    q: 2
    i: 3
    kind: associational
    rigour: 1
---

# Safety and Trustworthiness is strongly anti-correlated with Basic Education across the nine evaluated models (r = −0.83)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2` · `i3` large
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i3` Across the nine models, Basic Education is strongly anti-correlated with Safety (r = −0.83; Spearman −0.88), and the correlation is stable under leave-one-model-out recomputation. [→ Yilin Jiang 2026](#yilin-jiang-2026)

## Evidence

### Yilin Jiang 2026

Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou. (2026). ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models. https://arxiv.org/abs/2608.09548 [doi:10.48550/arxiv.2608.09548](https://doi.org/10.48550/arxiv.2608.09548)

`q2 · i3` · `associational · r1`

Correlational analysis across the nine evaluated models in the results section (Figure 2 scatter). The article prints r = −0.83 (Pearson) and Spearman −0.88 with a leave-one-model-out range of [−0.88, −0.79], reporting that "nosinglemodeldrivesit". No significance test beyond this stability check is printed.

> "Across the nine models, Basic Education is strongly anti-correlated with Safety (r=−0.83, Spearman−0.88; Figure 2), and the correlation is stable under leave-one-model-out recomputation ([−0.88,−0.79]),sonosinglemodeldrivesit."

## Discussion


## Related Claims
- [Pedagogy and production dimensions associated most strongly with global quality (Spearman ρ = 0.68 and 0.66), while content was relatively independent (ρ = 0.46)](bespoke-pedagogy-production-correlate-with-global-quality.md) — related
- [The solving–pedagogy correlation is statistically fragile: leave-one-out Pearson correlations range from 0.251 to 0.887, rising to 0.887 when Qwen2.5-Math-7B-Instruct is removed](leave-one-out-fragility-solving-pedagogy-correlation.md) — related
- [Safety and task quality are largely independent across models, implying safety guardrails impose no measurable performance tax](safety-quality-independence-academiclaw.md) — reports the opposite
