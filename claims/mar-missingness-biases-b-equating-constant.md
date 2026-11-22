---
type: claim
title: "MAR missing data mechanisms introduce positive bias in the B equating constant under SL equating, whereas MCAR does not, at missing rates up to 20%"
description: "MAR missing data mechanisms introduce positive bias in the B equating constant under SL equating, whereas MCAR does not, at missing rates up to 20%"
id: mar-missingness-biases-b-equating-constant
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

# MAR missing data mechanisms introduce positive bias in the B equating constant under SL equating, whereas MCAR does not, at missing rates up to 20%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under MAR conditions the B constant showed positive bias increasing with missing rate (0.0094 at 10%, 0.0251 at 20%), while MCAR bias stayed near zero. [→ Bilicioglu Gunes Ayse 2026](#bilicioglu-gunes-ayse-2026)

## Evidence

### Bilicioglu Gunes Ayse 2026

Bilicioglu Gunes Ayse, Zeybekoglu Yesil Serife. (2026). Examining the joint impact of missing data mechanisms and item parameter drift on the accuracy of item response theory-based test equating. PLOS One. https://doi.org/10.1371/journal.pone.0353665

`q2 · i?` · `causal · r2`

Monte Carlo simulation (500 replications, 2,000 examinees per form) comparing missing-data-only conditions K6–K9 against reference K1. The article reports that under MAR, "bias increased to 0.0094 in K8 (MAR 10%) and to 0.0251 in K9 (MAR 20%)"; under MCAR (K6–K7) bias stayed at 0.0027 and 0.0039.

> "Under MAR conditions, the pattern changes; bias increased to 0.0094 in K8 (MAR 10%) and to 0.0251 in K9 (MAR 20%). The delta values in Table 3 further highlight this difference, with ΔBias = 0.0258 and ΔRMSE = 0.0073 in K9."

## Discussion


## Related Claims
- [Item parameter drift alone, at 10–20% drift rates and Δb up to 0.50, produces no meaningful bias in SL equating constants but increases estimation variability (RMSE)](ipd-alone-increases-rmse-not-bias.md) — related
- [The joint effect of IPD and MAR missing data on equating error exceeds the sum of individual effects, indicating an interaction rather than an additive relationship](ipd-mar-interaction-exceeds-additive-error.md) — related
- [Multiple imputation by chained equations reduces equating error under MCAR but does not fully eliminate bias under MAR conditions](mice-effective-mcar-limited-mar.md) — possibly the same claim (merge candidate)
