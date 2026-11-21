---
type: claim
title: "Each LSGEN component contributes: removing any component decreases accuracy and B-F1, with reference-inspired generation most critical for smaller models"
description: "Each LSGEN component contributes: removing any component decreases accuracy and B-F1, with reference-inspired generation most critical for smaller models"
id: lsgen-ablation-component-contributions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: zhenlong-dai-2026
    resource: "https://doi.org/10.1609/aaai.v40i36.40300"
    title: "Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen. (2026). Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement. [doi:10.1609/aaai.v40i36.40300](https://doi.org/10.1609/aaai.v40i36.40300)"
    author: Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Each LSGEN component contributes: removing any component decreases accuracy and B-F1, with reference-inspired generation most critical for smaller models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In ablations on GPT-4o, Claude-4 and Qwen2.5-Coder-7B, removing edit-driven retrieval, iterative enhancement, or reference-inspired solution generation each lowers accuracy and B-F1; removing reference-inspired generation drops Qwen2.5-Coder-7B accuracy from 51.11% to 25.55%. [→ Zhenlong Dai 2026](#zhenlong-dai-2026)

## Evidence

### Zhenlong Dai 2026

Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen. (2026). Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement. [doi:10.1609/aaai.v40i36.40300](https://doi.org/10.1609/aaai.v40i36.40300)

`q2 · i?` · `causal · r2`

Ablation study (Table 3) removing each LSGEN component with iterations set to 1. The article reports "Removing each component results in a decrease in the performance of accuracy and B-F1" and a notable drop for Qwen2.5-Coder-7B without reference-inspired generation (51.11% to 25.55% accuracy).

> "Removing each component results in a decrease in the performance of accuracy and B-F1, which demonstrates the effectiveness of each component."

## Discussion


## Related Claims
- [Edit-driven solution retrieval outperforms code-similarity retrieval for program repair](edit-driven-retrieval-beats-code-retrieval.md) — related
- [Iterative Retrieval Enhancement improves repair accuracy and B-F1, with gains continuing over three iterations](iterative-retrieval-enhancement-improves-repair.md) — related
- [LSGEN outperforms program-repair baselines on LPR-Bench in code accuracy and bug-description F1](lsgen-outperforms-lpr-baselines.md) — related
