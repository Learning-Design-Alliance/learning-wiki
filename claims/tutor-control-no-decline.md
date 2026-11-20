---
type: claim
title: Training LLMs on tutor responses does not produce the performance decline seen with student-response training
description: Training LLMs on tutor responses does not produce the performance decline seen with student-response training
id: tutor-control-no-decline
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
    rigour: 2
---

# Training LLMs on tutor responses does not produce the performance decline seen with student-response training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Control tutor-7b and tutor-13b models trained on the same dialogues to predict tutor responses did not show the regressive effects seen in student models. [→ Shashank Sonkar 2024](#shashank-sonkar-2024)

## Evidence

### Shashank Sonkar 2024

Shashank Sonkar, Naiming Liu, Richard G. Baraniuk. (2024). Student Data Paradox and Curious Case of Single Student-Tutor Model: Regressive Side Effects of Training LLMs for Personalized Learning. arXiv. [doi:10.18653/v1/2024.findings-emnlp.912](https://doi.org/10.18653/v1/2024.findings-emnlp.912)

`q2 · i?` · `causal · r2`

Control experiment (Section 4.4) training Vicuna models on the same CLASS dataset to predict tutor responses instead of student responses; Table 2 shows tutor-7b averaging 61.0 versus vicuna-7b's 60.8, while student-7b averaged 55.4.

> "Our findings, as shown in Table 2, revealed that training the LLMs on tutor responses did not lead to the same performance decline observed when modeling student responses."

## Discussion


## Related Claims
- [Training LLMs on student-tutor dialogues to model student behavior significantly reduces reasoning accuracy on the ARC benchmark](student-data-paradox-arc-decline.md) — related
- [Training to model student responses substantially reduces TruthfulQA generation quality, largely recovered by hallucination tokens](truthfulqa-generation-rouge-decline.md) — related
- [Performance on MMLU, HellaSwag, and Winogrande remains relatively stable regardless of student or tutor response training](mmlu-hellaswag-winogrande-stable.md) — related
- [Training to model student responses drops TruthfulQA multiple-choice accuracy, with hallucination tokens partially recovering it](truthfulqa-mc2-drop-and-hal-recovery.md) — related
