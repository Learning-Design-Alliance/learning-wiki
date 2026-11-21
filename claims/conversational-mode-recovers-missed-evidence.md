---
type: claim
title: In exploratory conversational mode, directing prompts at specific rubric items and report elements allowed the model to incorporate evidence missed in batch grading
description: In exploratory conversational mode, directing prompts at specific rubric items and report elements allowed the model to incorporate evidence missed in batch grading
id: conversational-mode-recovers-missed-evidence
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: marcos-abreu-2026
    resource: "https://doi.org/10.1088/1361-6552/ae8110"
    title: "Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. [doi:10.1088/1361-6552/ae8110](https://doi.org/10.1088/1361-6552/ae8110)"
    author: Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# In exploratory conversational mode, directing prompts at specific rubric items and report elements allowed the model to incorporate evidence missed in batch grading

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In the subset of cases examined, targeted conversational verification produced feedback that no longer exhibited the verification limitations observed in automated batch grading. [→ Marcos Abreu 2026](#marcos-abreu-2026)

## Evidence

### Marcos Abreu 2026

Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. [doi:10.1088/1361-6552/ae8110](https://doi.org/10.1088/1361-6552/ae8110)

`q1 · i?` · `design · r2`

Exploratory diagnostic reanalysis in conversational mode on a subset of cases previously coded invalid; it did not modify the scores or coding of the main analysis. The article reports no effect size or test statistic for this observation.

> "In the cases reviewed, directing questions toward specific elements of the report allowed the model to consider evidence that had not been reliably incorporated in the batch workflow (e.g., embedded equations or information contained in images)."

## Discussion


## Related Claims
- [Fine-grained rubric grading of entire problems exceeds LLM bookkeeping capabilities, while parts-based grading is more reliable but misses nuances](rubric-granularity-affects-ai-grading-reliability.md) — related
- [Accurate LLM solution diagnosis does not reliably produce pedagogically actionable feedback, with lowest rubric scores on error identification and actionability](accurate-diagnosis-not-actionable-feedback.md) — related
- [Adding explanation text to rubric items targeting observed machine-grading errors cut cases where GPT-4o differed from both human graders from 21.7% to 9.6% on Question 2](rubric-explanation-targeting-machine-errors.md) — related
