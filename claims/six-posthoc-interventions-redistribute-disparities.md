---
type: claim
title: Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities across demographic groups without consistently reducing them
description: Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities across demographic groups without consistently reducing them
id: six-posthoc-interventions-redistribute-disparities
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: mcconvey-2026
    resource: "https://arxiv.org/abs/2609.38552"
    title: "McConvey, K., Zhai, A., Li, R., & Guha, S. (2026). Fairness Theatre: Evaluating Post-Hoc Fairness Interventions in Vendor-Controlled Early Warning Systems. arXiv. https://arxiv.org/abs/2609.38552"
    author: "McConvey, K., Zhai, A., Li, R., & Guha, S."
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities across demographic groups without consistently reducing them

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`

## Subclaims
`q2 i?` Across six post-hoc methods applied to calibrated EWS outputs under simulated procurement constraints, fairness interventions redistributed group disparities rather than consistently reducing them. [→ McConvey 2026](#mcconvey-2026)

## Evidence

### McConvey 2026

McConvey, K., Zhai, A., Li, R., & Guha, S. (2026). Fairness Theatre: Evaluating Post-Hoc Fairness Interventions in Vendor-Controlled Early Warning Systems. arXiv. https://arxiv.org/abs/2609.38552

`q2 · i?` · `causal · r?`

The article's abstract reports the headline outcome of its comparative evaluation of six post-hoc fairness methods on a research EWS replica built from 168,550 student records: "Interventions redistributed disparities without consistently reducing them." The full results section was not available in the supplied text, so this rests on the article's own summary statement rather than its printed tables.

> "Interventions redistributed disparities without consistently reducing them. Two implementations favored already-advantaged groups because they used group size to define disadvantage; small, marginalized groups remained poorly served."

## Discussion


## Related Claims
- [Two of six evaluated interventions directed corrections toward already-advantaged groups because disadvantage was operationalized using group size](group-size-disadvantage-favors-advantaged-groups.md) — related
- [When demographic groups have different base rates, no method can satisfy calibration, equalized odds, and statistical parity simultaneously](impossibility-fairness-metrics-base-rates.md) — a broader claim this one bears on
- [Preprocessing bias mitigation (DIR, RW, SUP) reduces subgroup disparities in TPR while maintaining acceptable balanced accuracy](preprocessing-mitigation-reduces-disparities-oulad.md) — related
- [Calibrated Equalized Odds Post-processing shows significant accuracy drops and higher EOD compared to preprocessing techniques](cpp-postprocessing-accuracy-fairness-tradeoff.md) — a narrower finding that bears on this claim
- [Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop](thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) — a narrower finding that bears on this claim
- [The xOrder fairness method proved inapplicable at institutional scale, with runtime scaling of approximately n^2.36](xorder-intractable-institutional-scale.md) — related
- [Standard ML models predicting student pass/fail from VLE data exhibit biased true-positive rates across demographic subgroups](baseline-ml-models-biased-tpr-oulad.md) — related
- [Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity](data-balancing-improves-accuracy-increases-bias.md) — related
