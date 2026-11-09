---
type: claim
title: Models trained on pooled data generalised across learners because CPR is standardised, but only while the experimental setup remains unchanged
description: Models trained on pooled data generalised across learners because CPR is standardised, but only while the experimental setup remains unchanged
id: generalisation-across-learners-requires-unchanged-setup
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-08
evidence_strength: weak
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

# Models trained on pooled data generalised across learners because CPR is standardised, but only while the experimental setup remains unchanged

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All manikin-tracked mistake classifiers generalised across different users, since individual differences appear not to hold strong influence for standardised, repetitive CPR movements. [→ Di Mitri Daniele 2019](#di-mitri-daniele-2019)
`q2 i?` Generalisation holds only when the setup is unchanged; moving the Kinect or altering the sensor set produces different features and makes generalising more difficult. [→ Di Mitri Daniele 2019](#di-mitri-daniele-2019)

## Evidence

### Di Mitri Daniele 2019

Di Mitri Daniele, Schneider Jan, Specht Marcus, Drachsler Hendrik. (2019). Detecting Mistakes in CPR Training with Multimodal Data and Neural Networks. Sensors (Basel, Switzerland). https://doi.org/10.3390/s19143099

`q2 · i?` · `design · r2`

Authors' interpretation in the Discussion of the pooled-training design: training per individual would have used around 400 data points instead of 5200, risking higher accuracy but also overfitting. This is a stated interpretation, not a tested comparison.

> "In general, as CPR is a standard procedure that requires the same and repetitive movements, the individual differences do not seem to hold a strong influence for the classifiers. This condition, however, applies only when the experimental setup is unchanged."

## Discussion


## Related Claims
- [Multimodal data can detect additional CPR training mistakes not tracked by commercial manikins — locked arms and incorrect body weight — with over 93% accuracy](multimodal-detect-additional-cpr-mistakes.md) — related
- [Multimodal sensor data can classify standard CPR training mistakes on compression rate, depth and release with over 70% accuracy compared to a ResusciAnne manikin baseline](multimodal-data-detect-standard-cpr-mistakes.md) — related
- [Sessions with CPR Tutor feedback showed no significant difference in overall mistake frequency compared with control sessions without feedback](cpr-tutor-no-overall-mistake-frequency-reduction.md) — related
- [An expert dataset of 4803 annotated chest compressions from 10 experts was collected and downsampled to 3434 samples to train the mistake-detection models](cpr-tutor-expert-dataset-4803-ccs.md) — related
- [The CPR Tutor architecture classifies a chest compression in about 70 milliseconds, supporting real-time feedback provision](cpr-tutor-real-time-classification-speed.md) — related
