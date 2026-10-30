---
type: claim
title: The most accurate scorer showed no gender disparity but a small significant language-background disparity favoring foreign-language speakers
description: The most accurate scorer showed no gender disparity but a small significant language-background disparity favoring foreign-language speakers
id: language-bias-favors-foreign-speakers-roberta-svm
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: nico-andersen-2025
    resource: "https://doi.org/10.1007/s40593-025-00495-5"
    title: "Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner. (2025). Algorithmic Fairness in Automatic Short Answer Scoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00495-5"
    author: Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# The most accurate scorer showed no gender disparity but a small significant language-background disparity favoring foreign-language speakers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For the RoBERTa-SVM model, demographic disparity was negligible for gender (DD = .000) but significant for language spoken at home (DD = −.011, p < .025), with foreign-language speakers receiving about 1% more false positive scorings than native speakers. [→ Nico Andersen 2025](#nico-andersen-2025)

## Evidence

### Nico Andersen 2025

Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner. (2025). Algorithmic Fairness in Automatic Short Answer Scoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00495-5

`q2 · i?` · `associational · r2`

In-depth fairness analysis of the best-performing RoBERTa-SVM across all items, comparing group-specific scoring bias D between native and foreign-language speakers. Both groups were overestimated; the disparity DD = −.011 was flagged significant at p < .025 via bootstrap significance testing (10,000 resamples).

> "Due to the differences for both native ( D = .02) and foreign language speakers ( D = .03) and the resulting disparity of ( DD = −.011), foreign language speakers receive around 1% more false positive scorings than native speakers."

## Discussion


## Related Claims
- [Demographic disparities in automatic scoring are concentrated at the item level, tied to class distributions and item difficulty](item-level-disparity-class-distribution-difficulty.md) — related
- [Methods with higher scoring accuracy showed lower demographic disparity across the tested model combinations](higher-accuracy-lower-disparity.md) — a broader claim this one bears on
- [Lower-performing groups gain relative advantage because the scorer detects incorrect responses better for them, producing more false positives](lower-performers-more-false-positives-advantage.md) — related
- [SVM with RoBERTa sentence embeddings was the most accurate automatic scoring method (κ = .82) among the four tested combinations](roberta-svm-most-accurate-scoring-pisa.md) — related
