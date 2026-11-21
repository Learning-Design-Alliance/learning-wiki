---
type: claim
title: Invalid AI evaluations were mainly associated with restricted access to evidence during text extraction and OCR, particularly for equations, figures, and graphs
description: Invalid AI evaluations were mainly associated with restricted access to evidence during text extraction and OCR, particularly for equations, figures, and graphs
id: invalid-ai-evaluations-evidence-accessibility
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: marcos-abreu-2026
    resource: "https://doi.org/10.1088/1361-6552/ae8110"
    title: "Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. [doi:10.1088/1361-6552/ae8110](https://doi.org/10.1088/1361-6552/ae8110)"
    author: Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: marcos-abreu-2026-2
    resource: "https://doi.org/10.1088/1361-6552/ae8110"
    title: "Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. [doi:10.1088/1361-6552/ae8110](https://doi.org/10.1088/1361-6552/ae8110)"
    author: Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Invalid AI evaluations were mainly associated with restricted access to evidence during text extraction and OCR, particularly for equations, figures, and graphs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Invalid evaluations concentrated where reports referenced equations, figures, or graphical evidence that could not be recovered from the extracted text. [→ Marcos Abreu 2026](#marcos-abreu-2026)
`q2 i?` The study distinguished explicit limitations (declared verification impossibilities) from inferred limitations (confident evaluations based on incomplete or distorted content). [→ Marcos Abreu 2026 (2)](#marcos-abreu-2026-2)

## Evidence

### Marcos Abreu 2026

Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. [doi:10.1088/1361-6552/ae8110](https://doi.org/10.1088/1361-6552/ae8110)

`q2 · i?` · `design · r2`

Abstract-level statement corroborated in Results and Discussion: e.g., the model failed to recognize a square root and concluded "the type-A estimate is confused with the expressionSn/N," and figures referenced in reports were not recoverable during extraction. No effect size is printed.

> "These limitations were mainly associated with restricted access to evidence during text extraction and OCR, particularly for equations, figures, and graphical representations."

### Marcos Abreu 2026 (2)

Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. [doi:10.1088/1361-6552/ae8110](https://doi.org/10.1088/1361-6552/ae8110)

`q2 · i?` · `design · r2`

Discussion-section characterization of the evidence-accessibility indicator introduced for invalid responses, disaggregated in Table 1 (e.g., Conclusions: 2% explicit vs. 9% inferred). Descriptive percentages only; no effect size.

> "Explicit limitations correspond to declared verification impossibilities, whereas inferred limitations involve confident evaluations based on incomplete or distorted representations of the recovered content (Table 1)."

## Discussion


## Related Claims
- [API-based evaluation fails on graphical and mathematical content because the model cannot parse images, tables, graphs and embedded equations](chatgpt-api-cannot-parse-figures-equations.md) — possibly the same claim (merge candidate)
- [Current AI tutoring systems misinterpret complex STEM engineering diagrams, omitting edges, misclassifying component connections, and flattening hierarchical topologies](ai-systems-misinterpret-stem-diagrams.md) — related
- [AI performance on AP Physics FRQs degrades substantially on tasks requiring visual extraction, spatial inference, or integration across sub-parts, despite strong algebraic performance](llm-physics-errors-cluster-visual-spatial-tasks.md) — related
- [AI grading errors concentrate in graphical tasks and include both false positives on incorrect equations and false negatives from misread sketches and labels](ai-grading-failure-modes-graphical-tasks.md) — related
- [The GPT-4 contextualization system fails on geometry problems involving graphs, tables, or diagrammatic components](gpt4-contextualization-geometry-visual-limitation.md) — related
- [Vision-assisted extraction identified chart type in all sampled images but showed ±5–10% numeric estimation error and two failure modes correctable via mandatory review](llm-chart-extraction-accuracy-failure-modes.md) — related
