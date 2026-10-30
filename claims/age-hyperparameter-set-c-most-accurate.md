---
type: claim
title: Hyperparameter setting with maximum token 53 and temperature 1 (Set C) yields the most accurate AGE grading performance
description: Hyperparameter setting with maximum token 53 and temperature 1 (Set C) yields the most accurate AGE grading performance
id: age-hyperparameter-set-c-most-accurate
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: mohammad-iqbal-2024
    resource: "https://doi.org/10.21203/rs.3.rs-5651820/v1"
    title: "Mohammad Iqbal, Tsamara Rana Nugraha and Hsing-Kuo Pao. (2024). Active Grade Estimator on Short Answer Assessment. https://doi.org/10.21203/rs.3.rs-5651820/v1"
    author: Mohammad Iqbal, Tsamara Rana Nugraha and Hsing-Kuo Pao
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Hyperparameter setting with maximum token 53 and temperature 1 (Set C) yields the most accurate AGE grading performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Set C with (max-token, temperature) = (53, 1) becomes the most accurate configuration in the hyperparameter ablation study. [→ Mohammad Iqbal 2024](#mohammad-iqbal-2024)

## Evidence

### Mohammad Iqbal 2024

Mohammad Iqbal, Tsamara Rana Nugraha and Hsing-Kuo Pao. (2024). Active Grade Estimator on Short Answer Assessment. https://doi.org/10.21203/rs.3.rs-5651820/v1

`q2 · i?` · `design · r2`

Ablation study of hyperparameter settings (temperature and max token) shown in Fig. 8(c). The article reports Set C "becomes the most accurate by letting the creativity be at maximum and a smaller token length (max-token, temperature) = (53, 1)".

> "Further, Se t C becomes the most accurate by letting the creativity be at maximum and a smaller token length (max-token, temperature) = (53, 1)."

## Discussion


## Related Claims

- [Higher LLM temperature settings yield the best English augmentation performance, with Llama temperature 2 the top generator overall](temperature-affects-augmentation-performance.md)
- [Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings](temperature-construct-type-interaction-coding.md)
- [Lowering an LLM's temperature setting is one lever for improving output consistency](lowering-temperature-improves-llm-consistency.md)
- [LLM temperature settings significantly affect generated-text length and complexity, with Llama3 producing more complex texts than GPT-3.5](temperature-drives-generated-text-complexity.md)
- [GPT-4 surpasses other LLMs in the AGE query selection with an accuracy rate 15% better](gpt4-surpasses-other-llms-15-percent.md)
