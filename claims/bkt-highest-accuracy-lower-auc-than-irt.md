---
type: claim
title: Per-pitch BKT attains the highest accuracy, lowest BCE and lowest Brier score of the four model families, but lower AUC than IRT
description: Per-pitch BKT attains the highest accuracy, lowest BCE and lowest Brier score of the four model families, but lower AUC than IRT
id: bkt-highest-accuracy-lower-auc-than-irt
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
evidence_strength: moderate
sources:
  - id: wei-2026
    resource: "https://doi.org/10.3389/fpsyg.2026.1905847"
    title: "Wei, Wang and Dong. (2026). Cognitive and skill acquisition trajectories in school-based music education: evidence from Chinese classrooms. Frontiers in Psychology. https://doi.org/10.3389/fpsyg.2026.1905847"
    author: Wei, Wang and Dong
    q: 2
    i: "?"
---

# Per-pitch BKT attains the highest accuracy, lowest BCE and lowest Brier score of the four model families, but lower AUC than IRT

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` BKT achieved accuracy 0.7520, BCE 0.5528 and Brier 0.180, beating IRT on accuracy by 0.025, while its AUC of 0.653 was 0.019 below the IRT AUC. [→ Wei 2026](#wei-2026)

## Evidence

### Wei 2026

Wei, Wang and Dong. (2026). Cognitive and skill acquisition trajectories in school-based music education: evidence from Chinese classrooms. Frontiers in Psychology. https://doi.org/10.3389/fpsyg.2026.1905847

`q2 · i?`

Held-out evaluation (Table 3) on the identical 492,633-attempt test partition; BKT parameters were estimated per pitch by forward–backward expectation–maximization. Both pairwise differences had bootstrap intervals excluding zero.

> "The BKT model achieved the lowest test BCE [0.5528 (0.534, 0.574)], the highest accuracy [0.7520 (0.740, 0.763)] and the lowest Brier score [0.180 (0.174, 0.188)] of all four families, with an AUC of 0.653 [(0.642, 0.664)] that is lower than the IRT AUC"

## Discussion


## Related Claims
- [A one-parameter IRT model outperforms global and per-pitch baselines on AUC, BCE and Brier score but not on threshold accuracy for held-out singing attempts](irt-outperforms-baselines-discrimination-not-accuracy.md) — related
- [BKT is the most efficient knowledge tracing approach overall in simulated online mastery learning, though DKT is more efficient for AS and M problems](bkt-most-efficient-online-mastery-learning.md) — related
- [Low-register pitches are sung more accurately than high-register pitches in Chinese classrooms, reproducing register compression at scale](register-compression-singing-accuracy-chinese-classrooms.md) — related
