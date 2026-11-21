---
type: claim
title: Edit-driven solution retrieval outperforms code-similarity retrieval for program repair
description: Edit-driven solution retrieval outperforms code-similarity retrieval for program repair
id: edit-driven-retrieval-beats-code-retrieval
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

# Edit-driven solution retrieval outperforms code-similarity retrieval for program repair

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Compared with retrieval based on cosine similarity between buggy codes (Code Retrieval), iterative retrieval enhancement is 15.23% higher in code accuracy and 5.13% higher in B-F1 on GPT-4o. [→ Zhenlong Dai 2026](#zhenlong-dai-2026)

## Evidence

### Zhenlong Dai 2026

Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen. (2026). Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement. [doi:10.1609/aaai.v40i36.40300](https://doi.org/10.1609/aaai.v40i36.40300)

`q2 · i?` · `design · r2`

Comparative experiments across retrieval methods (PSM, Hamming distance, edit distance, Code Retrieval, edit-driven) on GPT-4o and Qwen2.5-Coder-7B, shown in Fig. 3(a) with three iterations. The article reports "15.23% higher in code accuracy and 5.13% higher in B-F1 than Code Retrieval".

> "For example, Iterative Retrieval Enhancement is 15.23% higher in code accuracy and 5.13% higher in B-F1 than Code Retrieval on GPT-4o."

## Discussion


## Related Claims
- [LSGEN outperforms program-repair baselines on LPR-Bench in code accuracy and bug-description F1](lsgen-outperforms-lpr-baselines.md) — related
- [Iterative Retrieval Enhancement improves repair accuracy and B-F1, with gains continuing over three iterations](iterative-retrieval-enhancement-improves-repair.md) — related
- [Each LSGEN component contributes: removing any component decreases accuracy and B-F1, with reference-inspired generation most critical for smaller models](lsgen-ablation-component-contributions.md) — related
