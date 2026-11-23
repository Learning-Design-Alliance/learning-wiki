---
type: claim
title: "GPT-4o grades students' written explanations on EMCS conceptual physics questions with accuracy comparable to a human grader (0-3% discrepancy, mean Cohen's kappa 0.77)"
description: "GPT-4o grades students' written explanations on EMCS conceptual physics questions with accuracy comparable to a human grader (0-3% discrepancy, mean Cohen's kappa 0.77)"
id: gpt4o-grades-written-physics-explanations-comparable-to-human-graders
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

# GPT-4o grades students' written explanations on EMCS conceptual physics questions with accuracy comparable to a human grader (0-3% discrepancy, mean Cohen's kappa 0.77)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The LLM's overall-correctness classifications of student written responses differed from a human grader's by only 0-3% across three questions. [→ Sean Savage 2025](#sean-savage-2025)
`q2 i?` LLM-human agreement on a 20% validation sample showed mean Cohen's kappa of 0.77 (κ = 0.74, 0.65, 0.89 across the three questions), described as substantial to almost perfect. [→ Sean Savage 2025 (2)](#sean-savage-2025-2)

## Evidence

### Sean Savage 2025

Sean Savage, N. Sanjay Rebello. (2025). Using an LLM to Investigate Students’ Explanations on Conceptual Physics Questions. [doi:10.1119/perc.2025.pr.savage](https://doi.org/10.1119/perc.2025.pr.savage)

`q2 · i?` · `design · r2`

Findings-section validation: a human grader analyzed a randomly chosen 20% (N = 231) sample of the N = 1131 post-test written responses; the LLM-human discrepancy in overall correctness was "remarkably low (0-3%)". No effect size is printed.

> "The discrepancy obtained between LLM and HG for the overall correctness i.e., correct claim (answer) supported by correct explanation (evidence and reasoning), was remarkably low (0-3%)."

### Sean Savage 2025 (2)

Sean Savage, N. Sanjay Rebello. (2025). Using an LLM to Investigate Students’ Explanations on Conceptual Physics Questions. [doi:10.1119/perc.2025.pr.savage](https://doi.org/10.1119/perc.2025.pr.savage)

`q2 · i?` · `design · r2`

Agreement statistics for the same 20% (N = 231) human-graded validation sample: "the mean Cohen’s kappa was 0.77" across the three questions, which the authors note are "known to be substantial to almost perfect". Kappa is a reliability statistic, not an effect size.

> "For the ran- domly chosen 20 % (N = 231) responses, the mean Cohen’s kappa was 0.77 for the correct claim/evidence/reasoning across the three questions (κ = 0.74, 0.65, and 0.89, respectively)."

## Discussion


## Related Claims
- [Scaffolded COT prompting brings GPT-3.5 grading agreement with human raters to 70%-80%, comparable to agreement between two human raters](scaffolded-cot-human-level-agreement-gpt35-grading.md) — related
- [Self-consistency mode scores outperform individual grading runs for all three problems](self-consistency-mode-beats-individual-runs.md) — related
- [GPT-4o self-consistency mode grading of physics explanations reaches agreement with human graders almost identical to the agreement between the human graders themselves](gpt4o-self-consistency-human-level-grading-agreement.md) — a narrower finding that bears on this claim
- [Adding explanation text to rubric items targeting observed machine-grading errors cut cases where GPT-4o differed from both human graders from 21.7% to 9.6% on Question 2](rubric-explanation-targeting-machine-errors.md) — related
- [LLM scores are more consistent across trials than human scores, with GPT-4 using explanations showing the greatest confidence](llm-trial-consistency-exceeds-human-consistency.md) — related
- [An LLM grader using a four-level explanation-quality rubric achieved substantial agreement with human consensus scores (quadratic-weighted κ=0.78).](llm-grader-substantial-agreement-human-consensus.md) — related
- [GPT-4o achieved substantial agreement with human raters for the Physics Concepts theme (Cohen's κ = 0.7) after optimization](gpt4o-substantial-agreement-physics-concepts-coding.md) — related
