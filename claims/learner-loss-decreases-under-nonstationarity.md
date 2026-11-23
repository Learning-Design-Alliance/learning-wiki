---
type: claim
title: Learner training cross-entropy decreases rather than destabilizing under the moving training distribution in all three domains (RQ2)
description: Learner training cross-entropy decreases rather than destabilizing under the moving training distribution in all three domains (RQ2)
id: learner-loss-decreases-under-nonstationarity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: venkat-margapuri-and-mustafa-teber-2026
    resource: "https://doi.org/10.48550/arXiv.2610.11803"
    title: "Venkat Margapuri and Mustafa Teber. (2026). PRAXIS: Learning Dynamics of Self-Improving Models with Symbolic Archives. [doi:10.48550/arXiv.2610.11803](https://doi.org/10.48550/arXiv.2610.11803)"
    author: Venkat Margapuri and Mustafa Teber
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Learner training cross-entropy decreases rather than destabilizing under the moving training distribution in all three domains (RQ2)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Rolling training cross-entropy decreases in MIT Indoor (1.007 to 0.080), GraphLog (0.702 to 0.109), and CLRS (0.617 to 0.421, minimum 0.361) under adaptive sampling. [→ Venkat Margapuri and Mustafa Teber 2026](#venkat-margapuri-and-mustafa-teber-2026)

## Evidence

### Venkat Margapuri and Mustafa Teber 2026

Venkat Margapuri and Mustafa Teber. (2026). PRAXIS: Learning Dynamics of Self-Improving Models with Symbolic Archives. [doi:10.48550/arXiv.2610.11803](https://doi.org/10.48550/arXiv.2610.11803)

`q2 · i?` · `design · r2`

Learner-side diagnostics reported in Fig. 2 across the three-domain evaluation. The article cautions these observations are "consistent with stable optimization under a moving objective, but training loss is not a direct measurement of the gradient-norm quantity bounded in Theorem 5.14".

> "In all three domains, the rolling training cross-entropy decreases rather than destabilizing under adaptive sampling. MIT Indoor decreases from 1.007 to 0.080, GraphLog from 0.702 to 0.109, and CLRS from 0.617 to 0.421 with a minimum of 0.361."

## Discussion


## Related Claims
- [Across three domains the PRAXIS generator concentrates the training distribution while one-step KL drift stays bounded (RQ1)](praxis-generator-concentrates-with-bounded-drift.md) — related
- Symbolic archive weights concentrate and non-elite programs are suppressed across domains (RQ3) — related
- Component ablations show the empirical value of adaptive selection and archive regularization is domain dependent — related
