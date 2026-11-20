---
type: claim
title: Accuracy gains from additional fine-tuning data plateau beyond 30 seconds per class
description: Accuracy gains from additional fine-tuning data plateau beyond 30 seconds per class
id: fine-tuning-gain-plateau-beyond-30-seconds
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
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

# Accuracy gains from additional fine-tuning data plateau beyond 30 seconds per class

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Increasing tuning data beyond 30 seconds per class produced an insignificant gain in accuracy, indicating the amount of personalization data can be traded off. [→ Dhruv Verma 2023](#dhruv-verma-2023)

## Evidence

### Dhruv Verma 2023

Dhruv Verma, Sejal Bhalla, S. V. Sai Santosh, Saumya Yadav, Aman Parnami, Jainendra Shukla. (2023). AttentioNet: Monitoring Student Attention Type in Learning with EEG-Based Measurement System. [doi:10.1109/acii59096.2023.10388212](https://doi.org/10.1109/acii59096.2023.10388212)

`q2 · i?` · `design · r2`

Numerical result from the incremental fine-tuning procedure shown in Fig. 3, where 10 seconds of the test subject's data per class were added stepwise; the paper reports the insignificant gain beyond the 30-second configuration.

> "Any further increase in the tuning d ata beyond this point resulted in an insigniﬁcant gain in accura cy, suggesting that additional data can be traded off to minimiz e the data required for ﬁne-tuning the base model."

## Discussion


## Related Claims
- [Transfer-learning personalization with 30 seconds of per-class EEG data raises AttentioNet accuracy to 92.3%](attentionet-personalization-30-seconds-92-3.md) — related
- [Pre-training on synthetic data before fine-tuning on limited real data improves math operation classification accuracy, with the largest gains when real data is extremely limited](synthetic-pretraining-finetuning-limited-real-data.md) — related
- [AttentioNet significantly outperforms the EEGNet baseline in subject-independent 5-class EEG attention classification](attentionet-outperforms-eegnet-subject-independent.md) — related
