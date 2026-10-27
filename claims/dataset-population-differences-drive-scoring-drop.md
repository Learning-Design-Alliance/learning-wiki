---
type: claim
title: Part of the crosslingual performance drop is attributable to differences between learner populations and datasets, not only language
description: Part of the crosslingual performance drop is attributable to differences between learner populations and datasets, not only language
id: dataset-population-differences-drive-scoring-drop
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
sources:
  - id: andrea-horbach-2024
    resource: "https://doi.org/10.1007/s40593-023-00370-1"
    title: "Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding. (2024). Crosslingual Content Scoring in Five Languages Using Machine-Translation and Multilingual Transformer Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00370-1"
    author: Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: andrea-horbach-2024-2
    resource: "https://doi.org/10.1007/s40593-023-00370-1"
    title: "Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding. (2024). Crosslingual Content Scoring in Five Languages Using Machine-Translation and Multilingual Transformer Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00370-1"
    author: Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# Part of the crosslingual performance drop is attributable to differences between learner populations and datasets, not only language

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q1`–`q2`

## Subclaims
`q2 i?` The authors conclude that different user populations think or write differently about the same prompt, contributing to the crosslingual scoring gap. [→ Andrea Horbach 2024 (2)](#andrea-horbach-2024-2)
`q1 i?` Similarity and n-gram analyses indicate the Chinese data is conceptually different from the other datasets. [→ Andrea Horbach 2024 (2)](#andrea-horbach-2024-2)

## Evidence

### Andrea Horbach 2024

Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding. (2024). Crosslingual Content Scoring in Five Languages Using Machine-Translation and Multilingual Transformer Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00370-1

`q2 · i?` · `design · r2`

Further Analyses section: SBERT-based maximum answer-similarity comparisons between datasets and inspection of high-frequency n-grams per dataset. The article reports most cross-dataset histograms look similar, while Chinese answers show distinct concepts such as PH value and acid rain.

> "We therefore conclude that part of the drop in performance is due to the nature of the different datasets, i.e. that different user populations think or at least write differently about the same prompt."

### Andrea Horbach 2024 (2)

Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding. (2024). Crosslingual Content Scoring in Five Languages Using Machine-Translation and Multilingual Transformer Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00370-1

`q1 · i?` · `causal · r2`

Authors' interpretation of the n-gram analysis for Prompt 1, where terms like PH value and acid rain appear only in the Chinese top-10 list while other languages discuss the amount of vinegar. The article leaves open whether this reflects cultural differences or task approaches.

> "This supports our assumption that Chinese data is indeed conceptually different from other datasets."

## Discussion


## Related Claims
- [Crosslingual content scoring transfer works better between closely related languages, with Chinese the hardest target in this setup](crosslingual-transfer-language-proximity.md) — related
- [Higher-scored learner answers tend to be longer, and crowdsourced answers tend to be shorter than original classroom data](higher-scored-answers-tend-longer.md) — possibly the same claim (merge candidate)
- [Machine translation of training and test data does not degrade monolingual content scoring performance and can normalize learner errors](mt-normalizes-learner-errors-scoring.md) — related
