---
type: claim
title: "Personalized calibration raises emotion recognition accuracy from 27.4% to 88.9% and improves robustness of classification"
description: "Personalized calibration raises emotion recognition accuracy from 27.4% to 88.9% and improves robustness of classification"
id: personalized-calibration-raises-accuracy-27-4-to-88-9
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

# Personalized calibration raises emotion recognition accuracy from 27.4% to 88.9% and improves robustness of classification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` An ablation study shows overall recognition accuracy improves from 27.4% to 88.9% with personalized calibration, with increased true positive rates across all emotions. [→ Kushan Choksi 2024](#kushan-choksi-2024)

## Evidence

### Kushan Choksi 2024

Kushan Choksi, Hongkai Chen, Karan Joshi, Sukrutha Jade, Shahriar Nirjon, and Shan Lin. (2024). SensEmo: Enabling Affective Learning through Real-time Emotion Recognition with Smartwatches. arXiv preprint. [doi:10.1109/mass62177.2024.00066](https://doi.org/10.1109/mass62177.2024.00066)

`q2 · i?` · `design · r2`

Ablation study comparing confusion matrices with and without personalized local min-max normalization of six physiological features. The article reports accuracy "improves from 27.4% to 88.9%" and observed unstable classification without calibration.

> "Additionally, the overall recognition accuracy improves from 27.4% to 88.9% with the implementation of personalized calibration."

## Discussion


## Related Claims
- [A Fine Gaussian SVM on personalized-calibrated smartwatch physiological features classifies four learning-related emotions with 88.9% accuracy, outperforming KNN at 75.2%](sensemoo-svm-88-9-emotion-accuracy.md) — possibly the same claim (merge candidate)
