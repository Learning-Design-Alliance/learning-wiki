---
type: claim
title: Phrase-level bias labels are the most effective visualization for training bias detection, and sentence labels only add value when no phrase labels are shown
description: Phrase-level bias labels are the most effective visualization for training bias detection, and sentence labels only add value when no phrase labels are shown
id: phrase-labels-most-effective
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: spinde-2025
    resource: "https://doi.org/10.1016/j.ipm.2025.104244"
    title: "Spinde, T., Wu, F., Gaissmaier, W., Demartini, G., & Giese, H. (2025). Enhancing Media Literacy: The Effectiveness of (Human) Annotations and Bias Visualizations on Bias Detection. [doi:10.1016/j.ipm.2025.104244](https://doi.org/10.1016/j.ipm.2025.104244)"
    author: "Spinde, T., Wu, F., Gaissmaier, W., Demartini, G., & Giese, H."
    q: 3
    i: 2
    kind: causal
    rigour: 3
  - id: spinde-2025-2
    resource: "https://doi.org/10.1016/j.ipm.2025.104244"
    title: "Spinde, T., Wu, F., Gaissmaier, W., Demartini, G., & Giese, H. (2025). Enhancing Media Literacy: The Effectiveness of (Human) Annotations and Bias Visualizations on Bias Detection. [doi:10.1016/j.ipm.2025.104244](https://doi.org/10.1016/j.ipm.2025.104244)"
    author: "Spinde, T., Wu, F., Gaissmaier, W., Demartini, G., & Giese, H."
    q: 3
    i: 2
    kind: causal
    rigour: 3
---

# Phrase-level bias labels are the most effective visualization for training bias detection, and sentence labels only add value when no phrase labels are shown

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r3` · `q3` · `i2` medium
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i2` Biased phrase labeling reliably increased sentence-level F1 accuracy (η2part = 0.048), regardless of sentence labeling. [→ Spinde 2025](#spinde-2025)
`q3 i2` Simple and advanced biased sentence labels beat control only when no additional biased phrase labels were presented (d = 0.51 and d = 0.47 vs. d = 0.03 and d = 0.06). [→ Spinde 2025 (2)](#spinde-2025-2)

## Evidence

### Spinde 2025

Spinde, T., Wu, F., Gaissmaier, W., Demartini, G., & Giese, H. (2025). Enhancing Media Literacy: The Effectiveness of (Human) Annotations and Bias Visualizations on Bias Detection. [doi:10.1016/j.ipm.2025.104244](https://doi.org/10.1016/j.ipm.2025.104244)

`q3 · i2` · `causal · r3`

Study 2 ANOVA main effects on test-article F1 scores: biased phrase labels had the larger printed effect size (η2part = 0.048), and "biased phrase labeling always increased performance regardless of biased sentence labeling (all t(834) ≥ 2.22, all p ≥ .027, all d ≥ 0.26)."

> "participants were better able to correctly identify biased sentences in the test phase, when they were trained with a biased sentence (F(834,2) = 5.58, p = .004, η2part = 0.012) and biased phrase labels (F(834,1) = 44.00, p < .001, η2part = 0.048)."

### Spinde 2025 (2)

Spinde, T., Wu, F., Gaissmaier, W., Demartini, G., & Giese, H. (2025). Enhancing Media Literacy: The Effectiveness of (Human) Annotations and Bias Visualizations on Bias Detection. [doi:10.1016/j.ipm.2025.104244](https://doi.org/10.1016/j.ipm.2025.104244)

`q3 · i2` · `causal · r3`

Study 2 biased sentence × biased phrase interaction (F(834,2) = 4.16, p = .002, η2part = 0.01) with Bonferroni-corrected contrasts: with phrase labels absent, simple and advanced sentence labels beat control (d = 0.51 and d = 0.47); with phrase labels present the differences were d = 0.03 and d = 0.06 (both p = 1).

> "Simple and advanced biased sentence labels in the training phase were only superior in F1 accuracy compared to control, when no additional biased phrase labels were presented"

## Discussion


## Related Claims
- [Bias-detection learning effects generalize to plain, unannotated news materials on new topics after visualizations are removed](bias-training-generalizes-new-topics.md) — related
- [Both Human-annotated and AI-generated bias labels improve news consumers' correct detection of media bias compared to an untrained control group](human-ai-bias-labels-improve-bias-detection.md) — related
- [Politicized phrase labels decrease sentence-level bias detection accuracy but help participants identify the more biased of two training articles](politicized-labels-reduce-detection.md) — reports the opposite
