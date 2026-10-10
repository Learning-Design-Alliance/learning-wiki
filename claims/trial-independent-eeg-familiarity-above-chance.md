---
type: claim
title: Trial-independent EEG familiarity classification remains statistically significantly above chance for the 4-class, equations-only, and faces-only tasks under Bonferroni-corrected permutation tests
description: Trial-independent EEG familiarity classification remains statistically significantly above chance for the 4-class, equations-only, and faces-only tasks under Bonferroni-corrected permutation tests
id: trial-independent-eeg-familiarity-above-chance
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
    kind: design
    rigour: 2
---

# Trial-independent EEG familiarity classification remains statistically significantly above chance for the 4-class, equations-only, and faces-only tasks under Bonferroni-corrected permutation tests

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Permutation tests (1000 permutations, HistGradient Boosting proxy) showed all three familiarity tasks significantly above chance: 4-class (adjusted p≤0.0030), faces-only (adjusted p=0.0060), equations-only (adjusted p=0.0360). [→ Isuru Nanayakkara and Thilina Halloluwa 2026](#isuru-nanayakkara-and-thilina-halloluwa-2026)

## Evidence

### Isuru Nanayakkara and Thilina Halloluwa 2026

Isuru Nanayakkara and Thilina Halloluwa. (2026). Automating Learner Assessment: Benchmarking Machine Learning and Deep Learning Models for EEG-Based Familiarity Prediction. https://arxiv.org/abs/2608.16541

`q2 · i?` · `design · r2`

Empirical permutation testing (1000 permutations, trial-group-level label shuffling) using HistGradient Boosting as a computationally efficient proxy; the article reports that "all three tasks achieve statistical significance" under Bonferroni correction. No effect size is printed.

> "Under this correction, all three tasks achieve statistical significance: the 4-class task (p≤0.0010, adjusted p≤0.0030), the faces-only task (p=0.0020, adjusted p=0.0060), and the equations-only task (p=0.0120, adjusted p=0.0360)."

## Discussion


## Related Claims
- [Trial-level spectral features robustly differentiate stimulus domains (faces vs. equations) but no familiarity-driven spectral shift survives FDR correction](domain-robust-familiarity-subtle-univariate-eeg.md) — related
- [Domain-separated EEG classifiers decode familiarity within each stimulus category, with peak LOGO Mean Recall of 0.8992 for faces-only (HistGradient Boosting) and 0.8670 for equations-only (CNN)](domain-separated-eeg-familiarity-decoding.md) — related
- [Temporal leakage from shuffled neighboring epochs inflates EEG familiarity classification, with peak weighted F1 dropping from 0.9853 (CNN, stratified) to 0.6038 (CNN, Group K-Fold)](temporal-leakage-inflates-eeg-familiarity-classification.md) — related
- [Familiarity recognition is represented by a distributed multivariate spatial-spectral pattern rather than localized single-feature shifts, necessitating multivariate machine learning](multivariate-distributed-familiarity-pattern.md) — related
