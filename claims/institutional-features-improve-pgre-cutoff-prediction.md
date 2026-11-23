---
type: claim
title: Adding institutional features to a conditional inference forest improves accuracy and AUC for predicting P-GRE cut-off attainment at every cut-off
description: Adding institutional features to a conditional inference forest improves accuracy and AUC for predicting P-GRE cut-off attainment at every cut-off
id: institutional-features-improve-pgre-cutoff-prediction
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

# Adding institutional features to a conditional inference forest improves accuracy and AUC for predicting P-GRE cut-off attainment at every cut-off

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Replacing a CIF without institutional features with one including the Carnegie classification and number of PhD graduates improves both accuracy and AUC regardless of cut-off. [→ Nils J. Mikkelsen 2021](#nils-j-mikkelsen-2021)

## Evidence

### Nils J. Mikkelsen 2021

Nils J. Mikkelsen, Nicholas T. Young, and Marcos D. Caballero. (2021). Investigating institutional influence on graduate program admissions by modelling physics GRE cut-off scores. [doi:10.1103/physrevphyseducres.17.010109](https://doi.org/10.1103/physrevphyseducres.17.010109)

`q2 · i?` · `associational · r2`

K-fold (K = 10) cross-validated comparison of conditional inference forests with all features, with two institutional features, and without institutional features, shown in Figure 7. The article reports "a considerable improvement for both metrics" from adding the two institutional features; no effect size is printed.

> "The results of the comparison is summarized in Figure 7: The addition of only two institutional features makes a considerable improvement for both metrics, regardless of the cut-oﬀ."

## Discussion


## Related Claims
- [The conditional inference forest achieves mostly outstanding AUC (>0.9) stable across cut-offs, and three features suffice for AUC near 0.9](cif-auc-stable-three-features.md) — related
- [The set of significant and important features changes with the P-GRE cut-off, though institutional features contribute at every cut-off](feature-significance-varies-with-cutoff.md) — related
- [Attending a most competitive institution, one with highest research activity, or one with a large physics bachelor program is statistically significant for a majority of P-GRE cut-offs](institutional-features-significant-majority-cutoffs.md) — related
