---
type: claim
title: Client datasets in remote learner-state detection differ sharply in sample counts and positive sample rates
description: Client datasets in remote learner-state detection differ sharply in sample counts and positive sample rates
id: client-data-heterogeneity-learner-state-datasets
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: bodonhelyi-2026
    resource: "https://doi.org/10.48550/arXiv.2602.09904"
    title: "Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E. (2026). Safeguarding Privacy: Privacy-Preserving Detection of Mind Wandering and Disengagement Using Federated Learning in Online Education. [doi:10.48550/arXiv.2602.09904](https://doi.org/10.48550/arXiv.2602.09904)"
    author: Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Client datasets in remote learner-state detection differ sharply in sample counts and positive sample rates

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the Colorado dataset, despite an overall positive sample rate of 30% among 130 users, 8 users had only mind-wandering samples while 15 never reported mind wandering, illustrating severe client-level heterogeneity. [→ Bodonhelyi 2026](#bodonhelyi-2026)

## Evidence

### Bodonhelyi 2026

Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E. (2026). Safeguarding Privacy: Privacy-Preserving Detection of Mind Wandering and Disengagement Using Federated Learning in Online Education. [doi:10.48550/arXiv.2602.09904](https://doi.org/10.48550/arXiv.2602.09904)

`q2 · i?` · `design · r2`

Descriptive analysis of the Colorado dataset's client-level distribution (Figure 3a): despite the "overall positive sample rate among 130 users reaches 30%", 8 users had only mind-wandering samples and 15 never reported mind wandering.

> "Although the overall positive sample rate among 130 users reaches 30%, 8 of them have only mind wandering samples, while 15 participants never reported mind wandering during experiments."

## Discussion


## Related Claims
- [Lab-trained mind wandering detectors generalize to in-the-wild lecture viewing across task, setting, and cultural group, with BiLSTM on latent features reaching F1 = 0.352](cross-dataset-generalization-mind-wandering-detection.md) — related
- [Latent transfer-learned features yield better overall mind wandering detection than explicit OpenFace features, and temporal models add a small improvement, especially cross-dataset](latent-features-beat-explicit-features-overall.md) — related
- [Transfer-learned latent facial features support above-chance video-based mind wandering detection within a lab reading dataset, with LSTM reaching F1 = 0.459](latent-features-within-lab-mind-wandering-detection.md) — related
- [Low working memory span individuals are more prone to mind-wandering, but only on tasks they want to attend to](low-span-mind-wandering-goal-relevant-tasks.md) — related
