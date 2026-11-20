---
type: claim
title: The GPT-4 contextualization system fails on geometry problems involving graphs, tables, or diagrammatic components
description: The GPT-4 contextualization system fails on geometry problems involving graphs, tables, or diagrammatic components
id: gpt4-contextualization-geometry-visual-limitation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: gautam-yadav-2023
    resource: "https://doi.org/10.48550/arXiv.2306.00190"
    title: "Gautam Yadav, Ying-Jui Tseng and Xiaolin Ni. (2023). Contextualizing Problems to Student Interests at Scale in Intelligent Tutoring System Using Large Language Models. CEUR Workshop Proceedings. [doi:10.48550/arXiv.2306.00190](https://doi.org/10.48550/arXiv.2306.00190)"
    author: Gautam Yadav, Ying-Jui Tseng and Xiaolin Ni
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The GPT-4 contextualization system fails on geometry problems involving graphs, tables, or diagrammatic components

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q1 i?` While the system excels at solving algebraic equations, it struggles with geometric problems, especially those involving graphs, tables, or diagrammatic components, and fails to produce suitable diagrams for linear algebra questions requiring visual components. [→ Gautam Yadav 2023](#gautam-yadav-2023)

## Evidence

### Gautam Yadav 2023

Gautam Yadav, Ying-Jui Tseng and Xiaolin Ni. (2023). Contextualizing Problems to Student Interests at Scale in Intelligent Tutoring System Using Large Language Models. CEUR Workshop Proceedings. [doi:10.48550/arXiv.2306.00190](https://doi.org/10.48550/arXiv.2306.00190)

`q1 · i?` · `design · r2`

The authors' stated limitation of their system in the Future Work and Limitations section. They note GPT's "existing capabilities" limit its ability to create images aligning with problem text, and that the system "fails to produce suitable diagrams for linear algebra questions requiring visual components."

> "While it excels in solving algebraic equations, it needs help with geometric problems, especially those involving graphs, tables, or diagrammatic components."

## Discussion


## Related Claims
- [State-of-the-art multimodal LLMs cannot reliably interpret circuit diagrams and therefore cannot independently solve circuit analysis problems](vlm-cannot-interpret-circuit-diagrams.md) — a narrower finding that bears on this claim
- [Reasoning with ground-truth auxiliary diagrams consistently outperforms reasoning from the original diagram alone on GeoVAD-Bench](gt-aux-consistently-outperforms-no-aux-geometry.md) — related
- [Current AI tutoring systems misinterpret complex STEM engineering diagrams, omitting edges, misclassifying component connections, and flattening hierarchical topologies](ai-systems-misinterpret-stem-diagrams.md) — related
- [Conventionally taught students struggled to differentiate broken from smooth lines and to shade out unwanted regions, while both groups could form inequalities and equations](conventional-methods-graphing-shading-difficulties.md) — related
- [Iterative prompt engineering of GPT-4 achieved meaningful contextualization of algebra problems that preserved difficulty and original intent](gpt4-prompt-engineering-contextualization-preserves-intent.md) — reports the opposite
- [GPT-4 tends to excel on questions where students also perform well, but struggles on some mathematical-derivation problems students handle well](gpt4-excells-where-students-excel.md) — related
