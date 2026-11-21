---
type: claim
title: "No single assistance type is best: actions that help reattempting the current question are not always best for future-question performance"
description: "No single assistance type is best: actions that help reattempting the current question are not always best for future-question performance"
id: no-single-best-assistance-type-tradeoff
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
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# No single assistance type is best: actions that help reattempting the current question are not always best for future-question performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across evaluated assistance actions, no single assistance type (e.g., hint, keyword definitions) is uniformly most effective, and actions benefiting current-question reattempts are not always best for future questions. [→ Schmucker 2025](#schmucker-2025)

## Evidence

### Schmucker 2025

Schmucker, R., Pachapurkar, N., Bala, S., Shah, M., & Mitchell, T. (2025). Learning to Optimize Feedback for One Million Students: Insights from Multi-Armed and Contextual Bandits in Large-Scale Online Tutoring. [doi:10.48550/arXiv.2508.00270](https://doi.org/10.48550/arXiv.2508.00270)

`q2 · i?` · `causal · r2`

Offline policy evaluation over 43,355 assistance actions from randomized log data in six science courses; the analysis finds "no single best assistance type" and a trade-off between current-question and future-question benefits.

> "Studying assistance actions selected by these policies, we find that there is no single best assistance type (e.g., hint, keyword definitions clarifying the question text). We further find that assistance actions that benefit students the most when reattempting the current question are not always best for promoting performance on future questions."

## Discussion


## Related Claims
- [Assistance actions exhibit heterogeneous treatment effects across students, but effect sizes are often too small for contextual bandit policies to significantly outperform well-optimized MAB policies](hte-exists-but-cb-gains-limited.md) — related
- [A per-question training-objective algorithm choosing between combined reward and low-variance reattempt correctness yields policies that improve both immediate and session-level outcomes](per-question-training-objective-algorithm.md) — related
- [Reattempt correctness correlates with end-of-session student ability (r = 0.27) but is mostly uncorrelated with next-question correctness (r = 0.04)](reattempt-correctness-correlates-ability-not-next-question.md) — related
- [The survey reports, citing Pavlik et al., that no single knowledge tracing model was always the best, and that a better model must consider multiple student features and the learning context.](no-single-knowledge-tracing-model-is-always-best.md) — a broader claim this one bears on
