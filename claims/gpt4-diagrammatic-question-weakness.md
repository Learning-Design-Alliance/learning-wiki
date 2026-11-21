---
type: claim
title: GPT-4 struggles with diagrammatical and graphical questions, though it can describe visual content accurately in prose.
description: GPT-4 struggles with diagrammatical and graphical questions, though it can describe visual content accurately in prose.
id: gpt4-diagrammatic-question-weakness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: pimbblet-2024
    resource: "https://doi.org/10.1088/1361-6404/ad9874"
    title: "Pimbblet, K.A., & Morrell, L.J. (2024). Can ChatGPT pass a physics degree? Making a case for reformation of assessment of undergraduate degrees. European Journal of Physics. [doi:10.1088/1361-6404/ad9874](https://doi.org/10.1088/1361-6404/ad9874)"
    author: "Pimbblet, K.A., & Morrell, L.J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 struggles with diagrammatical and graphical questions, though it can describe visual content accurately in prose.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4 performs poorly at parsing graphical and diagrammatical questions across multiple modules. [→ Pimbblet 2024](#pimbblet-2024)
`q2 i?` GPT-4 can describe graphs and diagrams well in prose even when it cannot sketch them. [→ Pimbblet 2024](#pimbblet-2024)

## Evidence

### Pimbblet 2024

Pimbblet, K.A., & Morrell, L.J. (2024). Can ChatGPT pass a physics degree? Making a case for reformation of assessment of undergraduate degrees. European Journal of Physics. [doi:10.1088/1361-6404/ad9874](https://doi.org/10.1088/1361-6404/ad9874)

`q2 · i?` · `design · r2`

Across multiple modules the authors found GPT-4 struggled with graphical questions. In the Quantum Physics module, "ChatGPT refused to even attempt to sketch a graph for several questions" yet "did describe the graph well" when asked about a particle in an infinite potential well.

> "even though ChatGPT refused to even attempt to sketch a graph for several questions, it did describe the graph well"

## Discussion


## Related Claims
- [The GPT-4 contextualization system fails on geometry problems involving graphs, tables, or diagrammatic components](gpt4-contextualization-geometry-visual-limitation.md) — possibly the same claim (merge candidate)
- [GPT-4 tends to excel on questions where students also perform well, but struggles on some mathematical-derivation problems students handle well](gpt4-excells-where-students-excel.md) — related
- [GPT-4 performs exceptionally well on coding tasks and simple single-step problems, but poorly on multi-step problems, longer prose, and interdisciplinary problems.](gpt4-strong-coding-weak-multistep-prose.md) — related
- [API-based evaluation is efficient for large-scale processing but struggles with graphical content, while customized ChatGPT gives more contextualized feedback with lower reproducibility](api-versus-custom-gpt-complementary-tradeoff.md) — related
- [API-based evaluation fails on graphical and mathematical content because the model cannot parse images, tables, graphs and embedded equations](chatgpt-api-cannot-parse-figures-equations.md) — a broader claim this one bears on
