---
type: claim
title: A single decision-and-confidence model with no condition-specific parameters fits decision weights across all three methods
description: A single decision-and-confidence model with no condition-specific parameters fits decision weights across all three methods
id: unitary-model-fits-all-three-methods
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-18
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: lorenz-weise-2022
    resource: "https://doi.org/10.1007/s11409-021-09286-4"
    title: "Lorenz Weise, Saskia D. Forster, Siegfried Gauggel. (2022). Reverse-correlation reveals internal error-corrections during information-seeking. Metacognition and Learning (2022) 17:321–335. https://doi.org/10.1007/s11409-021-09286-4"
    author: Lorenz Weise, Saskia D. Forster, Siegfried Gauggel
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: lorenz-weise-2022-2
    resource: "https://doi.org/10.1007/s11409-021-09286-4"
    title: "Lorenz Weise, Saskia D. Forster, Siegfried Gauggel. (2022). Reverse-correlation reveals internal error-corrections during information-seeking. Metacognition and Learning (2022) 17:321–335. https://doi.org/10.1007/s11409-021-09286-4"
    author: Lorenz Weise, Saskia D. Forster, Siegfried Gauggel
    q: 2
    i: 3
    kind: causal
    rigour: 2
---

# A single decision-and-confidence model with no condition-specific parameters fits decision weights across all three methods

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2` · `i3` large
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The full model accommodated the general pattern of decision weights without any parameter varying between the confidence-assessment methods. [→ Lorenz Weise 2022](#lorenz-weise-2022)
`q2 i3` The model's predicted proportion of high-confidence trials correlated significantly with the observed proportion (r = 0.63). [→ Lorenz Weise 2022 (2)](#lorenz-weise-2022-2)

## Evidence

### Lorenz Weise 2022

Lorenz Weise, Saskia D. Forster, Siegfried Gauggel. (2022). Reverse-correlation reveals internal error-corrections during information-seeking. Metacognition and Learning (2022) 17:321–335. https://doi.org/10.1007/s11409-021-09286-4

`q2 · i?` · `causal · r2`

Simulation-based model fitting: 100,000 simulated trials per run, grid search plus Nelder-Mead fitting of cutoff and scale to each participant's weights. The article reports the full model accommodated the general pattern with no condition-specific parameters.

> "the full model can accommodate the general pattern in the decision weights, without allowing any parameter to vary between the different methods of metacognitive judgment."

### Lorenz Weise 2022 (2)

Lorenz Weise, Saskia D. Forster, Siegfried Gauggel. (2022). Reverse-correlation reveals internal error-corrections during information-seeking. Metacognition and Learning (2022) 17:321–335. https://doi.org/10.1007/s11409-021-09286-4

`q2 · i3` · `causal · r2`

Out-of-sample validation: predicted high-confidence trial proportions, not fitted by the model, were correlated with each participant's observed proportion averaged across conditions, with printed effect size r = 0.63 (reported as r(25) = 0.63, p < 0.001), a large correlation.

> "The model's prediction was correlated significantly with the empirically observed value (r(25) = 0.63, p < 0.001), further corroborating the model."

## Discussion


## Related Claims
- [Reverse-correlation decision weights are positive for the chosen stimulus dimension and weaker on low-confidence trials across confidence-assessment methods](decision-weights-positive-chosen-weaker-low-confidence.md) — related
- [Internal error-corrections, not correct-to-incorrect changes-of-mind, produce the inverted low-confidence decision weights](error-corrections-produce-inverted-weights.md) — related
- [Low-confidence info-seeking trials show inverted decision weights, unlike explicit reports and post-decision wagering](inverted-decision-weights-low-confidence-info-seeking.md) — related
- [The inverted low-confidence info-seeking pattern persists when only each participant's first condition is analyzed](mixed-anova-confirms-inverted-weights.md) — reports the opposite
- [Primary task accuracy is higher in the info-seeking condition than in the explicit reports and wagering conditions](info-seeking-condition-higher-accuracy.md) — related
