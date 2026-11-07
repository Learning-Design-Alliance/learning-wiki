---
type: claim
title: A small set of latent factors (3–4) predicts individual error patterns far better than graph-type or question-type decompositions
description: A small set of latent factors (3–4) predicts individual error patterns far better than graph-type or question-type decompositions
id: latent-factors-outperform-design-categories
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: brockbank-2025
    resource: "https://doi.org/10.1186/s41235-025-00622-9"
    title: "Brockbank, E., Verma, A., Lloyd, H., Huey, H., Padilla, L., & Fan, J. E. (2025). Evaluating convergence between two data visualization literacy assessments. Cognitive Research: Principles and Implications. https://doi.org/10.1186/s41235-025-00622-9"
    author: "Brockbank, E., Verma, A., Lloyd, H., Huey, H., Padilla, L., & Fan, J. E."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# A small set of latent factors (3–4) predicts individual error patterns far better than graph-type or question-type decompositions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Neither graph type nor question type accounts for much of the explainable variation in individual error patterns; a 4-factor latent model achieves much lower prediction error. [→ Brockbank 2025](#brockbank-2025)

## Evidence

### Brockbank 2025

Brockbank, E., Verma, A., Lloyd, H., Huey, H., Padilla, L., & Fan, J. E. (2025). Evaluating convergence between two data visualization literacy assessments. Cognitive Research: Principles and Implications. https://doi.org/10.1186/s41235-025-00622-9

`q2 · i?` · `associational · r2`

Exploratory factor analysis with fivefold cross-validation on the combined 66-item assessment; the latent model (MSE = 0.93) beat the graph-type model (MSE = 5.07), question-type model (MSE = 9.62), and 2-factor test model (MSE = 11.52).

> "both the graph type and question type models perform substantially worse than the 4-factor latent factor model (MSE = 0.93, 95% CI: [0.89, 0.96]). Taken together, these results suggest that neither graph type nor question type on their own can account for much of the explainable variation in individual error patterns."

## Discussion


## Related Claims
- [Graph type reliably accounts for variation in assessment performance, within each test and combined](graph-type-accounts-for-performance-variance.md) — reports the opposite
- [Model and prompt choice account for only a small share of misalignment error, which concentrates in transcript-conditioned higher-order interactions](variance-decomposition-model-prompt-weak-levers.md) — related
- [Multidimensional IRT scores that account for latent variable covariances over time produce better recovery of growth parameters in longitudinal growth models than sum scores and other IRT approaches](multidimensional-irt-covariance-scores-better-growth-recovery.md) — related
- [Risk category explains the largest share of variation in educational attack success, far more than LLM usage context or curriculum topic](risk-category-dominates-educational-safety-variance.md) — related
- [Question type reliably accounts for variation in assessment performance within each test and combined](question-type-accounts-for-performance-variance.md) — reports the opposite
