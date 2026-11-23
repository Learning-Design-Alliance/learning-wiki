---
type: claim
title: Answer-only and original-trace supervision rank differently on source-task versus cross-benchmark performance
description: Answer-only and original-trace supervision rank differently on source-task versus cross-benchmark performance
id: answer-only-original-trace-rank-reversal
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
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

# Answer-only and original-trace supervision rank differently on source-task versus cross-benchmark performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Answer-only training raises MuSiQue source EM above the raw model while lowering 2Wiki transfer EM, whereas original-trace supervision shows the reverse profile, so higher source-task accuracy does not imply better transfer. [→ Shaoang Li 2026](#shaoang-li-2026)

## Evidence

### Shaoang Li 2026

Shaoang Li, Yanhang Shi, Yufei Li, Mingfu Liang, Frank Shyu, Sandeep Pandey, Luke Simon, Xi Liu, Jian Li. (2026). Beyond the Answer: Student-Conditioned Trace Construction for Reasoning Distillation. [doi:10.48550/arXiv.2610.23831](https://doi.org/10.48550/arXiv.2610.23831)

`q2 · i?` · `causal · r2`

Qwen3-8B benchmark experiment under MuSiQue supervision: answer-only reaches 0.562 source EM but 0.479 2Wiki EM, while original-trace reaches 0.426 and 0.521, "reversing the ranking of these two recipes across benchmarks".

> "Answer-only training raises MuSiQue EM from 0.342 to 0.562, while 2Wiki EM falls from 0.516 to 0.479. Original-trace supervision reaches 0.426 and 0.521, respectively, reversing the ranking of these two recipes across benchmarks."

## Discussion


## Related Claims
- ReDiST supervision achieves the highest reported point estimates across all four benchmarks in the primary Qwen3-8B comparison, including 58.4% MuSiQue EM and 68.6% 2Wiki EM — related
- ReDiST gains extend across four target students from two model families, though its advantage over competing strategies depends on the student — related
- Both trace and final-answer supervision are needed: answer-loss-only and trace-only objectives forfeit transfer gains or collapse overall — related
- Draft conditioning and answer-assisted repair matter most for transfer performance — related
- Selecting among student drafts improves supervision, and full ReDiST construction adds further gains that are larger on transfer benchmarks — related
- [Construction-time repair success does not predict downstream transfer, so rewrite teachers should be evaluated through distilled-student performance](repair-success-does-not-predict-transfer.md) — a narrower finding that bears on this claim
