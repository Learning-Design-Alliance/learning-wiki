---
type: claim
title: Machine translation of training and test data does not degrade monolingual content scoring performance and can normalize learner errors
description: Machine translation of training and test data does not degrade monolingual content scoring performance and can normalize learner errors
id: mt-normalizes-learner-errors-scoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: andrea-horbach-2024
    resource: "https://doi.org/10.1007/s40593-023-00370-1"
    title: "Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding. (2024). Crosslingual Content Scoring in Five Languages Using Machine-Translation and Multilingual Transformer Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00370-1"
    author: Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Machine translation of training and test data does not degrade monolingual content scoring performance and can normalize learner errors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In Study 1, scoring machine-translated datasets performed in the same ballpark as scoring the originals, sometimes slightly higher for Chinese as the source language. [→ Andrea Horbach 2024](#andrea-horbach-2024)
`q1 i?` Manual probing found misspellings such as vinagar often translated correctly, supporting a normalization-by-translation effect. [→ Andrea Horbach 2024](#andrea-horbach-2024)

## Evidence

### Andrea Horbach 2024

Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding. (2024). Crosslingual Content Scoring in Five Languages Using Machine-Translation and Multilingual Transformer Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00370-1

`q2 · i?` · `design · r2`

Study 1 monolingual baseline experiments translating both training and test data with DeepL into each other language. The article reports results "in the same ballpark as the original data" and attributes this to normalization of spelling errors, with manual checks of misspelled sentences.

> "In most cases, results produced on translated datasets are in the same ballpark as the original data, sometimes even slightly higher especially in the case of Chinese as the original language. This points at a normalizing effect that machine translation can have, for example on spelling errors."

## Discussion


## Related Claims
- [Crosslingual content scoring transfer works better between closely related languages, with Chinese the hardest target in this setup](crosslingual-transfer-language-proximity.md) — related
- [M-BERT with machine translation is the best crosslingual method, outperforming logistic regression with MT and M-BERT zero-shot](mbert-with-mt-best-crosslingual-method.md) — related
- [Monolingual English BERT shows only a slight advantage over multilingual BERT for English content scoring](monolingual-bert-slight-advantage-over-mbert.md) — related
- [Higher-scored learner answers tend to be longer, and crowdsourced answers tend to be shorter than original classroom data](higher-scored-answers-tend-longer.md) — related
- [Part of the crosslingual performance drop is attributable to differences between learner populations and datasets, not only language](dataset-population-differences-drive-scoring-drop.md) — related
