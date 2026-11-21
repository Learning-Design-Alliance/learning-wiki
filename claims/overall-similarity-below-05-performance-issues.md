---
type: claim
title: Direct transfer models tend to experience more pronounced performance issues when overall contextual similarity between source and target institutions falls below 0.5
description: Direct transfer models tend to experience more pronounced performance issues when overall contextual similarity between source and target institutions falls below 0.5
id: overall-similarity-below-05-performance-issues
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
sources:
  - id: chengyuan-yao-2025
    title: Chengyuan Yao 2025
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Direct transfer models tend to experience more pronounced performance issues when overall contextual similarity between source and target institutions falls below 0.5

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Higher overall contextual similarity between institutions is associated with improved AUC scores and reduced performance drop, with more pronounced performance issues below an overall similarity of 0.5 and two distinct clusters at 0.15–0.45 and 0.65–0.95. [→ Chengyuan Yao 2025](#chengyuan-yao-2025)

## Evidence

### Chengyuan Yao 2025

Chengyuan Yao, Carmen Cortez, and Renzhe Yu. 2025. Towards Fair and Privacy-Aware Transfer Learning for Educational Predictive Modeling: A Case Study on Retention Prediction in Community Colleges. In LAK25: The 15th International Learning Analytics and Knowledge Conference (LAK 2025), March 03–07, 2025, Dublin, Ireland. ACM, New York, NY, USA, 17 pages. https://doi.org/10.1145/3706468.3706567

`q2 · i?` · `associational · r2`

Figure 3 analysis of overall similarity (coefficient-significance weighted, cost similarity dropped) versus Test AUC, inverted AUC drop, and AUC Gap, showing a "positive linear trend" for performance and a largely flat, slightly negative trend for AUC Gap.

> "The left two plots demonstrate a positive linear trend, indicating that higher overall similarity between institutions is associated with improved AUC scores and a reduced performance drop. Notably, when overall similarity falls below 0.5, the model tends to experience more pronounced performance issues."

## Discussion


## Related Claims
- [Selecting a pre-trained model from the most contextually similar training institution (MSTI) improves predictive performance over random model selection without improving fairness](msti-selection-improves-performance-over-random.md) — related
- [Sequential training over two institutions selected by demographic similarity improves model fairness without compromising performance, and the larger the initial unfairness the stronger the mitigation](sequential-training-improves-fairness-without-performance-loss.md) — related
- [Transfer between isomorphic questions depends on contextual closeness: no significant gain for the far pair (7)-(8) but significant gain for the closer pair (9)-(10)](transfer-depends-on-context-closeness.md) — related
