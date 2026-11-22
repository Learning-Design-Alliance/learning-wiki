---
type: claim
title: Bandit-optimized assistance policies significantly improve student outcomes over a randomized assistance policy in live use across 166,000 practice sessions
description: Bandit-optimized assistance policies significantly improve student outcomes over a randomized assistance policy in live use across 166,000 practice sessions
id: mab-assistance-policy-improves-outcomes-ab-test
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: schmucker-2025
    resource: "https://doi.org/10.48550/arXiv.2508.00270"
    title: "Schmucker, R., Pachapurkar, N., Bala, S., Shah, M., & Mitchell, T. (2025). Learning to Optimize Feedback for One Million Students: Insights from Multi-Armed and Contextual Bandits in Large-Scale Online Tutoring. [doi:10.48550/arXiv.2508.00270](https://doi.org/10.48550/arXiv.2508.00270)"
    author: "Schmucker, R., Pachapurkar, N., Bala, S., Shah, M., & Mitchell, T."
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Bandit-optimized assistance policies significantly improve student outcomes over a randomized assistance policy in live use across 166,000 practice sessions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` A live A/B evaluation in over 166,000 learning sessions found that the learned assistance policy improved student learning outcomes significantly compared to a randomized assistance policy. [→ Schmucker 2025](#schmucker-2025)

## Evidence

### Schmucker 2025

Schmucker, R., Pachapurkar, N., Bala, S., Shah, M., & Mitchell, T. (2025). Learning to Optimize Feedback for One Million Students: Insights from Multi-Armed and Contextual Bandits in Large-Scale Online Tutoring. [doi:10.48550/arXiv.2508.00270](https://doi.org/10.48550/arXiv.2508.00270)

`q3 · i?` · `causal · r2`

Large-scale live A/B evaluation of the trained MAB policy against a randomized assistance policy in the CK-12 Flexbook 2.0 system; the article reports the learned policy "improves learning outcomes of future students significantly" across the evaluated sessions.

> "We evaluate the assistance policy trained using our algorithm in comparison to a randomized assistance policy in live use in over 166, 000 learning sessions. We find that the system's ability to learn to teach better using data from prior students improves learning outcomes of future students significantly."

## Discussion


## Related Claims
- [Assistance actions exhibit heterogeneous treatment effects across students, but effect sizes are often too small for contextual bandit policies to significantly outperform well-optimized MAB policies](hte-exists-but-cb-gains-limited.md) — related
- [The PPO-driven policy substantially outperformed a random policy baseline, with cumulative reward of 95.12 ± 1.23 versus 12.3 ± 4.7](ppo-outperforms-random-baseline-reward.md) — related
- [The authors report AI-Tutor outperforms state-of-the-art baselines on engagement, retention, and final outcomes in a large-scale empirical evaluation](ai-tutor-outperforms-baselines-large-scale-evaluation.md) — related
