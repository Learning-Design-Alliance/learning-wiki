---
type: claim
title: Question utility is only weakly correlated with salience and not significantly correlated with expected information gain
description: Question utility is only weakly correlated with salience and not significantly correlated with expected information gain
id: utility-uncorrelated-with-salience-and-eig
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: dong-ho-lee-2026
    resource: "https://doi.org/10.18653/2026.findings-emnlp.97"
    title: "Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara. (2026). Which Questions Improve Learning the Most? Utility Estimation of Questions with LM-based Simulations. arXiv. Originally published 2025. [doi:10.18653/2026.findings-emnlp.97](https://doi.org/10.18653/2026.findings-emnlp.97)"
    author: Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara
    q: 2
    i: 0
    kind: design
    rigour: 2
---

# Question utility is only weakly correlated with salience and not significantly correlated with expected information gain

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i0` negligible
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i0` Utility has a weak correlation with salience (ρ = 0.097) and no significant correlation with EIG (ρ = −0.022), suggesting it captures a distinct signal from indirect metrics. [→ Dong-Ho Lee 2026](#dong-ho-lee-2026)

## Evidence

### Dong-Ho Lee 2026

Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara. (2026). Which Questions Improve Learning the Most? Utility Estimation of Questions with LM-based Simulations. arXiv. Originally published 2025. [doi:10.18653/2026.findings-emnlp.97](https://doi.org/10.18653/2026.findings-emnlp.97)

`q2 · i0` · `design · r2`

Correlational analysis of three metrics (utility, salience, EIG) computed on generated questions from the TEXTBOOK-EXAM training set. The article reports "only a weak correlation with salience (ρ= 0.097)" and no significant correlation with EIG (ρ=−0.022), concluding indirect metrics "may not reliably reflect a question's actual impact on learning outcomes".

> "As shown in Table 3, utility has only a weak correlation with salience (ρ= 0.097) and no significant correlation with EIG (ρ=−0.022)."

## Discussion


## Related Claims
- [Simulation-computed utility is moderately positively correlated with usefulness as perceived by human evaluators, without reducing interestingness](utility-moderately-correlates-human-perceived-usefulness.md) — related
- [Training on utility-filtered questions yields the highest exam performance, while optimizing for salience or EIG fails to enhance utility](utility-optimization-beats-indirect-metric-optimization.md) — related
- [High-utility questions are weakly related to exam-question similarity and Bloom's cognitive depth, suggesting they are not paraphrases of exam questions](high-utility-questions-not-exam-paraphrases.md) — related
