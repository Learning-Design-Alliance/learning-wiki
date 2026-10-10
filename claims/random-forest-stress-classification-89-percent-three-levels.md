---
type: claim
title: "A Random Forest classifier reached 89.09% test accuracy with 0.89 macro F1 across three stress-severity levels, exceeding an SVM comparison (88.48%) and a reported Random Forest benchmark (87.93%) on similar data"
description: "A Random Forest classifier reached 89.09% test accuracy with 0.89 macro F1 across three stress-severity levels, exceeding an SVM comparison (88.48%) and a reported Random Forest benchmark (87.93%) on similar data"
id: random-forest-stress-classification-89-percent-three-levels
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: muhammad-fahad-bashir-2026
    resource: "https://scholar.google.com/scholar?q=An+AI-Powered+Culturally+Aware+Chatbot+for+Stress+Detection+and+Wellness+Support+among+Pakistani+University+Students"
    title: "Muhammad Fahad Bashir, Muhammad Afzal. (2026). An AI-Powered Culturally Aware Chatbot for Stress Detection and Wellness Support among Pakistani University Students Using NLP and Machine Learning. https://scholar.google.com/scholar?q=An+AI-Powered+Culturally+Aware+Chatbot+for+Stress+Detection+and+Wellness+Support+among+Pakistani+University+Students"
    author: Muhammad Fahad Bashir, Muhammad Afzal
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: muhammad-fahad-bashir-2026-2
    resource: "https://scholar.google.com/scholar?q=An+AI-Powered+Culturally+Aware+Chatbot+for+Stress+Detection+and+Wellness+Support+among+Pakistani+University+Students"
    title: "Muhammad Fahad Bashir, Muhammad Afzal. (2026). An AI-Powered Culturally Aware Chatbot for Stress Detection and Wellness Support among Pakistani University Students Using NLP and Machine Learning. https://scholar.google.com/scholar?q=An+AI-Powered+Culturally+Aware+Chatbot+for+Stress+Detection+and+Wellness+Support+among+Pakistani+University+Students"
    author: Muhammad Fahad Bashir, Muhammad Afzal
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A Random Forest classifier reached 89.09% test accuracy with 0.89 macro F1 across three stress-severity levels, exceeding an SVM comparison (88.48%) and a reported Random Forest benchmark (87.93%) on similar data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` On a held-out test set, the Random Forest classifier obtained 89.09% accuracy and a macro F1-score of 0.89 over three stress categories, with class-level F1-scores of 0.87 (Low), 0.92 (Moderate) and 0.89 (High). [→ Muhammad Fahad Bashir 2026](#muhammad-fahad-bashir-2026)
`q2 i?` On the same data splits, Random Forest's 89.09% accuracy exceeded the Support Vector Machine comparison classifier's 88.48% and the 87.93% accuracy reported by Zahra et al. on a similar but smaller, less balanced student stress dataset. [→ Muhammad Fahad Bashir 2026 (2)](#muhammad-fahad-bashir-2026-2)

## Evidence

### Muhammad Fahad Bashir 2026

Muhammad Fahad Bashir, Muhammad Afzal. (2026). An AI-Powered Culturally Aware Chatbot for Stress Detection and Wellness Support among Pakistani University Students Using NLP and Machine Learning. https://scholar.google.com/scholar?q=An+AI-Powered+Culturally+Aware+Chatbot+for+Stress+Detection+and+Wellness+Support+among+Pakistani+University+Students

`q2 · i?` · `design · r2`

Classification evaluation in the Results section: a Random Forest model trained on the public 1100-response, 20-feature student stress survey was scored on a held-out test set. The article reports "an accuracy of 89.09%" with macro F1 0.89, and per-class F1-scores of 0.87, 0.92 and 0.89 for Low, Moderate and High stress.

> "The proposed Random Forest classifier obtained an accuracy of 89.09% and an F1 -score of 0.89 on the held-out test set with macro-average over all three stress categories."

### Muhammad Fahad Bashir 2026 (2)

Muhammad Fahad Bashir, Muhammad Afzal. (2026). An AI-Powered Culturally Aware Chatbot for Stress Detection and Wellness Support among Pakistani University Students Using NLP and Machine Learning. https://scholar.google.com/scholar?q=An+AI-Powered+Culturally+Aware+Chatbot+for+Stress+Detection+and+Wellness+Support+among+Pakistani+University+Students

`q2 · i?` · `design · r2`

Comparison reported in the Results section and its accuracy-comparison figure: the same-split SVM classifier reached 88.48% accuracy with macro F1 0.89, and the article states the proposed model "achieves higher accuracy than Zahra et al. [16] with 87.93% accuracy on Random Forest" on a similar dataset that "was not as large and balanced".

> "Test set accuracy comparison between Random Forest (89.09%), SVM (88.48%), and the benchmark result reported by Zahra et al. [16] (87.93%)."

## Discussion


## Related Claims
- [The classifier's dominant error was labelling Low Stress students as Moderate Stress, a bias the authors judge safe because over-assignment yields extra support while the dangerous high-as-low error was uncommon](confusion-matrix-low-to-moderate-misclassification-safe-direction.md) — related
- [Random Forest feature importance on the 20-feature student stress survey ranked blood pressure first (15.6%), teacher-student relationship second (10.0%) and sleep quality third (9.3%), with anxiety level only ninth (4.8%)](feature-importance-blood-pressure-teacher-relationship-top-stress-predictors.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — a broader claim this one bears on
- [Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021](nlp-la-algorithm-adoption-random-forest-to-deep-learning.md) — related
