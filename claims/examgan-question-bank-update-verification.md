---
type: claim
title: "ExamGAN can reveal when an exam question bank needs updating: on assistments1213 it was hard to generate scripts with difficulty above 0.5"
description: "ExamGAN can reveal when an exam question bank needs updating: on assistments1213 it was hard to generate scripts with difficulty above 0.5"
id: examgan-question-bank-update-verification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
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

# ExamGAN can reveal when an exam question bank needs updating: on assistments1213 it was hard to generate scripts with difficulty above 0.5

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the assistments1213 dataset it was hard to generate exam scripts with difficulty level greater than 0.5, implying the question bank was too easy relative to student mastery; the article presents this as a side benefit for verifying whether a question bank update is necessary. [→ Zhengyang Wu 2021](#zhengyang-wu-2021)

## Evidence

### Zhengyang Wu 2021

Zhengyang Wu, Ke Deng, Judy Qiu, Yong Tang. (2021). ExamGAN and Twin-ExamGAN for Exam Script Generation. [doi:10.48550/arXiv.2108.09656](https://doi.org/10.48550/arXiv.2108.09656)

`q2 · i?` · `design · r2`

Observation from the benchmark experiments (Figs. 5-7): on assistments1213, generated scripts could not exceed difficulty 0.5, which the article reads as the question bank being too easy and as a "side beneﬁt" for quality-assessment maintenance.

> "Interestingly, it is hard for dataset assistments1213 to generate exam scripts with difﬁculty level greater than 0.5. It implies that the questions in the exam question bank are too easy considering the knowledge mastery level of the students"

## Discussion


## Related Claims
- [In a real teaching case study, ExamGAN-generated exam scripts for three real classes showed highly desirable and consistent difficulty, distinguishability, rationality, and validity](examgan-case-study-real-course-desirable.md) — related
- [ExamGAN generates exam scripts closer to desirable difficulty, validity, rationality, and distinguishability values than RSF, GA, and ExamVAE baselines on three benchmark datasets](examgan-outperforms-baselines-exam-quality.md) — related
- [IRT analysis showed the tutor-web item banks contained more easy than difficult questions](tutor-web-item-banks-skewed-easy.md) — related
