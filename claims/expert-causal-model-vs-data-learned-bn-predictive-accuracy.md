---
type: claim
title: Expert-elicited causal model is compatible with observed data but slightly less predictive than a data-learned Bayesian network
description: Expert-elicited causal model is compatible with observed data but slightly less predictive than a data-learned Bayesian network
id: expert-causal-model-vs-data-learned-bn-predictive-accuracy
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: francesca-mangili-2026
    resource: "https://arxiv.org/abs/2608.24632"
    title: "Francesca Mangili, Alessandro Antonucci, Rafael Cabañas de Paz. (2026). Causal Modelling of Support Interventions for Student Competency Assessment. arXiv. https://arxiv.org/abs/2608.24632"
    author: Francesca Mangili, Alessandro Antonucci, Rafael Cabañas de Paz
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Expert-elicited causal model is compatible with observed data but slightly less predictive than a data-learned Bayesian network

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In five-fold cross-validation on the CAT assessment data, the expert-elicited FSCM achieved lower held-out log-likelihood and answer prediction accuracy than a BN learned from data, while hint accuracy was comparable. [→ Francesca Mangili 2026](#francesca-mangili-2026)

## Evidence

### Francesca Mangili 2026

Francesca Mangili, Alessandro Antonucci, Rafael Cabañas de Paz. (2026). Causal Modelling of Support Interventions for Student Competency Assessment. arXiv. https://arxiv.org/abs/2608.24632

`q2 · i?` · `design · r2`

Five-fold cross-validation comparison on the CAT assessment data (109 students) between the expert-elicited FSCM and a BN learned directly from data, evaluating held-out log-likelihood and posterior prediction accuracy for answers and hints. The FSCM showed "a reduction in predictive accuracy compared to a purely data-driven approach".

> "The results show a test log-likelihood of -277±19.1 (standard deviation) for the BN and -287±18.5 for the FSCM, and a prediction accuracy of 0.84±0.02 (answers) and 0.84±0.04 (hints) for the BN, compared to 0.77±0.02 (answers) and 0.82±0.04 (hints) for the FSCM."

## Discussion


## Related Claims
- [The framework's validation is limited: structure and parameterisation were tested only on a small dataset and only for predictive accuracy](causal-assessment-framework-validation-limitations.md) — possibly the same claim (merge candidate)
