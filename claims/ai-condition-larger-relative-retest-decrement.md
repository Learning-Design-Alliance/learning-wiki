---
type: claim
title: Tasks first learned with the AI teammate showed a larger retest performance drop relative to initial team performance, while absolute retest performance did not differ significantly
description: Tasks first learned with the AI teammate showed a larger retest performance drop relative to initial team performance, while absolute retest performance did not differ significantly
id: ai-condition-larger-relative-retest-decrement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: mixed
newest_evidence: 2026
sources:
  - id: gardella-2026
    resource: "https://doi.org/10.1145/3765964.3811664"
    title: "Gardella, N., Prather, J., Leinonen, J., Denny, P., Pettit, R., & Riggs, S. L. (2026). Fast and Forgettable: A Controlled Study of Novices' Performance, Learning, Workload, and Emotion in AI-Assisted and Human Pair Programming Paradigms. [doi:10.1145/3765964.3811664](https://doi.org/10.1145/3765964.3811664)"
    author: "Gardella, N., Prather, J., Leinonen, J., Denny, P., Pettit, R., & Riggs, S. L."
    q: 3
    i: 3
    kind: causal
    rigour: 2
  - id: gardella-2026-2
    resource: "https://doi.org/10.1145/3765964.3811664"
    title: "Gardella, N., Prather, J., Leinonen, J., Denny, P., Pettit, R., & Riggs, S. L. (2026). Fast and Forgettable: A Controlled Study of Novices' Performance, Learning, Workload, and Emotion in AI-Assisted and Human Pair Programming Paradigms. [doi:10.1145/3765964.3811664](https://doi.org/10.1145/3765964.3811664)"
    author: "Gardella, N., Prather, J., Leinonen, J., Denny, P., Pettit, R., & Riggs, S. L."
    q: 3
    i: 1
    kind: causal
    rigour: 2
---

# Tasks first learned with the AI teammate showed a larger retest performance drop relative to initial team performance, while absolute retest performance did not differ significantly

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3` · `i1`–`i3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i3` Relative retest performance change (Session 2 minus Session 1) was worse for the AI condition, marginally significant after adjustment (g = -1.13). [→ Gardella 2026](#gardella-2026)
`q3 i1` Absolute retest performance was not significantly different between conditions (g = -0.27, p_adj = .529). [→ Gardella 2026 (2)](#gardella-2026-2)

## Evidence

### Gardella 2026

Gardella, N., Prather, J., Leinonen, J., Denny, P., Pettit, R., & Riggs, S. L. (2026). Fast and Forgettable: A Controlled Study of Novices' Performance, Learning, Workload, and Emotion in AI-Assisted and Human Pair Programming Paradigms. [doi:10.1145/3765964.3811664](https://doi.org/10.1145/3765964.3811664)

`q3 · i3` · `causal · r2`

Regression on retest performance change in the one-week solo retention test. The AI condition dropped roughly 19 points of 100 further than the human condition; the printed effect size is "-1.13" with p = .015 but adjusted p = .054, i.e. marginally significant.

> "Retest Performance Change (Session 2 - Session 1) Constant -2.65 6.03 -15.74 10.34 Session 1 Teammate = AI -18.88 6.33 -32.87 -5.01.015.054 -1.13"

### Gardella 2026 (2)

Gardella, N., Prather, J., Leinonen, J., Denny, P., Pettit, R., & Riggs, S. L. (2026). Fast and Forgettable: A Controlled Study of Novices' Performance, Learning, Workload, and Emotion in AI-Assisted and Human Pair Programming Paradigms. [doi:10.1145/3765964.3811664](https://doi.org/10.1145/3765964.3811664)

`q3 · i1` · `causal · r2`

Regression on absolute Session 2 solo retest scores. The AI-condition coefficient was -4.79 points, not statistically significant (p_adj = .529), with printed effect size "-0.27"; equivalence was not tested.

> "Absolute Retest Performance (Session 2) Constant 71.65 5.58 59.40 83.81 Session 1 Teammate = AI -4.79 5.58 -16.86 7.46 .397 .529 -0.27"

## Discussion


## Related Claims
- [Stronger teammates showed a marginally significant absolute retest decrement for AI-learned tasks, while weaker teammates' decrement was not significant](stronger-teammates-retest-decrement-ai-tasks.md) — related
- [Two-person teams scored significantly higher on timed Python tasks when the teammate was the AI (Copilot) rather than a human, with a large effect](ai-teammate-higher-team-performance-score.md) — related
- [Participants' self-grades of their own team performance did not differ significantly between the AI-teammate and human-teammate conditions](self-grade-no-significant-condition-difference.md) — related
