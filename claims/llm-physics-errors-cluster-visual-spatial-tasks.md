---
type: claim
title: AI performance on AP Physics FRQs degrades substantially on tasks requiring visual extraction, spatial inference, or integration across sub-parts, despite strong algebraic performance
description: AI performance on AP Physics FRQs degrades substantially on tasks requiring visual extraction, spatial inference, or integration across sub-parts, despite strong algebraic performance
id: llm-physics-errors-cluster-visual-spatial-tasks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: bilas-paul-2026
    resource: "https://doi.org/10.1088/1361-6552/ae700a"
    title: "Bilas Paul, Jashandeep Kaur, Shantanu Chakraborty, and Shruti Shrestha. (2026). How Well Do AI Systems Solve AP Physics? A Comparative Evaluation of Large Language Models on Algebra-Based Free Response Questions. [doi:10.1088/1361-6552/ae700a](https://doi.org/10.1088/1361-6552/ae700a)"
    author: Bilas Paul, Jashandeep Kaur, Shantanu Chakraborty, and Shruti Shrestha
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# AI performance on AP Physics FRQs degrades substantially on tasks requiring visual extraction, spatial inference, or integration across sub-parts, despite strong algebraic performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Design limits** · Bilas Paul 2026: no comparison group (read from the study by two models, 2026-11-21)

## Subclaims
`q2 i?` All four LLMs perform most reliably on algebraic manipulation of well-defined equations but degrade substantially when problems require extracting quantitative information from visual representations, three-dimensional spatial inference, or coherent integration of multiple principles across sub-parts. [→ Bilas Paul 2026](#bilas-paul-2026)
`q2 i?` Recurring error categories across all models include diagram misinterpretation, graph reading and construction errors, vector direction errors, circuit topology errors, and right-hand rule failures. [→ Bilas Paul 2026](#bilas-paul-2026)

## Evidence

### Bilas Paul 2026

Bilas Paul, Jashandeep Kaur, Shantanu Chakraborty, and Shruti Shrestha. (2026). How Well Do AI Systems Solve AP Physics? A Comparative Evaluation of Large Language Models on Algebra-Based Free Response Questions. [doi:10.1088/1361-6552/ae700a](https://doi.org/10.1088/1361-6552/ae700a)

`q2 · i?` · `causal · r1`

Qualitative error analysis of AI-generated responses across the scored FRQ corpus, cataloguing recurring failure modes. The article states errors "are not random—they cluster around tasks that require accurate extraction of information from visual representations" and that low-scoring years were disproportionately represented among error instances.

> "all four LLMs perform most reliably when problems can be resolved through algebraic manipulation of well- defined equations, but performance degrades substantially when problems require accurate extraction of quantitative information from visual representations"

## Discussion


## Related Claims
- [Four leading LLM-based AI systems all achieve mean scores above 82% on algebra-based AP Physics free-response questions scored with official rubrics](llms-exceed-82-percent-ap-physics-frq.md) — related
- [LLMs are substantially less accurate at extracting and categorizing derived data based on predefined categories than at extracting explicitly stated data](llms-less-accurate-derived-categorical-data-extraction.md) — related
- [LLM errors on multimodal physics problems fall into four categories, with visual processing errors most prevalent, and error type distribution does not differ significantly across models](four-category-llm-multimodal-error-taxonomy.md) — a narrower finding that bears on this claim
- [The Multimodal Interference Effect: mapping visual representations to physical concepts degrades LLM performance even on non-visual problem aspects](multimodal-interference-effect-llms.md) — related
- [LLM factual errors during collaborative circuit debugging occurred almost exclusively after image inputs, attributed to limited 3D spatial reasoning from breadboard or PCB photos](llm-factual-errors-after-image-inputs-3d-reasoning.md) — related
- [All evaluated models struggle with spatial reasoning and precise visual replication on Turtle Graphics tasks](vlms-struggle-spatial-reasoning-visual-precision.md) — related
- [Invalid AI evaluations were mainly associated with restricted access to evidence during text extraction and OCR, particularly for equations, figures, and graphs](invalid-ai-evaluations-evidence-accessibility.md) — related
- [Earlier LLM generations failed spatial-geometry steps in Electromagnetism, such as deducing induced-current direction with the right-hand rule](llm-spatial-geometry-em-bottleneck.md) — a narrower finding that bears on this claim
- [Enabling reasoning in GPT-5.2 resolves physics-error items but not visual-error items, with non-monotonic degradation on visually demanding items](reasoning-depth-interaction-error-type.md) — a narrower finding that bears on this claim
