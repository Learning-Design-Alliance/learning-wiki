---
type: claim
title: Joint training of the feature encoders contributes the largest single-module ablation loss in AAM-TSA
description: Joint training of the feature encoders contributes the largest single-module ablation loss in AAM-TSA
id: joint-training-crucial-aam-tsa-ablation
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
    rigour: 2
---

# Joint training of the feature encoders contributes the largest single-module ablation loss in AAM-TSA

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Removing joint training (RoBERTa and HuBERT no longer jointly trained) causes the largest performance drop among the module ablations, and removing asymmetric cross-modal attention further lowers performance. [→ Zhiyi Duan 2026](#zhiyi-duan-2026)

## Evidence

### Zhiyi Duan 2026

Zhiyi Duan, Xiangren Wang, Hongyu Yuan, Qianli Xing. (2026). Advancing Multimodal Teacher Sentiment Analysis: The Large-Scale T-MED Dataset & The Effective AAM-TSA Model. arXiv preprint. Originally published 2025. [doi:10.1609/aaai.v40i3.37157](https://doi.org/10.1609/aaai.v40i3.37157)

`q2 · i?` · `design · r2`

Appendix E.2 ablation experiments: variant Var-FECI without joint training scored 83.30 WA / 82.85 W-F1, and a further deletion of the asymmetric cross-modal attention module (Var-JI versus Var-JICI) decreased WA and W-F1 by 0.53% and 0.58%.

> "Compared with AAM-TSA, W A and W-F1 decreased by 3.54% and 3.52%, respectively."

## Discussion


## Related Claims
- [AAM-TSA outperforms state-of-the-art multimodal sentiment baselines on the T-MED teacher sentiment benchmark](aam-tsa-outperforms-multimodal-baselines-t-med.md) — related
- [Instructional information (subject and educational stage) improves teacher sentiment classification when embedded as a modality](instructional-information-modality-improves-teacher-sentiment.md) — related
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](cognitive-load-module-largest-ablation-drop.md) — related
- [Omitting the teacher's communication strategy causes the greatest drop in classifier accuracy, marking communication choice as the most impactful feature category.](communication-strategy-most-impactful-ablation.md) — related
- [Ablations show the trustworthiness module contributes most to performance, and the explanation generator cuts human review time by 41%](ablation-trust-module-largest-contribution.md) — related
- [Ablation study shows metadata-enriched embeddings produce the largest accuracy drop, while attention masking, KV caching and dynamic batching primarily support inference efficiency](ablation-metadata-embeddings-largest-accuracy-drop.md) — related
