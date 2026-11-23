---
type: claim
title: "The conditional inference forest achieves mostly outstanding AUC (>0.9) stable across cut-offs, and three features suffice for AUC near 0.9"
description: "The conditional inference forest achieves mostly outstanding AUC (>0.9) stable across cut-offs, and three features suffice for AUC near 0.9"
id: cif-auc-stable-three-features
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: nils-j-mikkelsen-2021
    resource: "https://doi.org/10.1103/physrevphyseducres.17.010109"
    title: "Nils J. Mikkelsen, Nicholas T. Young, and Marcos D. Caballero. (2021). Investigating institutional influence on graduate program admissions by modelling physics GRE cut-off scores. [doi:10.1103/physrevphyseducres.17.010109](https://doi.org/10.1103/physrevphyseducres.17.010109)"
    author: Nils J. Mikkelsen, Nicholas T. Young, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# The conditional inference forest achieves mostly outstanding AUC (>0.9) stable across cut-offs, and three features suffice for AUC near 0.9

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The CIF's AUC score is mostly above 0.9 and very stable with respect to changes in the P-GRE cut-off. [→ Nils J. Mikkelsen 2021](#nils-j-mikkelsen-2021)
`q2 i?` Using only U-GPA, gender and number of PhD graduates, the CIF scores about 0.9 AUC and roughly 80-90% accuracy. [→ Nils J. Mikkelsen 2021](#nils-j-mikkelsen-2021)

## Evidence

### Nils J. Mikkelsen 2021

Nils J. Mikkelsen, Nicholas T. Young, and Marcos D. Caballero. (2021). Investigating institutional influence on graduate program admissions by modelling physics GRE cut-off scores. [doi:10.1103/physrevphyseducres.17.010109](https://doi.org/10.1103/physrevphyseducres.17.010109)

`q2 · i?` · `associational · r2`

K-fold (K = 10) cross-validated performance of conditional inference forests (200 trees, 3 features per tree) built on admissions records, reported in Figures 4 and 6. The article reports AUC "mostlyoutstanding (>0.9)" and stable across cut-offs; accuracy is interpreted relative to class imbalance.

> "Using only the three features with the highest importance measures (U-GPA, gender and number of PhD graduates), the CIF is able to score≈ 0.9 on the AUC metric and roughly between 80% and 90% on the accuracy metric."

## Discussion


## Related Claims
- [Adding institutional features to a conditional inference forest improves accuracy and AUC for predicting P-GRE cut-off attainment at every cut-off](institutional-features-improve-pgre-cutoff-prediction.md) — related
- [The set of significant and important features changes with the P-GRE cut-off, though institutional features contribute at every cut-off](feature-significance-varies-with-cutoff.md) — related
- [A conditional inference forest acceptably models pre-rubric physics graduate admissions decisions, with physics GRE score, quantitative GRE score, and undergraduate GPA the only meaningful features](pre-rubric-admissions-model-quantitative-metrics-meaningful.md) — related
- [A reduced model using only the five meaningful features performs nearly as well as the full 44-feature model](five-feature-model-nearly-full-performance.md) — related
- [A conditional inference random forest model predicts physics PhD admissions decisions on held-out data with 75.8% average accuracy](random-forest-predicts-physics-phd-admissions-75-8-percent.md) — related
