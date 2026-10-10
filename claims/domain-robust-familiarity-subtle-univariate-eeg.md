---
type: claim
title: Trial-level spectral features robustly differentiate stimulus domains (faces vs. equations) but no familiarity-driven spectral shift survives FDR correction
description: Trial-level spectral features robustly differentiate stimulus domains (faces vs.
id: domain-robust-familiarity-subtle-univariate-eeg
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: isuru-nanayakkara-and-thilina-halloluwa-2026
    resource: "https://arxiv.org/abs/2608.16541"
    title: "Isuru Nanayakkara and Thilina Halloluwa. (2026). Automating Learner Assessment: Benchmarking Machine Learning and Deep Learning Models for EEG-Based Familiarity Prediction. https://arxiv.org/abs/2608.16541"
    author: Isuru Nanayakkara and Thilina Halloluwa
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Trial-level spectral features robustly differentiate stimulus domains (faces vs. equations) but no familiarity-driven spectral shift survives FDR correction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` FDR-corrected Welch's t-tests on trial-aggregated PSD features found robust domain differences (e.g., F4 Low Gamma, t(35)=5.14, p_FDR=0.0013) but no familiarity contrast surviving correction (minimum adjusted p=0.195). [→ Isuru Nanayakkara and Thilina Halloluwa 2026](#isuru-nanayakkara-and-thilina-halloluwa-2026)

## Evidence

### Isuru Nanayakkara and Thilina Halloluwa 2026

Isuru Nanayakkara and Thilina Halloluwa. (2026). Automating Learner Assessment: Benchmarking Machine Learning and Deep Learning Models for EEG-Based Familiarity Prediction. https://arxiv.org/abs/2608.16541

`q2 · i?` · `associational · r1`

Trial-level aggregation (N=37 independent trials) with two-sample Welch's t-tests and Benjamini-Hochberg FDR correction across 84 features; the article reports robust domain differences in Gamma features. No standardized effect size is printed.

> "Multiple frontal and occipital Gamma band features survived the FDR correction, such as F4 Low Gamma (Mean Eq = 0.317, Mean Face = 0.120, Welch's t(35) =5.14,p raw <0.0001,p FDR =0.0013)"

## Discussion


## Related Claims
- [Familiarity recognition is represented by a distributed multivariate spatial-spectral pattern rather than localized single-feature shifts, necessitating multivariate machine learning](multivariate-distributed-familiarity-pattern.md) — related
- [Domain-separated EEG classifiers decode familiarity within each stimulus category, with peak LOGO Mean Recall of 0.8992 for faces-only (HistGradient Boosting) and 0.8670 for equations-only (CNN)](domain-separated-eeg-familiarity-decoding.md) — related
- [Trial-independent EEG familiarity classification remains statistically significantly above chance for the 4-class, equations-only, and faces-only tasks under Bonferroni-corrected permutation tests](trial-independent-eeg-familiarity-above-chance.md) — related
- [Random Forest and SHAP analyses identify Gamma and Beta band power at temporal and frontal channels (T3, P3, F7, T4, T4, F8, F7) as the most critical features for EEG familiarity classification](gamma-beta-temporal-frontal-familiarity-biomarkers.md) — related
