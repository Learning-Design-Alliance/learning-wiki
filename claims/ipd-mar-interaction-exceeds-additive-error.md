---
type: claim
title: The joint effect of IPD and MAR missing data on equating error exceeds the sum of individual effects, indicating an interaction rather than an additive relationship
description: The joint effect of IPD and MAR missing data on equating error exceeds the sum of individual effects, indicating an interaction rather than an additive relationship
id: ipd-mar-interaction-exceeds-additive-error
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: bilicioglu-gunes-ayse-2026
    resource: "https://doi.org/10.1371/journal.pone.0353665"
    title: "Bilicioglu Gunes Ayse, Zeybekoglu Yesil Serife. (2026). Examining the joint impact of missing data mechanisms and item parameter drift on the accuracy of item response theory-based test equating. PLOS One. https://doi.org/10.1371/journal.pone.0353665"
    author: Bilicioglu Gunes Ayse, Zeybekoglu Yesil Serife
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The joint effect of IPD and MAR missing data on equating error exceeds the sum of individual effects, indicating an interaction rather than an additive relationship

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Combined IPD and MAR conditions produced the highest bias and RMSE (K25: Bias_B 0.0289, RMSE 0.0647), with most threshold-exceeding conditions involving moderate-to-severe combinations of both factors. [→ Bilicioglu Gunes Ayse 2026](#bilicioglu-gunes-ayse-2026)

## Evidence

### Bilicioglu Gunes Ayse 2026

Bilicioglu Gunes Ayse, Zeybekoglu Yesil Serife. (2026). Examining the joint impact of missing data mechanisms and item parameter drift on the accuracy of item response theory-based test equating. PLOS One. https://doi.org/10.1371/journal.pone.0353665

`q2 · i?` · `causal · r2`

Simulation analysis of combined conditions K10–K25. The article reports the highest error in K25 (IPD 20%, Δb = 0.50, MAR 20%), where "the bias for the B constant reached 0.029 and the RMSE value was 0.065", and that MAR panels in Fig 1 show larger line separation than MCAR panels.

> "Most of the conditions marked with an asterisk in Table 3 involve the combination of moderate missing rates and moderate IPD, suggesting that the joint effect of these factors is not merely additive but reflects an interaction."

## Discussion


## Related Claims
- [The A (scale) equating constant remains largely stable across IPD and missing data conditions, with error concentrated in the B constant](a-constant-stable-across-conditions.md) — related
- [Item parameter drift alone, at 10–20% drift rates and Δb up to 0.50, produces no meaningful bias in SL equating constants but increases estimation variability (RMSE)](ipd-alone-increases-rmse-not-bias.md) — related
- [Multiple imputation by chained equations reduces equating error under MCAR but does not fully eliminate bias under MAR conditions](mice-effective-mcar-limited-mar.md) — related
- [MAR missing data mechanisms introduce positive bias in the B equating constant under SL equating, whereas MCAR does not, at missing rates up to 20%](mar-missingness-biases-b-equating-constant.md) — related
