---
type: claim
title: Gemini-2.5-Flash showed weaker grading consistency than Claude-3.7-Sonnet (R² = 0.63, residual SD 1.51 vs 1.17), limiting its utility for formal assessment
description: Gemini-2.5-Flash showed weaker grading consistency than Claude-3.7-Sonnet (R² = 0.63, residual SD 1.51 vs 1.17), limiting its utility for formal assessment
id: gemini-flash-grading-inconsistency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yuan-sen-ting-teaghan-obriain-2026
    resource: "https://doi.org/10.33232/001c.160220"
    title: "Yuan-Sen Ting & Teaghan O'Briain. (2026). Teaching Astronomy with Large Language Models. Originally published 2025. [doi:10.33232/001c.160220](https://doi.org/10.33232/001c.160220)"
    author: "Yuan-Sen Ting & Teaghan O'Briain"
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Gemini-2.5-Flash showed weaker grading consistency than Claude-3.7-Sonnet (R² = 0.63, residual SD 1.51 vs 1.17), limiting its utility for formal assessment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The more economical Gemini-2.5-Flash grader showed degraded performance (R² = 0.63) and greater inconsistency at the individual assignment level (SD 1.51 vs 1.17 for Claude). [→ Yuan-Sen Ting & Teaghan O'Briain 2026](#yuan-sen-ting-teaghan-obriain-2026)

## Evidence

### Yuan-Sen Ting & Teaghan O'Briain 2026

Yuan-Sen Ting & Teaghan O'Briain. (2026). Teaching Astronomy with Large Language Models. Originally published 2025. [doi:10.33232/001c.160220](https://doi.org/10.33232/001c.160220)

`q2 · i?` · `design · r2`

Same parallel grading experiment (Figure 8 comparison of the two models). The article states Gemini Flash "still serves as a reasonable study companion" but that the reduced grading consistency limits its utility for formal assessment, with scatter varying across question types and complexity levels.

> "Claude demonstrates stronger correlation (R2 = 0.83) and lower variability (Std = 1.17) compared to Gemini (R 2 = 0.63, Std = 1.51)"

## Discussion


## Related Claims
- [In one study of repeated LLM scoring of 60 IELTS essays, Gemini 2.5 Flash was moderately reliable (ICC 0.63-0.75) while Claude Sonnet 4 and DeepSeek R1 stayed below 0.70 in most dimensions](llm-essay-scoring-reliability-stratification.md) — reports the opposite
- [Large closed-weights LLMs show high test-retest reliability when scoring clinical summary statements across repeated runs](llm-high-test-retest-reliability-summary-statement-scoring.md) — related
- [Claude, Copilot, and Gemini showed model-specific topic strengths and weaknesses and lower cross-attempt reliability than GPT-4o](claude-copilot-gemini-topic-strengths-reliability.md) — related
- [Inter-model agreement is moderate, indicating models do not consistently identify the same questions correctly](moderate-inter-model-agreement-endodontic-questions.md) — related
