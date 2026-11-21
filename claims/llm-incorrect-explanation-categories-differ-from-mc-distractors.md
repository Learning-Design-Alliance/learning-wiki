---
type: claim
title: LLM-generated categories of incorrect explanations do not align with the multiple-choice distractors of the original EMCS questions
description: LLM-generated categories of incorrect explanations do not align with the multiple-choice distractors of the original EMCS questions
id: llm-incorrect-explanation-categories-differ-from-mc-distractors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
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
  - id: sean-savage-2025-2
    resource: "https://doi.org/10.1119/perc.2025.pr.savage"
    title: "Sean Savage, N. Sanjay Rebello. (2025). Using an LLM to Investigate Students’ Explanations on Conceptual Physics Questions. [doi:10.1119/perc.2025.pr.savage](https://doi.org/10.1119/perc.2025.pr.savage)"
    author: Sean Savage, N. Sanjay Rebello
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM-generated categories of incorrect explanations do not align with the multiple-choice distractors of the original EMCS questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Emergent LLM categories such as 'Misapplying Collision Type' and 'Misidentifying Collision Type' on Q05 were not reflected in the MC distractors, though some overlap existed with MC option A. [→ Sean Savage 2025](#sean-savage-2025)
`q2 i?` For Q16 and Q23, the LLM captured both omissions of relevant principles and misapplications of principles, a dimension the MC options failed to capture. [→ Sean Savage 2025 (2)](#sean-savage-2025-2)

## Evidence

### Sean Savage 2025

Sean Savage, N. Sanjay Rebello. (2025). Using an LLM to Investigate Students’ Explanations on Conceptual Physics Questions. [doi:10.1119/perc.2025.pr.savage](https://doi.org/10.1119/perc.2025.pr.savage)

`q2 · i?` · `design · r2`

Findings-section comparison of LLM emergent categories against the printed MC distractors for Q05 (misapplying conservation of momentum, energy, or Newton's Laws). Some overlap with MC option A was observed, but the collision-type categories were absent from the distractors.

> "However, several key LLM-derived cat- egories for Question 5, such as ’Misapplying Collision Type’ and ’Misidentifying Collision Type’, were not reflected in the MC distractors (Table V)."

### Sean Savage 2025 (2)

Sean Savage, N. Sanjay Rebello. (2025). Using an LLM to Investigate Students’ Explanations on Conceptual Physics Questions. [doi:10.1119/perc.2025.pr.savage](https://doi.org/10.1119/perc.2025.pr.savage)

`q2 · i?` · `design · r2`

For Q16 and Q23, whose MC answer choices were restricted to identifying which principles were applicable, the LLM analysis of written responses surfaced both omissions and misapplications of principles; the article prints the category percentages in Tables III and IV.

> "While the LLM-generated categories did capture omissions of relevant principles, they also revealed instances where principles were incorrectly applied, an equally important di- mension of student reasoning through the problem that the MC options failed to capture."

## Discussion


## Related Claims
- [Students can reach the correct claim via incorrect explanations, so MC scoring alone masks unproductive conceptual resources](correct-claim-incorrect-explanation-masked-by-mc.md) — related
- [Open-response beta piloting confirmed that planned multiple-choice distractors covered the most frequent incorrect student answers](spruce-distractor-validation-betas.md) — reports the opposite
- [LLM-generated incorrect-explanation categories persisted across multiple API runs, indicating consistent grading performance](llm-categories-persist-across-runs.md) — related
