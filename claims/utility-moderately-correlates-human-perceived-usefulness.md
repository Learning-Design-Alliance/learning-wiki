---
type: claim
title: Simulation-computed utility is moderately positively correlated with usefulness as perceived by human evaluators, without reducing interestingness
description: Simulation-computed utility is moderately positively correlated with usefulness as perceived by human evaluators, without reducing interestingness
id: utility-moderately-correlates-human-perceived-usefulness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: dong-ho-lee-2026
    resource: "https://doi.org/10.18653/2026.findings-emnlp.97"
    title: "Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara. (2026). Which Questions Improve Learning the Most? Utility Estimation of Questions with LM-based Simulations. arXiv. Originally published 2025. [doi:10.18653/2026.findings-emnlp.97](https://doi.org/10.18653/2026.findings-emnlp.97)"
    author: Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara
    q: 2
    i: 2
    kind: design
    rigour: 2
---

# Simulation-computed utility is moderately positively correlated with usefulness as perceived by human evaluators, without reducing interestingness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i2` medium
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i2` Utility is moderately positively correlated with usefulness perceived by humans (ρ = 0.321), while salience and EIG are weakly negatively correlated; high-utility questions are ranked and rated higher for usefulness and are rated as interesting as the others. [→ Dong-Ho Lee 2026](#dong-ho-lee-2026)

## Evidence

### Dong-Ho Lee 2026

Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara. (2026). Which Questions Improve Learning the Most? Utility Estimation of Questions with LM-based Simulations. arXiv. Originally published 2025. [doi:10.18653/2026.findings-emnlp.97](https://doi.org/10.18653/2026.findings-emnlp.97)

`q2 · i2` · `design · r2`

Human evaluation study where participants answer exam problems after reading a section and QA sets, ranking and rating questions of exclusively high utility, salience, and EIG. The article prints the correlation "ρ= 0.321" with human-perceived usefulness, a moderate positive relationship, with high-utility questions ranked highest for usefulness.

> "The results show that utility is moderately positively correlated with usefulness perceived by hu- mans (ρ= 0.321), while other metrics are weakly negatively correlated. In addition, high utility ques- tions are consistently ranked and rated higher than high salience and high EIG questions for useful- ness."

## Discussion


## Related Claims
- [Question utility is only weakly correlated with salience and not significantly correlated with expected information gain](utility-uncorrelated-with-salience-and-eig.md) — related
- [Training on utility-filtered questions yields the highest exam performance, while optimizing for salience or EIG fails to enhance utility](utility-optimization-beats-indirect-metric-optimization.md) — related
- [High-utility questions are weakly related to exam-question similarity and Bloom's cognitive depth, suggesting they are not paraphrases of exam questions](high-utility-questions-not-exam-paraphrases.md) — related
