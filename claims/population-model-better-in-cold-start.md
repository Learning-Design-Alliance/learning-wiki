---
type: claim
title: The population-based engagement model outperforms per-learner personalised models when individual training data is limited (around 60 events)
description: The population-based engagement model outperforms per-learner personalised models when individual training data is limited (around 60 events)
id: population-model-better-in-cold-start
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: sahan-bulathwela-2020
    resource: "https://doi.org/10.48550/arXiv.2006.00592"
    title: "Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)"
    author: Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The population-based engagement model outperforms per-learner personalised models when individual training data is limited (around 60 events)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For the 20 most active VLN learners, the population-based model achieves lower MAE than the personalised model while per-learner training examples are limited (approximately 60). [→ Sahan Bulathwela 2020](#sahan-bulathwela-2020)

## Evidence

### Sahan Bulathwela 2020

Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)

`q2 · i?` · `design · r2`

Comparison on the 20 most active learners, each with a temporal 70:30 train-test split, evaluating MAE difference between population-based and personalised models (Figure 8). A negative MAE difference indicates the population model is better; the green line marks zero difference.

> "shows that the population-based model has better predic- tive power when the number of training examples available for the individual learner is limited ( ≈ 60)."

## Discussion


## Related Claims
- [AI-supported adaptive systems are reported to enhance adult learner engagement, motivation, and outcomes when aligned with learner goals and prior knowledge](ai-adaptive-systems-enhance-adult-engagement.md) — related
- [Multi-agent tutoring architectures show superior behaviour modelling and feedback compared to single-agent or rule-based tutors](multi-agent-tutoring-superior-single-agent.md) — related
