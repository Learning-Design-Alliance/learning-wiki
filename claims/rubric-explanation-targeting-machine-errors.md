---
type: claim
title: "Adding explanation text to rubric items targeting observed machine-grading errors cut cases where GPT-4o differed from both human graders from 21.7% to 9.6% on Question 2"
description: "Adding explanation text to rubric items targeting observed machine-grading errors cut cases where GPT-4o differed from both human graders from 21.7% to 9.6% on Question 2"
id: rubric-explanation-targeting-machine-errors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
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

# Adding explanation text to rubric items targeting observed machine-grading errors cut cases where GPT-4o differed from both human graders from 21.7% to 9.6% on Question 2

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A revised Detailed Compare 2 rubric explaining two ambiguous student answer patterns significantly improved every metric, dropping diff-both from 21.7% to 9.6%. [→ Zhongzhou Chen and Tong Wan 2025](#zhongzhou-chen-and-tong-wan-2025)

## Evidence

### Zhongzhou Chen and Tong Wan 2025

Zhongzhou Chen and Tong Wan. (2025). Using Large Language Models to Assign Partial Credit to Students' Explanations of Problem-Solving Process: Grade at Human Level Accuracy with Grading Confidence Index and Personalized Student-facing Feedback. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010126](https://doi.org/10.1103/physrevphyseducres.21.010126)

`q2 · i?` · `design · r2`

Iterative rubric-refinement experiment on Question 2 (83 responses, conservation of mechanical energy): after adding explanations of omitted zero elastic-energy terms and alternate reference heights, the article reports the fraction of cases differing from both human graders fell "from 21.7 % to only 9 .6%."

> "those modifications 
to the rubric explanation significantly improves the 
performance of the LLM  grader on every metric 
(Detailed Compare 2), especially in dropping the 
fraction of cases in which the AI differs from both 
human graders from 21.7 % to only 9 .6%."

## Discussion


## Related Claims
- [Focused rubric refinement that made required physics and scoring conditions explicit reduced AI–official disagreements on targeted questions (e.g., Grover item MAD 1.1 to 0.4 marks, r 0.70 to 0.82)](explicit-rubric-conditions-reduce-ai-disagreement.md) — possibly the same claim (merge candidate)
- [Revising the rubric to operationalize pedagogical constructs raises human–machine agreement for openness and depth](rubric-revision-improves-machine-alignment.md) — related
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](prompt-rubric-quality-drives-llm-grading.md) — a broader claim this one bears on
- [GPT-4o self-consistency mode grading of physics explanations reaches agreement with human graders almost identical to the agreement between the human graders themselves](gpt4o-self-consistency-human-level-grading-agreement.md) — related
- [Self-consistency mode scores outperform individual grading runs for all three problems](self-consistency-mode-beats-individual-runs.md) — related
