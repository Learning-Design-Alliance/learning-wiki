---
type: claim
title: A substantial part of the LLM rating advantage appears attributable to comment length, as length-adjusted scores converge on every dimension except tone
description: A substantial part of the LLM rating advantage appears attributable to comment length, as length-adjusted scores converge on every dimension except tone
id: length-explains-llm-rating-advantage
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: yijun-liu-2026
    resource: "https://arxiv.org/abs/2606.06271"
    title: "Yijun Liu, Yifan Song, John Gallagher, Sarah Sterman, Tal August. (2026). FOXGLOVE: Understanding Goal-Oriented and Anchored Writing Feedback from Experts and LLMs on Argumentative Essays. https://arxiv.org/abs/2606.06271"
    author: Yijun Liu, Yifan Song, John Gallagher, Sarah Sterman, Tal August
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# A substantial part of the LLM rating advantage appears attributable to comment length, as length-adjusted scores converge on every dimension except tone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` After length adjustment, human ratings rise and LLM ratings fall on every dimension except tone, with the largest effects for specificity (1.85→0.45) and actionability (1.40→0.42). [→ Yijun Liu 2026](#yijun-liu-2026)

## Evidence

### Yijun Liu 2026

Yijun Liu, Yifan Song, John Gallagher, Sarah Sterman, Tal August. (2026). FOXGLOVE: Understanding Goal-Oriented and Anchored Writing Feedback from Experts and LLMs on Argumentative Essays. https://arxiv.org/abs/2606.06271

`q2 · i?` · `associational · r2`

Length-adjusted analysis (§5.1.1): OLS regression of each rubric dimension on word count for the 85 rated sentence-level items, with adjusted means evaluated at the overall mean length (≈64 words). The article reports "Adjustment convergesbothsides rather than just lowering LLM scores".

> "We found that a substantial part of the apparent human-model rating gap appears to be driven by length. Adjustment convergesbothsides rather than just lowering LLM scores: at the average length, human ratings rise and LLM ratings fall on every dimension except tone."

## Discussion


## Related Claims
- [LLM feedback receives higher expert ratings on six of seven quality dimensions, with tone the exception](llm-feedback-higher-expert-ratings.md) — related
- [Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)](human-llm-judge-preference-alignment-deeptutor.md) — related
