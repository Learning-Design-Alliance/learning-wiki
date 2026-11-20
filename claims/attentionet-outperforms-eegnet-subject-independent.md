---
type: claim
title: AttentioNet significantly outperforms the EEGNet baseline in subject-independent 5-class EEG attention classification
description: AttentioNet significantly outperforms the EEGNet baseline in subject-independent 5-class EEG attention classification
id: attentionet-outperforms-eegnet-subject-independent
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

# AttentioNet significantly outperforms the EEGNet baseline in subject-independent 5-class EEG attention classification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In leave-one-subject-out evaluation, AttentioNet achieved 53.75% average accuracy (SD=4.58, chance=20%) versus 43.8% (SD=6.20) for EEGNet, a difference confirmed significant by a t-test. [→ Dhruv Verma 2023](#dhruv-verma-2023)

## Evidence

### Dhruv Verma 2023

Dhruv Verma, Sejal Bhalla, S. V. Sai Santosh, Saumya Yadav, Aman Parnami, Jainendra Shukla. (2023). AttentioNet: Monitoring Student Attention Type in Learning with EEG-Based Measurement System. [doi:10.1109/acii59096.2023.10388212](https://doi.org/10.1109/acii59096.2023.10388212)

`q2 · i?` · `design · r2`

Leave-one-subject-out cross-validation experiment over 20 subjects in the subject-independent setting; the paper reports AttentioNet's LOSO accuracy as 53.75% (SD=4.58, chance=20%) "while for EEGNet, it was 43.8% (SD=6.20)".

> "while for EEGNet, it was 43.8% (SD=6.20). Our approach signiﬁcantly outperformed EEGNet, and we conﬁrmed this with a Students’ T-test ( p : 1.5 × 10−6)."

## Discussion


## Related Claims
- [Transfer-learning personalization with 30 seconds of per-class EEG data raises AttentioNet accuracy to 92.3%](attentionet-personalization-30-seconds-92-3.md) — related
- [Accuracy gains from additional fine-tuning data plateau beyond 30 seconds per class](fine-tuning-gain-plateau-beyond-30-seconds.md) — related
