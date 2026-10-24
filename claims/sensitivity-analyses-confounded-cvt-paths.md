---
type: claim
title: Sensitivity analyses showed most sequential CVT paths were spurious due to confounders; only interest→enjoyment was robust
description: Sensitivity analyses showed most sequential CVT paths were spurious due to confounders; only interest→enjoyment was robust
id: sensitivity-analyses-confounded-cvt-paths
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-23
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: chevalère-2023
    resource: "https://doi.org/10.1016/j.learninstruc.2023.101799"
    title: "Chevalère, J., Yun, H. S., Henke, A., Pinkwart, N., Hafner, V., & Lazarides, R. (2023). A sequence of learning processes in an intelligent tutoring system from topic-related appraisals to learning gains. Learning and Instruction, 87, 101799. https://doi.org/10.1016/j.learninstruc.2023.101799"
    author: "Chevalère, J., Yun, H. S., Henke, A., Pinkwart, N., Hafner, V., & Lazarides, R."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: chevalère-2023-2
    resource: "https://doi.org/10.1016/j.learninstruc.2023.101799"
    title: "Chevalère, J., Yun, H. S., Henke, A., Pinkwart, N., Hafner, V., & Lazarides, R. (2023). A sequence of learning processes in an intelligent tutoring system from topic-related appraisals to learning gains. Learning and Instruction, 87, 101799. https://doi.org/10.1016/j.learninstruc.2023.101799"
    author: "Chevalère, J., Yun, H. S., Henke, A., Pinkwart, N., Hafner, V., & Lazarides, R."
    q: 2
    i: 0
    kind: associational
    rigour: 2
---

# Sensitivity analyses showed most sequential CVT paths were spurious due to confounders; only interest→enjoyment was robust

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2` · `i0` negligible
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Nearly all paths identified in the reverse causality models were no longer significant when coevals and covariates were controlled for (ps ≥ .11), whereas the interest→enjoyment link was highly robust to unobserved confounders (ρ(U) = .31). [→ Chevalère 2023](#chevalere-2023)
`q3 i0` The only Forward path unbiased by observed confounders, performance T6 → final performance → learning gains (β = .08), was sensitive to unobserved confounding, abolished at ρ(U) = .18. [→ Chevalère 2023 (2)](#chevalere-2023-2)

## Evidence

### Chevalère 2023

Chevalère, J., Yun, H. S., Henke, A., Pinkwart, N., Hafner, V., & Lazarides, R. (2023). A sequence of learning processes in an intelligent tutoring system from topic-related appraisals to learning gains. Learning and Instruction, 87, 101799. https://doi.org/10.1016/j.learninstruc.2023.101799

`q2 · i?` · `associational · r2`

Mediation-based sensitivity analyses (Imai et al. framework, 5,000 bootstrapped samples) broke each sequence into simple mediation models conditioning on observed coevals; the article states "nearly all paths identified in the reverse causality models (in bold) contained spurious associations".

> "the analyses revealed that these paths were no longer significant when coevals and other covariates were controlled for, ps ≥ .11"

### Chevalère 2023 (2)

Chevalère, J., Yun, H. S., Henke, A., Pinkwart, N., Hafner, V., & Lazarides, R. (2023). A sequence of learning processes in an intelligent tutoring system from topic-related appraisals to learning gains. Learning and Instruction, 87, 101799. https://doi.org/10.1016/j.learninstruc.2023.101799

`q2 · i0` · `associational · r2`

For the sole unbiased Forward path, the mediation model "proved sensitive to the presence of an unobserved confounder U", with the indirect effect abolished at ρ(U) = .18, below the article's robust threshold of .20.

> "the unique variance of performance 6 predicted learning gains through the final performance score, β = . 08, SE = .04, t = 2.03, p = .030 [.001; .18]"

## Discussion


## Related Claims
- [The ESDM's unidirectional trait-ACH-to-trait-ASC path is not empirically identified, and the confounder-based RI-LTVC alternative shows poor fit with no support for a time-varying confounder](esdm-directional-path-not-identified-ri-ltvc-no-support.md) — related
- [Reanalyses of simulated and PALMA data provide converging support for the extended reciprocal effects model, including an effect of academic self-concept on achievement](reanalyses-converging-support-extended-rem-asc-effect.md) — related
