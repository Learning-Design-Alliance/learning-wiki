---
type: claim
title: AAM-TSA outperforms state-of-the-art multimodal sentiment baselines on the T-MED teacher sentiment benchmark
description: AAM-TSA outperforms state-of-the-art multimodal sentiment baselines on the T-MED teacher sentiment benchmark
id: aam-tsa-outperforms-multimodal-baselines-t-med
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: zhiyi-duan-2026
    resource: "https://doi.org/10.1609/aaai.v40i3.37157"
    title: "Zhiyi Duan, Xiangren Wang, Hongyu Yuan, Qianli Xing. (2026). Advancing Multimodal Teacher Sentiment Analysis: The Large-Scale T-MED Dataset & The Effective AAM-TSA Model. arXiv preprint. Originally published 2025. [doi:10.1609/aaai.v40i3.37157](https://doi.org/10.1609/aaai.v40i3.37157)"
    author: Zhiyi Duan, Xiangren Wang, Hongyu Yuan, Qianli Xing
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# AAM-TSA outperforms state-of-the-art multimodal sentiment baselines on the T-MED teacher sentiment benchmark

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the T-MED test set, AAM-TSA achieves higher weighted accuracy and weighted F1 than nine general multimodal sentiment analysis baselines, including the best baseline MFMB Net. [→ Zhiyi Duan 2026](#zhiyi-duan-2026)

## Evidence

### Zhiyi Duan 2026

Zhiyi Duan, Xiangren Wang, Hongyu Yuan, Qianli Xing. (2026). Advancing Multimodal Teacher Sentiment Analysis: The Large-Scale T-MED Dataset & The Effective AAM-TSA Model. arXiv preprint. Originally published 2025. [doi:10.1609/aaai.v40i3.37157](https://doi.org/10.1609/aaai.v40i3.37157)

`q2 · i?` · `design · r3`

Benchmark comparison on the T-MED test split (80/10/10 split, weighted accuracy and weighted F1 metrics) in which AAM-TSA, the only method using instructional information features, reached WA 86.84% and W-F1 86.37% versus MFMB Net's 80.91/79.81; the authors note "the accuracy rate is increased by 5.93%, and W-F1 is increased by 6.56%".

> "Compared with the current optimal baseline MFMB Net, the accuracy rate is increased by 5.93%, and W-F1 is increased by 6.56%."

## Discussion


## Related Claims
- [AAM-TSA improves recognition across all eight emotion categories, including teacher-specific emotions, over the strongest baseline](aam-tsa-fine-grained-eight-emotion-gains.md) — a narrower finding that bears on this claim
- [Instructional information (subject and educational stage) improves teacher sentiment classification when embedded as a modality](instructional-information-modality-improves-teacher-sentiment.md) — related
- [Raw video features degrade teacher sentiment classification, while LLM-generated video descriptions improve it](raw-video-noise-video-descriptions-help-t-med.md) — related
- [Joint training of the feature encoders contributes the largest single-module ablation loss in AAM-TSA](joint-training-crucial-aam-tsa-ablation.md) — related
- [Audio is the core carrier of teacher emotional expression: audio-only features outperform text-only and video-description-only variants](audio-core-carrier-teacher-emotion-t-med.md) — related
