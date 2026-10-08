---
type: claim
title: Partial dependence plots showed higher word count, more dependent clauses, and higher custom magnitude raised predicted flag probability, with non-linear relationships
description: Partial dependence plots showed higher word count, more dependent clauses, and higher custom magnitude raised predicted flag probability, with non-linear relationships
id: partial-dependence-nonlinear-relationships
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: weak
sources:
  - id: kole-norberg-2025
    resource: "https://doi.org/10.5281/zenodo.15870274"
    title: "Kole Norberg, Husni Almoubayyed, and Stephen Fancsali. (2025). Linguistic Features Predicting Math Word Problem Readability Among Less-Skilled Readers. Proceedings of the 18th International Conference on Educational Data Mining, Palermo, Italy. https://doi.org/10.5281/zenodo.15870274"
    author: Kole Norberg, Husni Almoubayyed, and Stephen Fancsali
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: kole-norberg-2025-2
    resource: "https://doi.org/10.5281/zenodo.15870274"
    title: "Kole Norberg, Husni Almoubayyed, and Stephen Fancsali. (2025). Linguistic Features Predicting Math Word Problem Readability Among Less-Skilled Readers. Proceedings of the 18th International Conference on Educational Data Mining, Palermo, Italy. https://doi.org/10.5281/zenodo.15870274"
    author: Kole Norberg, Husni Almoubayyed, and Stephen Fancsali
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Partial dependence plots showed higher word count, more dependent clauses, and higher custom magnitude raised predicted flag probability, with non-linear relationships

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` Higher word counts were associated with higher probability the model classified a problem as having potential poor readability, reversing the descriptive means pattern. [→ Kole Norberg 2025](#kole-norberg-2025)
`q2 i?` More dependent clauses relative to independent clauses and higher custom magnitude values were each associated with increased probability of readability concerns. [→ Kole Norberg 2025 (2)](#kole-norberg-2025-2)

## Evidence

### Kole Norberg 2025

Kole Norberg, Husni Almoubayyed, and Stephen Fancsali. (2025). Linguistic Features Predicting Math Word Problem Readability Among Less-Skilled Readers. Proceedings of the 18th International Conference on Educational Data Mining, Palermo, Italy. https://doi.org/10.5281/zenodo.15870274

`q2 · i?` · `associational · r2`

Partial dependence plots for the top four readability metrics (Figure 2) from the fitted random forest. The article states the plots "reveal non-linear relationships" with sharp boundaries; associations are model-derived, not causal tests.

> "Reversing the pattern in the means, higher word counts were associated with higher probability that the model would classify a problem as having potential poor readability."

### Kole Norberg 2025 (2)

Kole Norberg, Husni Almoubayyed, and Stephen Fancsali. (2025). Linguistic Features Predicting Math Word Problem Readability Among Less-Skilled Readers. Proceedings of the 18th International Conference on Educational Data Mining, Palermo, Italy. https://doi.org/10.5281/zenodo.15870274

`q2 · i?` · `associational · r2`

Same partial dependence analysis (Figure 2): clause ratio and custom magnitude showed straightforward positive relationships with predicted flag probability. The article notes higher custom magnitude indicates more specific or distinctive semantic content.

> "Having more dependent clauses as compared to independent clauses led the model to give the MWP a higher probability of having poor readability."

## Discussion


## Related Claims
- [Flagged word problems were shorter (lower word count) but had more sentences than non-flagged problems in descriptive statistics](flagged-problems-shorter-more-sentences-descriptives.md) — related
- [4,446 of 9,421 MATHia word problems showed larger-than-expected error-rate gaps between less- and more-skilled readers and were flagged for potential readability concerns](mathia-word-problems-flagged-reading-gaps.md) — related
- [In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom](word-count-top-traditional-formulas-unimportant.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
