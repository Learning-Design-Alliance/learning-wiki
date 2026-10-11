---
type: claim
title: "Vision-assisted extraction identified chart type in all sampled images but showed ±5–10% numeric estimation error and two failure modes correctable via mandatory review"
description: "Vision-assisted extraction identified chart type in all sampled images but showed ±5–10% numeric estimation error and two failure modes correctable via mandatory review"
id: llm-chart-extraction-accuracy-failure-modes
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: lawrence-obiuwevwi-2026
    resource: "https://arxiv.org/abs/2607.01214"
    title: "Lawrence Obiuwevwi, Krzysztof J. Rechowicz, Jessica M. Johnson, Erika Frydenlund, Vikas Ashok, Sachin Shetty, & Sampath Jayarathna. (2026). Touching and Feeling the Data: A Reusable Software Pipeline for Tactile Statistical Graphs in Accessible Education. arXiv. https://arxiv.org/abs/2607.01214"
    author: "Lawrence Obiuwevwi, Krzysztof J. Rechowicz, Jessica M. Johnson, Erika Frydenlund, Vikas Ashok, Sachin Shetty, & Sampath Jayarathna"
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Vision-assisted extraction identified chart type in all sampled images but showed ±5–10% numeric estimation error and two failure modes correctable via mandatory review

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` Over an informal sample of textbook chart images, the multimodal LLM correctly identified chart type in all cases and recovered most numeric values within ±5–10% visual estimation error. [→ Lawrence Obiuwevwi 2026](#lawrence-obiuwevwi-2026)

## Evidence

### Lawrence Obiuwevwi 2026

Lawrence Obiuwevwi, Krzysztof J. Rechowicz, Jessica M. Johnson, Erika Frydenlund, Vikas Ashok, Sachin Shetty, & Sampath Jayarathna. (2026). Touching and Feeling the Data: A Reusable Software Pipeline for Tactile Statistical Graphs in Accessible Education. arXiv. https://arxiv.org/abs/2607.01214

`q1 · i?` · `design · r2`

Informal assessment of the optional Layer 3 extraction over textbook chart images; the article calls the sample informal and reports chart type identified in all cases with most numeric values within ±5–10% visual estimation error. No formal user study was conducted.

> "Vision extraction over an informal sample of textbook chart images correctly identified chart type in all cases and recovered most numeric values within ±5–10% visual estimation error."

## Discussion


## Related Claims
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — related
- [In a contrastive audit, visual misreading is the dominant failure mode for non-reasoning models on items reasoning models solve](visual-misread-dominant-non-reasoning-failure.md) — related
- [VLMs achieve higher accuracy on non-erroneous than erroneous student math responses even when controlling for the math problem](vlms-underperform-on-erroneous-student-math-responses.md) — related
- [Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)](five-error-types-llm-diagnosis-vague-evidence.md) — related
