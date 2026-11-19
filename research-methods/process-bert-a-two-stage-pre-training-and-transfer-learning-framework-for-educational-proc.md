---
type: research-method
id: process-bert-a-two-stage-pre-training-and-transfer-learning-framework-for-educational-proc
title: "Process-BERT: a two-stage pre-training and transfer learning framework for educational process data"
description: Process-BERT is a generic framework for representation learning on educational process data that comes in the form of time series.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
---

# Process-BERT: a two-stage pre-training and transfer learning framework for educational process data

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Process-BERT is a generic framework for representation learning on educational process data that comes in the form of time series. It has three components: a process model that turns an event sequence into latent representation vectors, self-supervised pre-training objectives that predict event properties such as event type and timestamp from surrounding context, and a transfer function that adapts the representations for downstream learning outcome prediction. The authors state that "our framework can be applied to any educational process data that is in the form of time series", and instantiate it with a Bi-LSTM process model and an attention-based transfer function on NAEP assessment clickstreams.

## Accounts
<!-- How each source describes or uses the method -->
- **Process-BERT: a two-stage pre-training and transfer learning framework for educational process data**: Process-BERT is a generic framework for representation learning on educational process data that comes in the form of time series. It has three components: a process model that turns an event sequence into latent representation vectors, self-supervised pre-training objectives that predict event properties such as event type and timestamp from surrounding context, and a transfer function that adapts the representations for downstream learning outcome prediction. The authors state that "our framework can be applied to any educational process data that is in the form of time series", and instantiate it with a Bi-LSTM process model and an attention-based transfer function on NAEP assessment clickstreams. (Alexander Scarlatos et al. (2022))

### Claims
- [On the NAEP score label, Process-BERT slightly outperforms the CKT autoencoder baseline and both neural models outperform feature engineering](../claims/process-bert-outperforms-baselines-score-label.md) [+M]

## Related Research Methods
-

## Key Sources
- Alexander Scarlatos, Christopher Brinton, and Andrew Lan. (2022). Process-BERT: A Framework for Representation Learning on Educational Process Data. https://arxiv.org/abs/2204.13607
