---
type: claim
title: "In a reduced mean-field model, an adaptive policy targeting a fixed success rate exhibits a bifurcation under asymmetric false-negative noise: below a critical threshold the protected group is served easier content but still learns, above it ability decays geometrically"
description: "In a reduced mean-field model, an adaptive policy targeting a fixed success rate exhibits a bifurcation under asymmetric false-negative noise: below a critical threshold the protected group is served easier content bu..."
id: algorithmic-drift-bifurcation-trapping-threshold
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: firuz-kamalov-2026
    resource: "https://doi.org/10.48550/arXiv.2610.31041"
    title: "Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani. (2026). Algorithmic drift in generative adaptive learning. arXiv. [doi:10.48550/arXiv.2610.31041](https://doi.org/10.48550/arXiv.2610.31041)"
    author: Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# In a reduced mean-field model, an adaptive policy targeting a fixed success rate exhibits a bifurcation under asymmetric false-negative noise: below a critical threshold the protected group is served easier content but still learns, above it ability decays geometrically

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Below the critical noise level the protected group is served strictly easier content with a deficit strictly increasing in noise, yet both groups remain inside the ZPD and continue to learn. [→ Firuz Kamalov 2026](#firuz-kamalov-2026)
`q2 i?` At or above the critical noise level the protected group's served difficulty leaves the ZPD and ability decays geometrically, so the protected trajectory diverges monotonically from the reference trajectory. [→ Firuz Kamalov 2026](#firuz-kamalov-2026)

## Evidence

### Firuz Kamalov 2026

Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani. (2026). Algorithmic drift in generative adaptive learning. arXiv. [doi:10.48550/arXiv.2610.31041](https://doi.org/10.48550/arXiv.2610.31041)

`q2 · i?` · `theoretical · r3`

Analytical derivation (Proposition 1) under stated Assumption 1: a Rasch link, a false-negative observation channel, a quasi-static policy targeting a fixed observed success rate, and a hard-indicator ZPD learning rule. The proof establishes the closed-form critical noise level ϵ⋆ = 1− p⋆/σ(ω) and the 'progress-but-under-challenged' versus 'trapped-and-declining' regimes.

> "For ϵ≥ϵ ⋆ the protected group’s served difficulty leaves the ZPD, the learning indicator collapses to I(·) = 0, and ability decays geometrically as θt+1 = (1 −λ )θt, so the protected trajectory diverges monotonically from the reference trajectory."

## Discussion


## Related Claims
- [In the agent-based simulation at baseline noise ϵ = 0.05, the protected group shows trajectory decoupling: lower final latent ability, a positive gap widening, and excess estimation pessimism relative to the reference group, with the gap growing substantially at higher noise](simulation-baseline-algorithmic-drift.md) — related
- [In a matched-pair grading protocol, open-weight LLM graders show demographically asymmetric false-negative behaviour against second-language variants, with the most affected grader rejecting 5% of correct second-language answers it accepts in Standard English](llm-grader-asymmetric-false-negatives.md) — related
- [Screening classification errors carry asymmetric costs: false positives risk unnecessary intensive placement while false negatives delay early intervention](false-positive-false-negative-screening-tradeoff.md) — related
