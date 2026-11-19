---
type: claim
title: In a real teaching case study, ExamGAN-generated exam scripts for three real classes showed highly desirable and consistent difficulty, distinguishability, rationality, and validity
description: In a real teaching case study, ExamGAN-generated exam scripts for three real classes showed highly desirable and consistent difficulty, distinguishability, rationality, and validity
id: examgan-case-study-real-course-desirable
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

# In a real teaching case study, ExamGAN-generated exam scripts for three real classes showed highly desirable and consistent difficulty, distinguishability, rationality, and validity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a case study in an undergraduate Programming course (533 students' 384,945 exercise records used to train DKT, AUC of 0.83606), exam scripts generated for three real classes had highly desirable and consistent quality metrics. [→ Zhengyang Wu 2021](#zhengyang-wu-2021)

## Evidence

### Zhengyang Wu 2021

Zhengyang Wu, Ke Deng, Judy Qiu, Yong Tang. (2021). ExamGAN and Twin-ExamGAN for Exam Script Generation. [doi:10.48550/arXiv.2108.09656](https://doi.org/10.48550/arXiv.2108.09656)

`q2 · i?` · `design · r2`

Case study in a real teaching scenario at South China Normal University: ExamGAN trained on 100 randomly formed groups of 30 students, then used to create 40-question scripts for three real classes; Table 4 reports e.g. difficulty 0.754/0.712/0.723 and validity 0.934/0.929/0.940.

> "From the test results, difﬁculty, distinguishability, rationality, and validity of the generated exam scripts can be derived and shown in TABLE 4. Clearly, they are highly desirable and consistent for all classes."

## Discussion


## Related Claims
- [ExamGAN generates exam scripts closer to desirable difficulty, validity, rationality, and distinguishability values than RSF, GA, and ExamVAE baselines on three benchmark datasets](examgan-outperforms-baselines-exam-quality.md) — related
- [ExamGAN can reveal when an exam question bank needs updating: on assistments1213 it was hard to generate scripts with difficulty above 0.5](examgan-question-bank-update-verification.md) — related
