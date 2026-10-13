---
type: research-method
id: multimodal-engagement-prediction-framework-with-perceiver-io-fusion-hierarchical-bayesian
title: Multimodal engagement-prediction framework with Perceiver IO fusion, hierarchical Bayesian participant context, and uncertainty-aware heads
description: "A computational framework that jointly predicts a continuous engagement score in [1,5] and a binary label from tutoring-video clips."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Multimodal engagement-prediction framework with Perceiver IO fusion, hierarchical Bayesian participant context, and uncertainty-aware heads

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 4 studies (3 design, 1 associational), `q2` · 1 of 4 report an effect size · 2 claims rest on one study

## Description
A computational framework that jointly predicts a continuous engagement score in [1,5] and a binary label from tutoring-video clips. It fuses pretrained encoders (V-JEPA 2 for student and instructor video, CLIP for screen content, AudioMAE for audio) with five explicit behavioral streams — "head pose, CWT head dynamics, facial action units, gaze/head angles, and emotion prediction probabilities" — through a Perceiver IO latent bottleneck. Student and instructor personalities are modeled as variational posteriors over learnable embeddings with partial pooling toward a shared prior, and evidential NIG regression and SNGP classification heads output predictions with explicit epistemic uncertainty.

## Accounts
<!-- How each source describes or uses the method -->
- **Multimodal engagement-prediction framework with Perceiver IO fusion, hierarchical Bayesian participant context, and uncertainty-aware heads**: A computational framework that jointly predicts a continuous engagement score in [1,5] and a binary label from tutoring-video clips. It fuses pretrained encoders (V-JEPA 2 for student and instructor video, CLIP for screen content, AudioMAE for audio) with five explicit behavioral streams — "head pose, CWT head dynamics, facial action units, gaze/head angles, and emotion prediction probabilities" — through a Perceiver IO latent bottleneck. Student and instructor personalities are modeled as variational posteriors over learnable embeddings with partial pooling toward a shared prior, and evidential NIG regression and SNGP classification heads output predictions with explicit epistemic uncertainty. (Mind the Student: Behavioral and Contextual Cues for Automated Engagement Prediction in On)

### Claims

- [The Bayesian context layer applies stronger posterior personalization to students with fewer training clips, correlating clip count with KL divergence from the prior (r=-0.748, p=0.001)](../claims/bayesian-context-kl-clip-count-correlation.md) [+M]
- [NIG-head predictive uncertainty is dominated by epistemic uncertainty and shows negligible correlation with the absolute engagement score (Pearson r 0.016 aleatoric, 0.025 epistemic)](../claims/epistemic-dominant-uncertainty-uncorrelated-with-engagement.md) [+M]
- [Between-student differences explain a large fraction of CASED label variance, limiting what any clip-level visual model can learn](../claims/between-student-label-variance-limits-clip-models.md) [+M]

## Related Research Methods
-

## Key Sources
- Alperen Kantarcı, Visvanathan Ramesh, and Gemma Roig. 2026. Mind the Student: Behavioral and Contextual Cues for Automated Engagement Prediction in Online Learning. ICMI '26, Napoli, Italy. https://doi.org/10.1145/3776574.3832485
