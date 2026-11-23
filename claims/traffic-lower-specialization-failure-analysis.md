---
type: claim
title: Traffic shows the lowest regime specialization (SI = 0.573), which the authors attribute to six regimes, temporal regime correlation, and regime overlap — a boundary condition, not a failure
description: Traffic shows the lowest regime specialization (SI = 0.573), which the authors attribute to six regimes, temporal regime correlation, and regime overlap — a boundary condition, not a failure
id: traffic-lower-specialization-failure-analysis
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yuhao-li-2026
    resource: "https://doi.org/10.48550/arXiv.2601.19943"
    title: "Yuhao Li. (2026). Emergent Specialization in Learner Populations: Competition as the Source of Diversity. arXiv preprint. [doi:10.48550/arXiv.2601.19943](https://doi.org/10.48550/arXiv.2601.19943)"
    author: Yuhao Li
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Traffic shows the lowest regime specialization (SI = 0.573), which the authors attribute to six regimes, temporal regime correlation, and regime overlap — a boundary condition, not a failure

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the six-regime Traffic domain, NichePopulation reaches SI = 0.573, lower than other domains, yet still achieves +23.8% performance improvement with 100% method coverage. [→ Yuhao Li 2026](#yuhao-li-2026)

## Evidence

### Yuhao Li 2026

Yuhao Li. (2026). Emergent Specialization in Learner Populations: Competition as the Source of Diversity. arXiv preprint. [doi:10.48550/arXiv.2601.19943](https://doi.org/10.48550/arXiv.2601.19943)

`q2 · i?` · `design · r2`

Failure analysis in Section 5.6 for the NYC TLC traffic domain, which has 6 regimes with temporal correlation and an overlapping transition regime. The article prints SI = 0.573 and attributes lower specialization to regime dilution and correlated regimes; no standardized effect size is printed for this domain contrast.

> "Despite lower SI, Traffic still achieves +23.8% performance improvement through method specialization, demonstrating thateven partial specialization provides value. The domain uses 100% of available methods"

## Discussion


## Related Claims
- [Competition alone, with no niche bonus (λ = 0), induces significant specialization in learner populations, exceeding random baselines in all six domains](competition-alone-induces-specialization-lambda-zero.md) — related
