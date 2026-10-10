---
type: claim
title: Temporal leakage from shuffled neighboring epochs inflates EEG familiarity classification, with peak weighted F1 dropping from 0.9853 (CNN, stratified) to 0.6038 (CNN, Group K-Fold)
description: Temporal leakage from shuffled neighboring epochs inflates EEG familiarity classification, with peak weighted F1 dropping from 0.9853 (CNN, stratified) to 0.6038 (CNN, Group K-Fold)
id: temporal-leakage-inflates-eeg-familiarity-classification
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
    rigour: 2
---

# Temporal leakage from shuffled neighboring epochs inflates EEG familiarity classification, with peak weighted F1 dropping from 0.9853 (CNN, stratified) to 0.6038 (CNN, Group K-Fold)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Under stratified K-Fold, models reached up to 0.9853 weighted F1 (CNN), but under trial-independent Group K-Fold the peak dropped to 0.6038 (CNN) with Gradient Boosting at 0.5510, confirming massive temporal leakage from shuffled neighboring epochs. [→ Isuru Nanayakkara and Thilina Halloluwa 2026](#isuru-nanayakkara-and-thilina-halloluwa-2026)

## Evidence

### Isuru Nanayakkara and Thilina Halloluwa 2026

Isuru Nanayakkara and Thilina Halloluwa. (2026). Automating Learner Assessment: Benchmarking Machine Learning and Deep Learning Models for EEG-Based Familiarity Prediction. https://arxiv.org/abs/2608.16541

`q2 · i?` · `associational · r2`

Benchmarking of fifteen ML/DL models on EEG spectral features from 23 participants, comparing Stratified K-Fold versus Group K-Fold protocols; the article reports the drop "to 0.6038 F1-score (using CNN)" and attributes it to "massive temporal leakage". No effect size is printed for this comparison.

> "However, under the rigorous trial-independent Group K-Fold protocol, the peak performance dropped to 0.6038 F1-score (using CNN), with the Gradient Boosting reaching 0.5510. This drop confirms that shuffling neighboring epochs introduces massive temporal leakage."

## Discussion


## Related Claims
- [Domain-separated EEG classifiers decode familiarity within each stimulus category, with peak LOGO Mean Recall of 0.8992 for faces-only (HistGradient Boosting) and 0.8670 for equations-only (CNN)](domain-separated-eeg-familiarity-decoding.md) — related
- [Random Forest and SHAP analyses identify Gamma and Beta band power at temporal and frontal channels (T3, P3, F7, T4, T4, F8, F7) as the most critical features for EEG familiarity classification](gamma-beta-temporal-frontal-familiarity-biomarkers.md) — related
- [Familiarity recognition is represented by a distributed multivariate spatial-spectral pattern rather than localized single-feature shifts, necessitating multivariate machine learning](multivariate-distributed-familiarity-pattern.md) — related
- [Trial-independent EEG familiarity classification remains statistically significantly above chance for the 4-class, equations-only, and faces-only tasks under Bonferroni-corrected permutation tests](trial-independent-eeg-familiarity-above-chance.md) — related
