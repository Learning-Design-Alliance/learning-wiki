---
type: claim
title: Local data influence captures student data preferences better than LLM-as-a-Judge or training loss, and optimizing the teacher beats bootstrapping
description: Local data influence captures student data preferences better than LLM-as-a-Judge or training loss, and optimizing the teacher beats bootstrapping
id: local-influence-and-teacher-optimization-ablations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
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

# Local data influence captures student data preferences better than LLM-as-a-Judge or training loss, and optimizing the teacher beats bootstrapping

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Optimizing the teacher's parameters is generally better than merely bootstrapping influential data, and instruction optimization outperforms response optimization across all tasks. [→ Xiaochuan Li 2024](#xiaochuan-li-2024)

## Evidence

### Xiaochuan Li 2024

Xiaochuan Li, Zichun Yu, Chenyan Xiong. (2024). MONTESSORI-INSTRUCT: GENERATE INFLUENTIAL TRAINING DATA TAILORED FOR STUDENT LEARNING. Preprint. [doi:10.48550/arXiv.2410.14208](https://doi.org/10.48550/arXiv.2410.14208)

`q2 · i?` · `causal · r2`

Teacher-optimization ablation (§5.3, Table 2) comparing full teacher optimization against bootstrapping the top 50% influential data as seed and against response-only optimization. The article reports instruction optimization outperforms response optimization across all tasks, attributed to the smaller search space of response optimization.

> "optimizing the teacher is generally better than merely bootstrapping influential data, highlighting the necessity of adapting the teacher to the student's needs."

## Discussion


## Related Claims
- [Student performance correlates positively with the teacher's DPO optimization progress and with the share of positive-influence data](teacher-learning-student-performance-correlation.md) — related
- [Data from a teacher optimized for a 1.1B student's preferences yields consistent gains across four different student models](montessori-data-generalizes-across-students.md) — related
- [Montessori-Instruct significantly outperforms Self-Instruct on in-domain Alpaca Eval in the 8B setting](montessori-instruct-outperforms-self-instruct-alpaca-eval.md) — a narrower finding that bears on this claim
