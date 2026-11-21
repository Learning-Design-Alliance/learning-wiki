---
type: claim
title: "QUEST-trained question generators raise simulated exam scores by 18.5% over the next strongest baseline across five subjects"
description: "QUEST-trained question generators raise simulated exam scores by 18.5% over the next strongest baseline across five subjects"
id: quest-trained-generators-18-5-percent-exam-gain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: dong-ho-lee-2026
    resource: "https://doi.org/10.18653/2026.findings-emnlp.97"
    title: "Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara. (2026). Which Questions Improve Learning the Most? Utility Estimation of Questions with LM-based Simulations. arXiv. Originally published 2025. [doi:10.18653/2026.findings-emnlp.97](https://doi.org/10.18653/2026.findings-emnlp.97)"
    author: Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# QUEST-trained question generators raise simulated exam scores by 18.5% over the next strongest baseline across five subjects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` QUEST-trained generators achieve the highest simulated exam scores across all five subjects, with an average gain of 18.5% over the next strongest baseline (CoT). [→ Dong-Ho Lee 2026](#dong-ho-lee-2026)
`q2 i?` The subject-specific QUEST variant consistently outperforms the cross-subject variant. [→ Dong-Ho Lee 2026](#dong-ho-lee-2026)

## Evidence

### Dong-Ho Lee 2026

Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara. (2026). Which Questions Improve Learning the Most? Utility Estimation of Questions with LM-based Simulations. arXiv. Originally published 2025. [doi:10.18653/2026.findings-emnlp.97](https://doi.org/10.18653/2026.findings-emnlp.97)

`q2 · i?` · `design · r2`

Simulation study on TEXTBOOK-EXAM test chapters comparing prompting, SFT, and QUEST generators, averaged over three trials (Table 2). QUEST subject-specific reached an average score of 55.1 versus 46.5 for CoT; the article reports "an average gain of 18.5% over the next strongest baseline (CoT)". Improvements were statistically significant at p <0.01 with paired t-test on average and for three of five subjects.

> "QUESTachieves the highest exam scores across all subjects, with an average gain of 18.5% over the next strongest baseline (CoT). Its subject-specific variant consistently outperforms the cross-subject version, highlighting the importance of domain-specific optimization."

## Discussion


## Related Claims
- [Training on utility-filtered questions yields the highest exam performance, while optimizing for salience or EIG fails to enhance utility](utility-optimization-beats-indirect-metric-optimization.md) — related
- [GPT-4 (CoT) prompting achieves the highest recall but the lowest F1 score among GPT baselines because most of its generated questions do not match ground truth](gpt4-cot-highest-recall-lowest-f1.md) — related
