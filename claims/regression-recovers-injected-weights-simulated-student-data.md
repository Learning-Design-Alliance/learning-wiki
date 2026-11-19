---
type: claim
title: Linear regression trained on simulated student data recovers the injected weight parameters linking five activity inputs to exam performance
description: Linear regression trained on simulated student data recovers the injected weight parameters linking five activity inputs to exam performance
id: regression-recovers-injected-weights-simulated-student-data
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: bibhuprasad-mahakud-2022
    resource: "https://doi.org/10.48550/arXiv.2211.05829"
    title: "Bibhuprasad Mahakud, Ipsit Panda, Souvik Maity, Arpita Sahoo, Reeta Sharma, Bibhuti Parida. (2022). A Machine Learning system to monitor student progress in educational institutes. [doi:10.48550/arXiv.2211.05829](https://doi.org/10.48550/arXiv.2211.05829)"
    author: Bibhuprasad Mahakud, Ipsit Panda, Souvik Maity, Arpita Sahoo, Reeta Sharma, Bibhuti Parida
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: bibhuprasad-mahakud-2022-2
    resource: "https://doi.org/10.48550/arXiv.2211.05829"
    title: "Bibhuprasad Mahakud, Ipsit Panda, Souvik Maity, Arpita Sahoo, Reeta Sharma, Bibhuti Parida. (2022). A Machine Learning system to monitor student progress in educational institutes. [doi:10.48550/arXiv.2211.05829](https://doi.org/10.48550/arXiv.2211.05829)"
    author: Bibhuprasad Mahakud, Ipsit Panda, Souvik Maity, Arpita Sahoo, Reeta Sharma, Bibhuti Parida
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Linear regression trained on simulated student data recovers the injected weight parameters linking five activity inputs to exam performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On 3000 simulated data points, fitted theta parameters in both training and test sets are quite close to the injected values used to generate the data. [→ Bibhuprasad Mahakud 2022](#bibhuprasad-mahakud-2022)
`q2 i?` The cost decreases and reaches a plateau over iterations, which the authors use to check the model does not underfit the data. [→ Bibhuprasad Mahakud 2022 (2)](#bibhuprasad-mahakud-2022-2)

## Evidence

### Bibhuprasad Mahakud 2022

Bibhuprasad Mahakud, Ipsit Panda, Souvik Maity, Arpita Sahoo, Reeta Sharma, Bibhuti Parida. (2022). A Machine Learning system to monitor student progress in educational institutes. [doi:10.48550/arXiv.2211.05829](https://doi.org/10.48550/arXiv.2211.05829)

`q2 · i?` · `design · r2`

Simulation study using linear regression with least-squares cost and gradient descent on 3000 simulated points (2400 train, 600 test). The authors report that "injected values of θs and fitted θs are quite close" (Table 3).

> "It shows the injected values of θs and fitted θs are quite close and hence ensures that models works for the set of data considered in the study."

### Bibhuprasad Mahakud 2022 (2)

Bibhuprasad Mahakud, Ipsit Panda, Souvik Maity, Arpita Sahoo, Reeta Sharma, Bibhuti Parida. (2022). A Machine Learning system to monitor student progress in educational institutes. [doi:10.48550/arXiv.2211.05829](https://doi.org/10.48550/arXiv.2211.05829)

`q2 · i?` · `design · r2`

Numerical training diagnostic (Fig. 4): cost versus number of iterations up to 10000 with learning rate α = 0.05, showing the cost "decreases and reaches a plateu", used to rule out underfitting.

> "The number of iterations are taken enough to ensure the cost decreases and reaches a plateu."

## Discussion


## Related Claims
- [The general polytomous testlet model recovers true item parameters well in simulation, with average correlations of 0.9680, 0.8608, and 0.9982 for discrimination and difficulty parameters](polytomous-testlet-model-good-parameter-recovery.md) — a broader claim this one bears on
- [A semi-supervised deep learning architecture recovers the ability distribution of anchor students more accurately than direct 2PL-IRT fitting under simulated nonignorable missingness](semi-supervised-deep-learning-unbiased-ability-estimates.md) — related
- [Linear regression outperformed equipercentile and mean-sigma equating for predicting ARM scores and was selected as the final linking model](linear-regression-selected-linking-model.md) — related
