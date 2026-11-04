---
type: claim
title: Observed case pass rates closely align with expected case pass rates computed under question independence
description: Observed case pass rates closely align with expected case pass rates computed under question independence
id: observed-cpr-matches-expected-independence-benchmark
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: cha-j-2026
    resource: "https://doi.org/10.2196/95342"
    title: "Cha J, Zhao Y, Zong H. (2026). Large Language Model Performance on Multistep Clinical Cases: Comparative Study Across Question and Case Levels. JMIR Medical Education. https://doi.org/10.2196/95342"
    author: Cha J, Zhao Y, Zong H.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Observed case pass rates closely align with expected case pass rates computed under question independence

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Expected CPRs under a conditional-independence assumption (76.6% DeepSeek-R1, 76.3% Qwen2.5-32B, 68.6% Gemini-2.5-Flash, 64.4% GPT-4o) closely matched the observed CPRs. [→ Cha J 2026](#cha-j-2026)

## Evidence

### Cha J 2026

Cha J, Zhao Y, Zong H. (2026). Large Language Model Performance on Multistep Clinical Cases: Comparative Study Across Question and Case Levels. JMIR Medical Education. https://doi.org/10.2196/95342

`q2 · i?` · `design · r2`

A stratified expected-CPR analysis grouped cases by length and used group-level question accuracy to estimate the probability of answering all questions in a case correctly under independence. Observed and expected values were closely aligned across models.

> "The expected CPRs were 76.6% for DeepSeek-R1, 76.3% for Qwen2.5-32B, 68.6% for Gemini-2.5-Flash, and 64.4% for GPT-4o."

## Discussion


## Related Claims
- [DeepSeek-R1 and Qwen2.5-32B significantly outperformed GPT-4o on both question-level and case-level accuracy](deepseek-qwen32b-outperform-gpt4o-clinical-cases.md) — related
- [Scaling Qwen2.5 from 3B to 32B parameters improved both metrics and reduced the consistency gap by approximately 50%](model-scaling-reduces-consistency-gap.md) — related
- [LLMs with high question-level accuracy on medical licensing exam cases show substantially lower case-level accuracy, with consistency gaps of 10% to 17.9%](llm-consistency-gap-question-vs-case-level.md) — related
