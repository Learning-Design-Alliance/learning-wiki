---
type: research-method
id: humanmachine-agreement-matrix-for-automated-scoring-uncertainty
title: Human–machine agreement matrix for automated scoring uncertainty
description: "The human-machine agreement matrix is \"a normalized confusion matrix of the AS model's predictions and the ground truth, precomputed on validation data or historical test data\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
---

# Human–machine agreement matrix for automated scoring uncertainty

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
The human-machine agreement matrix is "a normalized confusion matrix of the AS model's predictions and the ground truth, precomputed on validation data or historical test data". Each entry gives the probability that the human-labeled class aligns with the machine-predicted class, e.g. m[Low B1][High B1] = 0.27. It drives both uncertainty sampling, via cross-entropy of each row against the ideal one-hot distribution, and reward sampling, via the p(c|m) term in the expected-reward calculation.

## Accounts
<!-- How each source describes or uses the method -->
- **Human-machine agreement matrix for quantifying per-class scoring uncertainty**: The human-machine agreement matrix is "a normalized confusion matrix of the AS model's predictions and the ground truth, precomputed on validation data or historical test data". Each entry gives the probability that the human-labeled class aligns with the machine-predicted class, e.g. m[Low B1][High B1] = 0.27. It drives both uncertainty sampling, via cross-entropy of each row against the ideal one-hot distribution, and reward sampling, via the p(c|m) term in the expected-reward calculation. (Yaman Kumar Singla et al. (2022))

### Claims

## Related Research Methods
-

## Key Sources
- Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen. (2022). Using Sampling to Estimate and Improve Performance of Automated Scoring Systems with Guarantees. https://arxiv.org/abs/2111.08906
