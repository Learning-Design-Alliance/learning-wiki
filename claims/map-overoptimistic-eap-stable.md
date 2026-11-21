---
type: claim
title: "MAP rises near-instantly toward 100% under consistent wins while EAP increases only with numerous comparisons, making EAP more stable under conflicting information"
description: "MAP rises near-instantly toward 100% under consistent wins while EAP increases only with numerous comparisons, making EAP more stable under conflicting information"
id: map-overoptimistic-eap-stable
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: andy-gray-2025
    resource: "https://doi.org/10.2139/ssrn.5674497"
    title: "Andy Gray, Alma Rahat, Tom Crick, Stephen Lindsay. (2025). Bayesian Active Learning for Comparative Judgement: Reliability Estimation and Multi-Criteria Evaluation with Applications in Educational Assessment. [doi:10.2139/ssrn.5674497](https://doi.org/10.2139/ssrn.5674497)"
    author: Andy Gray, Alma Rahat, Tom Crick, Stephen Lindsay
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# MAP rises near-instantly toward 100% under consistent wins while EAP increases only with numerous comparisons, making EAP more stable under conflicting information

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In simulated agreement scenarios, MAP shifts toward 100% almost immediately even with few wins, whereas EAP reaches high values only after numerous comparisons, and EAP fluctuates less when wins and losses conflict. [→ Andy Gray 2025](#andy-gray-2025)

## Evidence

### Andy Gray 2025

Andy Gray, Alma Rahat, Tom Crick, Stephen Lindsay. (2025). Bayesian Active Learning for Comparative Judgement: Reliability Estimation and Multi-Criteria Evaluation with Applications in Educational Assessment. [doi:10.2139/ssrn.5674497](https://doi.org/10.2139/ssrn.5674497)

`q1 · i?` · `design · r2`

Illustrative simulation over numbers of comparisons (Figures 3 and 4): with an item winning every comparison, "the MAP will show a rather instantaneous shift towards 100%", while with an item winning only every second comparison, EAP is more stable and MAP fluctuates rapidly, with overshoots shrinking as data accumulates.

> "Hence, the MAP will show a rather instantaneous shift towards 100%, but EAP would only do so when there are numerous comparisons and all indicate wins for the item:see Figure 3."

## Discussion


## Related Claims
- [MAP and EAP quantify assessor agreement at the pairwise level from BCJ Beta posteriors, identifying contentious comparisons that a single aggregate reliability score cannot](map-eap-pairwise-reliability-metrics.md) — a broader claim this one bears on
