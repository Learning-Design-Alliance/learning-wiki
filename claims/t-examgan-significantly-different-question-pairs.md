---
type: claim
title: T-ExamGAN generates pairs of exam scripts with significantly different question sets, while independently generated ExamGAN pairs are almost the same
description: T-ExamGAN generates pairs of exam scripts with significantly different question sets, while independently generated ExamGAN pairs are almost the same
id: t-examgan-significantly-different-question-pairs
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

# T-ExamGAN generates pairs of exam scripts with significantly different question sets, while independently generated ExamGAN pairs are almost the same

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` T-ExamGAN@S1 and T-ExamGAN@S2 ensure significant difference between the two exam scripts of each pair (measured by Jaccard coefficient), whereas ExamGAN@500 and ExamGAN@1500 generate two exam scripts almost the same as each other; the twin difference priority strategy (S2) performs much better on difference than S1. [→ Zhengyang Wu 2021](#zhengyang-wu-2021)

## Evidence

### Zhengyang Wu 2021

Zhengyang Wu, Ke Deng, Judy Qiu, Yong Tang. (2021). ExamGAN and Twin-ExamGAN for Exam Script Generation. [doi:10.48550/arXiv.2108.09656](https://doi.org/10.48550/arXiv.2108.09656)

`q2 · i?` · `design · r2`

Benchmark comparison generating 100 pairs per method on the three datasets (Figs. 14-16, right diagrams); Jaccard coefficient shows T-ExamGAN pairs differ significantly while independently generated ExamGAN pairs are "almost same to each other".

> "Clearly, T-ExamGAN@S1 and T-ExamGAN@S2 ensure the signiﬁcant difference between the two exam scripts of each pair while ExamGAN@500 and ExamGAN@1500 generate two exam scripts almost same to each other."

## Discussion


## Related Claims
- [ExamGAN generates exam scripts closer to desirable difficulty, validity, rationality, and distinguishability values than RSF, GA, and ExamVAE baselines on three benchmark datasets](examgan-outperforms-baselines-exam-quality.md) — related
- [The loss in assessment equivalency of T-ExamGAN pairs is trivial overall, with individual quality priority (S1) slightly better than twin difference priority (S2)](t-examgan-assessment-equivalency-loss-trivial.md) — related
