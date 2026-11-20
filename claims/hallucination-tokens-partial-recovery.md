---
type: claim
title: Hallucination tokens substantially improve performance across benchmarks but do not fully restore baseline performance
description: Hallucination tokens substantially improve performance across benchmarks but do not fully restore baseline performance
id: hallucination-tokens-partial-recovery
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

# Hallucination tokens substantially improve performance across benchmarks but do not fully restore baseline performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Introducing [hal] and [/hal] tokens during training yields substantial improvement across all datasets, yet baseline performance is not fully restored. [→ Shashank Sonkar 2024](#shashank-sonkar-2024)

## Evidence

### Shashank Sonkar 2024

Shashank Sonkar, Naiming Liu, Richard G. Baraniuk. (2024). Student Data Paradox and Curious Case of Single Student-Tutor Model: Regressive Side Effects of Training LLMs for Personalized Learning. arXiv. [doi:10.18653/v1/2024.findings-emnlp.912](https://doi.org/10.18653/v1/2024.findings-emnlp.912)

`q2 · i?` · `causal · r1`

Evaluation of student-hal models across the benchmark suite (Tables 1 and 2); for example student-hal-7b averages 58.0 versus student-7b's 55.4 and vicuna-7b's 60.8. The article reports improvement without a printed effect size.

> "Our results indicate a substantial improvement in the model's performance across all datasets after introducing this token. However, these tokens do not fully restore the model's baseline performance, underscoring the complexity of the issue."

## Discussion


## Related Claims
- [Training to model student responses substantially reduces TruthfulQA generation quality, largely recovered by hallucination tokens](truthfulqa-generation-rouge-decline.md) — related
- [Training to model student responses drops TruthfulQA multiple-choice accuracy, with hallucination tokens partially recovering it](truthfulqa-mc2-drop-and-hal-recovery.md) — related
- [Supervised fine-tuning on misconception-faithful demonstrations sharply improves SFS (up to +0.555 on Malrule for Qwen3-4B)](sft-improves-selective-update-behavior.md) — related
