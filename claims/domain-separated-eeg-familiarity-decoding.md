---
type: claim
title: Domain-separated EEG classifiers decode familiarity within each stimulus category, with peak LOGO Mean Recall of 0.8992 for faces-only (HistGradient Boosting) and 0.8670 for equations-only (CNN)
description: Domain-separated EEG classifiers decode familiarity within each stimulus category, with peak LOGO Mean Recall of 0.8992 for faces-only (HistGradient Boosting) and 0.8670 for equations-only (CNN)
id: domain-separated-eeg-familiarity-decoding
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

# Domain-separated EEG classifiers decode familiarity within each stimulus category, with peak LOGO Mean Recall of 0.8992 for faces-only (HistGradient Boosting) and 0.8670 for equations-only (CNN)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` Under Leave-One-Group-Out validation, binary classifiers achieved high average single-class recall for equations-only familiarity (CNN 0.8670 ± 0.2392) and faces-only familiarity (HistGradient Boosting 0.8992 ± 0.0850), plus domain-only classification at 0.9491 (CNN). [→ Isuru Nanayakkara and Thilina Halloluwa 2026](#isuru-nanayakkara-and-thilina-halloluwa-2026)

## Evidence

### Isuru Nanayakkara and Thilina Halloluwa 2026

Isuru Nanayakkara and Thilina Halloluwa. (2026). Automating Learner Assessment: Benchmarking Machine Learning and Deep Learning Models for EEG-Based Familiarity Prediction. https://arxiv.org/abs/2608.16541

`q2 · i?` · `associational · r1`

Secondary domain-isolated LOGO evaluations on 37 trial blocks (24 equation, 13 face); the article reports the faces-only HistGradient Boosting model "outperforming the CNN Optimized model". LOGO Mean Recall is a recall-based metric not directly comparable to balanced F1.

> "For the equations-only familiarity task, the CNN Optimized model achieved an average LOGO Mean Recall of 0.8670 ± 0.2392, and the HistGradient Boosting classifier achieved 0.7588 ± 0.3256. For the faces-only familiarity task, the HistGradient Boosting classifier achieved a peak average LOGO Mean Recall of 0.8992 ± 0.0850, outperforming the CNN Optimized model which achieved 0.8875 ± 0.2347."

## Discussion


## Related Claims
- [Trial-level spectral features robustly differentiate stimulus domains (faces vs. equations) but no familiarity-driven spectral shift survives FDR correction](domain-robust-familiarity-subtle-univariate-eeg.md) — related
- [Trial-independent EEG familiarity classification remains statistically significantly above chance for the 4-class, equations-only, and faces-only tasks under Bonferroni-corrected permutation tests](trial-independent-eeg-familiarity-above-chance.md) — related
- [Temporal leakage from shuffled neighboring epochs inflates EEG familiarity classification, with peak weighted F1 dropping from 0.9853 (CNN, stratified) to 0.6038 (CNN, Group K-Fold)](temporal-leakage-inflates-eeg-familiarity-classification.md) — related
- [Familiarity recognition is represented by a distributed multivariate spatial-spectral pattern rather than localized single-feature shifts, necessitating multivariate machine learning](multivariate-distributed-familiarity-pattern.md) — related
