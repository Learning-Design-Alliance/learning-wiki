---
type: claim
title: LLM difficulty predictions for fraction items are less stable across repeated runs than for the overall item set
description: LLM difficulty predictions for fraction items are less stable across repeated runs than for the overall item set
id: llm-fraction-predictions-run-to-run-instability
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
---

# LLM difficulty predictions for fraction items are less stable across repeated runs than for the overall item set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Fraction items produced higher flip rates (run-to-run inconsistency in difficulty predictions) than the overall item set, with Gemini showing almost 91% inconsistency across repetitions. [→ La Hadi 2025](#la-hadi-2025)

## Evidence

### La Hadi 2025

La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T. (2025). The “Easy Trap”: Why LLMs Underestimate Misconception-Driven Difficulty. https://arxiv.org/abs/2607.26067 [doi:10.48550/arxiv.2607.26067](https://doi.org/10.48550/arxiv.2607.26067)

`q2 · i?` · `associational · r2`

Flip-rate analysis across five runs (Figure 3) shows "fraction items produced higher rates of inconsistent difficulty predictions than the overall item set"; the article suggests LLM judgments on misconception-driven problems are also less stable across repeated evaluations.

> "Especially for Gemini, which shows almost 91% inconsistency during repetition, which means 10 out of 11 fractions get different difficulty estimation more than 3 times."

## Discussion


## Related Claims
- [LLMs systematically underestimate fraction items whose difficulty is driven by misconceptions (the \"Easy Trap\")](easy-trap-fraction-items-underestimated-by-llms.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](ai-grading-run-to-run-reliability-icc.md) — related
- [Smaller local LLMs show a minor position bias toward option ordering and partially guessing-like error variation, but accuracy remains relatively stable across permutations and repeated sampling runs](minor-position-bias-and-partial-guessing-in-small-llms.md) — related
- [Human annotators judge later-round CPIG items as improved in complexity but not in difficulty, with modest rater agreement](human-review-complexity-improves-difficulty-static.md) — related
- [Exploratory analysis found item difficulty differed across sources, driven by the Google Gemini versus NLE contrast](item-difficulty-differs-across-sources-gemini-nle.md) — related
