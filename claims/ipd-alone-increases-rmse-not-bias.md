---
type: claim
title: "Item parameter drift alone, at 10–20% drift rates and Δb up to 0.50, produces no meaningful bias in SL equating constants but increases estimation variability (RMSE)"
description: "Item parameter drift alone, at 10–20% drift rates and Δb up to 0.50, produces no meaningful bias in SL equating constants but increases estimation variability (RMSE)"
id: ipd-alone-increases-rmse-not-bias
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

# Item parameter drift alone, at 10–20% drift rates and Δb up to 0.50, produces no meaningful bias in SL equating constants but increases estimation variability (RMSE)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` IPD-only conditions showed small bias (B range −0.0011 to 0.0060) while RMSE of B rose from 0.0493 in K1 to 0.0580 in K5, an increase of about 18%. [→ Bilicioglu Gunes Ayse 2026](#bilicioglu-gunes-ayse-2026)

## Evidence

### Bilicioglu Gunes Ayse 2026

Bilicioglu Gunes Ayse, Zeybekoglu Yesil Serife. (2026). Examining the joint impact of missing data mechanisms and item parameter drift on the accuracy of item response theory-based test equating. PLOS One. https://doi.org/10.1371/journal.pone.0353665

`q2 · i?` · `causal · r2`

Simulation analysis of IPD-only conditions K2–K5 against control K1 with no missing data. The article states bias values were "quite small (−0.0011 to 0.0060)" and that "RMSE increased as the magnitude of IPD increased", reaching 0.0580 at the most severe drift condition.

> "The value, which was 0.0493 in K1, reached 0.0580 in K5 (IPD rate = 20%, Δb = 0.50). When the delta values in Table 3 are examined, ΔRMSE_B in K5 is 0.0087, corresponding to an increase of approximately 18% compared to K1."

## Discussion


## Related Claims
- [The A (scale) equating constant remains largely stable across IPD and missing data conditions, with error concentrated in the B constant](a-constant-stable-across-conditions.md) — related
- [The joint effect of IPD and MAR missing data on equating error exceeds the sum of individual effects, indicating an interaction rather than an additive relationship](ipd-mar-interaction-exceeds-additive-error.md) — related
- [MAR missing data mechanisms introduce positive bias in the B equating constant under SL equating, whereas MCAR does not, at missing rates up to 20%](mar-missingness-biases-b-equating-constant.md) — related
- [Multiple imputation by chained equations reduces equating error under MCAR but does not fully eliminate bias under MAR conditions](mice-effective-mcar-limited-mar.md) — related
