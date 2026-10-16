---
type: claim
title: "LLMs systematically underestimate fraction items whose difficulty is driven by misconceptions (the \"Easy Trap\")"
description: "LLMs systematically underestimate fraction items whose difficulty is driven by misconceptions (the \"Easy Trap\")"
id: easy-trap-fraction-items-underestimated-by-llms
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: la-hadi-2025
    resource: "https://doi.org/10.48550/arxiv.2607.26067"
    title: "La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T. (2025). The “Easy Trap”: Why LLMs Underestimate Misconception-Driven Difficulty. https://arxiv.org/abs/2607.26067 [doi:10.48550/arxiv.2607.26067](https://doi.org/10.48550/arxiv.2607.26067)"
    author: "La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: la-hadi-2025-2
    resource: "https://arxiv.org/abs/2607.26067"
    title: "La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T. (2025). The “Easy Trap”: Why LLMs Underestimate Misconception-Driven Difficulty. https://arxiv.org/abs/2607.26067"
    author: "La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# LLMs systematically underestimate fraction items whose difficulty is driven by misconceptions (the "Easy Trap")

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` Fraction items consistently rated as easy by LLMs were among the most difficult for students; in the most extreme case only 34.2% of students correctly solved 100 ÷ 1/2. [→ La Hadi 2025](#la-hadi-2025)
`q2 i?` As empirical difficulty increases (β > 0), fraction items become much harder for students while LLM-predicted difficulty increases less than expected, indicating a domain-specific bias rather than random error. [→ La Hadi 2025](#la-hadi-2025)

## Evidence

### La Hadi 2025

La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T. (2025). The “Easy Trap”: Why LLMs Underestimate Misconception-Driven Difficulty. https://arxiv.org/abs/2607.26067 [doi:10.48550/arxiv.2607.26067](https://doi.org/10.48550/arxiv.2607.26067)

`q2 · i?` · `associational · r2`

Analysis of the five most underestimated fraction items (Table 2) shows all were "consistently rated as “easy” by LLMs despite empirical failure rates exceeding 66.8%"; the hardest item had only 34.2% correct.

> "In the most extreme case, only 34.2% of students correctly solved division between whole number and fraction (100 ÷ !" ), although it was consistently categorized as a basic procedural task."

### La Hadi 2025 (2)

La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T. (2025). The “Easy Trap”: Why LLMs Underestimate Misconception-Driven Difficulty. https://arxiv.org/abs/2607.26067

`q2 · i?` · `associational · r2`

Figure 2 comparison of LLM-predicted versus empirical IRT difficulty shows non-fraction items follow the expected positive trend while "fraction items systematically deviate from this relationship," a repeated and directional deviation the authors call domain-specific bias.

> "As empirical difficulty increases (β > 0), fraction items become much harder for students, but the increase in LLM-predicted difficulty is smaller than expected."

## Discussion


## Related Claims
- [Student errors on underestimated fraction items reflect systematic misconception patterns rather than random error](fraction-errors-systematic-misconception-patterns.md) — a narrower finding that bears on this claim
- [LLM difficulty predictions for fraction items are less stable across repeated runs than for the overall item set](llm-fraction-predictions-run-to-run-instability.md) — related
- [LLM-generated difficulty ratings show only moderate rank alignment with empirical student performance on basic arithmetic items](llm-difficulty-moderate-rank-alignment-arithmetic.md) — a broader claim this one bears on
- [Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)](llm-difficulty-magnitude-error-varies-across-models.md) — related
- Fine-tuned classifiers detect only about 57% of correct-answer misconceptions despite near-perfect wrong-answer classification — related
- [On the PRM800K validation dataset, detection rates dropped by 10.5 percentage points when final answers were correct, consistent with the correct answer trap extending beyond the Eedi data](cat-extends-to-prm800k-validation.md) — related
- [Correct-answer-trap cases concentrate in specific question types where common flawed reasoning happens to produce the correct numerical answer, with the top two question types accounting for 71% of all TM cases](cat-failures-concentrate-in-two-question-types.md) — related
- Standard ML interventions do not improve hidden-misconception detection beyond the fine-tuned classifier baseline — related
- [The taxonomy decodes overlapping misconceptions behind a single observed loop-tracing error](taxonomy-decodes-overlapping-loop-misconceptions.md) — related
- Only 25% of US Grade 4 students identified the fraction closest to 1/2 on the 2009 NAEP test — related
