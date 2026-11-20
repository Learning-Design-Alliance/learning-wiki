---
type: claim
title: GPT-4 performance degrades on harder and cognitively more complex questions
description: GPT-4 performance degrades on harder and cognitively more complex questions
id: gpt4-performance-degrades-on-harder-questions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: borges-2024
    resource: "https://doi.org/10.1073/pnas.2414955121"
    title: "Borges, et al. (2024). Could ChatGPT get an Engineering Degree? Evaluating Higher Education Vulnerability to AI Assistants. [doi:10.1073/pnas.2414955121](https://doi.org/10.1073/pnas.2414955121)"
    author: Borges, et al
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 performance degrades on harder and cognitively more complex questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4 performs worse on instructor-rated harder questions (a 38% accuracy gap between Very Easy and Very Hard Bachelor questions) and its performance is negatively correlated with Bloom's taxonomy cognitive complexity. [→ Borges 2024](#borges-2024)

## Evidence

### Borges 2024

Borges, et al. (2024). Could ChatGPT get an Engineering Degree? Evaluating Higher Education Vulnerability to AI Assistants. [doi:10.1073/pnas.2414955121](https://doi.org/10.1073/pnas.2414955121)

`q2 · i?` · `design · r2`

Difficulty-stratified analysis of 376 Bachelor's and 693 Master's instructor-annotated questions and 207 questions annotated with Bloom's taxonomy by two learning-sciences researchers (Figure 3). The article reports GPT-4 "performance is negatively correlated with the cognitive complexity of the question". No effect size is printed.

> "The results, grouped by taxonomy category in Figure 3c, illustrate that GPT-4 performance is negatively correlated with the cognitive complexity of the question, with higher performance on lower-level tasks compared to analysis and application tasks."

## Discussion


## Related Claims
- [Success rates decrease monotonically from easy to medium to hard difficulty levels across all models](monotonic-difficulty-decline-turtleai.md) — a broader claim this one bears on
- [Under 6,000-token segmentation, GPT-4.1 accuracy did not differ significantly across Bloom's taxonomy cognitive levels](no-bloom-level-accuracy-differences-under-token-splitting.md) — reports the opposite
- [LLM accuracy declines steadily as question complexity increases, from roughly 80% on recall questions to 28.6–33.3% on case-analysis questions, mirroring the human trend](llm-accuracy-declines-with-question-complexity.md) — a broader claim this one bears on
