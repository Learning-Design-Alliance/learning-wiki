---
type: research-method
id: post-hoc-probabilistic-affect-and-behaviour-detection-from-tutor-log-data
title: Post-hoc probabilistic affect and behaviour detection from tutor log data
description: "The article uses \"Affect and behaviour detectors\" that estimate student states \"based on post-hoc analysis of tutor log-data\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
---

# Post-hoc probabilistic affect and behaviour detection from tutor log data

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (1 causal, 1 associational), `q3` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The article uses "Affect and behaviour detectors" that estimate student states "based on post-hoc analysis of tutor log-data". For every student action in the tutor, the detectors output a probability that the student is bored, in engaged concentration, confused, or frustrated, plus the probability that the student is off-task or gaming. These per-action estimates supply the features for the study's correlational and predictive analyses.

## Accounts
<!-- How each source describes or uses the method -->
- **Automated affect and behaviour detectors estimating per-action probabilities of boredom, engaged concentration, confusion, frustration, off-task and gaming**: The article uses "Affect and behaviour detectors" that estimate student states "based on post-hoc analysis of tutor log-data". For every student action in the tutor, the detectors output a probability that the student is bored, in engaged concentration, confused, or frustrated, plus the probability that the student is off-task or gaming. These per-action estimates supply the features for the study's correlational and predictive analyses. (Pardos et al. (2014))
- **Machine-learned confrustion and gaming detectors built from Decimal Point gameplay logs**: The authors built affect and behavior detectors from student interaction logs in the Decimal Point game. They applied text replay coding to label 1,560 clips (irr κ = .74) and trained detectors on 23 interaction features (attempts, time spent, restart behavior). The confrustion detector used an XGBoost classifier (AUC ROC = .97, κ = .81) and the gaming detector a J-Rip classifier (AUC ROC = .85, κ = .62). (Bittencourt Ig Ibert et al. (2020))

### Claims
- [A unified model combining affect, disengaged behaviour, and in-system performance achieves high overall correlation to standardized exam scores](../claims/unified-affect-behavior-performance-model-predicts-exam-scores.md) [+M]
- [Confrustion is a significant negative predictor of posttest performance in a decimals learning game, even after controlling for pretest](../claims/confrustion-negative-predictor-posttest-decimals-game.md) [+M]
- [Gaming the system is a significant negative predictor of posttest performance in the decimals game, controlling for pretest](../claims/gaming-negative-predictor-posttest-decimals-game.md) [+M]

## Related Research Methods
-

## Key Sources
- Pardos, Z. A., Baker, R. S., San Pedro, M., Gowda, S. M., & Gowda, S. M. (2014). Affective States and State Tests: Investigating How Affect and Engagement during the School Year Predict End-of-Year Learning Outcomes. Journal of Learning Analytics, 1(1), 107-128. https://doi.org/10.18608/jla.2014.11.6
- Bittencourt Ig Ibert, Cukurova Mutlu, Muldner Kasia, Luckin Rose, Millán Eva, Mogessie Michael, Richey Elizabeth J., McLaren Bruce M., Andres-Bray Juan Miguel L., Baker Ryan S. (2020). Confrustion and Gaming While Learning with Erroneous Examples in a Decimals Game. Artificial Intelligence in Education. https://doi.org/10.1007/978-3-030-52240-7_38
