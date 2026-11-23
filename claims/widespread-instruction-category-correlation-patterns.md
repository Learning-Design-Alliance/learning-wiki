---
type: claim
title: Correlation patterns between categories of instructions are widespread across multiple instruction categories and different LLMs
description: Correlation patterns between categories of instructions are widespread across multiple instruction categories and different LLMs
id: widespread-instruction-category-correlation-patterns
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
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

# Correlation patterns between categories of instructions are widespread across multiple instruction categories and different LLMs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Effect equivalence coefficients reveal correlation patterns across multiple instruction categories and across different LLMs, with similar patterns across models. [→ Hanyu Zhao 2025](#hanyu-zhao-2025)

## Evidence

### Hanyu Zhao 2025

Hanyu Zhao, Li Du, Yiming Ju, Chengwei Wu, Tengfei Pan. (2025). Beyond IID: Optimizing Instruction Learning from the Perspective of Instruction Interaction and Dependency. Originally published 2024. [doi:10.1609/aaai.v39i24.34798](https://doi.org/10.1609/aaai.v39i24.34798)

`q2 · i?` · `causal · r2`

Causal intervention analysis fine-tuning Qwen-1.5-7B and Llama3-8B on a base instruction set with 1,000 instructions per category, adding 2,000 instructions of one category at a time. The authors report that "the correlation patterns show sim- ilarities across different LLMs"; no effect size is printed.

> "The existence of the correlation pattern is widespread, as it could be found across multiple categories, and upon dif- ferent LLMs. Moreover, the correlation patterns show sim- ilarities across different LLMs."

## Discussion


## Related Claims
- [Negative effect equivalence coefficients were observed between instruction categories; performance on one category fell from pre-test to post-test after another category was added, in one single-group pre-post study](antagonistic-instruction-category-effects.md) — a narrower finding that bears on this claim
- [Hierarchical clustering of effect equivalence coefficients was reported to identify two meta-groups: a Symbolic Reasoning group and a Commonsense Memorization group](instruction-meta-groups-symbolic-commonsense.md) — a narrower finding that bears on this claim
