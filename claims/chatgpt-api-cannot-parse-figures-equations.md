---
type: claim
title: API-based evaluation fails on graphical and mathematical content because the model cannot parse images, tables, graphs and embedded equations
description: API-based evaluation fails on graphical and mathematical content because the model cannot parse images, tables, graphs and embedded equations
id: chatgpt-api-cannot-parse-figures-equations
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

# API-based evaluation fails on graphical and mathematical content because the model cannot parse images, tables, graphs and embedded equations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The API could not correctly render images, tables, graphs or embedded equations, producing incomplete or overly critical evaluations even when the information was present. [→ Abreu M 2026](#abreu-m-2026)

## Evidence

### Abreu M 2026

Abreu M, Suárez A, Stari C and Martí A C. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. Originally published 2025. [doi:10.1088/1361-6552/ae8110](https://doi.org/10.1088/1361-6552/ae8110)

`q2 · i?` · `design · r2`

Qualitative analysis of system limitations in the API-based modality. The article reports the AI was "unable to correctly render images, tables, graphs, or embedded equations" and that limitations "do not necessarily reflect errors in the students' work, but rather the system's restricted ability" to process graphical and mathematical elements.

> "When data, graphs, or equations are not presented in a clear, machine-readable format—i.e., embedded as text rather than as images or screenshots—the API cannot access them, leading the system to produce incomplete or overly critical evaluations, even when the information was present and correctly elaborated."

## Discussion


## Related Claims
- [API-based evaluation is efficient for large-scale processing but struggles with graphical content, while customized ChatGPT gives more contextualized feedback with lower reproducibility](api-versus-custom-gpt-complementary-tradeoff.md) — a broader claim this one bears on
- [The GPT-4 contextualization system fails on geometry problems involving graphs, tables, or diagrammatic components](gpt4-contextualization-geometry-visual-limitation.md) — a narrower finding that bears on this claim
- [Current AI tutoring systems misinterpret complex STEM engineering diagrams, omitting edges, misclassifying component connections, and flattening hierarchical topologies](ai-systems-misinterpret-stem-diagrams.md) — a narrower finding that bears on this claim
- [Graphical GenAI systems failed to produce reliable scientific illustrations for college-level content, with error rates approaching 100%](image-genai-error-rates-approaching-100-percent.md) — related
- [GPT-4 struggles with diagrammatical and graphical questions, though it can describe visual content accurately in prose.](gpt4-diagrammatic-question-weakness.md) — a narrower finding that bears on this claim
- [State-of-the-art multimodal LLMs cannot reliably interpret circuit diagrams and therefore cannot independently solve circuit analysis problems](vlm-cannot-interpret-circuit-diagrams.md) — a narrower finding that bears on this claim
- [The customized ChatGPT can accurately process graphical information when images are submitted directly through the interface](custom-gpt-direct-image-submission-accurate.md) — reports the opposite
