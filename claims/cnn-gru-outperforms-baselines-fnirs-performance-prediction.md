---
type: claim
title: A hybrid CNN-GRU deep learning model outperforms traditional machine learning and standalone deep models in predicting quiz performance from fNIRS signals
description: A hybrid CNN-GRU deep learning model outperforms traditional machine learning and standalone deep models in predicting quiz performance from fNIRS signals
id: cnn-gru-outperforms-baselines-fnirs-performance-prediction
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
---

# A hybrid CNN-GRU deep learning model outperforms traditional machine learning and standalone deep models in predicting quiz performance from fNIRS signals

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The hybrid CNN-GRU model achieved the highest accuracy (73.08%) and F1 score (82.05%) among all compared models for binary classification of quiz responses from fNIRS data. [→ Shayla Sharmin and Roghayeh Leila Barmaki 2025](#shayla-sharmin-and-roghayeh-leila-barmaki-2025)

## Evidence

### Shayla Sharmin and Roghayeh Leila Barmaki 2025

Shayla Sharmin and Roghayeh Leila Barmaki. 2025. Hybrid Deep Learning Model to Estimate Cognitive Effort from fNIRS Signals. Companion Proceedings of the 27th International Conference on Multimodal Interaction (ICMI Companion '25). https://doi.org/10.1145/3747327.3764901

`q2 · i?` · `design · r2`

Model-comparison experiment on a participant-wise split (13 train, 3 test participants) of fNIRS data from an educational quiz game. The results section reports the hybrid model "outperformed all baseline models" with accuracy 73.08% and F1 82.05%.

> "Our proposed hybrid model, CNN-GRU, outperformed all baseline models. It achieved an accuracy of 73.08%, with a remarkable F1 score of 82.05%, demonstrating excellent performance in balancing precision (74%) and recall (91.18%)."

## Discussion


## Related Claims
- [Traditional machine learning models show mixed results predicting quiz performance from fNIRS, with Random Forest achieving the highest recall and Neural Network and LightGBM the lowest test accuracy](traditional-ml-mixed-fnirs-quiz-prediction.md) — related
- [XGBoost accuracy improves when trained on deep-learned representations, with CNN-GRU features yielding the highest XGBoost accuracy](deep-features-improve-xgboost-fnirs.md) — related
- [The DMO-GRU model achieves the best classification results among the compared models, with 91.2% accuracy, 90.8% F1-score, 90.1% precision and 92.5% recall](dmo-gru-best-classification-results.md) — reports the opposite
- [DMO-GRU trains faster than the deep learning baselines, with a 98 s training time versus 150 s for CNN-GRU and 138 s for LSTM](dmo-gru-faster-training-time.md) — related
- [Deep learning models (LSTM, GRU, transformer) achieve high and comparable accuracy (0.90–0.93) on physiological exam-outcome prediction](deep-learning-models-comparable-accuracy-physiological-exam-prediction.md) — related
- [Random forest achieves the highest mean test accuracy (0.9590) of all models compared for predicting exam grade categories from physiological signals](random-forest-highest-accuracy-physiological-exam-prediction.md) — reports the opposite
