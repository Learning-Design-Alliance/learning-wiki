---
type: claim
title: "GPT-4 grading agrees best with the instructor when the prompt includes the instructor's model answer with a rubric, and worst with an AI-generated rubric alone"
description: "GPT-4 grading agrees best with the instructor when the prompt includes the instructor's model answer with a rubric, and worst with an AI-generated rubric alone"
id: prompt-design-model-answer-plus-rubric-best
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: chris-impey-2024
    resource: "https://doi.org/10.21203/rs.3.rs-3962175/v1"
    title: "Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer. (2024). Using Large Language Models for Automated Grading of Student Writing about Science. Preprint. https://doi.org/10.21203/rs.3.rs-3962175/v1"
    author: Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# GPT-4 grading agrees best with the instructor when the prompt includes the instructor's model answer with a rubric, and worst with an AI-generated rubric alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Worst GPT-4 performance occurred when the prompt was solely an AI-generated rubric, and the authors state a model answer is crucial for reliability. [→ Chris Impey 2024](#chris-impey-2024)

## Evidence

### Chris Impey 2024

Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer. (2024). Using Large Language Models for Automated Grading of Student Writing about Science. Preprint. https://doi.org/10.21203/rs.3.rs-3962175/v1

`q2 · i?` · `causal · r1`

Results analysis of prompt conditions; the authors add that relying solely on rubrics may not be sufficient and the presence of a master answer is crucial for grading reliability.

> "Notably, the worst performance for GPT-4 is seen when the prompt is solely an AI-generated rubric, followed by the situation where the prompt includes only the instructor’s model answer."

## Discussion


## Related Claims
- [GPT-4 generally outperforms GPT-3.5 in matching instructor grades, with lower internal variance](gpt4-outperforms-gpt35-grading-instructor-agreement.md) — related
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](prompt-rubric-quality-drives-llm-grading.md) — a broader claim this one bears on
- [Adding a model answer to the GPT-4 prompt was counterproductive, lowering scoring reliability](model-answer-in-prompt-lowered-reliability.md) — reports the opposite
