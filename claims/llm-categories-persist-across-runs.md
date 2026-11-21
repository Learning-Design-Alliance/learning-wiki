---
type: claim
title: LLM-generated incorrect-explanation categories persisted across multiple API runs, indicating consistent grading performance
description: LLM-generated incorrect-explanation categories persisted across multiple API runs, indicating consistent grading performance
id: llm-categories-persist-across-runs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: sean-savage-2025
    resource: "https://doi.org/10.1119/perc.2025.pr.savage"
    title: "Sean Savage, N. Sanjay Rebello. (2025). Using an LLM to Investigate Students’ Explanations on Conceptual Physics Questions. [doi:10.1119/perc.2025.pr.savage](https://doi.org/10.1119/perc.2025.pr.savage)"
    author: Sean Savage, N. Sanjay Rebello
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM-generated incorrect-explanation categories persisted across multiple API runs, indicating consistent grading performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When the API was re-prompted with no category limit, the main categories persisted across multiple runs for all questions. [→ Sean Savage 2025](#sean-savage-2025)

## Evidence

### Sean Savage 2025

Sean Savage, N. Sanjay Rebello. (2025). Using an LLM to Investigate Students’ Explanations on Conceptual Physics Questions. [doi:10.1119/perc.2025.pr.savage](https://doi.org/10.1119/perc.2025.pr.savage)

`q2 · i?` · `design · r2`

Findings-section validation check: the API, normally constrained in the number of emergent categories it generated from the input data, was prompted with no category limit; "the main categories persisted across multiple runs of the API for all questions". Consistency is reported descriptively, with no statistical test.

> "To vali- date the grading performance by the API, we prompted it with no category limit. Although niche situations appeared, the main categories persisted across multiple runs of the API for all questions, indicating a consistent grading performance."

## Discussion


## Related Claims
- [Inter-run reliability of LLM performance on the EBHS examination was consistently high, with an overall mean Cohen's κ of 0.821 and no model falling below moderate agreement.](llm-ebhs-inter-run-reliability-high-kappa-0821.md) — related
- [Preliminary re-testing found scaffolded COT unstable across runs while GPT-4o in chat mode reliably reached about 75% agreement using Detailed-Rubric COT](gpt4o-chat-mode-detailed-rubric-reliability.md) — related
- [LLMs can self-correct errors within a single session but revert to the original incorrect responses when the same questions are re-entered in a new session](llm-self-correction-does-not-persist-across-sessions.md) — related
- [LLM-generated categories of incorrect explanations do not align with the multiple-choice distractors of the original EMCS questions](llm-incorrect-explanation-categories-differ-from-mc-distractors.md) — related
