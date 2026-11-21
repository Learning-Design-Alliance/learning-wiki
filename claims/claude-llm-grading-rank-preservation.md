---
type: claim
title: Claude-3.7-Sonnet LLM grading preserved student performance rankings relative to human graders (R² = 0.83) while being systematically more stringent
description: Claude-3.7-Sonnet LLM grading preserved student performance rankings relative to human graders (R² = 0.83) while being systematically more stringent
id: claude-llm-grading-rank-preservation
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
    kind: associational
    rigour: 1
  - id: yuan-sen-ting-teaghan-obriain-2026-2
    resource: "https://doi.org/10.33232/001c.160220"
    title: "Yuan-Sen Ting & Teaghan O'Briain. (2026). Teaching Astronomy with Large Language Models. Originally published 2025. [doi:10.33232/001c.160220](https://doi.org/10.33232/001c.160220)"
    author: "Yuan-Sen Ting & Teaghan O'Briain"
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Claude-3.7-Sonnet LLM grading preserved student performance rankings relative to human graders (R² = 0.83) while being systematically more stringent

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a parallel LLM-grading experiment, Claude-3.7-Sonnet achieved R² = 0.83 with human graders on student-average homework scores, largely preserving rankings. [→ Yuan-Sen Ting & Teaghan O'Briain 2026](#yuan-sen-ting-teaghan-obriain-2026)
`q2 i?` Both LLM graders exhibited regression slopes greater than one, indicating LLM grading tends to be more stringent than human evaluation. [→ Yuan-Sen Ting & Teaghan O'Briain 2026 (2)](#yuan-sen-ting-teaghan-obriain-2026-2)

## Evidence

### Yuan-Sen Ting & Teaghan O'Briain 2026

Yuan-Sen Ting & Teaghan O'Briain. (2026). Teaching Astronomy with Large Language Models. Originally published 2025. [doi:10.33232/001c.160220](https://doi.org/10.33232/001c.160220)

`q2 · i?` · `associational · r1`

Parallel grading experiment in the course: students each graded on four homework assignments by Claude-3.7-Sonnet and a human grader, regression fitted on student averages. The article reports "Claude achievesR 2 = 0.83 with human graders" and that rankings are largely preserved.

> "When analyzing average homework scores for individual students and fitting a linear regression model, Claude achievesR 2 = 0.83 with human graders, meaning that student performance rankings are largely preserved"

### Yuan-Sen Ting & Teaghan O'Briain 2026 (2)

Yuan-Sen Ting & Teaghan O'Briain. (2026). Teaching Astronomy with Large Language Models. Originally published 2025. [doi:10.33232/001c.160220](https://doi.org/10.33232/001c.160220)

`q2 · i?` · `design · r2`

Same parallel grading experiment. The article reports systematic differences from human grading patterns, with "regression slopes consistently greater than one", and the regression line sitting below the perfect-agreement diagonal across most of the observed score range (Figure 8).

> "both models exhibit systematic differences from human grading patterns, with regression slopes consistently greater than one, indicating that LLM grading tends to be more stringent than human evaluation"

## Discussion


## Related Claims
- [Llama 4 Maverick shows the strongest human-LLM alignment, while Claude Sonnet 4 performs weakest with poor calibration](llama-strongest-human-llm-alignment-claude-weakest.md) — reports the opposite
- [Even the best LLM grader reaches only moderate agreement with human teachers, below the threshold for good reliability](llm-grading-moderate-human-agreement-icc.md) — reports the opposite
- [LLMs differ systematically in grading strictness, forming liberal, restrictive, and balanced grading styles on programming assignments](llms-differ-liberal-restrictive-balanced-grading-styles.md) — related
- [Three LLMs showed inconsistent systematic bias on multimodal OSPE grading: Claude over-scored by +2.5 points (proportional), Gemini under-scored by −5.0 and ChatGPT by −10.0 points (non-proportional)](llm-ospe-systematic-bias-bland-altman.md) — related
