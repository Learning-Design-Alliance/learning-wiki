---
type: claim
title: "Transfer-learning personalization with 30 seconds of per-class EEG data raises AttentioNet accuracy to 92.3%"
description: "Transfer-learning personalization with 30 seconds of per-class EEG data raises AttentioNet accuracy to 92.3%"
id: attentionet-personalization-30-seconds-92-3
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: dhruv-verma-2023
    resource: "https://doi.org/10.1109/acii59096.2023.10388212"
    title: "Dhruv Verma, Sejal Bhalla, S. V. Sai Santosh, Saumya Yadav, Aman Parnami, Jainendra Shukla. (2023). AttentioNet: Monitoring Student Attention Type in Learning with EEG-Based Measurement System. [doi:10.1109/acii59096.2023.10388212](https://doi.org/10.1109/acii59096.2023.10388212)"
    author: Dhruv Verma, Sejal Bhalla, S. V. Sai Santosh, Saumya Yadav, Aman Parnami, Jainendra Shukla
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Transfer-learning personalization with 30 seconds of per-class EEG data raises AttentioNet accuracy to 92.3%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Fine-tuning a pre-trained base model with 30 seconds of a left-out subject's data per class yields 92.3% average across-subject accuracy (SD=3.04) in 5-class attention classification. [→ Dhruv Verma 2023](#dhruv-verma-2023)

## Evidence

### Dhruv Verma 2023

Dhruv Verma, Sejal Bhalla, S. V. Sai Santosh, Saumya Yadav, Aman Parnami, Jainendra Shukla. (2023). AttentioNet: Monitoring Student Attention Type in Learning with EEG-Based Measurement System. [doi:10.1109/acii59096.2023.10388212](https://doi.org/10.1109/acii59096.2023.10388212)

`q2 · i?` · `design · r2`

Subject-dependent (adaptive) evaluation using LOSO cross-validation with incremental fine-tuning; the paper reports that "using 30 seconds of data per class was found to be sufficient to personalize the model" and gives the 92.3% (SD=3.04) accuracy.

> "Notably, using 30 seconds of data per class was found to be sufﬁcient to personalize the model for any given subject. At this conﬁguration, the average across-subject accuracy of AttentioNet was 92.3% (SD=3.04), making it well-suited for end-user applications."

## Discussion


## Related Claims
- [AttentioNet significantly outperforms the EEGNet baseline in subject-independent 5-class EEG attention classification](attentionet-outperforms-eegnet-subject-independent.md) — related
- [Accuracy gains from additional fine-tuning data plateau beyond 30 seconds per class](fine-tuning-gain-plateau-beyond-30-seconds.md) — related
- [Pre-training on synthetic data before fine-tuning on limited real data improves math operation classification accuracy, with the largest gains when real data is extremely limited](synthetic-pretraining-finetuning-limited-real-data.md) — related
