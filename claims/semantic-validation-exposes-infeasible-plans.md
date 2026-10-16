---
type: claim
title: Activating availability constraints in the IP pipeline lowers SHACL conformance to 0.875 without reducing optimization cost, exposing infeasible plans
description: Activating availability constraints in the IP pipeline lowers SHACL conformance to 0.875 without reducing optimization cost, exposing infeasible plans
id: semantic-validation-exposes-infeasible-plans
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: ngoc-luyen-le-2026
    resource: "https://doi.org/10.48550/arxiv.2608.17618"
    title: "Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge. (2026). From Student Risk Prediction to SC2R: Semantics-Constrained Counterfactual Recourse for Educational Decision Support. arXiv preprint. https://arxiv.org/abs/2608.17618 [doi:10.48550/arxiv.2608.17618](https://doi.org/10.48550/arxiv.2608.17618)"
    author: Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Activating availability constraints in the IP pipeline lowers SHACL conformance to 0.875 without reducing optimization cost, exposing infeasible plans

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In a 200-case ablation, IP and Wachter-style baselines have nearly identical average cost (24.127 vs. 24.175) with perfect conformance, but IP with availability constraints drops to conformance 0.875 at the same cost. [→ Ngoc Luyen Le 2026](#ngoc-luyen-le-2026)

## Evidence

### Ngoc Luyen Le 2026

Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge. (2026). From Student Risk Prediction to SC2R: Semantics-Constrained Counterfactual Recourse for Educational Decision Support. arXiv preprint. https://arxiv.org/abs/2608.17618 [doi:10.48550/arxiv.2608.17618](https://doi.org/10.48550/arxiv.2608.17618)

`q2 · i?` · `design · r2`

Controlled 200-case ablation comparing IP recourse, Wachter-style recourse, and IP with availability constraints (Fig. 5). The article reports that "the conformance rate decreases to0.875without any reduction in optimization cost" when availability constraints are activated.

> "The IP solver and the Wachter-style baseline have nearly identical average cost (24.127 vs. 24.175), and both achieve perfect model validity and SHACL conformance under the baseline con- straint configuration. However, when availability constraints are activated in the IP pipeline, the conformance rate decreases to0.875without any reduction in optimization cost."

## Discussion


## Related Claims
- [Integer-programming recourse generates compact, model-valid, SHACL-conformant intervention plans at scale on OULAD](ip-recourse-compact-plans-at-scale.md) — related
