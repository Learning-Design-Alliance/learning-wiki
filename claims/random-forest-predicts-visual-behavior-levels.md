---
type: claim
title: "Random Forest most accurately predicts novices' visual behavior levels from CV-DL-extracted metrics, with fixation rates on objects and tool speed as key predictors"
description: "Random Forest most accurately predicts novices' visual behavior levels from CV-DL-extracted metrics, with fixation rates on objects and tool speed as key predictors"
id: random-forest-predicts-visual-behavior-levels
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: khanfar-aseel-f-2025
    resource: "https://doi.org/10.1007/s00464-025-12369-x"
    title: "Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett. (2025). From gaze to proficiency: deep learning-driven prediction of novice performance in laparoscopic training using AOI-dependent metrics. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12369-x"
    author: Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: khanfar-aseel-f-2025-2
    resource: "https://doi.org/10.1007/s00464-025-12369-x"
    title: "Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett. (2025). From gaze to proficiency: deep learning-driven prediction of novice performance in laparoscopic training using AOI-dependent metrics. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12369-x"
    author: Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Random Forest most accurately predicts novices' visual behavior levels from CV-DL-extracted metrics, with fixation rates on objects and tool speed as key predictors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Random Forest achieved the highest accuracy (83.33%) and F1-score (0.8333) among four ML classifiers under LOOCV. [→ Khanfar Aseel F. 2025](#khanfar-aseel-f-2025)
`q2 i?` Gini importance identified fixation rates on objects and tool speed as the most influential predictors of visual behavior levels. [→ Khanfar Aseel F. 2025 (2)](#khanfar-aseel-f-2025-2)

## Evidence

### Khanfar Aseel F. 2025

Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett. (2025). From gaze to proficiency: deep learning-driven prediction of novice performance in laparoscopic training using AOI-dependent metrics. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12369-x

`q2 · i?` · `associational · r1`

Four ML classifiers (RF, SVM, CART, ANN) were trained on CV-DL-extracted metrics with leave-one-out cross-validation to predict the clustered visual behavior levels of 18 novices. RF achieved the highest accuracy (83.33%) and F1-score (0.8333).

> "The results showed that RF achieved the highest accuracy and F1-score (83.33%, 0.8333, respectively) in predicting novices' visual behavior levels, followed by ANNs (79.16%, 0.7647), SVM (75%, 0.6554), and CART (70.83%, 0.5132), with the least accuracy and F1-score."

### Khanfar Aseel F. 2025 (2)

Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett. (2025). From gaze to proficiency: deep learning-driven prediction of novice performance in laparoscopic training using AOI-dependent metrics. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12369-x

`q2 · i?` · `associational · r1`

Gini (impurity) importance was computed in the Random Forest model to rank predictor significance (Fig. 11). Fixation rates on objects and tool speed ranked highest; fixation rates on tools and object-two-tools interaction ranked lowest.

> "As shown in Fig. 11, fixation rates on objects and tool speed were the most influential features for predicting visual behavior levels, followed by fixation rates on not-moving objects and fixation rates on object-one-tool interaction."

## Discussion


## Related Claims
- [AOI-dependent eye-tracking and motion metrics classify novices into High and Mid-Low skill levels during early-stage peg transfer training](aoi-metrics-classify-novice-skill-levels-early-training.md) — related
- [More-skilled novices fixate more on objects and less on tools, with slower tool speed, than less-skilled novices](skilled-novices-object-fixation-pattern.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — a broader claim this one bears on
- [Random forest achieves the highest mean test accuracy (0.9590) of all models compared for predicting exam grade categories from physiological signals](random-forest-highest-accuracy-physiological-exam-prediction.md) — related
- [Fixation on not-moving objects was lower for more-skilled novices, contradicting the expected looking-ahead pattern](not-moving-object-fixation-contradicts-hypothesis.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — a broader claim this one bears on
