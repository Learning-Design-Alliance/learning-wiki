---
type: claim
title: "MSE-trained students are better calibrated than KL(τ = ∞)-trained students, with ECE closer to the teacher's"
description: "MSE-trained students are better calibrated than KL(τ = ∞)-trained students, with ECE closer to the teacher's"
id: mse-distillation-better-calibration-than-large-tau-kl
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2021
sources:
  - id: taehyeon-kim-2021
    resource: "https://doi.org/10.24963/ijcai.2021/362"
    title: "Taehyeon Kim, Jaehoon Oh, Nak Yil Kim, Sangwook Cho and Se-Young Yun. (2021). Comparing Kullback-Leibler Divergence and Mean Squared Error Loss in Knowledge Distillation. [doi:10.24963/ijcai.2021/362](https://doi.org/10.24963/ijcai.2021/362)"
    author: Taehyeon Kim, Jaehoon Oh, Nak Yil Kim, Sangwook Cho and Se-Young Yun
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# MSE-trained students are better calibrated than KL(τ = ∞)-trained students, with ECE closer to the teacher's

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On CIFAR-100, the MSE-trained WRN-16-2 student has ECE of 10.46% versus 14.38% for the LKL(τ = ∞) student, with a reliability-diagram slope closer to the teacher's (8.44%). [→ Taehyeon Kim 2021](#taehyeon-kim-2021)

## Evidence

### Taehyeon Kim 2021

Taehyeon Kim, Jaehoon Oh, Nak Yil Kim, Sangwook Cho and Se-Young Yun. (2021). Comparing Kullback-Leibler Divergence and Mean Squared Error Loss in Knowledge Distillation. [doi:10.24963/ijcai.2021/362](https://doi.org/10.24963/ijcai.2021/362)

`q2 · i?` · `causal · r2`

Appendix E calibration analysis: 10-bin reliability diagrams and expected calibration error on the CIFAR-100 training set for WRN-28-4 (t) and WRN-16-2 (s) trained with LCE, LKL(τ = ∞) and LMSE (Figure 8).

> "Besides, this consistency is also shown in ECE that the model trained withLMSE (10.46%) has less ECE than the model trained withLKL with inﬁniteτ (14.38%)."

## Discussion


## Related Claims
- [With a poorly trained (noisy) teacher, label matching outperforms logit matching, and MSE loss performs worst](noisy-teacher-label-matching-better.md) — related
- [KL divergence loss with small τ (≤ 1.0) mitigates noisy-label corruption better than extreme logit matching](small-tau-kl-mitigates-noisy-labels.md) — related
