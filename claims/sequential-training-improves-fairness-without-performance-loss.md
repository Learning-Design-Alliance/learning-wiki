---
type: claim
title: Sequential training over two institutions selected by demographic similarity improves model fairness without compromising performance, and the larger the initial unfairness the stronger the mitigation
description: Sequential training over two institutions selected by demographic similarity improves model fairness without compromising performance, and the larger the initial unfairness the stronger the mitigation
id: sequential-training-improves-fairness-without-performance-loss
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
    kind: causal
    rigour: 1
---

# Sequential training over two institutions selected by demographic similarity improves model fairness without compromising performance, and the larger the initial unfairness the stronger the mitigation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The WTNDD test for Test AUC distributions passed under all three MSTI AUC gap thresholds, indicating no significant performance difference between sequential and MSTI models, while AUC Gap distributions differed increasingly (Wasserstein Distances of 0.26, 0.37, and 0.46). [→ Chengyuan Yao 2025](#chengyuan-yao-2025)

## Evidence

### Chengyuan Yao 2025

Chengyuan Yao, Carmen Cortez, and Renzhe Yu. 2025. Towards Fair and Privacy-Aware Transfer Learning for Educational Predictive Modeling: A Case Study on Retention Prediction in Community Colleges. In LAK25: The 15th International Learning Analytics and Knowledge Conference (LAK 2025), March 03–07, 2025, Dublin, Ireland. ACM, New York, NY, USA, 17 pages. https://doi.org/10.1145/3706468.3706567

`q2 · i?` · `causal · r1`

Comparison of sequential model (MSTI plus a demographically dissimilar second institution, trained with Elastic Weight Consolidation) against MSTI models at AUC gap thresholds 0.00/0.05/0.10; the Test AUC WTNDD test passed under all three thresholds.

> "In contrast, the WTNDD test for differences in AUC Gap distributions failed, with Wasserstein Distances of 0.26, 0.37, and 0.46 for MSTI AUC Gaps exceeding 0.00, 0.05, and 0.10, respectively."

## Discussion


## Related Claims
- [Selecting a pre-trained model from the most contextually similar training institution (MSTI) improves predictive performance over random model selection without improving fairness](msti-selection-improves-performance-over-random.md) — related
- [Direct transfer models tend to experience more pronounced performance issues when overall contextual similarity between source and target institutions falls below 0.5](overall-similarity-below-05-performance-issues.md) — related
- [Educational AI systems risk perpetuating demographic bias, which a group-level disparity measure can quantify to promote fairness](demographic-disparity-measure-for-educational-ai-fairness.md) — a broader claim this one bears on
- [When demographic groups have different base rates, no method can satisfy calibration, equalized odds, and statistical parity simultaneously](impossibility-fairness-metrics-base-rates.md) — a broader claim this one bears on
- [Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities across demographic groups without consistently reducing them](six-posthoc-interventions-redistribute-disparities.md) — related
- [Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop](thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) — related
