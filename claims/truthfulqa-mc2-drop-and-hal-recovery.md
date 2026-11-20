---
type: claim
title: Training to model student responses drops TruthfulQA multiple-choice accuracy, with hallucination tokens partially recovering it
description: Training to model student responses drops TruthfulQA multiple-choice accuracy, with hallucination tokens partially recovering it
id: truthfulqa-mc2-drop-and-hal-recovery
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

# Training to model student responses drops TruthfulQA multiple-choice accuracy, with hallucination tokens partially recovering it

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On TruthfulQA MC2, student-7b accuracy fell from 50.37% (vicuna-7b) to 36.14%, and recovered to 44.68% with hallucination tokens. [→ Shashank Sonkar 2024](#shashank-sonkar-2024)

## Evidence

### Shashank Sonkar 2024

Shashank Sonkar, Naiming Liu, Richard G. Baraniuk. (2024). Student Data Paradox and Curious Case of Single Student-Tutor Model: Regressive Side Effects of Training LLMs for Personalized Learning. arXiv. [doi:10.18653/v1/2024.findings-emnlp.912](https://doi.org/10.18653/v1/2024.findings-emnlp.912)

`q2 · i?` · `causal · r1`

TruthfulQA MC2 in-depth analysis (Table 1) comparing vicuna-7b, student-7b, and student-hal-7b; the article reports the drop "from 50.37% in the vicuna-7b model to 36.14%" and, with hallucination tokens, "accuracy recovering to 44.68%". No effect size printed.

> "The student-7b model experienced a significant drop in accuracy, from 50.37% in the vicuna-7b model to 36.14% when trained to model student responses."

## Discussion


## Related Claims
- [Hallucination tokens substantially improve performance across benchmarks but do not fully restore baseline performance](hallucination-tokens-partial-recovery.md) — related
- [Training LLMs on student-tutor dialogues to model student behavior significantly reduces reasoning accuracy on the ARC benchmark](student-data-paradox-arc-decline.md) — related
- [Training to model student responses substantially reduces TruthfulQA generation quality, largely recovered by hallucination tokens](truthfulqa-generation-rouge-decline.md) — related
- [Training LLMs on tutor responses does not produce the performance decline seen with student-response training](tutor-control-no-decline.md) — related
