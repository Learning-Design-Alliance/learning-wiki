---
type: claim
title: Updating microcanonical temperature estimates converges to a monotonically increasing T(E), from which the entropy and density of states are obtained by integration
description: Updating microcanonical temperature estimates converges to a monotonically increasing T(E), from which the entropy and density of states are obtained by integration
id: microcanonical-temperature-estimate-convergence
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-10
evidence_strength: weak
newest_evidence: 2007
recheck_by: 2010
sources:
  - id: jan-tobochnik-and-harvey-gould-2007
    resource: "https://doi.org/10.48550/arXiv.0712.3488"
    title: "Jan Tobochnik and Harvey Gould. (2007). Teaching statistical physics by thinking about models and algorithms. arXiv:0712.3488. https://arxiv.org/abs/0712.3488"
    author: Jan Tobochnik and Harvey Gould
    q: 2
    i: "?"
    kind: design
    rigour: 1
---

# Updating microcanonical temperature estimates converges to a monotonically increasing T(E), from which the entropy and density of states are obtained by integration

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q2`
> **Currency** · newest study 2007 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2010**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the statistical temperature method, updating the temperature estimates at neighboring energies after each trial move drives the estimate T(E) to converge to a monotonically increasing function of the energy. [→ Jan Tobochnik and Harvey Gould 2007](#jan-tobochnik-and-harvey-gould-2007)

## Evidence

### Jan Tobochnik and Harvey Gould 2007

Jan Tobochnik and Harvey Gould. (2007). Teaching statistical physics by thinking about models and algorithms. arXiv:0712.3488. https://arxiv.org/abs/0712.3488 [doi:10.48550/arXiv.0712.3488](https://doi.org/10.48550/arXiv.0712.3488)

`q2 · i?` · `design · r1`

Analytical/algorithmic result in Section VII for the Ising model with discrete energies: after a trial move the entropy estimate is updated and the central-difference approximation yields updated inverse temperatures at j ± 1, with Tj−1 decreased and Tj+1 increased while Tj is unchanged. The article recommends restricting updates to a finite temperature range.

> "In this way ˜T (E) will converge to a monotonically increasing function of the energy. It is best to restrict the updates to a ﬁnite range o f temperatures between Tmin and Tmax."

## Discussion


## Related Claims
- [Gas energy converges on average to the expected value set by the heating/cooling wall temperature, with visible thermal fluctuations](gas-energy-converges-to-expected-with-fluctuations.md) — related
- [Theoretical results establish content fidelity, rendering stability, entropy boundedness, and integrity convergence for the BAVD model](bavd-theoretical-properties-fidelity-stability-convergence.md) — related
- [The additive entropy decomposition is an upper bound, not a security measure; adversary uncertainty is a conditional entropy](bavd-entropy-decomposition-upper-bound-not-security-measure.md) — related
