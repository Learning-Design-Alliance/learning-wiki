---
type: claim
title: Variance terms in multi-armed RCT estimators need slight adjustment under the finite-population framework, which can reduce precision
description: Variance terms in multi-armed RCT estimators need slight adjustment under the finite-population framework, which can reduce precision
id: variance-adjustment-reduces-precision-multi-armed
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: peter-z-schochet-2018
    resource: "https://www.mathematica.org/publications/design-based-estimators-for-average-treatment-effects-for-multi-armed-rcts"
    title: "Peter Z. Schochet. (2018). Design-Based Estimators for Average Treatment Effects for Multi-Armed RCTs. Journal of Educational and Behavioral Statistics, vol. 43, issue 5. https://www.mathematica.org/publications/design-based-estimators-for-average-treatment-effects-for-multi-armed-rcts"
    author: Peter Z. Schochet
    q: 2
    i: "?"
    kind: theoretical
    rigour: "?"
---

# Variance terms in multi-armed RCT estimators need slight adjustment under the finite-population framework, which can reduce precision

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r?` · `q2`

## Subclaims
`q2 i?` Variance terms need to be adjusted slightly under the finite-population framework in multi-armed trials, and this adjustment can reduce precision. [→ Peter Z. Schochet 2018](#peter-z-schochet-2018)

## Evidence

### Peter Z. Schochet 2018

Peter Z. Schochet. (2018). Design-Based Estimators for Average Treatment Effects for Multi-Armed RCTs. Journal of Educational and Behavioral Statistics, vol. 43, issue 5. https://www.mathematica.org/publications/design-based-estimators-for-average-treatment-effects-for-multi-armed-rcts

`q2 · i?` · `theoretical · r?`

Analytical methodological result derived from the article's key insight about pairwise contrast samples. The article states the variance adjustment "can reduce precision" and links it to a block-weighting requirement in the same sentence.

> "The implication is that variance terms need to be adjusted slightly under the finite-population framework that can reduce precision, and blocks need to be weighted to reflect the full randomized sample in the block or biases can result."

## Discussion


## Related Claims
- [Identifying and estimating the CACE parameter in the multi-armed context requires complex assumptions](multi-armed-cace-complex-assumptions.md) — related
- [Design-based estimators for two-group designs require modification for multi-armed designs when comparing pairs of research groups](multi-armed-estimators-modify-two-group-estimators.md) — a broader claim this one bears on
- [In multi-armed trials seeking the most effective treatments, each pairwise contrast sample is representative of the full set of randomized units](pairwise-contrast-samples-represent-full-randomized-set.md) — related
- [Appropriate average treatment effect estimators can be derived for both finite-population and super-population models of clustered RCTs](appropriate-estimators-derived-for-each-causal-model.md) — related
