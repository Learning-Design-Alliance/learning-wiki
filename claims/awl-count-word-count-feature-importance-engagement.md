---
type: claim
title: Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts
description: Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts
id: awl-count-word-count-feature-importance-engagement
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
sources:
  - id: gorgun-2022
    resource: "https://doi.org/10.5281/zenodo.6853149"
    title: "Gorgun, G., Yildirim-Erbasli, S. N., & Demmans Epp, C. (2022). Predicting cognitive engagement in online course discussion forums. Proceedings of the 15th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.6853149"
    author: "Gorgun, G., Yildirim-Erbasli, S. N., & Demmans Epp, C."
    q: 2
    i: "?"
---

# Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` Decision tree and random forest models identified the same top features (word count, AWL count, type-token ratio, Flesch-Kincaid grade level), while the SVM identified a different set led by second language readability. [→ Gorgun 2022](#gorgun-2022)

## Evidence

### Gorgun 2022

Gorgun, G., Yildirim-Erbasli, S. N., & Demmans Epp, C. (2022). Predicting cognitive engagement in online course discussion forums. Proceedings of the 15th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.6853149

`q2 · i?`

Feature importance analysis of the random forest classifier using mean decrease in Gini, compared with Gini-based importance from the decision tree. The decision tree's top predictor was AWL count, followed by whether a post is a reply, Flesch-Kincaid grade level, and word count.

> "Similar to the decision tree model, we found that the most important features were the number of words (i.e., DESWC), number of academic word list items (AWLCount), type-token ratio for all words (LDTTRa), and Flesch-Kincaid grade level (RDFKGL)."

## Discussion


## Related Claims
-
