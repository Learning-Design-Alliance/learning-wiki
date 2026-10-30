---
type: claim
title: An expert dataset of 4803 annotated chest compressions from 10 experts was collected and downsampled to 3434 samples to train the mistake-detection models
description: An expert dataset of 4803 annotated chest compressions from 10 experts was collected and downsampled to 3434 samples to train the mistake-detection models
id: cpr-tutor-expert-dataset-4803-ccs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2022
recheck_by: 2025
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

# An expert dataset of 4803 annotated chest compressions from 10 experts was collected and downsampled to 3434 samples to train the mistake-detection models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The expert group dataset contained 4803 chest compressions, each annotated with five target classes, and was downsampled to 3434 samples because of class imbalance. [→ Di Mitri 2022](#di-mitri-2022)

## Evidence

### Di Mitri 2022

Di Mitri, D., Schneider, J., & Drachsler, H. (2022). KeepMeInTheLoop: Real-Time Feedback with Multimodal Data. International Journal of Artificial Intelligence in Education (2022) 32:1093–1118. https://doi.org/10.1007/s40593-021-00281-z

`q2 · i?` · `design · r2`

Expert data collection phase with 10 participants performing four 1-minute sessions; the article reports the dataset "consisted of 4803 CCs" with five annotations per compression, later downsampled to 3434 samples (-28.5%) due to unbalanced classes.

> "The collected dataset from the expert group consisted of 4803 CCs. Each CC was annotated with five classes."

## Discussion


## Related Claims
- [Sessions with CPR Tutor feedback showed no significant difference in overall mistake frequency compared with control sessions without feedback](cpr-tutor-no-overall-mistake-frequency-reduction.md) — related
- [Dialogue-shuffling augmentation improves evaluator performance while downsampling reduces it](dialogue-shuffling-augmentation-improves-evaluator.md) — related
- [The CPR Tutor architecture classifies a chest compression in about 70 milliseconds, supporting real-time feedback provision](cpr-tutor-real-time-classification-speed.md) — related
- [Real-time audio feedback from the CPR Tutor is followed by a short-term decrease in Error Rates across all five target CPR classes within 10 seconds](cpr-tutor-short-term-error-rate-decrease.md) — related
