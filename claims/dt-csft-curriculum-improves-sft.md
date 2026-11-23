---
type: claim
title: DT-CSFT curriculum learning, which front-loads preliminary instruction categories, improves SFT performance over DEITA
description: DT-CSFT curriculum learning, which front-loads preliminary instruction categories, improves SFT performance over DEITA
id: dt-csft-curriculum-improves-sft
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: hanyu-zhao-2025
    resource: "https://doi.org/10.1609/aaai.v39i24.34798"
    title: "Hanyu Zhao, Li Du, Yiming Ju, Chengwei Wu, Tengfei Pan. (2025). Beyond IID: Optimizing Instruction Learning from the Perspective of Instruction Interaction and Dependency. Originally published 2024. [doi:10.1609/aaai.v39i24.34798](https://doi.org/10.1609/aaai.v39i24.34798)"
    author: Hanyu Zhao, Li Du, Yiming Ju, Chengwei Wu, Tengfei Pan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# DT-CSFT curriculum learning, which front-loads preliminary instruction categories, improves SFT performance over DEITA

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Adjusting only the learning order of instruction categories so preliminary categories dominate early SFT improves performance in general over the DEITA baseline, including on Llama-3 using a taxonomy induced from Qwen 1.5. [→ Hanyu Zhao 2025](#hanyu-zhao-2025)

## Evidence

### Hanyu Zhao 2025

Hanyu Zhao, Li Du, Yiming Ju, Chengwei Wu, Tengfei Pan. (2025). Beyond IID: Optimizing Instruction Learning from the Perspective of Instruction Interaction and Dependency. Originally published 2024. [doi:10.1609/aaai.v39i24.34798](https://doi.org/10.1609/aaai.v39i24.34798)

`q2 · i?` · `causal · r2`

Curriculum fine-tuning experiment on DEITA-selected sets of 10,000, 20,000, and 50,000 instances, where the first |D| instances increase the proportion of preliminary category instructions by 50%. The authors add that "the performance of LLama-3 could also be improved" from the Qwen-induced taxonomy; no effect size is printed.

> "Compared to the strong baseline DEITA, by only ad- justing the order of learning different categories of in- struction, DT-CSFT demonstrates improved performance in general."

## Discussion


## Related Claims
- [Uniformly adding more preliminary-category instructions (Mix+) does not necessarily improve performance, unlike sequenced curriculum learning](mix-plus-uniform-addition-not-beneficial.md) — related
- [EE-CPO improves LLM performance over the DEITA baseline by optimizing instruction category proportion alone](ee-cpo-improves-over-deita.md) — related
