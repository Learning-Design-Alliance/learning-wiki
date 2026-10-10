---
type: claim
title: The xOrder fairness method proved inapplicable at institutional scale, with runtime scaling of approximately n^2.36
description: The xOrder fairness method proved inapplicable at institutional scale, with runtime scaling of approximately n^2.36
id: xorder-intractable-institutional-scale
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

# The xOrder fairness method proved inapplicable at institutional scale, with runtime scaling of approximately n^2.36

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` One of seven initially selected methods, xOrder, was excluded because it is defined only for binary sensitive attributes and its dynamic program is computationally intractable at institutional scale; the article treats this inapplicability as a finding. [→ McConvey 2026](#mcconvey-2026)

## Evidence

### McConvey 2026

McConvey, K., Zhai, A., Li, R., & Guha, S. (2026). Fairness Theatre: Evaluating Post-Hoc Fairness Interventions in Vendor-Controlled Early Warning Systems. arXiv. https://arxiv.org/abs/2609.38552

`q2 · i?` · `causal · r2`

A benchmarking analysis of the xOrder method on the institution's data showed intractable scaling: "runtime scaling of approximately 𝑛2.36," extrapolating to months of computation and over one hundred gigabytes of memory for one domestic-international comparison. The method is also formally defined only for binary sensitive attributes, while two of the study's three attributes are not binary.

> "benchmarking it on our data yields runtime scaling of approximately 𝑛2.36, which extrapolates to months of computation and over one hundred gigabytes of memory for a single domestic–international comparison at full cohort size."

## Discussion


## Related Claims
- [Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities across demographic groups without consistently reducing them](six-posthoc-interventions-redistribute-disparities.md) — related
- [Two of six evaluated interventions directed corrections toward already-advantaged groups because disadvantage was operationalized using group size](group-size-disadvantage-favors-advantaged-groups.md) — related
- [Runtime GenUI adaptation is too late, too costly, and accuracy-risky to be equitable at scale for learners needing non-default representations](runtime-genui-too-late-costly-inequitable.md) — related
