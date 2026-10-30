---
type: claim
title: MRMR feature ranking identifies occipital alpha PSD as the most discriminative feature, followed by frontal gamma, high-beta, and theta
description: MRMR feature ranking identifies occipital alpha PSD as the most discriminative feature, followed by frontal gamma, high-beta, and theta
id: mrmr-occipital-alpha-top-feature
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: hui-xie-2025
    resource: "https://doi.org/10.1038/s41539-025-00376-5"
    title: "Hui Xie, Chunli Jia, Yanxia Luo, Jiangshan He, Zexiao Dong, Dan Liang, Ziqi Ren, Mingzhe Jiang, Xinbo Gao & Xueli Chen. (2025). EEG analysis of brain dynamics in a simulated multi-task and multi-stage learning environment. npj Science of Learning. https://doi.org/10.1038/s41539-025-00376-5"
    author: "Hui Xie, Chunli Jia, Yanxia Luo, Jiangshan He, Zexiao Dong, Dan Liang, Ziqi Ren, Mingzhe Jiang, Xinbo Gao & Xueli Chen"
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# MRMR feature ranking identifies occipital alpha PSD as the most discriminative feature, followed by frontal gamma, high-beta, and theta

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In MRMR feature selection, occipital alpha relative PSD received the highest classification weight, followed by frontal gamma, high-beta, and theta relative PSD. [→ Hui Xie 2025](#hui-xie-2025)

## Evidence

### Hui Xie 2025

Hui Xie, Chunli Jia, Yanxia Luo, Jiangshan He, Zexiao Dong, Dan Liang, Ziqi Ren, Mingzhe Jiang, Xinbo Gao & Xueli Chen. (2025). EEG analysis of brain dynamics in a simulated multi-task and multi-stage learning environment. npj Science of Learning. https://doi.org/10.1038/s41539-025-00376-5

`q2 · i?` · `associational · r1`

MRMR feature-importance analysis over the 84-feature stage-classification dataset, with the top 20 channel-band features ranked (Fig. 7). The authors note the high-weight regions and bands align with the bands emphasized in their spectral analysis.

> "The relative PSD in the alpha band in the occipital lobe was assigned the highest categorization weight, followed by the relative PSD in the gamma, high-beta, and theta bands in the frontal lobe"

## Discussion


## Related Claims
- [Random Forest and SHAP analyses identify Gamma and Beta band power at temporal and frontal channels (T3, P3, F7, T4, T4, F8, F7) as the most critical features for EEG familiarity classification](gamma-beta-temporal-frontal-familiarity-biomarkers.md) — related
- [Relative PSD shows stage- and task-specific band patterns, including higher high-beta in Stage 3 of labs and quizzes](relative-psd-band-stage-patterns.md) — related
- [Familiarity recognition is represented by a distributed multivariate spatial-spectral pattern rather than localized single-feature shifts, necessitating multivariate machine learning](multivariate-distributed-familiarity-pattern.md) — related
- [Teacher-initiated activities also increased theta power and decreased beta and gamma power, converging with the alpha-based inference of lower wakefulness and attention](theta-beta-gamma-convergent-evidence.md) — related
