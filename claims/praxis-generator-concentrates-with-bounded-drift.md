---
type: claim
title: Across three domains the PRAXIS generator concentrates the training distribution while one-step KL drift stays bounded (RQ1)
description: Across three domains the PRAXIS generator concentrates the training distribution while one-step KL drift stays bounded (RQ1)
id: praxis-generator-concentrates-with-bounded-drift
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: venkat-margapuri-and-mustafa-teber-2026
    resource: "https://doi.org/10.48550/arXiv.2610.11803"
    title: "Venkat Margapuri and Mustafa Teber. (2026). PRAXIS: Learning Dynamics of Self-Improving Models with Symbolic Archives. [doi:10.48550/arXiv.2610.11803](https://doi.org/10.48550/arXiv.2610.11803)"
    author: Venkat Margapuri and Mustafa Teber
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# Across three domains the PRAXIS generator concentrates the training distribution while one-step KL drift stays bounded (RQ1)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In MIT Indoor, GraphLog, and CLRS experiments, generator entropy decreases and maximum universe probability increases while the maximum observed KL drift proxy remains small in all domains. [→ Venkat Margapuri and Mustafa Teber 2026](#venkat-margapuri-and-mustafa-teber-2026)

## Evidence

### Venkat Margapuri and Mustafa Teber 2026

Venkat Margapuri and Mustafa Teber. (2026). PRAXIS: Learning Dynamics of Self-Improving Models with Symbolic Archives. [doi:10.48550/arXiv.2610.11803](https://doi.org/10.48550/arXiv.2610.11803)

`q2 · i?` · `theoretical · r3`

Empirical diagnostics over 50 PRAXIS iterations in three domains (Fig. 1 and accompanying table). Concentration strength is domain specific: MIT Indoor entropy falls from 4.68 to 3.91, GraphLog from 3.14 to 0.38, CLRS from 2.77 to 2.31, with max universe probability rising to 0.073, 0.925, and 0.198 respectively.

> "Despite these differences, the maximum observed drift proxy remains small in all cases: 0.0128 for MIT Indoor, 0.0173 for GraphLog, and 0.0016 for CLRS. This supports the prediction of Theorem 5.4: the Generator can concentrate the training distribution while keeping one-step movement controlled."

## Discussion


## Related Claims
- Symbolic archive weights concentrate and non-elite programs are suppressed across domains (RQ3) — possibly the same claim (merge candidate)
- [Learner training cross-entropy decreases rather than destabilizing under the moving training distribution in all three domains (RQ2)](learner-loss-decreases-under-nonstationarity.md) — related
- Component ablations show the empirical value of adaptive selection and archive regularization is domain dependent — related
