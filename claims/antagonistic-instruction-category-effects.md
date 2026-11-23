---
type: claim
title: Negative effect equivalence coefficients were observed between instruction categories; performance on one category fell from pre-test to post-test after another category was added, in one single-group pre-post study
description: Negative effect equivalence coefficients were observed between instruction categories; performance on one category fell from pre-test to post-test after another category was added, in one single-group pre-post study
id: antagonistic-instruction-category-effects
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

# Negative effect equivalence coefficients were observed between instruction categories; performance on one category fell from pre-test to post-test after another category was added, in one single-group pre-post study

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A large proportion of effect equivalence coefficients were negative, and performance on one category fell from pre-test to post-test after another category was added, in one single-group pre-post study. [→ Hanyu Zhao 2025](#hanyu-zhao-2025)

## Evidence

### Hanyu Zhao 2025

Hanyu Zhao, Li Du, Yiming Ju, Chengwei Wu, Tengfei Pan. (2025). Beyond IID: Optimizing Instruction Learning from the Perspective of Instruction Interaction and Dependency. Originally published 2024. [doi:10.1609/aaai.v39i24.34798](https://doi.org/10.1609/aaai.v39i24.34798)

`q2 · i?` · `causal · r2`

Causal intervention analysis of effect equivalence coefficients between 29 instruction categories on Qwen-1.5-7B and Llama3-8B. The authors note this "highlights the necessity of optimizing the category proportion of the whole instruction set beyond filtering individual high-quality instructions"; no effect size is printed.

> "Besides the positive relationships, the negative elements also account for a large proportion of the effect equivalence coefficients (e.g., The influence of Programming Ability on Text Summarization to Story Understanding)."

## Discussion


## Related Claims
- [Incorporating example problems does not necessarily improve LLM teaching and can degrade it via a shift to example-specific error correction](example-problems-degrade-llm-teaching.md) — a narrower finding that bears on this claim
- [Correlation patterns between categories of instructions are widespread across multiple instruction categories and different LLMs](widespread-instruction-category-correlation-patterns.md) — a broader claim this one bears on
- [EE-CPO improves LLM performance over the DEITA baseline by optimizing instruction category proportion alone](ee-cpo-improves-over-deita.md) — related
