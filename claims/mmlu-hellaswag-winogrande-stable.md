---
type: claim
title: Performance on MMLU, HellaSwag, and Winogrande remains relatively stable regardless of student or tutor response training
description: Performance on MMLU, HellaSwag, and Winogrande remains relatively stable regardless of student or tutor response training
id: mmlu-hellaswag-winogrande-stable
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: shashank-sonkar-2024
    resource: "https://doi.org/10.18653/v1/2024.findings-emnlp.912"
    title: "Shashank Sonkar, Naiming Liu, Richard G. Baraniuk. (2024). Student Data Paradox and Curious Case of Single Student-Tutor Model: Regressive Side Effects of Training LLMs for Personalized Learning. arXiv. [doi:10.18653/v1/2024.findings-emnlp.912](https://doi.org/10.18653/v1/2024.findings-emnlp.912)"
    author: Shashank Sonkar, Naiming Liu, Richard G. Baraniuk
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Performance on MMLU, HellaSwag, and Winogrande remains relatively stable regardless of student or tutor response training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` MMLU, HellaSwag, and Winogrande scores stayed relatively stable whether models were trained on tutor or student responses. [→ Shashank Sonkar 2024](#shashank-sonkar-2024)

## Evidence

### Shashank Sonkar 2024

Shashank Sonkar, Naiming Liu, Richard G. Baraniuk. (2024). Student Data Paradox and Curious Case of Single Student-Tutor Model: Regressive Side Effects of Training LLMs for Personalized Learning. arXiv. [doi:10.18653/v1/2024.findings-emnlp.912](https://doi.org/10.18653/v1/2024.findings-emnlp.912)

`q2 · i?` · `causal · r1`

Benchmark evaluation (Table 2) across the seven-benchmark suite; the article reports stability for these three benchmarks, e.g. MMLU 51.04 (vicuna-7b) versus 50.77 (student-7b). No effect size or test printed.

> "The performance of models on the MMLU, HellaSwag, and Winogrande benchmarks remained relatively stable, regardless of whether they were trained to model tutor or student responses."

## Discussion


## Related Claims
- [On benchmarks, GPT-3.5-turbo outperformed the fine-tuned Phi model in knowledge and story completion, while PhinetunEd scored best in story generation](phinetuned-benchmark-comparison-gpt.md) — related
- [Longer student histories do not improve LLM knowledge tracing: FKT AUC-ROC stays near 0.5-0.6 whether models see 50 or 400 prior interactions](context-length-no-effect-fkt.md) — related
- [Training LLMs on student-tutor dialogues to model student behavior significantly reduces reasoning accuracy on the ARC benchmark](student-data-paradox-arc-decline.md) — related
- [Training LLMs on tutor responses does not produce the performance decline seen with student-response training](tutor-control-no-decline.md) — related
