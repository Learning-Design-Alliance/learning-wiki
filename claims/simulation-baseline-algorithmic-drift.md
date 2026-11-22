---
type: claim
title: "In the agent-based simulation at baseline noise ϵ = 0.05, the protected group shows trajectory decoupling: lower final latent ability, a positive gap widening, and excess estimation pessimism relative to the reference group, with the gap growing substantially at higher noise"
description: "In the agent-based simulation at baseline noise ϵ = 0.05, the protected group shows trajectory decoupling: lower final latent ability, a positive gap widening, and excess estimation pessimism relative to the reference..."
id: simulation-baseline-algorithmic-drift
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: firuz-kamalov-2026
    resource: "https://doi.org/10.48550/arXiv.2610.31041"
    title: "Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani. (2026). Algorithmic drift in generative adaptive learning. arXiv. [doi:10.48550/arXiv.2610.31041](https://doi.org/10.48550/arXiv.2610.31041)"
    author: Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: firuz-kamalov-2026-2
    resource: "https://doi.org/10.48550/arXiv.2610.31041"
    title: "Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani. (2026). Algorithmic drift in generative adaptive learning. arXiv. [doi:10.48550/arXiv.2610.31041](https://doi.org/10.48550/arXiv.2610.31041)"
    author: Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
  - id: firuz-kamalov-2026-3
    resource: "https://doi.org/10.48550/arXiv.2610.31041"
    title: "Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani. (2026). Algorithmic drift in generative adaptive learning. arXiv. [doi:10.48550/arXiv.2610.31041](https://doi.org/10.48550/arXiv.2610.31041)"
    author: Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# In the agent-based simulation at baseline noise ϵ = 0.05, the protected group shows trajectory decoupling: lower final latent ability, a positive gap widening, and excess estimation pessimism relative to the reference group, with the gap growing substantially at higher noise

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · theoretical `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` At ϵ = 0.05 the protected group concluded with mean latent ability 0.884 and gap widening ∆ = 0.038, achieving roughly 9% less growth (gain ratio 0.911). [→ Firuz Kamalov 2026 (3)](#firuz-kamalov-2026-3)
`q2 i?` The epistemic distortion is larger than the capability gap: drift divergence was 0.268 for the protected group against 0.236 for the reference group, with estimation-bias gap Gb = −0.047. [→ Firuz Kamalov 2026 (3)](#firuz-kamalov-2026-3)
`q2 i?` The gap widens substantially as noise increases past the trapping threshold, reaching ∆ = 0.147 at ϵ = 0.15. [→ Firuz Kamalov 2026 (3)](#firuz-kamalov-2026-3)

## Evidence

### Firuz Kamalov 2026

Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani. (2026). Algorithmic drift in generative adaptive learning. arXiv. [doi:10.48550/arXiv.2610.31041](https://doi.org/10.48550/arXiv.2610.31041)

`q2 · i?` · `causal · r2`

Agent-based Monte Carlo simulation of 10,000 synthetic learner agents over T = 100 steps, R = 50 independent replications, online tracker estimator, ϵ = 0.05. Groups are ability-equivalent at baseline, so divergence is attributable to the observation channel.

> "the protected group concluded with a mean latent ability of µ = 0 .884 (95% CI [0 .883, 0.885]). The gap widening was ∆ = 0 .038 (95% CI [0 .037, 0.039]), meaning the protected group achieved roughly 9% less growth than their peers at this noise level (gain ratio ρ = 0.911)"

### Firuz Kamalov 2026 (2)

Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani. (2026). Algorithmic drift in generative adaptive learning. arXiv. [doi:10.48550/arXiv.2610.31041](https://doi.org/10.48550/arXiv.2610.31041)

`q2 · i?` · `theoretical · r3`

Same simulation, epistemic measures: mean estimated mastery for the protected group was 0.593 against a true mean of 0.884. Part of the underestimation is generic estimator lag affecting both groups; the protected-specific excess constitutes the drift.

> "the drift divergence is D = 0.268 for the protected group against D = 0.236 for the reference group, and the estimation-bias gap is Gb = −0.047 (reference group with a noiseless channel: Gb = +0.000). The protected-specific excess, visualized as the widening of the shaded region in Fig 3 (Scenario A) relative to the reference group, constitutes the algorithmic drift."

### Firuz Kamalov 2026 (3)

Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani. (2026). Algorithmic drift in generative adaptive learning. arXiv. [doi:10.48550/arXiv.2610.31041](https://doi.org/10.48550/arXiv.2610.31041)

`q2 · i?` · `theoretical · r3`

Sensitivity result reported in the baseline scenario subsection: the gap widening grows with the noise parameter once it passes the trapping threshold, per Table 6 of the sensitivity analysis.

> "as Table 6 shows, the gap widens substantially asϵincreases past the trapping threshold (to ∆ = 0.147 atϵ= 0.15)."

## Discussion


## Related Claims
- [In a reduced mean-field model, an adaptive policy targeting a fixed success rate exhibits a bifurcation under asymmetric false-negative noise: below a critical threshold the protected group is served easier content but still learns, above it ability decays geometrically](algorithmic-drift-bifurcation-trapping-threshold.md) — related
