---
type: claim
title: The CPR Tutor architecture classifies a chest compression in about 70 milliseconds, supporting real-time feedback provision
description: The CPR Tutor architecture classifies a chest compression in about 70 milliseconds, supporting real-time feedback provision
id: cpr-tutor-real-time-classification-speed
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2022
sources:
  - id: di-mitri-2022
    resource: "https://doi.org/10.1007/s40593-021-00281-z"
    title: "Di Mitri, D., Schneider, J., & Drachsler, H. (2022). KeepMeInTheLoop: Real-Time Feedback with Multimodal Data. International Journal of Artificial Intelligence in Education (2022) 32:1093–1118. https://doi.org/10.1007/s40593-021-00281-z"
    author: "Di Mitri, D., Schneider, J., & Drachsler, H."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The CPR Tutor architecture classifies a chest compression in about 70 milliseconds, supporting real-time feedback provision

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` SharpFlow classified one chest compression in about 70 milliseconds on average, and the authors report the architecture allowed provision of real-time multimodal feedback (H1). [→ Di Mitri 2022](#di-mitri-2022)

## Evidence

### Di Mitri 2022

Di Mitri, D., Schneider, J., & Drachsler, H. (2022). KeepMeInTheLoop: Real-Time Feedback with Multimodal Data. International Journal of Artificial Intelligence in Education (2022) 32:1093–1118. https://doi.org/10.1007/s40593-021-00281-z

`q2 · i?` · `design · r2`

In the real-time exploitation phase, the SharpFlow Python TCP server resampled incoming data chunks and fed them to the layered LSTMs; the article reports that "SharpFlow takes on average 70 milliseconds to classify one CC".

> "SharpFlow takes on average 70 milliseconds to classify one CC."

## Discussion


## Related Claims
- [An expert dataset of 4803 annotated chest compressions from 10 experts was collected and downsampled to 3434 samples to train the mistake-detection models](cpr-tutor-expert-dataset-4803-ccs.md) — related
- [Sessions with CPR Tutor feedback showed no significant difference in overall mistake frequency compared with control sessions without feedback](cpr-tutor-no-overall-mistake-frequency-reduction.md) — related
- [Real-time audio feedback from the CPR Tutor is followed by a short-term decrease in Error Rates across all five target CPR classes within 10 seconds](cpr-tutor-short-term-error-rate-decrease.md) — related
- [AI in psychomotor ITS is used predominantly for feedback construction rather than for task recommendation or adaptation](its-ai-feedback-over-recommendation.md) — a broader claim this one bears on
- [Real-time and dynamic feedback dominate feedback provision in ILEs for psychomotor skills](ile-psychomotor-feedback-realtime-dynamic-dominance.md) — a broader claim this one bears on
