---
type: claim
title: Selecting a pre-trained model from the most contextually similar training institution (MSTI) improves predictive performance over random model selection without improving fairness
description: Selecting a pre-trained model from the most contextually similar training institution (MSTI) improves predictive performance over random model selection without improving fairness
id: msti-selection-improves-performance-over-random
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
sources:
  - id: chengyuan-yao-2025
    title: Chengyuan Yao 2025
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Selecting a pre-trained model from the most contextually similar training institution (MSTI) improves predictive performance over random model selection without improving fairness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` MSTI model selection improves Test AUC over random model selection: for 21 out of 23 target institutions the MSTI model's Test AUC exceeds the expected AUC, but no significant improvements in fairness were observed. [→ Chengyuan Yao 2025](#chengyuan-yao-2025)

## Evidence

### Chengyuan Yao 2025

Chengyuan Yao, Carmen Cortez, and Renzhe Yu. 2025. Towards Fair and Privacy-Aware Transfer Learning for Educational Predictive Modeling: A Case Study on Retention Prediction in Community Colleges. In LAK25: The 15th International Learning Analytics and Knowledge Conference (LAK 2025), March 03–07, 2025, Dublin, Ireland. ACM, New York, NY, USA, 17 pages. https://doi.org/10.1145/3706468.3706567

`q2 · i?` · `design · r2`

Evaluation of Most Similar Training Institution (MSTI) selection across 23 target community colleges; MSTI Test AUC generally underperforms ideal local models (WTNDD failed) but shows "a marked improvement over the distribution of expected AUC obtained from random model selection" (WTNDD failed).

> "Figure 5 indicates that the Test AUC from the MSTI model for 21 out of 23 target institutions exceeds the expected AUC. However, no significant improvements in fairness were observed, consistent with our previous conclusions that fairness is less predictable from contextual similarity."

## Discussion


## Related Claims
- [Sequential training over two institutions selected by demographic similarity improves model fairness without compromising performance, and the larger the initial unfairness the stronger the mitigation](sequential-training-improves-fairness-without-performance-loss.md) — related
- [Direct transfer models tend to experience more pronounced performance issues when overall contextual similarity between source and target institutions falls below 0.5](overall-similarity-below-05-performance-issues.md) — related
