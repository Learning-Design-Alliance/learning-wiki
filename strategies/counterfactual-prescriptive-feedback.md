---
type: strategy
id: counterfactual-prescriptive-feedback
title: Generate prescriptive feedback via counterfactual modelling constrained to actionable features
description: "For students predicted high-risk, the dashboard models a minimal set of changes to the student's input values that would flip the prediction to low risk, using counterfactual modelling."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: gomathy-ramaswami-2023
    resource: "https://doi.org/10.18608/jla.2023.7935"
    title: "Gomathy Ramaswami, Teo Susnjak and Anuradha Mathrani. (2023). Effectiveness of a Learning Analytics Dashboard for Increasing Student Engagement Levels. Journal of Learning Analytics, 10(3). https://doi.org/10.18608/jla.2023.7935"
    author: Gomathy Ramaswami, Teo Susnjak and Anuradha Mathrani
---

# Generate prescriptive feedback via counterfactual modelling constrained to actionable features

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
For students predicted high-risk, the dashboard models a minimal set of changes to the student's input values that would flip the prediction to low risk, using counterfactual modelling. Changes are constrained "to only the features that are actionable, thus ignoring immutable features like citizenship." Outputs are converted into human-understandable textual feedback offering data-driven personalized suggestions for modifying learning behaviours.

## Design Implications

### Context
#### Requirements
- A trained predictive model and student feature data must be available; counterfactuals must be restricted to actionable (modifiable) features
#### Constraints
- Counterfactual outputs depend on the predictive model's accuracy and may be undermined by erroneous predictions, which the article notes can erode trust

### Target Learners
- tertiary students identified as at risk of course non-completion

### Target Learning Goals
- adjusting learning behaviour
- improving course outcomes
- self-regulated learning

### Affordances
- [Lad Theoretical Grounding Sct Srl Tl](../theories/lad-theoretical-grounding-sct-srl-tl.md)

## Related Strategies
- [Sensenablr Dashboard](../elements/sensenablr-dashboard.md)

## Examples
-

## Key Sources
- Gomathy Ramaswami, Teo Susnjak and Anuradha Mathrani. (2023). Effectiveness of a Learning Analytics Dashboard for Increasing Student Engagement Levels. Journal of Learning Analytics, 10(3). https://doi.org/10.18608/jla.2023.7935
