---
type: claim
title: SRJudge consistently outperforms state-of-the-art baselines on three knowledge concept tagging datasets
description: SRJudge consistently outperforms state-of-the-art baselines on three knowledge concept tagging datasets
id: srjudge-outperforms-baselines-three-datasets
status: review
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

# SRJudge consistently outperforms state-of-the-art baselines on three knowledge concept tagging datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` SRJudge achieves the best F1 scores of 0.7602 on S Math, 0.6987 on S Bio, and 0.6643 on S Phy, outperforming the leading baseline LGCEL. [→ Zhiwei Yang 2026](#zhiwei-yang-2026)

## Evidence

### Zhiwei Yang 2026

Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan. (2026). SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging. arXiv preprint. https://arxiv.org/abs/2609.36982 [doi:10.48550/arxiv.2609.36982](https://doi.org/10.48550/arxiv.2609.36982)

`q2 · i?` · `design · r2`

Benchmark comparison on three educational datasets (S Math, S Bio, S Phy) with 8:1:1 stratified splits, evaluating accuracy, precision, recall and macro F1 against SLM, LLM and task-specific baselines. The article reports SRJudge "consistently yielding the best results", with LGCEL the leading baseline at F1 0.7311, 0.6840 and 0.6476 respectively.

> "Overall, SRJudge outperforms LGCEL, achieving an F1 score of 0.7602 on S Math, 0.6987 on S Bio, and 0.6643 on S Phy, consistently yielding the best results."

## Discussion


## Related Claims
- [Applying GRPO alone to LLMs for tagging yields significantly lower performance than supervised fine-tuning](grpo-alone-inferior-to-sft-for-tagging.md) — related
- [Each SRJudge component contributes: the Reasoner and Judger add measurable F1 gains over the Selector alone](srjudge-ablation-components-contribute.md) — related
- [SRJudge improves prediction on hard-to-distinguish samples, with larger gains on S Math than on the higher-grade datasets](srjudge-gains-hard-to-distinguish-samples.md) — related
- [A dynamic position reward in RL training improves tagging performance and prevents overfitting to Selector outputs](dynamic-position-reward-improves-reasoner.md) — related
- [Pruning low-advantage completions during RL improves F1 up to a middle pruning rate while reducing training time](pruning-mechanism-improves-f1-and-training-time.md) — related
