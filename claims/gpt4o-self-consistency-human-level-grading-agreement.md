---
type: claim
title: GPT-4o self-consistency mode grading of physics explanations reaches agreement with human graders almost identical to the agreement between the human graders themselves
description: GPT-4o self-consistency mode grading of physics explanations reaches agreement with human graders almost identical to the agreement between the human graders themselves
id: gpt4o-self-consistency-human-level-grading-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: zhongzhou-chen-and-tong-wan-2025
    resource: "https://doi.org/10.1103/physrevphyseducres.21.010126"
    title: "Zhongzhou Chen and Tong Wan. (2025). Using Large Language Models to Assign Partial Credit to Students' Explanations of Problem-Solving Process: Grade at Human Level Accuracy with Grading Confidence Index and Personalized Student-facing Feedback. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010126](https://doi.org/10.1103/physrevphyseducres.21.010126)"
    author: Zhongzhou Chen and Tong Wan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4o self-consistency mode grading of physics explanations reaches agreement with human graders almost identical to the agreement between the human graders themselves

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For Question 1, the self-consistency mode score from five GPT-4o grading runs agreed with human graders at a level almost identical to the agreement between two human graders. [→ Zhongzhou Chen and Tong Wan 2025](#zhongzhou-chen-and-tong-wan-2025)

## Evidence

### Zhongzhou Chen and Tong Wan 2025

Zhongzhou Chen and Tong Wan. (2025). Using Large Language Models to Assign Partial Credit to Students' Explanations of Problem-Solving Process: Grade at Human Level Accuracy with Grading Confidence Index and Personalized Student-facing Feedback. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010126](https://doi.org/10.1103/physrevphyseducres.21.010126)

`q2 · i?` · `design · r2`

Grading experiment on 96 student responses to a conceptual energy-conservation exam question, comparing GPT-4o Detailed Compare self-consistency mode scores against two independent human graders; the article reports the mode score reached "almost identical to the level of agreement between human graders."

> "Based on all five metrics, the level of agreement bet ween self-
consistency mode score and human graders were 
almost identical to the level of agreement between 
human graders."

## Discussion


## Related Claims
- [Self-consistency mode scores outperform individual grading runs for all three problems](self-consistency-mode-beats-individual-runs.md) — related
- [Preliminary re-testing found scaffolded COT unstable across runs while GPT-4o in chat mode reliably reached about 75% agreement using Detailed-Rubric COT](gpt4o-chat-mode-detailed-rubric-reliability.md) — related
- [Large closed-weights LLMs show high test-retest reliability when scoring clinical summary statements across repeated runs](llm-high-test-retest-reliability-summary-statement-scoring.md) — related
- [Full-scale LLM versions consistently achieve higher agreement with human grades than their mini and nano counterparts](full-scale-llms-outperform-mini-nano-grading.md) — related
- [Adding explanation text to rubric items targeting observed machine-grading errors cut cases where GPT-4o differed from both human graders from 21.7% to 9.6% on Question 2](rubric-explanation-targeting-machine-errors.md) — related
- [Scaffolded COT prompting brings GPT-3.5 grading agreement with human raters to 70%-80%, comparable to agreement between two human raters](scaffolded-cot-human-level-agreement-gpt35-grading.md) — related
- [GPT-4o grades students' written explanations on EMCS conceptual physics questions with accuracy comparable to a human grader (0-3% discrepancy, mean Cohen's kappa 0.77)](gpt4o-grades-written-physics-explanations-comparable-to-human-graders.md) — a broader claim this one bears on
