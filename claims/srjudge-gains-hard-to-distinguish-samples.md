---
type: claim
title: SRJudge improves prediction on hard-to-distinguish samples, with larger gains on S Math than on the higher-grade datasets
description: SRJudge improves prediction on hard-to-distinguish samples, with larger gains on S Math than on the higher-grade datasets
id: srjudge-gains-hard-to-distinguish-samples
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: zhiwei-yang-2026
    resource: "https://doi.org/10.48550/arxiv.2609.36982"
    title: "Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan. (2026). SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging. arXiv preprint. https://arxiv.org/abs/2609.36982 [doi:10.48550/arxiv.2609.36982](https://doi.org/10.48550/arxiv.2609.36982)"
    author: Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SRJudge improves prediction on hard-to-distinguish samples, with larger gains on S Math than on the higher-grade datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On samples whose concept categories the Selector finds difficult to distinguish (Selector F1 below 0.5), SRJudge achieves average F1 improvements of 8.84% on S Math, 2.31% on S Bio, and 3.24% on S Phy. [→ Zhiwei Yang 2026](#zhiwei-yang-2026)

## Evidence

### Zhiwei Yang 2026

Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan. (2026). SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging. arXiv preprint. https://arxiv.org/abs/2609.36982 [doi:10.48550/arxiv.2609.36982](https://doi.org/10.48550/arxiv.2609.36982)

`q2 · i?` · `design · r2`

Difficulty-interval analysis (Figure 3) using the Selector's per-category F1 as a difficulty proxy across five intervals from [0, 0.1] to [0.4, 0.5]. The article reports improvements "across most difficulty intervals" and attributes gains to the RL-trained Reasoner's reasoning and the Judger's global evaluation.

> "Overall, SRJudge achieves average F1 improvements of 8.84% on S Math, 2.31% on S Bio, and 3.24% on S Phy, demonstrating the clear effectiveness of SR-Judge in improving knowledge concept prediction for hard-to-distinguish samples across different disciplines."

## Discussion


## Related Claims
- [Applying GRPO alone to LLMs for tagging yields significantly lower performance than supervised fine-tuning](grpo-alone-inferior-to-sft-for-tagging.md) — related
- [Each SRJudge component contributes: the Reasoner and Judger add measurable F1 gains over the Selector alone](srjudge-ablation-components-contribute.md) — related
- [SRJudge consistently outperforms state-of-the-art baselines on three knowledge concept tagging datasets](srjudge-outperforms-baselines-three-datasets.md) — related
