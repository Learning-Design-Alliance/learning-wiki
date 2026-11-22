---
type: claim
title: Multiple imputation by chained equations reduces equating error under MCAR but does not fully eliminate bias under MAR conditions
description: Multiple imputation by chained equations reduces equating error under MCAR but does not fully eliminate bias under MAR conditions
id: mice-effective-mcar-limited-mar
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: weak
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

# Multiple imputation by chained equations reduces equating error under MCAR but does not fully eliminate bias under MAR conditions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Design limits** · Bilicioglu Gunes Ayse 2026: the intervention came bundled with another change (read from the study by two models, 2026-11-22)

## Subclaims
`q2 i?` Under MCAR the B constant bias stayed close to zero across all missing rates, but under MAR bias increased noticeably with missing rate despite MICE being applied. [→ Bilicioglu Gunes Ayse 2026](#bilicioglu-gunes-ayse-2026)

## Evidence

### Bilicioglu Gunes Ayse 2026

Bilicioglu Gunes Ayse, Zeybekoglu Yesil Serife. (2026). Examining the joint impact of missing data mechanisms and item parameter drift on the accuracy of item response theory-based test equating. PLOS One. https://doi.org/10.1371/journal.pone.0353665

`q2 · i?` · `causal · r2`

Indirect evaluation of MICE effectiveness: MICE was applied in all missing-data conditions, so effectiveness was assessed by comparing MCAR (K6–K7) and MAR (K8–K9) outcomes. Imputations used logistic regression, with the number of imputations equal to the percentage of missing data.

> "Under MCAR conditions, the bias values of the B constant remain close to zero across all missing rates (K6: 0.0027; K7: 0.0039; see Table 2), suggesting that MICE effectively reduced equating bias when missingness was completely random. In contrast, under MAR conditions, bias increased noticeably with missing rate (K8: 0.0094; K9: 0.0251; see Table 2), indicating that MICE does not fully eliminate bias arising from systematic missingness."

## Discussion


## Related Claims
- [The joint effect of IPD and MAR missing data on equating error exceeds the sum of individual effects, indicating an interaction rather than an additive relationship](ipd-mar-interaction-exceeds-additive-error.md) — related
- [MAR missing data mechanisms introduce positive bias in the B equating constant under SL equating, whereas MCAR does not, at missing rates up to 20%](mar-missingness-biases-b-equating-constant.md) — possibly the same claim (merge candidate)
- [Item parameter drift alone, at 10–20% drift rates and Δb up to 0.50, produces no meaningful bias in SL equating constants but increases estimation variability (RMSE)](ipd-alone-increases-rmse-not-bias.md) — related
