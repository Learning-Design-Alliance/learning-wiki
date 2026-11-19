---
type: claim
title: The loss in assessment equivalency of T-ExamGAN pairs is trivial overall, with individual quality priority (S1) slightly better than twin difference priority (S2)
description: The loss in assessment equivalency of T-ExamGAN pairs is trivial overall, with individual quality priority (S1) slightly better than twin difference priority (S2)
id: t-examgan-assessment-equivalency-loss-trivial
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

# The loss in assessment equivalency of T-ExamGAN pairs is trivial overall, with individual quality priority (S1) slightly better than twin difference priority (S2)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Although T-ExamGAN pairs tend to have greater quality differences than independently generated ExamGAN pairs, the loss in assessment equivalency is trivial overall, and T-ExamGAN@S1 is slightly better than T-ExamGAN@S2 on equivalency. [→ Zhengyang Wu 2021](#zhengyang-wu-2021)

## Evidence

### Zhengyang Wu 2021

Zhengyang Wu, Ke Deng, Judy Qiu, Yong Tang. (2021). ExamGAN and Twin-ExamGAN for Exam Script Generation. [doi:10.48550/arXiv.2108.09656](https://doi.org/10.48550/arXiv.2108.09656)

`q2 · i?` · `design · r2`

Analysis of 100 generated pairs per method across the three datasets (Figs. 14-16, left diagrams): the article reports the equivalency loss "is trivial overall" and that the individual quality priority strategy yields more similar quality within pairs.

> "However, it is interesting that the loss in Assessment Equivalency is trivial overall as shown in Fig. 14, 15, and 16. Moreover, we observe that T-ExamGAN@S1 is slightly better than T-ExamGAN@S2."

## Discussion


## Related Claims
- [ExamGAN generates exam scripts closer to desirable difficulty, validity, rationality, and distinguishability values than RSF, GA, and ExamVAE baselines on three benchmark datasets](examgan-outperforms-baselines-exam-quality.md) — related
- [T-ExamGAN generates pairs of exam scripts with significantly different question sets, while independently generated ExamGAN pairs are almost the same](t-examgan-significantly-different-question-pairs.md) — related
