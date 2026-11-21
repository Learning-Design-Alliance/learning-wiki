---
type: claim
title: Absolute prevalence estimates differ across models and generally do not agree within uncertainties, despite similar trends
description: Absolute prevalence estimates differ across models and generally do not agree within uncertainties, despite similar trends
id: model-prevalence-estimates-differ-within-uncertainties
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: rebeckah-k-fussell-2025
    resource: "https://doi.org/10.1103/physrevphyseducres.21.010128"
    title: "Rebeckah K. Fussell, Megan Flynn, Anil Damle, Michael F.J. Fox, and N. G. Holmes. (2025). Comparing Large Language Models for supervised analysis of students’ lab notes. [doi:10.1103/physrevphyseducres.21.010128](https://doi.org/10.1103/physrevphyseducres.21.010128)"
    author: Rebeckah K. Fussell, Megan Flynn, Anil Damle, Michael F.J. Fox, and N. G. Holmes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Absolute prevalence estimates differ across models and generally do not agree within uncertainties, despite similar trends

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In each lab session, bag of words estimates higher average fraction values than BERT and LLaMA before considering systematic effects, and the measurements from each model generally do not agree within uncertainties. [→ Rebeckah K. Fussell 2025](#rebeckah-k-fussell-2025)

## Evidence

### Rebeckah K. Fussell 2025

Rebeckah K. Fussell, Megan Flynn, Anil Damle, Michael F.J. Fox, and N. G. Holmes. (2025). Comparing Large Language Models for supervised analysis of students’ lab notes. [doi:10.1103/physrevphyseducres.21.010128](https://doi.org/10.1103/physrevphyseducres.21.010128)

`q2 · i?` · `design · r2`

Outcomes analysis with statistical and systematic uncertainty estimates for QC and PI prevalence (Fig. 4). The article attributes discrepancies to systematics calculated from false positive and false negative rates across all lab notes, which likely vary across units.

> "In general, the measurements from each model do not agree within uncertainties, which are calculated using the methods described in Section A."

## Discussion


## Related Claims
- [All three trained models measure a similar trend in QC skill prevalence across lab units, with L1b highest and L1a fewest](qc-prevalence-trend-consistent-across-models.md) — related
- [For the PI code, all three models measure a similar low, stable prevalence across sessions, with the single-session L2 unit lowest](pi-prevalence-trend-l2-lowest.md) — related
- [Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)](llm-difficulty-magnitude-error-varies-across-models.md) — a broader claim this one bears on
- [Coordinate-specific uncertainties with model-specific error estimates give a more accurate representation of model-space span than pooled, equal-fractional assumptions, and show greater post-test than pretest uncertainty](coordinate-specific-uncertainties-more-accurate.md) — related
