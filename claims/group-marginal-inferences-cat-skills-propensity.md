---
type: claim
title: Group-level marginal inferences identify population propensity and autonomy but are nearly vacuous for higher algorithmic skill levels
description: Group-level marginal inferences identify population propensity and autonomy but are nearly vacuous for higher algorithmic skill levels
id: group-marginal-inferences-cat-skills-propensity
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

# Group-level marginal inferences identify population propensity and autonomy but are nearly vacuous for higher algorithmic skill levels

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Marginal queries on the CAT data show sharp, identifiable values for help-seeking propensity (few students inclined to ask for feedback, a relevant part avoiding support) and high likelihood of the lowest autonomy level, while skill marginals for levels 1D and 2D are almost vacuous. [→ Francesca Mangili 2026](#francesca-mangili-2026)

## Evidence

### Francesca Mangili 2026

Francesca Mangili, Alessandro Antonucci, Rafael Cabañas de Paz. (2026). Causal Modelling of Support Interventions for Student Competency Assessment. arXiv. https://arxiv.org/abs/2608.24632

`q2 · i?` · `design · r2`

Group-level marginal inference over the causal EM-derived FSCMs compatible with the CAT assessment data from 109 students. Propensity marginals were identifiable; skill marginals for 1D and 2D were "almost vacuous", while the lowest autonomy level was highly likely, consistent with the young age of the students.

> "for the propensity, we have sharp values (i.e., the query is identifiable):P(R= feedback) = 0.02andP(R= none) = 0.37show that while only few students are inclined to ask for feedback, a relevant part of them prefers to avoid external support."

## Discussion


## Related Claims
- [BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima](bkt-bf-cost-identifiability-em-local-minima.md) — related
- [Counterfactual probabilities of necessity and sufficiency quantify the causal effect of hints and skills on task performance](pn-ps-counterfactuals-help-and-skill-effects.md) — related
- [Individualised counterfactual inferences estimate whether a specific student would have performed differently under different help conditions](individual-counterfactuals-student-help-conditions.md) — related
- [Marginal luck probabilities diagnose question calibration, flagging questions 7–9 as prone to over-performance and question 12 as particularly challenging](luck-marginals-question-calibration-diagnostic.md) — related
