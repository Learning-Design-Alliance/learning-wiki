---
type: claim
title: "Preliminary re-testing found scaffolded COT unstable across runs while GPT-4o in chat mode reliably reached about 75% agreement using Detailed-Rubric COT"
description: "Preliminary re-testing found scaffolded COT unstable across runs while GPT-4o in chat mode reliably reached about 75% agreement using Detailed-Rubric COT"
id: gpt4o-chat-mode-detailed-rubric-reliability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: zhongzhou-chen-and-tong-wan-2024
    resource: "https://doi.org/10.1119/perc.2024.pr.chen"
    title: "Zhongzhou Chen and Tong Wan. (2024). Achieving Human Level Partial Credit Grading of Written Responses to Physics Conceptual Question using GPT-3.5 with Only Prompt Engineering. [doi:10.1119/perc.2024.pr.chen](https://doi.org/10.1119/perc.2024.pr.chen)"
    author: Zhongzhou Chen and Tong Wan
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Preliminary re-testing found scaffolded COT unstable across runs while GPT-4o in chat mode reliably reached about 75% agreement using Detailed-Rubric COT

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In preliminary experiments on the full 99-response dataset, scaffolded COT performance was not stable on multiple runs, but GPT-4o in chat mode reliably delivered the same level of performance (~75% agreement with human raters) using Detailed-Rubric COT. [→ Zhongzhou Chen and Tong Wan 2024](#zhongzhou-chen-and-tong-wan-2024)

## Evidence

### Zhongzhou Chen and Tong Wan 2024

Zhongzhou Chen and Tong Wan. (2024). Achieving Human Level Partial Credit Grading of Written Responses to Physics Conceptual Question using GPT-3.5 with Only Prompt Engineering. [doi:10.1119/perc.2024.pr.chen](https://doi.org/10.1119/perc.2024.pr.chen)

`q1 · i?` · `design · r2`

A preliminary re-experiment reported in the conclusions section, using the complete dataset of 99 responses with GPT-3.5 Turbo and GPT-4o in chat mode; the authors state the updated result will be reported in a future publication, so this finding is preliminary and unreported in detail.

> "Preliminary data found that the performance of Scaffolded COT prompt is not stable on multiple runs, but GPT-4o is able to reliably deliver the same level of performance (~75% agreement with human raters) using Detailed-Rubric COT"

## Discussion


## Related Claims
- [Scaffolded COT prompting brings GPT-3.5 grading agreement with human raters to 70%-80%, comparable to agreement between two human raters](scaffolded-cot-human-level-agreement-gpt35-grading.md) — related
- [Large closed-weights LLMs show high test-retest reliability when scoring clinical summary statements across repeated runs](llm-high-test-retest-reliability-summary-statement-scoring.md) — related
- [GPT-4o self-consistency mode grading of physics explanations reaches agreement with human graders almost identical to the agreement between the human graders themselves](gpt4o-self-consistency-human-level-grading-agreement.md) — related
- [Self-consistency mode scores outperform individual grading runs for all three problems](self-consistency-mode-beats-individual-runs.md) — related
- [LLM-generated incorrect-explanation categories persisted across multiple API runs, indicating consistent grading performance](llm-categories-persist-across-runs.md) — related
