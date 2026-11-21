---
type: claim
title: Self-consistency mode scores outperform individual grading runs for all three problems
description: Self-consistency mode scores outperform individual grading runs for all three problems
id: self-consistency-mode-beats-individual-runs
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

# Self-consistency mode scores outperform individual grading runs for all three problems

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For Question 2, the five-run mode score outperformed all individual runs and was closest to human-level agreement. [→ Zhongzhou Chen and Tong Wan 2025](#zhongzhou-chen-and-tong-wan-2025)

## Evidence

### Zhongzhou Chen and Tong Wan 2025

Zhongzhou Chen and Tong Wan. (2025). Using Large Language Models to Assign Partial Credit to Students' Explanations of Problem-Solving Process: Grade at Human Level Accuracy with Grading Confidence Index and Personalized Student-facing Feedback. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010126](https://doi.org/10.1103/physrevphyseducres.21.010126)

`q2 · i?` · `design · r2`

Self-consistency experiment repeating GPT-4o Detailed Compare grading five times on Question 2 responses; the article reports the mode score outperformed all individual runs and matched the human graders' Macro F1.

> "The mode score once again outperforms 
all the individual runs, and is closest to human le 
vel agreement, and even had identical Macro F1 score as 
between human graders."

## Discussion


## Related Claims
- [GPT-4o self-consistency mode grading of physics explanations reaches agreement with human graders almost identical to the agreement between the human graders themselves](gpt4o-self-consistency-human-level-grading-agreement.md) — related
- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](ai-grading-run-to-run-reliability-icc.md) — related
- [Large closed-weights LLMs show high test-retest reliability when scoring clinical summary statements across repeated runs](llm-high-test-retest-reliability-summary-statement-scoring.md) — related
- [Preliminary re-testing found scaffolded COT unstable across runs while GPT-4o in chat mode reliably reached about 75% agreement using Detailed-Rubric COT](gpt4o-chat-mode-detailed-rubric-reliability.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [Inter-run reliability of LLM performance on the EBHS examination was consistently high, with an overall mean Cohen's κ of 0.821 and no model falling below moderate agreement.](llm-ebhs-inter-run-reliability-high-kappa-0821.md) — related
- [Adding explanation text to rubric items targeting observed machine-grading errors cut cases where GPT-4o differed from both human graders from 21.7% to 9.6% on Question 2](rubric-explanation-targeting-machine-errors.md) — related
