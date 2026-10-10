---
type: claim
title: LLM-generated 7C collaboration assessment scores fall within the range of human expert variability across ten discussions
description: LLM-generated 7C collaboration assessment scores fall within the range of human expert variability across ten discussions
id: llm-7c-scores-within-expert-variability
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: dawei-xie-2026
    resource: "https://arxiv.org/abs/2605.17259"
    title: "Dawei Xie, Khalil Anderson, Tochukwu Eze, Chenghong Lin, Bookyung Shin, and Marcelo Worsley. (2026). CLARA: An AI-Augmented Analytics Dashboard for Collaboration Literacy. https://arxiv.org/abs/2605.17259"
    author: Dawei Xie, Khalil Anderson, Tochukwu Eze, Chenghong Lin, Bookyung Shin, and Marcelo Worsley
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: dawei-xie-2026-2
    resource: "https://arxiv.org/abs/2605.17259"
    title: "Dawei Xie, Khalil Anderson, Tochukwu Eze, Chenghong Lin, Bookyung Shin, and Marcelo Worsley. (2026). CLARA: An AI-Augmented Analytics Dashboard for Collaboration Literacy. https://arxiv.org/abs/2605.17259"
    author: Dawei Xie, Khalil Anderson, Tochukwu Eze, Chenghong Lin, Bookyung Shin, and Marcelo Worsley
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM-generated 7C collaboration assessment scores fall within the range of human expert variability across ten discussions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Adding the LLM as an additional rater did not reduce overall inter-rater agreement (alpha .637 vs .639), and LLM scores deviated less from the human mean than human scores deviated from each other (MAD 8.79 vs 10.25). [→ Dawei Xie 2026](#dawei-xie-2026)

## Evidence

### Dawei Xie 2026

Dawei Xie, Khalil Anderson, Tochukwu Eze, Chenghong Lin, Bookyung Shin, and Marcelo Worsley. (2026). CLARA: An AI-Augmented Analytics Dashboard for Collaboration Literacy. https://arxiv.org/abs/2605.17259

`q2 · i?` · `design · r2`

Score-level agreement study comparing LLM and human expert 7C assessments of 10 discussions, each scored 0-100 per dimension by 2-3 independent raters. The article reports "overall MAD:8.79vs.10.25on the 100-point scale" favoring the LLM, and overall Krippendorff's alpha essentially unchanged when the LLM was added (.637 vs .639).

> "In absolute terms, LLM-produced scores deviated less from the human mean than individual human scores deviated from each other (overall MAD:8.79vs.10.25on the 100-point scale)."

### Dawei Xie 2026 (2)

Dawei Xie, Khalil Anderson, Tochukwu Eze, Chenghong Lin, Bookyung Shin, and Marcelo Worsley. (2026). CLARA: An AI-Augmented Analytics Dashboard for Collaboration Literacy. https://arxiv.org/abs/2605.17259

`q2 · i?` · `design · r2`

Spearman correlation between LLM scores and human mean scores across the 10 discussions and 70 dimension-level assessments; the article reports "overallρ=.701,p < .001", with Conflict (.765), Communication (.760), and Climate (.711) strongest and Context weakest (.259).

> "LLM-produced scores’ rank-ordering of discussions tracked human consensus on most dimensions(overallρ=.701,p < .001)."

## Discussion


## Related Claims
- [LLM and human written 7C analyses show no overall difference in behavioral alignment or evidence correspondence, but align less on Communication and Constructive dimensions](llm-7c-analytical-alignment-mixed.md) — related
- [Making trustworthiness metrics and visualizations explicit increased inter-rater reliability among learning engineers evaluating LLM responses](trustworthiness-metrics-visualizations-increase-expert-agreement.md) — related
- [Three independent expert instructors reached exceptionally high inter-rater reliability when grading 1200 bash exam responses, establishing a reliable human reference standard](expert-triad-high-inter-rater-reliability-bash-grading.md) — related
- [Expert former math teachers rated GPT-4o's dialogue annotations very highly for student correctness and moderate-to-high for knowledge components, with volatile inter-rater reliability.](expert-teachers-rate-gpt-4o-dialogue-annotations-as-largely-accurate.md) — related
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [LLM ratings of classroom transcripts are more correlated with each other than with expert human ratings, across the same and different tasks](llm-llm-agreement-exceeds-llm-human-classroom-ratings.md) — related
