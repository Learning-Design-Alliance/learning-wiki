---
type: claim
title: Analytical derivation sets the desirable score distribution to a normal distribution with mean 70 and standard deviation 15 to achieve excellent distinguishability
description: Analytical derivation sets the desirable score distribution to a normal distribution with mean 70 and standard deviation 15 to achieve excellent distinguishability
id: desirable-score-distribution-mean-70-sd-15
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2021
sources:
  - id: zhengyang-wu-2021
    resource: "https://doi.org/10.48550/arXiv.2108.09656"
    title: "Zhengyang Wu, Ke Deng, Judy Qiu, Yong Tang. (2021). ExamGAN and Twin-ExamGAN for Exam Script Generation. [doi:10.48550/arXiv.2108.09656](https://doi.org/10.48550/arXiv.2108.09656)"
    author: Zhengyang Wu, Ke Deng, Judy Qiu, Yong Tang
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Analytical derivation sets the desirable score distribution to a normal distribution with mean 70 and standard deviation 15 to achieve excellent distinguishability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Under the moment-of-normal-distribution derivation, setting sigma = 15 (with mu = 70) makes the distance between the average of the 27% highest scores and the average of the 27% lowest scores greater than 39, i.e., excellent distinguishability. [→ Zhengyang Wu 2021](#zhengyang-wu-2021)

## Evidence

### Zhengyang Wu 2021

Zhengyang Wu, Ke Deng, Judy Qiu, Yong Tang. (2021). ExamGAN and Twin-ExamGAN for Exam Script Generation. [doi:10.48550/arXiv.2108.09656](https://doi.org/10.48550/arXiv.2108.09656)

`q1 · i?` · `design · r2`

Analytical derivation (Section 4.3) using conditional expectations of a normal distribution truncated at 0 and 100, with alpha as the 27%-quantile; the derivation yields "σ = 15 leads to excellent distinguishability" for the desirable distribution Z.

> "By substituting α into Equ. (10), we obtain the value of σ which makes the distance between the average of the 27% highest score and the average of the 27% lowest scores greater than 39. That is, σ = 15 leads to excellent distinguishability."

## Discussion


## Related Claims
- [Under normally distributed marks, CLO attainment is a linear function of questions' average marks and composite student achievement stays constant up to the 70% passing threshold](attainment-linear-achievement-constant-below-threshold.md) — related
- [The P.E. (median deviation) serves as an equal-step unit of difficulty, defined as the distance cutting off 25% of measures next the median](pe-unit-equal-steps-difficulty.md) — related
- [ExamGAN generates exam scripts closer to desirable difficulty, validity, rationality, and distinguishability values than RSF, GA, and ExamVAE baselines on three benchmark datasets](examgan-outperforms-baselines-exam-quality.md) — a narrower finding that bears on this claim
