---
type: claim
title: Training LLMs on student-tutor dialogues to model student behavior significantly reduces reasoning accuracy on the ARC benchmark
description: Training LLMs on student-tutor dialogues to model student behavior significantly reduces reasoning accuracy on the ARC benchmark
id: student-data-paradox-arc-decline
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
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

# Training LLMs on student-tutor dialogues to model student behavior significantly reduces reasoning accuracy on the ARC benchmark

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Fine-tuning Vicuna-7B on student responses dropped ARC accuracy from 53.24% to 40.61% relative to the base vicuna-7b model. [→ Shashank Sonkar 2024](#shashank-sonkar-2024)

## Evidence

### Shashank Sonkar 2024

Shashank Sonkar, Naiming Liu, Richard G. Baraniuk. (2024). Student Data Paradox and Curious Case of Single Student-Tutor Model: Regressive Side Effects of Training LLMs for Personalized Learning. arXiv. [doi:10.18653/v1/2024.findings-emnlp.912](https://doi.org/10.18653/v1/2024.findings-emnlp.912)

`q2 · i?` · `causal · r1`

Benchmark evaluation (Table 2, ARC 25-shot) comparing the base vicuna-7b-v1.5 model with the student-7b model fine-tuned on CLASS student-tutor dialogues; the article reports the accuracy "de- crease from 53.24% to 40.61%". No effect size or significance test is printed.

> "the vicuna-7b model saw its accuracy de- crease from 53.24% to 40.61% when trained on student dialogues."

## Discussion


## Related Claims
- [Training to model student responses drops TruthfulQA multiple-choice accuracy, with hallucination tokens partially recovering it](truthfulqa-mc2-drop-and-hal-recovery.md) — related
- [Training LLMs on tutor responses does not produce the performance decline seen with student-response training](tutor-control-no-decline.md) — related
- [Performance on MMLU, HellaSwag, and Winogrande remains relatively stable regardless of student or tutor response training](mmlu-hellaswag-winogrande-stable.md) — related
- ACER-trained models improve knowledge-intensive benchmarks ARC and GPQA by more than two absolute percentage points while remaining stable on AGIEval, GSM8K, and HellaSwag — related
