---
type: claim
title: Collateral information significantly improves the accuracy of short CAT administrations across progression models
description: Collateral information significantly improves the accuracy of short CAT administrations across progression models
id: collateral-information-improves-cat-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: jun-ichiro-yasuda-2025
    resource: "https://doi.org/10.1103/x2rq-z8lm"
    title: "Jun-ichiro Yasuda, Michael M. Hull, Naohiro Mae, Kentaro Kojima. (2025). Chained computerized adaptive testing for the Force Concept Inventory. arXiv. Originally published 2024. [doi:10.1103/x2rq-z8lm](https://doi.org/10.1103/x2rq-z8lm)"
    author: Jun-ichiro Yasuda, Michael M. Hull, Naohiro Mae, Kentaro Kojima
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Collateral information significantly improves the accuracy of short CAT administrations across progression models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using the previous test's proficiency estimate as collateral information yields session-averaged RMSE smaller than or comparable to basic CAT for all simulated progression models. [→ Jun-ichiro Yasuda 2025](#jun-ichiro-yasuda-2025)

## Evidence

### Jun-ichiro Yasuda 2025

Jun-ichiro Yasuda, Michael M. Hull, Naohiro Mae, Kentaro Kojima. (2025). Chained computerized adaptive testing for the Force Concept Inventory. arXiv. Originally published 2024. [doi:10.1103/x2rq-z8lm](https://doi.org/10.1103/x2rq-z8lm)

`q2 · i?` · `design · r2`

Monte Carlo simulation (10,000 generated response datasets per session) using calibrated 2PL FCI item parameters, comparing Chain-CAT with and without collateral information at L = 10 across progression models. The article reports the collateral-information case is "smaller than or comparable to" basic CAT for all models, with all-model average RMSE 0.249 versus 0.311.

> "In Table I, we can observe that the session-averaged RMSE in the case with collateral information is smaller than or comparable to that in the case without collateral information for all progression models."

## Discussion


## Related Claims
- [Without content balancing or exposure control, nine 5-item Chain-CAT administrations match pre-post accuracy with fewer total items](chain-cat-five-item-comparable-prepost-unconstrained.md) — related
- [With content balancing and item exposure control imposed, 5-item Chain-CAT is less efficient than the pre-post method](chain-cat-five-item-worse-with-constraints.md) — related
- [Joint IRT models including collateral information (raw score, gender, ethnicity) fit better than item-only base models for both tests](collateral-information-improves-joint-model-fit.md) — related
- [Adding collateral information has little effect on ability and item parameter estimates but more effect on speed parameter estimates](ci-effects-small-on-ability-item-larger-on-speed.md) — related
- [Scores from a different subject test can serve as collateral information: mathematics scores can improve reading item parameter estimation and vice versa](cross-test-scores-as-collateral-information.md) — related
