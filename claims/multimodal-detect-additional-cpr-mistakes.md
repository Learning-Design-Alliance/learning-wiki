---
type: claim
title: "Multimodal data can detect additional CPR training mistakes not tracked by commercial manikins — locked arms and incorrect body weight — with over 93% accuracy"
description: "Multimodal data can detect additional CPR training mistakes not tracked by commercial manikins — locked arms and incorrect body weight — with over 93% accuracy"
id: multimodal-detect-additional-cpr-mistakes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-08
evidence_strength: moderate
newest_evidence: 2019
sources:
  - id: di-mitri-daniele-2019
    resource: "https://doi.org/10.3390/s19143099"
    title: "Di Mitri Daniele, Schneider Jan, Specht Marcus, Drachsler Hendrik. (2019). Detecting Mistakes in CPR Training with Multimodal Data and Neural Networks. Sensors (Basel, Switzerland). https://doi.org/10.3390/s19143099"
    author: Di Mitri Daniele, Schneider Jan, Specht Marcus, Drachsler Hendrik
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Multimodal data can detect additional CPR training mistakes not tracked by commercial manikins — locked arms and incorrect body weight — with over 93% accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` An LSTM classifier for armsLocked reached 93.4% test accuracy and one for bodyWeight reached 97.8%, with ROC AUC of 93.7% and 98.3% respectively, before overfitting. [→ Di Mitri Daniele 2019](#di-mitri-daniele-2019)

## Evidence

### Di Mitri Daniele 2019

Di Mitri Daniele, Schneider Jan, Specht Marcus, Drachsler Hendrik. (2019). Detecting Mistakes in CPR Training with Multimodal Data and Neural Networks. Sensors (Basel, Switzerland). https://doi.org/10.3390/s19143099

`q2 · i?` · `design · r3`

A dedicated dataset of 1107 CCs from five sessions in which one participant deliberately mimicked the two mistakes was used to train two LSTM networks for 100 iterations; the authors report the accuracy of manual annotation was higher because these errors "are easier to track with a depth camera".

> "Before the model starts overfitting, we achieved for armsLocked 93.4% accuracy and for bodyWeight 97.8% accuracy, as shown in Table 7. We also show for both target classes the Area Under the Receiver Operating Characteristic Curve (ROC AUC), obtaining 93.7% and 98.3%, respectively."

## Discussion


## Related Claims
- [Models trained on pooled data generalised across learners because CPR is standardised, but only while the experimental setup remains unchanged](generalisation-across-learners-requires-unchanged-setup.md) — related
- [Multimodal sensor data can classify standard CPR training mistakes on compression rate, depth and release with over 70% accuracy compared to a ResusciAnne manikin baseline](multimodal-data-detect-standard-cpr-mistakes.md) — related
- [The CPR Tutor architecture classifies a chest compression in about 70 milliseconds, supporting real-time feedback provision](cpr-tutor-real-time-classification-speed.md) — related
- [An expert dataset of 4803 annotated chest compressions from 10 experts was collected and downsampled to 3434 samples to train the mistake-detection models](cpr-tutor-expert-dataset-4803-ccs.md) — related
