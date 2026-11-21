---
type: claim
title: Bias-detection learning effects generalize to plain, unannotated news materials on new topics after visualizations are removed
description: Bias-detection learning effects generalize to plain, unannotated news materials on new topics after visualizations are removed
id: bias-training-generalizes-new-topics
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
    i: 1
    kind: causal
    rigour: 3
---

# Bias-detection learning effects generalize to plain, unannotated news materials on new topics after visualizations are removed

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r3` · `q3` · `i1`–`i2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i2` Classification accuracy improved from training to testing phase (η2part = 0.065), rejecting the no-generalization null hypothesis. [→ Spinde 2025](#spinde-2025)
`q3 i1` In Study 2, training with biased sentence labels improved identification of biased sentences in a test article on a new topic (η2part = 0.012). [→ Spinde 2025 (2)](#spinde-2025-2)

## Evidence

### Spinde 2025

Spinde, T., Wu, F., Gaissmaier, W., Demartini, G., & Giese, H. (2025). Enhancing Media Literacy: The Effectiveness of (Human) Annotations and Bias Visualizations on Bias Detection. [doi:10.1016/j.ipm.2025.104244](https://doi.org/10.1016/j.ipm.2025.104244)

`q3 · i2` · `causal · r3`

Experiment 1 mixed ANOVA phase effect on F1 accuracy, with a printed effect size of η2part = 0.065: test sentences were unmarked and drawn from topics different from training, so learning transferred "from the training to testing phase" after visualization removal.

> "classifications improved from the training to testing phase (F(467,1) = 32.38, p < .001, η2part = 0.065; Fig. 3), suggesting that Null Hypothesis 2 should also be rejected."

### Spinde 2025 (2)

Spinde, T., Wu, F., Gaissmaier, W., Demartini, G., & Giese, H. (2025). Enhancing Media Literacy: The Effectiveness of (Human) Annotations and Bias Visualizations on Bias Detection. [doi:10.1016/j.ipm.2025.104244](https://doi.org/10.1016/j.ipm.2025.104244)

`q3 · i1` · `causal · r3`

Study 2 between-subjects ANOVA (N = 846) on sentence-level F1 scores for annotating a neutral test article (James Webb telescope launch) after training on articles about other topics: the biased sentence label main effect was significant with a printed effect size of η2part = 0.012.

> "Overall, participants were better able to correctly identify biased sentences in the test phase, when they were trained with a biased sentence (F(834,2) = 5.58, p = .004, η2part = 0.012) and biased phrase labels (F(834,1) = 44.00, p < .001, η2part = 0.048)."

## Discussion


## Related Claims
- [Both Human-annotated and AI-generated bias labels improve news consumers' correct detection of media bias compared to an untrained control group](human-ai-bias-labels-improve-bias-detection.md) — related
- [Bias-detection accuracy rose from training to test among untrained control participants after mere exposure to rating study materials (d = 0.21)](mere-exposure-improves-bias-detection.md) — related
- [Phrase-level bias labels are the most effective visualization for training bias detection, and sentence labels only add value when no phrase labels are shown](phrase-labels-most-effective.md) — related
