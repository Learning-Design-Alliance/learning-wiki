---
type: claim
title: "Multimodal sensor data can classify standard CPR training mistakes on compression rate, depth and release with over 70% accuracy compared to a ResusciAnne manikin baseline"
description: "Multimodal sensor data can classify standard CPR training mistakes on compression rate, depth and release with over 70% accuracy compared to a ResusciAnne manikin baseline"
id: multimodal-data-detect-standard-cpr-mistakes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-08
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: di-mitri-daniele-2019
    resource: "https://doi.org/10.3390/s19143099"
    title: "Di Mitri Daniele, Schneider Jan, Specht Marcus, Drachsler Hendrik. (2019). Detecting Mistakes in CPR Training with Multimodal Data and Neural Networks. Sensors (Basel, Switzerland). https://doi.org/10.3390/s19143099"
    author: Di Mitri Daniele, Schneider Jan, Specht Marcus, Drachsler Hendrik
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Multimodal sensor data can classify standard CPR training mistakes on compression rate, depth and release with over 70% accuracy compared to a ResusciAnne manikin baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` LSTM classifiers trained on multimodal data reached a test accuracy of 86.5% for classRate, 73.9% for classRelease and 71.8% for classDepth before overfitting, validating multimodal mistake detection against the manikin baseline. [→ Di Mitri Daniele 2019](#di-mitri-daniele-2019)
`q2 i?` All three classifiers reached accuracy above 70% before the overfitting point, with classRate most accurate. [→ Di Mitri Daniele 2019](#di-mitri-daniele-2019)

## Evidence

### Di Mitri Daniele 2019

Di Mitri Daniele, Schneider Jan, Specht Marcus, Drachsler Hendrik. (2019). Detecting Mistakes in CPR Training with Multimodal Data and Neural Networks. Sensors (Basel, Switzerland). https://doi.org/10.3390/s19143099

`q2 · i?` · `design · r2`

A quantitative observational study with 11 medical students performing 22 two-minute CC sessions (5254 labelled compressions) trained Keras LSTM networks on a (5254×8×41) tensor; Table 6 reports test accuracy of 0.8650 for classRate, 0.7391 for classRelease and 0.7180 for classDepth, with the authors noting depth-camera and Myo accelerometer features "can track temporal-related features".

> "With an accuracy of 86.5%, classRate is the best-classified target. A plausible explanation is that the depth-camera sensors, as well as the accelerometer embedded in the Myo, can track temporal-related features such as the acceleration in doing the compression."

## Discussion


## Related Claims
- [Models trained on pooled data generalised across learners because CPR is standardised, but only while the experimental setup remains unchanged](generalisation-across-learners-requires-unchanged-setup.md) — related
- [Individual participants made only one type of mistake per indicator, so data from multiple participants is needed to cover the full range of mistakes](individual-mistake-distribution-not-representative.md) — related
- [Multimodal data can detect additional CPR training mistakes not tracked by commercial manikins — locked arms and incorrect body weight — with over 93% accuracy](multimodal-detect-additional-cpr-mistakes.md) — related
- [An expert dataset of 4803 annotated chest compressions from 10 experts was collected and downsampled to 3434 samples to train the mistake-detection models](cpr-tutor-expert-dataset-4803-ccs.md) — related
