---
type: claim
title: "The framework's validation is limited: structure and parameterisation were tested only on a small dataset and only for predictive accuracy"
description: "The framework's validation is limited: structure and parameterisation were tested only on a small dataset and only for predictive accuracy"
id: causal-assessment-framework-validation-limitations
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: francesca-mangili-2026
    resource: "https://arxiv.org/abs/2608.24632"
    title: "Francesca Mangili, Alessandro Antonucci, Rafael Cabañas de Paz. (2026). Causal Modelling of Support Interventions for Student Competency Assessment. arXiv. https://arxiv.org/abs/2608.24632"
    author: Francesca Mangili, Alessandro Antonucci, Rafael Cabañas de Paz
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The framework's validation is limited: structure and parameterisation were tested only on a small dataset and only for predictive accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` The authors state the learner model's structure and parameterisation are not really validated, having been tested only on a small dataset, against a BN learned directly from data, and only for predictive accuracy. [→ Francesca Mangili 2026](#francesca-mangili-2026)

## Evidence

### Francesca Mangili 2026

Francesca Mangili, Alessandro Antonucci, Rafael Cabañas de Paz. (2026). Causal Modelling of Support Interventions for Student Competency Assessment. arXiv. https://arxiv.org/abs/2608.24632

`q1 · i?` · `design · r2`

Authors' stated limitations in the conclusions section. Benchmarking is limited by the lack of suitable empirically validated competence models with large interventional datasets and the absence of comparable causal learner modelling frameworks. The authors do not claim evidence regarding impact on decision-making or correctness of counterfactual estimates.

> "structure and parameterisation are not re-ally validated, having been tested only on a small dataset, against a BN learned directly from data, and only for predictive accuracy."

## Discussion


## Related Claims
- [Expert-elicited causal model is compatible with observed data but slightly less predictive than a data-learned Bayesian network](expert-causal-model-vs-data-learned-bn-predictive-accuracy.md) — possibly the same claim (merge candidate)
- [Instructional design models are rarely tested against outcomes; their credibility comes from practitioners finding them useful.](instructional-design-models-are-validated-by-adoption-not-testing.md) — a broader claim this one bears on
