---
type: claim
title: Hidden Markov Model analysis reveals that personalized and random short videos induce qualitatively different latent event structures during subsequent encoding
description: Hidden Markov Model analysis reveals that personalized and random short videos induce qualitatively different latent event structures during subsequent encoding
id: hmm-latent-event-structure-personalized-vs-random
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
sources:
  - id: li-2025
    resource: "https://doi.org/10.1038/s41539-025-00378-3"
    title: "Li, H., Li, J., Hao, X., & Liu, W. (2025). Behavioral and eye-tracking investigation of event segmentation following short video watching. npj Science of Learning. https://doi.org/10.1038/s41539-025-00378-3"
    author: "Li, H., Li, J., Hao, X., & Liu, W."
    q: 3
    i: 3
    kind: causal
    rigour: 2
  - id: li-2025-2
    resource: "https://doi.org/10.1038/s41539-025-00378-3"
    title: "Li, H., Li, J., Hao, X., & Liu, W. (2025). Behavioral and eye-tracking investigation of event segmentation following short video watching. npj Science of Learning. https://doi.org/10.1038/s41539-025-00378-3"
    author: "Li, H., Li, J., Hao, X., & Liu, W."
    q: 3
    i: 3
    kind: causal
    rigour: 2
---

# Hidden Markov Model analysis reveals that personalized and random short videos induce qualitatively different latent event structures during subsequent encoding

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3` · `i3` large

## Subclaims
`q3 i3` The Short-Personalized group showed significantly lower optimal K values (fewer latent events) than the Short-Random group (d = -1.29), contrary to the initial hypothesis. [→ Li 2025](#li-2025)
`q3 i3` Higher optimal K (more fragmented segmentation) negatively predicted detail recall (r = -0.42, p < 0.001). [→ Li 2025 (2)](#li-2025-2)

## Evidence

### Li 2025

Li, H., Li, J., Hao, X., & Liu, W. (2025). Behavioral and eye-tracking investigation of event segmentation following short video watching. npj Science of Learning. https://doi.org/10.1038/s41539-025-00378-3

`q3 · i3` · `causal · r2`

Study 1 HMM analysis with leave-one-subject-out cross-validation on eye-tracking time series (pupil diameter, gaze coordinates). One-way ANOVA on optimal K showed a significant Group effect (F = 7.26, p < 0.001, ηp² = 0.179); the quoted Tukey contrast was the only significant pairwise difference.

> "the Short-P group exhibited signiﬁcantly lower optimal K values compared to the Short-R group (mean difference = −1.93, 95% CI [ −3.00, −0.85], p < 0.001, Cohen’sd = −1.29, 95% CI [ −2.08, −0.51])."

### Li 2025 (2)

Li, H., Li, J., Hao, X., & Liu, W. (2025). Behavioral and eye-tracking investigation of event segmentation following short video watching. npj Science of Learning. https://doi.org/10.1038/s41539-025-00378-3

`q3 · i3` · `causal · r2`

Cognitive-relevance analysis of the HMM-derived optimal K across Study 1 participants. K was not linked to the number of events recalled (F = 0.23, p = 0.87) but negatively predicted the detail score, supporting the interpretation that more fragmented segmentation accompanies poorer detail memory.

> "A linear correlation analysis revealed that the optimal K value negatively predicted the detail score (r = −0.42, p <0 . 0 0 1 ) ."

## Discussion


## Related Claims
- [Eye-tracking findings survive correction for low-level stimulus confounds (luminance, motion energy, audio volume)](eye-tracking-findings-robust-low-level-confounds.md) — related
- [Random short video watching attenuates eye-movement synchronization (ISC) at event boundaries during subsequent movie encoding](random-short-video-reduces-boundary-isc.md) — related
- [Acute exposure to randomly selected short videos, combined with habitual daily viewing, is associated with poorer memory for continuous movies](random-short-video-impairs-continuous-memory.md) — related
- [Short-video exposure does not impair memory encoding of static pictures (Study 2 null result)](short-video-no-effect-static-picture-encoding.md) — related
