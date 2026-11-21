---
type: claim
title: The customized ChatGPT can accurately process graphical information when images are submitted directly through the interface
description: The customized ChatGPT can accurately process graphical information when images are submitted directly through the interface
id: custom-gpt-direct-image-submission-accurate
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: abreu-m-2026
    resource: "https://doi.org/10.1088/1361-6552/ae8110"
    title: "Abreu M, Suárez A, Stari C and Martí A C. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. Originally published 2025. [doi:10.1088/1361-6552/ae8110](https://doi.org/10.1088/1361-6552/ae8110)"
    author: Abreu M, Suárez A, Stari C and Martí A C.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The customized ChatGPT can accurately process graphical information when images are submitted directly through the interface

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When a histogram image was submitted directly through the interface, the model produced an accurate quantitative reading of the experimental data. [→ Abreu M 2026](#abreu-m-2026)

## Evidence

### Abreu M 2026

Abreu M, Suárez A, Stari C and Martí A C. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. Originally published 2025. [doi:10.1088/1361-6552/ae8110](https://doi.org/10.1088/1361-6552/ae8110)

`q2 · i?` · `design · r2`

Qualitative case within the customized GPT modality's system limitations section. The article reports that when relevant information such as images, graphs, tables or equations was provided directly through the interface, the system processed it effectively and produced accurate evaluations.

> "when a histogram image was submitted, the model responded: “The distribution of periods fits a Gaussian with a mean of 1.96 s and a standard deviation of 0.02 s, confirming the consistency of the experimental data.”"

## Discussion


## Related Claims
- [API-based evaluation is efficient for large-scale processing but struggles with graphical content, while customized ChatGPT gives more contextualized feedback with lower reproducibility](api-versus-custom-gpt-complementary-tradeoff.md) — related
- [API-based evaluation fails on graphical and mathematical content because the model cannot parse images, tables, graphs and embedded equations](chatgpt-api-cannot-parse-figures-equations.md) — reports the opposite
- [LLM factual errors during collaborative circuit debugging occurred almost exclusively after image inputs, attributed to limited 3D spatial reasoning from breadboard or PCB photos](llm-factual-errors-after-image-inputs-3d-reasoning.md) — related
- [LLMs expressed unjustified confidence in recommendations based on visual inputs, asserting incorrect pin-connection diagnoses with high stated certainty](llm-unjustified-confidence-visual-recommendations.md) — related
