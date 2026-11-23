---
type: claim
title: "Student performance correlates positively with the teacher's DPO optimization progress and with the share of positive-influence data"
description: "Student performance correlates positively with the teacher's DPO optimization progress and with the share of positive-influence data"
id: teacher-learning-student-performance-correlation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
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

# Student performance correlates positively with the teacher's DPO optimization progress and with the share of positive-influence data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across teacher checkpoints, student performance shows a positive correlation with the teacher's optimization progress (DPO learning margin), and the influence distribution of the teacher's synthetic data shifts toward the positive side as the teacher is optimized. [→ Xiaochuan Li 2024](#xiaochuan-li-2024)

## Evidence

### Xiaochuan Li 2024

Xiaochuan Li, Zichun Yu, Chenyan Xiong. (2024). MONTESSORI-INSTRUCT: GENERATE INFLUENTIAL TRAINING DATA TAILORED FOR STUDENT LEARNING. Preprint. [doi:10.48550/arXiv.2410.14208](https://doi.org/10.48550/arXiv.2410.14208)

`q2 · i?` · `causal · r2`

Analysis in §5.2 (Figures 3a-3d) comparing students trained on data from intermediate teacher checkpoints and examining local data influence distributions. The article observes that as the teacher is optimized, its synthetic data distribution "shifts towards the positive side", and the updated teacher maintains a higher proportion of positive-influence data than a regular teacher.

> "The results indicate a positive correlation between the student's performance and the teacher's optimization progress."

## Discussion


## Related Claims
- [Local data influence captures student data preferences better than LLM-as-a-Judge or training loss, and optimizing the teacher beats bootstrapping](local-influence-and-teacher-optimization-ablations.md) — related
- [A DPO-optimized Llama 2-7B model gives the best Rouge-L scores among all compared Socratic question generation methods, including GPT-3.5 and GPT-4 prompting baselines](dpo-llama2-best-rouge-l-socratic-question-generation.md) — related
- [DPO consistently outperforms supervised fine-tuning (SFT) for Socratic question generation with Llama 2](dpo-outperforms-sft-socratic-questions.md) — related
- [DPO training with IRT-likelihood preference pairs makes simulated student responses strongly follow their prompted ability (θ-Align)](dpo-irt-preference-pairs-ability-alignment.md) — related
