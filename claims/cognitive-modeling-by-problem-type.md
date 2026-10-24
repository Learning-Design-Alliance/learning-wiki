---
type: claim
title: "Cognitive modeling of exact student responses is hardest for multi-select problems and rare-error answers, with select-all accuracy of only 12-15% and cognitive accuracy dropping to as low as 3.7% when answers are incorrect"
description: "Cognitive modeling of exact student responses is hardest for multi-select problems and rare-error answers, with select-all accuracy of only 12-15% and cognitive accuracy dropping to as low as 3.7% when answers are inc..."
id: cognitive-modeling-by-problem-type
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: eamon-worden-2026
    resource: "https://doi.org/10.48550/arxiv.2602.00070"
    title: "Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar. (2026). FoundationalASSIST: An Educational Dataset for Foundational Knowledge Tracing and Pedagogical Grounding of LLMs. https://arxiv.org/abs/2602.00070 [doi:10.48550/arxiv.2602.00070](https://doi.org/10.48550/arxiv.2602.00070)"
    author: Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: eamon-worden-2026-2
    resource: "https://arxiv.org/abs/2602.00070"
    title: "Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar. (2026). FoundationalASSIST: An Educational Dataset for Foundational Knowledge Tracing and Pedagogical Grounding of LLMs. https://arxiv.org/abs/2602.00070"
    author: Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Cognitive modeling of exact student responses is hardest for multi-select problems and rare-error answers, with select-all accuracy of only 12-15% and cognitive accuracy dropping to as low as 3.7% when answers are incorrect

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All models achieve only 12-15% accuracy on select-all problems (baseline approximately 2.9%), and cognitive accuracy for incorrect answers drops as low as 3.7% (Llama-3.3-70B). [→ Eamon Worden 2026](#eamon-worden-2026)
`q2 i?` Fill-in-the-blank cognitive modeling reaches 40-50% accuracy despite near-zero random chance, suggesting some genuine capability to anticipate what students write. [→ Eamon Worden 2026 (2)](#eamon-worden-2026-2)

## Evidence

### Eamon Worden 2026

Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar. (2026). FoundationalASSIST: An Educational Dataset for Foundational Knowledge Tracing and Pedagogical Grounding of LLMs. https://arxiv.org/abs/2602.00070 [doi:10.48550/arxiv.2602.00070](https://doi.org/10.48550/arxiv.2602.00070)

`q2 · i?` · `design · r2`

Cognitive modeling accuracy broken down by problem type (Table 6) and by correctness (Table 7) in Sections 6.1.3-6.1.4. The article reports the quoted 12-15% select-all range and notes cognitive accuracy drops to 13.5% for Qwen3 Instruct and "just 3.7% when the student's answer does not match the correct answer".

> "All models achieve only 12-15% accuracy on “select all” problems, exceeding the random baseline of approximately 2.9% but not performing reliably well."

### Eamon Worden 2026 (2)

Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar. (2026). FoundationalASSIST: An Educational Dataset for Foundational Knowledge Tracing and Pedagogical Grounding of LLMs. https://arxiv.org/abs/2602.00070

`q2 · i?` · `design · r2`

Same Section 6.1.3 analysis of cognitive modeling by problem type, where fill-in problems have essentially zero random baseline. The article quotes the "40-50%" fill-in performance as evidence of some understanding of common student responses.

> "The fill-in-the-blank performance of 40-50% is particularly notable: for open-ended numerical responses where random chance is essentially zero, models demonstrate genuine capability to anticipate what students will write."

## Discussion


## Related Claims
- [LLMs predict common distractors above chance but fall 15 percentage points below chance at predicting which errors students rarely select](llm-distractor-prediction-asymmetry.md) — related
- [LLM error simulation rarely fails, but the model is less likely to reproduce a targeted distractor on problems with longer correct solutions](error-simulation-accurate-but-longer-solutions-harder.md) — related
- [LLMs perform competently at comparing item difficulty but fall below random chance on comparing item discrimination](llms-below-chance-item-discrimination.md) — related
