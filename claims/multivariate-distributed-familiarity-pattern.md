---
type: claim
title: Familiarity recognition is represented by a distributed multivariate spatial-spectral pattern rather than localized single-feature shifts, necessitating multivariate machine learning
description: Familiarity recognition is represented by a distributed multivariate spatial-spectral pattern rather than localized single-feature shifts, necessitating multivariate machine learning
id: multivariate-distributed-familiarity-pattern
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
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

# Familiarity recognition is represented by a distributed multivariate spatial-spectral pattern rather than localized single-feature shifts, necessitating multivariate machine learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` Because univariate FDR-corrected t-tests found no single familiarity-differentiating feature while multivariate models achieved high LOGO scores, the article concludes familiarity is encoded in a joint multivariate pattern across channels and bands. [→ Isuru Nanayakkara and Thilina Halloluwa 2026](#isuru-nanayakkara-and-thilina-halloluwa-2026)

## Evidence

### Isuru Nanayakkara and Thilina Halloluwa 2026

Isuru Nanayakkara and Thilina Halloluwa. (2026). Automating Learner Assessment: Benchmarking Machine Learning and Deep Learning Models for EEG-Based Familiarity Prediction. https://arxiv.org/abs/2608.16541

`q2 · i?` · `associational · r1`

Authors' interpretation reconciling the univariate t-test nulls (Section IV-A) with significant multivariate permutation-tested classification; the article states familiarity is "represented by a complex, distributed spatial-spectral pat- tern across channels". This is an interpretation, not a directly tested contrast.

> "This demonstrates that familiarity recognition is represented by a complex, distributed spatial-spectral pat- tern across channels rather than localized changes in indi- vidual features, necessitating multivariate machine learning approaches."

## Discussion


## Related Claims
- [Trial-level spectral features robustly differentiate stimulus domains (faces vs. equations) but no familiarity-driven spectral shift survives FDR correction](domain-robust-familiarity-subtle-univariate-eeg.md) — related
- [Domain-separated EEG classifiers decode familiarity within each stimulus category, with peak LOGO Mean Recall of 0.8992 for faces-only (HistGradient Boosting) and 0.8670 for equations-only (CNN)](domain-separated-eeg-familiarity-decoding.md) — related
- [Random Forest and SHAP analyses identify Gamma and Beta band power at temporal and frontal channels (T3, P3, F7, T4, T4, F8, F7) as the most critical features for EEG familiarity classification](gamma-beta-temporal-frontal-familiarity-biomarkers.md) — related
- [Temporal leakage from shuffled neighboring epochs inflates EEG familiarity classification, with peak weighted F1 dropping from 0.9853 (CNN, stratified) to 0.6038 (CNN, Group K-Fold)](temporal-leakage-inflates-eeg-familiarity-classification.md) — related
- [Trial-independent EEG familiarity classification remains statistically significantly above chance for the 4-class, equations-only, and faces-only tasks under Bonferroni-corrected permutation tests](trial-independent-eeg-familiarity-above-chance.md) — related
