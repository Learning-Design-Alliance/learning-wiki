---
type: claim
title: MAP and EAP quantify assessor agreement at the pairwise level from BCJ Beta posteriors, identifying contentious comparisons that a single aggregate reliability score cannot
description: MAP and EAP quantify assessor agreement at the pairwise level from BCJ Beta posteriors, identifying contentious comparisons that a single aggregate reliability score cannot
id: map-eap-pairwise-reliability-metrics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: andy-gray-2025
    resource: "https://doi.org/10.2139/ssrn.5674497"
    title: "Andy Gray, Alma Rahat, Tom Crick, Stephen Lindsay. (2025). Bayesian Active Learning for Comparative Judgement: Reliability Estimation and Multi-Criteria Evaluation with Applications in Educational Assessment. [doi:10.2139/ssrn.5674497](https://doi.org/10.2139/ssrn.5674497)"
    author: Andy Gray, Alma Rahat, Tom Crick, Stephen Lindsay
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# MAP and EAP quantify assessor agreement at the pairwise level from BCJ Beta posteriors, identifying contentious comparisons that a single aggregate reliability score cannot

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The proposed MAP and EAP metrics, derived from Beta posteriors over pairwise preferences, quantify agreement among assessors and help identify controversial comparisons. [→ Andy Gray 2025](#andy-gray-2025)

## Evidence

### Andy Gray 2025

Andy Gray, Alma Rahat, Tom Crick, Stephen Lindsay. (2025). Bayesian Active Learning for Comparative Judgement: Reliability Estimation and Multi-Criteria Evaluation with Applications in Educational Assessment. [doi:10.2139/ssrn.5674497](https://doi.org/10.2139/ssrn.5674497)

`q2 · i?` · `design · r2`

Analytical derivation in the paper's methods sections: MAP measures divergence of the Beta posterior mode from 0.5, and EAP integrates |p − 0.5| over the posterior density, so both "quantifythelevelofagree- ment among assessors". The EAP closed form was validated through simulation by the authors.

> "We introduce two novel metrics – Mode Agreement Percentage (MAP) and Expected Agreement Percentage (EAP) – based on a Beta prior over pairwise preferences.Thesemetricsquantifythelevelofagree- ment among assessors and help identify controversial comparisons."

## Discussion


## Related Claims
- [Entropy-based pair selection in BCJ was shown to be superior to random and No-Repeating-Pairs selection methods](entropy-selection-beats-random-nrp.md) — related
- [MAP rises near-instantly toward 100% under consistent wins while EAP increases only with numerous comparisons, making EAP more stable under conflicting information](map-overoptimistic-eap-stable.md) — a narrower finding that bears on this claim
- [MBCJ performs comparably to standard BCJ on real assessment data while providing finer-grained criterion-level insights](mbcj-comparable-to-bcj-with-criterion-insight.md) — related
