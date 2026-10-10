---
type: claim
title: In the model, social learning creates consensus in trust without shifting aggregate reliance; connectivity alone does not produce collective overreliance
description: In the model, social learning creates consensus in trust without shifting aggregate reliance; connectivity alone does not produce collective overreliance
id: social-learning-consensus-not-aggregate-overreliance
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: ahana-biswas-2026
    resource: "https://arxiv.org/abs/2608.19616"
    title: "Ahana Biswas. (2026). Modeling AI Overreliance as a Complex Adaptive System. arXiv. https://arxiv.org/abs/2608.19616"
    author: Ahana Biswas
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
  - id: ahana-biswas-2026-2
    resource: "https://arxiv.org/abs/2608.19616"
    title: "Ahana Biswas. (2026). Modeling AI Overreliance as a Complex Adaptive System. arXiv. https://arxiv.org/abs/2608.19616"
    author: Ahana Biswas
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
---

# In the model, social learning creates consensus in trust without shifting aggregate reliance; connectivity alone does not produce collective overreliance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · theoretical `r3` · `q1`–`q2`

## Subclaims
`q2 i?` In the 2×2 topology×tagging design with feedback off, all four cells give overreliance 0.30–0.31; with feedback on, all rise together to ≈0.51. [→ Ahana Biswas 2026](#ahana-biswas-2026)
`q2 i?` Social learning compresses trust dispersion while leaving the aggregate unchanged, consistent with the mean-preservation theorem. [→ Ahana Biswas 2026](#ahana-biswas-2026)
`q1 i?` Analytically, under a DeGroot update with doubly-stochastic influence weights the population mean of trust is invariant and cross-sectional variance is non-increasing. [→ Ahana Biswas 2026 (2)](#ahana-biswas-2026-2)

## Evidence

### Ahana Biswas 2026

Ahana Biswas. (2026). Modeling AI Overreliance as a Complex Adaptive System. arXiv. https://arxiv.org/abs/2608.19616

`q2 · i?` · `theoretical · r3`

Simulation crossing network topology (ER vs BA) with source tagging on/off, with and without the social-proof channel (Fig. 3a), the empirical counterpart of Proposition 2. The article reports "all four cells give overreliance 0.30–0.31 (within CI)" without feedback, and that social learning "sharply compresses trust dispersion (consensus)".

> "with feedback off, all four cells give overreliance 0.30–0.31 (within CI); with feedback on, all rise together to≈0.51. Social learning sharply compresses trust dispersion (consensus) while leaving the aggregate unchanged."

### Ahana Biswas 2026 (2)

Ahana Biswas. (2026). Modeling AI Overreliance as a Complex Adaptive System. arXiv. https://arxiv.org/abs/2608.19616

`q1 · i?` · `theoretical · r3`

Analytical result (Proposition 2, proof in supplement): under the DeGroot trust update with doubly-stochastic weights, "the population mean¯τis invariant" and variance is non-increasing; the Dirichlet variant used in the main model is verified computationally.

> "Under the DeGroot stepτ ′ = (1−λ)τ+λWτ with doubly-stochasticW, the population mean¯τis invariant and the cross-sectional variance is non-increasing."

## Discussion


## Related Claims
- [In the model, topology shifts aggregate reliance only under opinion dynamics, when influential hubs transmit correlated beliefs that move agents across the verify/use margin](opinion-dynamics-hubs-shift-consensus-trust.md) — possibly the same claim (merge candidate)
- [In the model, interventions that alter the feedback channel (verification visibility, social-proof damping) reduce overreliance and regret, while lowering verification cost alone does not lower regret](verification-visibility-counter-cascade-interventions.md) — related
- [In the model, visible unverified peer use (social proof) suppresses verification and tips the population into collective overreliance, via a smooth crossover with no hysteresis](social-proof-verification-collapse-cascade.md) — related
