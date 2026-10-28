---
type: claim
title: When demographic groups have different base rates, no method can satisfy calibration, equalized odds, and statistical parity simultaneously
description: When demographic groups have different base rates, no method can satisfy calibration, equalized odds, and statistical parity simultaneously
id: impossibility-fairness-metrics-base-rates
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: mcconvey-2026
    resource: "https://doi.org/10.48550/arxiv.2609.38552"
    title: "McConvey, K., Zhai, A., Li, R., & Guha, S. (2026). Fairness Theatre: Evaluating Post-Hoc Fairness Interventions in Vendor-Controlled Early Warning Systems. arXiv. https://arxiv.org/abs/2609.38552 [doi:10.48550/arxiv.2609.38552](https://doi.org/10.48550/arxiv.2609.38552)"
    author: "McConvey, K., Zhai, A., Li, R., & Guha, S."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# When demographic groups have different base rates, no method can satisfy calibration, equalized odds, and statistical parity simultaneously

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` A mathematical impossibility result, cited from prior work, constrains all post-hoc fairness interventions: with differing group base rates, calibration, equalized odds, and statistical parity cannot be satisfied at once. [→ McConvey 2026](#mcconvey-2026)

## Evidence

### McConvey 2026

McConvey, K., Zhai, A., Li, R., & Guha, S. (2026). Fairness Theatre: Evaluating Post-Hoc Fairness Interventions in Vendor-Controlled Early Warning Systems. arXiv. https://arxiv.org/abs/2609.38552 [doi:10.48550/arxiv.2609.38552](https://doi.org/10.48550/arxiv.2609.38552)

`q1 · i?` · `design · r2`

The article states this as a mathematical constraint shaping its whole evaluation, citing prior impossibility results (Kleinberg et al.; Chouldechova) proving that with different group base rates it is impossible to simultaneously satisfy calibration, equalized odds, and statistical parity. This is a cited theoretical result, not a new empirical finding of this article.

> "when demographic groups succeed at different base rates, no method can satisfy calibration, equalized odds, and statistical parity at once [12, 35] (see Section 3.1)."

## Discussion

## Related Claims

- [Both prior performance flags and the machine learning algorithm are less accurate when predicting outcomes for students who are Black](ews-and-algorithm-less-accurate-black-students.md) — the general claim this finding bears on, with the studies behind it
- [Two of six evaluated interventions directed corrections toward already-advantaged groups because disadvantage was operationalized using group size](group-size-disadvantage-favors-advantaged-groups.md) — related
- [Calibrated Equalized Odds Post-processing showed lower balanced accuracy and higher EOD than the preprocessing techniques DIR and RW in student performance prediction](cpp-postprocessing-accuracy-fairness-tradeoff.md) — related
- [Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop](thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) — related
- [Preprocessing bias mitigation (DIR, RW, SUP) reduced subgroup disparities in TPR on OULAD, with effectiveness varying by demographic attribute](preprocessing-mitigation-reduces-disparities-oulad.md) — related
- [Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities across demographic groups without consistently reducing them](six-posthoc-interventions-redistribute-disparities.md) — a narrower finding that bears on this claim
- [The xOrder fairness method proved inapplicable at institutional scale, with runtime scaling of approximately n^2.36](xorder-intractable-institutional-scale.md) — related
- [The study generalizes individual fairness to education by targeting equal principle consistency for all learners without pairwise learner similarity](individual-fairness-generalized-equal-consistency-all-learners.md) — related
