---
type: claim
title: "A Fine Gaussian SVM on personalized-calibrated smartwatch physiological features classifies four learning-related emotions with 88.9% accuracy, outperforming KNN at 75.2%"
description: "A Fine Gaussian SVM on personalized-calibrated smartwatch physiological features classifies four learning-related emotions with 88.9% accuracy, outperforming KNN at 75.2%"
id: sensemoo-svm-88-9-emotion-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: kushan-choksi-2024
    resource: "https://doi.org/10.1109/mass62177.2024.00066"
    title: "Kushan Choksi, Hongkai Chen, Karan Joshi, Sukrutha Jade, Shahriar Nirjon, and Shan Lin. (2024). SensEmo: Enabling Affective Learning through Real-time Emotion Recognition with Smartwatches. arXiv preprint. [doi:10.1109/mass62177.2024.00066](https://doi.org/10.1109/mass62177.2024.00066)"
    author: Kushan Choksi, Hongkai Chen, Karan Joshi, Sukrutha Jade, Shahriar Nirjon, and Shan Lin
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A Fine Gaussian SVM on personalized-calibrated smartwatch physiological features classifies four learning-related emotions with 88.9% accuracy, outperforming KNN at 75.2%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A Fine Gaussian SVM trained on calibrated physiological features achieves 88.9% overall emotion classification accuracy under 10-fold cross-validation, versus 75.2% for KNN. [→ Kushan Choksi 2024](#kushan-choksi-2024)

## Evidence

### Kushan Choksi 2024

Kushan Choksi, Hongkai Chen, Karan Joshi, Sukrutha Jade, Shahriar Nirjon, and Shan Lin. (2024). SensEmo: Enabling Affective Learning through Real-time Emotion Recognition with Smartwatches. arXiv preprint. [doi:10.1109/mass62177.2024.00066](https://doi.org/10.1109/mass62177.2024.00066)

`q2 · i?` · `design · r2`

Evaluation with 22 graduate students viewing IAPS images; physiological data from Microsoft Band 2 smartwatches, 70:15:15 train/validation/test split, 10-fold cross-validation. The article reports the Fine Gaussian SVM "achieves an overall accuracy of 88.9%" versus KNN's 75.2%.

> "The experimental findings indicate that the Fine Gaussian SVM achieves an overall accuracy of 88.9%. In comparison, the k-nearest neighbors algorithm (KNN) yields an accuracy of 75.2%."

## Discussion


## Related Claims
- [Personalized calibration raises emotion recognition accuracy from 27.4% to 88.9% and improves robustness of classification](personalized-calibration-raises-accuracy-27-4-to-88-9.md) — possibly the same claim (merge candidate)
- [In an online learning experiment, students using SensEmo scored 40.0% higher on comprehension quizzes than students without it](sensemoo-online-quiz-40-percent-higher.md) — related
- [Log-file features are suitable for recognising perceived task-difficulty per task, with SVM the best single classifier (25.24% average test error).](svm-best-single-classifier-task-difficulty.md) — related
