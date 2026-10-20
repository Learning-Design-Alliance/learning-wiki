---
type: claim
title: LLMs perform competently at comparing item difficulty but fall below random chance on comparing item discrimination
description: LLMs perform competently at comparing item difficulty but fall below random chance on comparing item discrimination
id: llms-below-chance-item-discrimination
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: eamon-worden-2026
    resource: "https://doi.org/10.48550/arxiv.2602.00070"
    title: "Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar. (2026). FoundationalASSIST: An Educational Dataset for Foundational Knowledge Tracing and Pedagogical Grounding of LLMs. https://arxiv.org/abs/2602.00070 [doi:10.48550/arxiv.2602.00070](https://doi.org/10.48550/arxiv.2602.00070)"
    author: Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLMs perform competently at comparing item difficulty but fall below random chance on comparing item discrimination

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Models achieve up to 80.0% accuracy on difficulty comparison when problems differ substantially, yet every model performs below random chance on discrimination comparison, suggesting they do not grasp what makes one problem more diagnostic than another. [→ Eamon Worden 2026](#eamon-worden-2026)

## Evidence

### Eamon Worden 2026

Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar. (2026). FoundationalASSIST: An Educational Dataset for Foundational Knowledge Tracing and Pedagogical Grounding of LLMs. https://arxiv.org/abs/2602.00070 [doi:10.48550/arxiv.2602.00070](https://doi.org/10.48550/arxiv.2602.00070)

`q2 · i?` · `design · r2`

Reported summary of the pedagogical grounding results (difficulty and discrimination comparison tasks with stratified problem pairs, ground truth from IRT 2PL parameters). The article states models show "reasonable competence at comparing item difficulty" while they "completely fail to understand item discrimination".

> "While models show reasonable competence at comparing item difficulty, achieving up to 80.0% accuracy when problems differ substantially, they completely fail to understand item discrimination."

## Discussion


## Related Claims
- [LLMs predict common distractors above chance but fall 15 percentage points below chance at predicting which errors students rarely select](llm-distractor-prediction-asymmetry.md) — related
- [Zero-shot LLMs perform only marginally above random in five-class competency classification but exceed 70% accuracy on binary classification](zero-shot-llm-granularity-competency-classification.md) — related
- [CTT item selection dropped five low-discrimination items, retaining 20 items of moderate difficulty](glat-item-selection-discrimination.md) — related
- [Cognitive modeling of exact student responses is hardest for multi-select problems and rare-error answers, with select-all accuracy of only 12-15% and cognitive accuracy dropping to as low as 3.7% when answers are incorrect](cognitive-modeling-by-problem-type.md) — related
