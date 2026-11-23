---
type: claim
title: Montessori-Instruct significantly outperforms Self-Instruct on in-domain Alpaca Eval in the 8B setting
description: Montessori-Instruct significantly outperforms Self-Instruct on in-domain Alpaca Eval in the 8B setting
id: montessori-instruct-outperforms-self-instruct-alpaca-eval
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

# Montessori-Instruct significantly outperforms Self-Instruct on in-domain Alpaca Eval in the 8B setting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Training Llama3-8B on data synthesized by the preference-optimized teacher significantly outperforms Self-Instruct by 6.37% LC-WR and 10.15% WR on Alpaca Eval. [→ Xiaochuan Li 2024](#xiaochuan-li-2024)

## Evidence

### Xiaochuan Li 2024

Xiaochuan Li, Zichun Yu, Chenyan Xiong. (2024). MONTESSORI-INSTRUCT: GENERATE INFLUENTIAL TRAINING DATA TAILORED FOR STUDENT LEARNING. Preprint. [doi:10.48550/arXiv.2410.14208](https://doi.org/10.48550/arXiv.2410.14208)

`q2 · i?` · `causal · r2`

Evaluation results (§5.1, Table 1) comparing students trained on 10K instruction-response pairs from the optimized teacher versus the unoptimized Self-Instruct teacher, using Alpaca Eval 2.0 with gpt-4-turbo as evaluator. The article reports the method "significantly outperforms Self-Instruct by 6.37% LC-WR and 10.15% WR".

> "In the 8B setting, Montessori-Instruct significantly outperforms Self-Instruct by 6.37% LC-WR and 10.15% WR on Alpaca Eval."

## Discussion


## Related Claims
- [Local data influence captures student data preferences better than LLM-as-a-Judge or training loss, and optimizing the teacher beats bootstrapping](local-influence-and-teacher-optimization-ablations.md) — a broader claim this one bears on
- [Data from a teacher optimized for a 1.1B student's preferences yields consistent gains across four different student models](montessori-data-generalizes-across-students.md) — related
- [Montessori-Instruct outperforms all baselines on out-of-domain tasks, with maximum MT-Bench improvements of 0.673 and 0.372](montessori-instruct-out-of-domain-gains.md) — related
- [Data tailored to the student by a weaker teacher surpasses data from the stronger GPT-4o teacher](tailored-weaker-teacher-beats-gpt4o-data.md) — related
