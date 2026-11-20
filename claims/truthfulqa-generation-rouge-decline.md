---
type: claim
title: Training to model student responses substantially reduces TruthfulQA generation quality, largely recovered by hallucination tokens
description: Training to model student responses substantially reduces TruthfulQA generation quality, largely recovered by hallucination tokens
id: truthfulqa-generation-rouge-decline
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
  - id: shashank-sonkar-2024-2
    resource: "https://doi.org/10.18653/v1/2024.findings-emnlp.912"
    title: "Shashank Sonkar, Naiming Liu, Richard G. Baraniuk. (2024). Student Data Paradox and Curious Case of Single Student-Tutor Model: Regressive Side Effects of Training LLMs for Personalized Learning. arXiv. [doi:10.18653/v1/2024.findings-emnlp.912](https://doi.org/10.18653/v1/2024.findings-emnlp.912)"
    author: Shashank Sonkar, Naiming Liu, Richard G. Baraniuk
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Training to model student responses substantially reduces TruthfulQA generation quality, largely recovered by hallucination tokens

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1`–`r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On TruthfulQA generation, student-7b ROUGE (unigram) fell from 51.41 to 29.74, improving to 47.61 with hallucination tokens. [→ Shashank Sonkar 2024](#shashank-sonkar-2024)
`q2 i?` Hallucination tokens produced a significant recovery in generation performance. [→ Shashank Sonkar 2024 (2)](#shashank-sonkar-2024-2)

## Evidence

### Shashank Sonkar 2024

Shashank Sonkar, Naiming Liu, Richard G. Baraniuk. (2024). Student Data Paradox and Curious Case of Single Student-Tutor Model: Regressive Side Effects of Training LLMs for Personalized Learning. arXiv. [doi:10.18653/v1/2024.findings-emnlp.912](https://doi.org/10.18653/v1/2024.findings-emnlp.912)

`q2 · i?` · `causal · r1`

TruthfulQA generation task (Table 1) evaluated with ROUGE for 1-2 sentence answers; the article reports the decrease "from 51.41 in the vicuna-7b model to 29.74". No effect size printed.

> "The student-7b model saw a significant decrease in ROUGE scores, from 51.41 in the vicuna-7b model to 29.74, indicating a substantial loss in the ability to generate truthful, relevant responses."

### Shashank Sonkar 2024 (2)

Shashank Sonkar, Naiming Liu, Richard G. Baraniuk. (2024). Student Data Paradox and Curious Case of Single Student-Tutor Model: Regressive Side Effects of Training LLMs for Personalized Learning. arXiv. [doi:10.18653/v1/2024.findings-emnlp.912](https://doi.org/10.18653/v1/2024.findings-emnlp.912)

`q2 · i?` · `causal · r2`

Same TruthfulQA generation analysis; the article reports ROUGE "improving to 47.61" with hallucination tokens, still below the 51.41 baseline.

> "the introduction of hallucination tokens led to a significant recovery in performance, with ROUGE scores improving to 47.61."

## Discussion


## Related Claims
- [Hallucination tokens substantially improve performance across benchmarks but do not fully restore baseline performance](hallucination-tokens-partial-recovery.md) — related
- [Training to model student responses drops TruthfulQA multiple-choice accuracy, with hallucination tokens partially recovering it](truthfulqa-mc2-drop-and-hal-recovery.md) — related
- [Training LLMs on tutor responses does not produce the performance decline seen with student-response training](tutor-control-no-decline.md) — related
