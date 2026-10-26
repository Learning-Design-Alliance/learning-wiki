---
type: claim
title: Random Forest and SHAP analyses identify Gamma and Beta band power at temporal and frontal channels (T3, P3, F7, T4, T4, F8, F7) as the most critical features for EEG familiarity classification
description: Random Forest and SHAP analyses identify Gamma and Beta band power at temporal and frontal channels (T3, P3, F7, T4, T4, F8, F7) as the most critical features for EEG familiarity classification
id: gamma-beta-temporal-frontal-familiarity-biomarkers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: isuru-nanayakkara-and-thilina-halloluwa-2026
    resource: "https://doi.org/10.48550/arxiv.2608.16541"
    title: "Isuru Nanayakkara and Thilina Halloluwa. (2026). Automating Learner Assessment: Benchmarking Machine Learning and Deep Learning Models for EEG-Based Familiarity Prediction. https://arxiv.org/abs/2608.16541 [doi:10.48550/arxiv.2608.16541](https://doi.org/10.48550/arxiv.2608.16541)"
    author: Isuru Nanayakkara and Thilina Halloluwa
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Random Forest and SHAP analyses identify Gamma and Beta band power at temporal and frontal channels (T3, P3, F7, T4, T4, F8, F7) as the most critical features for EEG familiarity classification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Random Forest importances ranked High Gamma (32.2%), Low Gamma (26.2%), and Beta (15.8%) as top spectral features, with temporal and parietal channels (T3, P3, F7, T4) contributing most; SHAP showed higher Gamma/Beta power at T4, F8, F7 drove predictions toward familiar states. [→ Isuru Nanayakkara and Thilina Halloluwa 2026](#isuru-nanayakkara-and-thilina-halloluwa-2026)

## Evidence

### Isuru Nanayakkara and Thilina Halloluwa 2026

Isuru Nanayakkara and Thilina Halloluwa. (2026). Automating Learner Assessment: Benchmarking Machine Learning and Deep Learning Models for EEG-Based Familiarity Prediction. https://arxiv.org/abs/2608.16541 [doi:10.48550/arxiv.2608.16541](https://doi.org/10.48550/arxiv.2608.16541)

`q2 · i?` · `associational · r2`

Interpretability analysis of the 4-class Random Forest (feature importances) and DNN (SHAP values), both trained on the full 4-class configuration; the article reports Gamma and Beta power at temporal-frontal sites driving familiar-state predictions. No effect size is printed.

> "Higher power in the Gamma and Beta bands at T4, F8, and F7 strongly drove the model toward predicting familiar states, neurophysiologically aligning with active memory retrieval processes."

## Discussion


## Related Claims
- [Trial-level spectral features robustly differentiate stimulus domains (faces vs. equations) but no familiarity-driven spectral shift survives FDR correction](domain-robust-familiarity-subtle-univariate-eeg.md) — related
- [Temporal leakage from shuffled neighboring epochs inflates EEG familiarity classification, with peak weighted F1 dropping from 0.9853 (CNN, stratified) to 0.6038 (CNN, Group K-Fold)](temporal-leakage-inflates-eeg-familiarity-classification.md) — related
- [Familiarity recognition is represented by a distributed multivariate spatial-spectral pattern rather than localized single-feature shifts, necessitating multivariate machine learning](multivariate-distributed-familiarity-pattern.md) — related
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — related
- [Domain-separated EEG classifiers decode familiarity within each stimulus category, with peak LOGO Mean Recall of 0.8992 for faces-only (HistGradient Boosting) and 0.8670 for equations-only (CNN)](domain-separated-eeg-familiarity-decoding.md) — related
- [EEG-derived temporal flexibility and search information in specific Brodmann areas and frequency bands are associated with simulator task performance](eeg-flexibility-search-information-associated-performance.md) — related
- [MRMR feature ranking identifies occipital alpha PSD as the most discriminative feature, followed by frontal gamma, high-beta, and theta](mrmr-occipital-alpha-top-feature.md) — related
