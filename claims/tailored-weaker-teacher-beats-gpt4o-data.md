---
type: claim
title: Data tailored to the student by a weaker teacher surpasses data from the stronger GPT-4o teacher
description: Data tailored to the student by a weaker teacher surpasses data from the stronger GPT-4o teacher
id: tailored-weaker-teacher-beats-gpt4o-data
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: xiaochuan-li-2024
    resource: "https://doi.org/10.48550/arXiv.2410.14208"
    title: "Xiaochuan Li, Zichun Yu, Chenyan Xiong. (2024). MONTESSORI-INSTRUCT: GENERATE INFLUENTIAL TRAINING DATA TAILORED FOR STUDENT LEARNING. Preprint. [doi:10.48550/arXiv.2410.14208](https://doi.org/10.48550/arXiv.2410.14208)"
    author: Xiaochuan Li, Zichun Yu, Chenyan Xiong
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Data tailored to the student by a weaker teacher surpasses data from the stronger GPT-4o teacher

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Montessori-Instruct with Llama3-8B-Instruct as teacher still surpasses Self-Instruct with GPT-4o as the teacher, suggesting a stronger LLM does not necessarily produce more beneficial data than a weaker LLM tailored to the student. [→ Xiaochuan Li 2024](#xiaochuan-li-2024)

## Evidence

### Xiaochuan Li 2024

Xiaochuan Li, Zichun Yu, Chenyan Xiong. (2024). MONTESSORI-INSTRUCT: GENERATE INFLUENTIAL TRAINING DATA TAILORED FOR STUDENT LEARNING. Preprint. [doi:10.48550/arXiv.2410.14208](https://doi.org/10.48550/arXiv.2410.14208)

`q2 · i?` · `causal · r2`

Comparison in §5.1 (Table 1) between Montessori-Instruct data from the Llama3-8B-Instruct teacher and Self-Instruct data synthesized by GPT-4o, both training the Llama3-8B student on 10K pairs. The article states the tailored weaker teacher "still surpasses Self-Instruct with GPT-4o as the teacher".

> "Notably, our method still surpasses Self-Instruct with GPT-4o as the teacher, suggesting that a stronger LLM does not necessarily produce more beneficial data than a weaker LLM that is tailored to the student's needs."

## Discussion


## Related Claims
- [Montessori-Instruct significantly outperforms Self-Instruct on in-domain Alpaca Eval in the 8B setting](montessori-instruct-outperforms-self-instruct-alpaca-eval.md) — related
- [Data from a teacher optimized for a 1.1B student's preferences yields consistent gains across four different student models](montessori-data-generalizes-across-students.md) — related
