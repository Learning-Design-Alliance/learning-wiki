---
type: claim
title: Iterative Retrieval Enhancement improves repair accuracy and B-F1, with gains continuing over three iterations
description: Iterative Retrieval Enhancement improves repair accuracy and B-F1, with gains continuing over three iterations
id: iterative-retrieval-enhancement-improves-repair
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: zhenlong-dai-2026
    resource: "https://doi.org/10.1609/aaai.v40i36.40300"
    title: "Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen. (2026). Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement. [doi:10.1609/aaai.v40i36.40300](https://doi.org/10.1609/aaai.v40i36.40300)"
    author: Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Iterative Retrieval Enhancement improves repair accuracy and B-F1, with gains continuing over three iterations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Using evaluation results of generated code as retrieval signals, iterative retrieval enhancement raises accuracy: LSGEN iter1 outperforms LSGEN base by 7.37% in accuracy and 2.99% in B-F1 on Qwen3-Embedding-0.6B, and accuracy rises from 87.96% to 91.40% from iter1 to iter3. [→ Zhenlong Dai 2026](#zhenlong-dai-2026)

## Evidence

### Zhenlong Dai 2026

Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen. (2026). Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement. [doi:10.1609/aaai.v40i36.40300](https://doi.org/10.1609/aaai.v40i36.40300)

`q2 · i?` · `design · r2`

Experiments varying iteration count from 0 to 3 across three retrieval models on GPT-4o (Fig. 3b). The article reports "LSGEN iter1 outperforms the LSGEN base by 7.37% in accuracy and 2.99% in B-F1" and continued improvement through iter3.

> "on Qwen3-Embedding-0.6B, LSGEN iter1 outperforms the LSGEN base by 7.37% in accuracy and 2.99% in B-F1. From LSGEN iter1 to LSGEN iter3, accuracy rises from 87.96% to 91.40%."

## Discussion


## Related Claims
- [Edit-driven solution retrieval outperforms code-similarity retrieval for program repair](edit-driven-retrieval-beats-code-retrieval.md) — related
- [LSGEN outperforms program-repair baselines on LPR-Bench in code accuracy and bug-description F1](lsgen-outperforms-lpr-baselines.md) — related
- [Each LSGEN component contributes: removing any component decreases accuracy and B-F1, with reference-inspired generation most critical for smaller models](lsgen-ablation-component-contributions.md) — related
- [Beam search-based self-refinement improves simulated solution alignment with predicted student behavior](beam-search-self-refinement-improves-solution-simulation.md) — related
