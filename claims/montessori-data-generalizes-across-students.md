---
type: claim
title: "Data from a teacher optimized for a 1.1B student's preferences yields consistent gains across four different student models"
description: "Data from a teacher optimized for a 1.1B student's preferences yields consistent gains across four different student models"
id: montessori-data-generalizes-across-students
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

# Data from a teacher optimized for a 1.1B student's preferences yields consistent gains across four different student models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Data synthesized by a teacher optimized toward the 1.1B student's preferences leads to consistent performance gains across Llama3-8B, Mistral-7B, Qwen1.5-7B and Gemma2-9B students compared to Self-Instruct. [→ Xiaochuan Li 2024](#xiaochuan-li-2024)

## Evidence

### Xiaochuan Li 2024

Xiaochuan Li, Zichun Yu, Chenyan Xiong. (2024). MONTESSORI-INSTRUCT: GENERATE INFLUENTIAL TRAINING DATA TAILORED FOR STUDENT LEARNING. Preprint. [doi:10.48550/arXiv.2410.14208](https://doi.org/10.48550/arXiv.2410.14208)

`q2 · i?` · `causal · r2`

Generalization experiment (§5.4, Figure 5) training four student models (Llama3-8B, Mistral-7B, Qwen1.5-7B, Gemma2-9B) on data from the teacher optimized for the 1.1B student's preferences. The article reports "consistent performance gains across all the students compared to Self-Instruct".

> "As shown in Figure 5, the data synthesized by one teacher leads to consistent performance gains across all the students compared to Self-Instruct."

## Discussion


## Related Claims
- [Local data influence captures student data preferences better than LLM-as-a-Judge or training loss, and optimizing the teacher beats bootstrapping](local-influence-and-teacher-optimization-ablations.md) — related
- [Montessori-Instruct significantly outperforms Self-Instruct on in-domain Alpaca Eval in the 8B setting](montessori-instruct-outperforms-self-instruct-alpaca-eval.md) — related
- [Montessori-Instruct outperforms all baselines on out-of-domain tasks, with maximum MT-Bench improvements of 0.673 and 0.372](montessori-instruct-out-of-domain-gains.md) — related
- [Data tailored to the student by a weaker teacher surpasses data from the stronger GPT-4o teacher](tailored-weaker-teacher-beats-gpt4o-data.md) — related
