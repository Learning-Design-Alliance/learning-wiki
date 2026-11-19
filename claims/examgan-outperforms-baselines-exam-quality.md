---
type: claim
title: ExamGAN generates exam scripts closer to desirable difficulty, validity, rationality, and distinguishability values than RSF, GA, and ExamVAE baselines on three benchmark datasets
description: ExamGAN generates exam scripts closer to desirable difficulty, validity, rationality, and distinguishability values than RSF, GA, and ExamVAE baselines on three benchmark datasets
id: examgan-outperforms-baselines-exam-quality
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: zhengyang-wu-2021
    resource: "https://doi.org/10.48550/arXiv.2108.09656"
    title: "Zhengyang Wu, Ke Deng, Judy Qiu, Yong Tang. (2021). ExamGAN and Twin-ExamGAN for Exam Script Generation. [doi:10.48550/arXiv.2108.09656](https://doi.org/10.48550/arXiv.2108.09656)"
    author: Zhengyang Wu, Ke Deng, Judy Qiu, Yong Tang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ExamGAN generates exam scripts closer to desirable difficulty, validity, rationality, and distinguishability values than RSF, GA, and ExamVAE baselines on three benchmark datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On three benchmark datasets, exam scripts generated using ExamGAN tend to be closer to the desirable difficulty, validity, rationality, and distinguishability values than those from the RSF, GA, and ExamVAE baselines, and are more concentrated (more reliable). [→ Zhengyang Wu 2021](#zhengyang-wu-2021)

## Evidence

### Zhengyang Wu 2021

Zhengyang Wu, Ke Deng, Judy Qiu, Yong Tang. (2021). ExamGAN and Twin-ExamGAN for Exam Script Generation. [doi:10.48550/arXiv.2108.09656](https://doi.org/10.48550/arXiv.2108.09656)

`q2 · i?` · `design · r2`

Simulation-style benchmark evaluation on assistments0910, assistments1213, and olies2011 (100 classes of 50 students each), comparing ExamGAN against RSF, GA, and ExamVAE; results in Figs. 5-11 show ExamGAN scripts "closer to the desirable difﬁculty value ( 0.7)" and more concentrated in quality.

> "Compared with the baselines, the exam scripts generated using ExamGAN tend to be closer to the desirable difﬁculty value ( 0.7), closer to the desirable validity value (closer to 1 is better), closer to the desirable rationality value"

## Discussion


## Related Claims
- [In a real teaching case study, ExamGAN-generated exam scripts for three real classes showed highly desirable and consistent difficulty, distinguishability, rationality, and validity](examgan-case-study-real-course-desirable.md) — related
- [ExamGAN can reveal when an exam question bank needs updating: on assistments1213 it was hard to generate scripts with difficulty above 0.5](examgan-question-bank-update-verification.md) — related
- [T-ExamGAN generates pairs of exam scripts with significantly different question sets, while independently generated ExamGAN pairs are almost the same](t-examgan-significantly-different-question-pairs.md) — related
- [Analytical derivation sets the desirable score distribution to a normal distribution with mean 70 and standard deviation 15 to achieve excellent distinguishability](desirable-score-distribution-mean-70-sd-15.md) — a broader claim this one bears on
- [The loss in assessment equivalency of T-ExamGAN pairs is trivial overall, with individual quality priority (S1) slightly better than twin difference priority (S2)](t-examgan-assessment-equivalency-loss-trivial.md) — related
