---
type: claim
title: A one-parameter IRT model outperforms global and per-pitch baselines on AUC, BCE and Brier score but not on threshold accuracy for held-out singing attempts
description: A one-parameter IRT model outperforms global and per-pitch baselines on AUC, BCE and Brier score but not on threshold accuracy for held-out singing attempts
id: irt-outperforms-baselines-discrimination-not-accuracy
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
    kind: associational
    rigour: 2
  - id: wei-2026-2
    resource: "https://doi.org/10.3389/fpsyg.2026.1905847"
    title: "Wei, Wang and Dong. (2026). Cognitive and skill acquisition trajectories in school-based music education: evidence from Chinese classrooms. Frontiers in Psychology. https://doi.org/10.3389/fpsyg.2026.1905847"
    author: Wei, Wang and Dong
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# A one-parameter IRT model outperforms global and per-pitch baselines on AUC, BCE and Brier score but not on threshold accuracy for held-out singing attempts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` The IRT model's AUC advantage over the global and per-pitch baselines was 0.172 and 0.131, with bootstrap confidence intervals excluding zero. [→ Wei 2026](#wei-2026)
`q2 i?` On threshold accuracy the IRT model (0.7252) did not beat the baselines (0.7305 and 0.7304), whose intervals overlap the IRT value. [→ Wei 2026 (2)](#wei-2026-2)

## Evidence

### Wei 2026

Wei, Wang and Dong. (2026). Cognitive and skill acquisition trajectories in school-based music education: evidence from Chinese classrooms. Frontiers in Psychology. https://doi.org/10.3389/fpsyg.2026.1905847

`q2 · i?` · `associational · r2`

Held-out evaluation (Table 3) of four model families on the identical 492,633-attempt test partition from an 80/20 within-sequence split, with 95% clustered bootstrap confidence intervals (1,000 replications). The IRT AUC was 0.673.

> "its AUC advantage over the global and per-pitch baselines was 0.172 [([0.160, 0.185)] and 0.131 [(0.118, 0.146)], respectively, and its BCE and Brier scores were lower than both, with all of these intervals excluding zero."

### Wei 2026 (2)

Wei, Wang and Dong. (2026). Cognitive and skill acquisition trajectories in school-based music education: evidence from Chinese classrooms. Frontiers in Psychology. https://doi.org/10.3389/fpsyg.2026.1905847

`q2 · i?` · `associational · r2`

Same held-out comparison, accuracy metric at the 0.5 threshold. The article explains baselines score highly on raw accuracy by predicting the majority correct class even though their AUC is at or near chance.

> "On threshold accuracy, however, the IRT model did not beat the baselines: its accuracy of 0.7252 was marginally below the global mean baseline (0.7305) and the per-pitch baseline (0.7304), whose accuracy confidence intervals overlap the IRT value."

## Discussion


## Related Claims
- [Per-pitch BKT attains the highest accuracy, lowest BCE and lowest Brier score of the four model families, but lower AUC than IRT](bkt-highest-accuracy-lower-auc-than-irt.md) — related
- [In Mnemosyne log data, item-specific difficulty parameters outperform a global difficulty for lower and higher Leitner decks, while global difficulty performs better for intermediate decks.](item-specific-difficulty-helps-only-at-low-and-high-leitner-decks.md) — related
- [Latent singing ability varies widely across learners, with sequence-level theta estimates spanning −3.79 to 3.36 logits](wide-latent-ability-spread-singing-learners.md) — related
- [Low-register pitches are sung more accurately than high-register pitches in Chinese classrooms, reproducing register compression at scale](register-compression-singing-accuracy-chinese-classrooms.md) — related
