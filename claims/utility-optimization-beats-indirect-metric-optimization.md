---
type: claim
title: Training on utility-filtered questions yields the highest exam performance, while optimizing for salience or EIG fails to enhance utility
description: Training on utility-filtered questions yields the highest exam performance, while optimizing for salience or EIG fails to enhance utility
id: utility-optimization-beats-indirect-metric-optimization
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: dong-ho-lee-2026
    resource: "https://doi.org/10.18653/2026.findings-emnlp.97"
    title: "Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara. (2026). Which Questions Improve Learning the Most? Utility Estimation of Questions with LM-based Simulations. arXiv. Originally published 2025. [doi:10.18653/2026.findings-emnlp.97](https://doi.org/10.18653/2026.findings-emnlp.97)"
    author: Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Training on utility-filtered questions yields the highest exam performance, while optimizing for salience or EIG fails to enhance utility

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` QUEST models trained on questions filtered by utility > 0.1 consistently yield the highest exam performance across all subjects, whereas models trained on salience = 5 or EIG > 0 questions improve their respective metric but fail to enhance utility. [→ Dong-Ho Lee 2026](#dong-ho-lee-2026)

## Evidence

### Dong-Ho Lee 2026

Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara. (2026). Which Questions Improve Learning the Most? Utility Estimation of Questions with LM-based Simulations. arXiv. Originally published 2025. [doi:10.18653/2026.findings-emnlp.97](https://doi.org/10.18653/2026.findings-emnlp.97)

`q2 · i?` · `design · r2`

Comparison experiment (Table 5) training QUEST models on datasets filtered by three criteria: utility > 0.1, salience = 5, and EIG > 0, evaluated on exam score, average salience, and average EIG. For example, in Microbiology the utility-filtered model scored 64.27 versus 34.42 (salience-filtered) and 61 (EIG-filtered).

> "We observe that training on utility-optimized questions consistently yields the highest exam per- formance across all subjects. In contrast, optimiz- ing for salience or EIG improves the respective metric, but fails to enhance utility."

## Discussion


## Related Claims
- [QUEST-trained question generators raise simulated exam scores by 18.5% over the next strongest baseline across five subjects](quest-trained-generators-18-5-percent-exam-gain.md) — related
- [Simulation-computed utility is moderately positively correlated with usefulness as perceived by human evaluators, without reducing interestingness](utility-moderately-correlates-human-perceived-usefulness.md) — related
- [Question utility is only weakly correlated with salience and not significantly correlated with expected information gain](utility-uncorrelated-with-salience-and-eig.md) — related
