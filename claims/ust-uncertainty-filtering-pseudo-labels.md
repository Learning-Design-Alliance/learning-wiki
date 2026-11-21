---
type: claim
title: MC-dropout uncertainty estimates separate reliable from unreliable pseudo-labels, and balanced low-uncertainty sampling best matches the target score distribution
description: MC-dropout uncertainty estimates separate reliable from unreliable pseudo-labels, and balanced low-uncertainty sampling best matches the target score distribution
id: ust-uncertainty-filtering-pseudo-labels
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: hongseok-choi-2026
    resource: "https://doi.org/10.1109/ACCESS.2026.3718177"
    title: "Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177"
    author: Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: hongseok-choi-2026-2
    resource: "https://doi.org/10.1109/ACCESS.2026.3718177"
    title: "Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177"
    author: Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# MC-dropout uncertainty estimates separate reliable from unreliable pseudo-labels, and balanced low-uncertainty sampling best matches the target score distribution

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` The 256 most uncertain samples yield much lower QWK than the 256 least uncertain and balanced-low samples, both of which exceed the full-set QWK. [→ Hongseok Choi 2026](#hongseok-choi-2026)
`q3 i?` At dr = 0.1 and nr = 0.1, the QWK gap between Bal-256 and Top-256 is about 0.28 for MC-dropout and 0.24 for embedding noise; both estimators are largely insensitive to hyperparameters over [0.05, 0.2]. [→ Hongseok Choi 2026 (2)](#hongseok-choi-2026-2)

## Evidence

### Hongseok Choi 2026

Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177

`q3 · i?` · `causal · r2`

Analysis of the uncertainty estimate at T = 10 on ASAP++ (Fig. 5), comparing MC-dropout and embedding-noise estimators across four subsets of the unlabeled set (Top-256, Bot-256, Bal-256, All).

> "The uncertainty estimate clearly separates reliable from unreliable predictions: Top-256 yields a much lower QWK than Bot-256 and Bal-256, both of which exceed the full-set QWK."

### Hongseok Choi 2026 (2)

Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177

`q3 · i?` · `causal · r2`

The article adds that although Bot-256 attains QWK comparable to Bal-256, the balanced subset's score-distribution entropy is closer to the full set, so its pseudo-labels better match the target distribution for self-training.

> "at dr = 0.1 and nr = 0.1, the QWK gap between Bal-256 and Top-256 is about 0.28 for MC-dropout and 0.24 for embedding noise."

## Discussion


## Related Claims
-
