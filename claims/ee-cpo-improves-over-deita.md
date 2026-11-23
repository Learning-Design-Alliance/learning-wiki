---
type: claim
title: EE-CPO improves LLM performance over the DEITA baseline by optimizing instruction category proportion alone
description: EE-CPO improves LLM performance over the DEITA baseline by optimizing instruction category proportion alone
id: ee-cpo-improves-over-deita
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

# EE-CPO improves LLM performance over the DEITA baseline by optimizing instruction category proportion alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Hanyu Zhao 2024: the intervention came bundled with another change (read from the study by two models, 2026-11-23)

## Subclaims
`q2 i?` Compared to DEITA, EE-CPO further increases LLM performance by optimizing only the proportion of instruction categories, without adding instances, with consistent advantage across sample sizes. [→ Hanyu Zhao 2025](#hanyu-zhao-2025)

## Evidence

### Hanyu Zhao 2025

Hanyu Zhao, Li Du, Yiming Ju, Chengwei Wu, Tengfei Pan. (2025). Beyond IID: Optimizing Instruction Learning from the Perspective of Instruction Interaction and Dependency. Originally published 2024. [doi:10.1609/aaai.v39i24.34798](https://doi.org/10.1609/aaai.v39i24.34798)

`q2 · i?` · `causal · r2`

Fine-tuning experiment on instruction sets of 10,000, 20,000, and 50,000 instructions, evaluated on MT-Bench and AlpacaEval 2.0 with Llama3-8B and Qwen-1.5-7B; Table 4 reports EE-CPO (50k) at 7.17 and 7.51 on MT-Bench versus DEITA (50k) at 7.02 and 7.13. No effect size is printed.

> "Compared to the State-of-the-Art method DEITA, our approach EE-CPO could further increase the performance of LLMs by only optimizing the proportion of instruction category, without incorporating additional instances."

## Discussion


## Related Claims
- [Negative effect equivalence coefficients were observed between instruction categories; performance on one category fell from pre-test to post-test after another category was added, in one single-group pre-post study](antagonistic-instruction-category-effects.md) — related
- [DT-CSFT curriculum learning, which front-loads preliminary instruction categories, improves SFT performance over DEITA](dt-csft-curriculum-improves-sft.md) — related
- [Uniformly adding more preliminary-category instructions (Mix+) does not necessarily improve performance, unlike sequenced curriculum learning](mix-plus-uniform-addition-not-beneficial.md) — related
