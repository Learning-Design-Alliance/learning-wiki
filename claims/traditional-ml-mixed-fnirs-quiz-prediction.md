---
type: claim
title: Traditional machine learning models show mixed results predicting quiz performance from fNIRS, with Random Forest achieving the highest recall and Neural Network and LightGBM the lowest test accuracy
description: Traditional machine learning models show mixed results predicting quiz performance from fNIRS, with Random Forest achieving the highest recall and Neural Network and LightGBM the lowest test accuracy
id: traditional-ml-mixed-fnirs-quiz-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
sources:
  - id: shayla-sharmin-and-roghayeh-leila-barmaki-2025
    title: Shayla Sharmin and Roghayeh Leila Barmaki 2025
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: shayla-sharmin-and-roghayeh-leila-barmaki-2025-2
    title: Shayla Sharmin and Roghayeh Leila Barmaki 2025 (2)
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Traditional machine learning models show mixed results predicting quiz performance from fNIRS, with Random Forest achieving the highest recall and Neural Network and LightGBM the lowest test accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 associational `r1`, 1 design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Random Forest achieved the highest recall (0.92) and F1-score (0.77) among traditional ML models under 5-fold cross-validation. [→ Shayla Sharmin and Roghayeh Leila Barmaki 2025](#shayla-sharmin-and-roghayeh-leila-barmaki-2025)
`q2 i?` Neural Network and LightGBM showed poor generalization with the lowest test accuracy values (0.65 and 0.54, respectively). [→ Shayla Sharmin and Roghayeh Leila Barmaki 2025 (2)](#shayla-sharmin-and-roghayeh-leila-barmaki-2025-2)

## Evidence

### Shayla Sharmin and Roghayeh Leila Barmaki 2025

Shayla Sharmin and Roghayeh Leila Barmaki. 2025. Hybrid Deep Learning Model to Estimate Cognitive Effort from fNIRS Signals. Companion Proceedings of the 27th International Conference on Multimodal Interaction (ICMI Companion '25). https://doi.org/10.1145/3747327.3764901

`q2 · i?` · `design · r2`

Evaluation of traditional ML algorithms on the fNIRS quiz dataset using 5-fold cross-validation (Table 2). The results section reports Random Forest "achieved the highest recall (0.92) and F1-score (0.77)".

> "The Random Forest model achieved the highest recall (0.92) and F1-score (0.77). SVM and XGBoost also demonstrated strong recall values (0.82and0 .80, respectively), with SVM achieving an F1-score of0 .73."

### Shayla Sharmin and Roghayeh Leila Barmaki 2025 (2)

Shayla Sharmin and Roghayeh Leila Barmaki. 2025. Hybrid Deep Learning Model to Estimate Cognitive Effort from fNIRS Signals. Companion Proceedings of the 27th International Conference on Multimodal Interaction (ICMI Companion '25). https://doi.org/10.1145/3747327.3764901

`q2 · i?` · `associational · r1`

Same 5-fold cross-validated ML comparison (Table 2). The results section reports Neural Network and LightGBM "showed poor generalization with the lowest test accuracy values (0.65and0 .54, respectively)".

> "However, Neural Network and LightGBM showed poor generalization with the lowest test accuracy values (0.65and0 .54, respectively)."

## Discussion


## Related Claims
- [A hybrid CNN-GRU deep learning model outperforms traditional machine learning and standalone deep models in predicting quiz performance from fNIRS signals](cnn-gru-outperforms-baselines-fnirs-performance-prediction.md) — related
- [Deep learning models (LSTM, GRU, transformer) achieve high and comparable accuracy (0.90–0.93) on physiological exam-outcome prediction](deep-learning-models-comparable-accuracy-physiological-exam-prediction.md) — related
