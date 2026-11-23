---
type: claim
title: Construction-time repair success does not predict downstream transfer, so rewrite teachers should be evaluated through distilled-student performance
description: Construction-time repair success does not predict downstream transfer, so rewrite teachers should be evaluated through distilled-student performance
id: repair-success-does-not-predict-transfer
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: shaoang-li-2026
    resource: "https://doi.org/10.48550/arXiv.2610.23831"
    title: "Shaoang Li, Yanhang Shi, Yufei Li, Mingfu Liang, Frank Shyu, Sandeep Pandey, Luke Simon, Xi Liu, Jian Li. (2026). Beyond the Answer: Student-Conditioned Trace Construction for Reasoning Distillation. [doi:10.48550/arXiv.2610.23831](https://doi.org/10.48550/arXiv.2610.23831)"
    author: Shaoang Li, Yanhang Shi, Yufei Li, Mingfu Liang, Frank Shyu, Sandeep Pandey, Luke Simon, Xi Liu, Jian Li
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Construction-time repair success does not predict downstream transfer, so rewrite teachers should be evaluated through distilled-student performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A rewrite teacher with higher repair success can yield lower transfer EM: Gemma4-26B-A4B has higher repair success than Qwen3-14B (62.15% versus 61.78%) but lower 2Wiki EM (0.624 vs. 0.686). [→ Shaoang Li 2026](#shaoang-li-2026)

## Evidence

### Shaoang Li 2026

Shaoang Li, Yanhang Shi, Yufei Li, Mingfu Liang, Frank Shyu, Sandeep Pandey, Luke Simon, Xi Liu, Jian Li. (2026). Beyond the Answer: Student-Conditioned Trace Construction for Reasoning Distillation. [doi:10.48550/arXiv.2610.23831](https://doi.org/10.48550/arXiv.2610.23831)

`q2 · i?` · `causal · r2`

Rewrite-teacher sweep with a fixed Qwen3-8B student initialization (Appendix Table 6) comparing construction-time repair success with downstream 2Wiki EM; the printed percentages and EMs invert the ordering.

> "Gemma4-26B-A4B has higher reported repair success than Qwen3-14B (62.15% versus 61.78%) but yields lower 2Wiki EM (0.624 vs. 0.686)."

## Discussion


## Related Claims
- Draft conditioning and answer-assisted repair matter most for transfer performance — related
- ReDiST supervision achieves the highest reported point estimates across all four benchmarks in the primary Qwen3-8B comparison, including 58.4% MuSiQue EM and 68.6% 2Wiki EM — related
- [Answer-only and original-trace supervision rank differently on source-task versus cross-benchmark performance](answer-only-original-trace-rank-reversal.md) — a broader claim this one bears on
- ReDiST gains extend across four target students from two model families, though its advantage over competing strategies depends on the student — related
