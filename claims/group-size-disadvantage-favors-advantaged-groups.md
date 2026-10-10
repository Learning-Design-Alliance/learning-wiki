---
type: claim
title: Two of six evaluated interventions directed corrections toward already-advantaged groups because disadvantage was operationalized using group size
description: Two of six evaluated interventions directed corrections toward already-advantaged groups because disadvantage was operationalized using group size
id: group-size-disadvantage-favors-advantaged-groups
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
    rigour: 2
---

# Two of six evaluated interventions directed corrections toward already-advantaged groups because disadvantage was operationalized using group size

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Two of the six post-hoc methods favored already-advantaged groups; the article attributes the immediate cause to implementations that used group size to define disadvantage, and its persistence to procurement's informational constraints. [→ McConvey 2026](#mcconvey-2026)

## Evidence

### McConvey 2026

McConvey, K., Zhai, A., Li, R., & Guha, S. (2026). Fairness Theatre: Evaluating Post-Hoc Fairness Interventions in Vendor-Controlled Early Warning Systems. arXiv. https://arxiv.org/abs/2609.38552

`q2 · i?` · `causal · r2`

The article's contributions paragraph reports this failure pattern from its evaluation of six interventions on the research EWS replica: methods "operationalized disadvantage using group size," so corrections flowed to already-advantaged groups and small marginalized groups remained poorly served. The specific per-method results were in a truncated portion of the supplied text.

> "Two of the six methods we evaluate directed corrections toward already-advantaged groups, a failure whose immediate cause is how our implementations operationalized disadvantage using group size, and which persists because the informational constraints of procurement leave institutions unable to detect or override it."

## Discussion


## Related Claims
- [Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities across demographic groups without consistently reducing them](six-posthoc-interventions-redistribute-disparities.md) — related
- [When demographic groups have different base rates, no method can satisfy calibration, equalized odds, and statistical parity simultaneously](impossibility-fairness-metrics-base-rates.md) — related
- [The xOrder fairness method proved inapplicable at institutional scale, with runtime scaling of approximately n^2.36](xorder-intractable-institutional-scale.md) — related
