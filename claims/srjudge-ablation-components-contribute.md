---
type: claim
title: "Each SRJudge component contributes: the Reasoner and Judger add measurable F1 gains over the Selector alone"
description: "Each SRJudge component contributes: the Reasoner and Judger add measurable F1 gains over the Selector alone"
id: srjudge-ablation-components-contribute
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

# Each SRJudge component contributes: the Reasoner and Judger add measurable F1 gains over the Selector alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Adding the GRPO-trained Reasoner on top of the Selector improves F1 by 2.02%, 0.96%, and 1.92% on S Math, S Bio, and S Phy respectively, and adding the Judger further improves performance on all three datasets. [→ Zhiwei Yang 2026](#zhiwei-yang-2026)

## Evidence

### Zhiwei Yang 2026

Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan. (2026). SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging. arXiv preprint. https://arxiv.org/abs/2609.36982 [doi:10.48550/arxiv.2609.36982](https://doi.org/10.48550/arxiv.2609.36982)

`q2 · i?` · `design · r2`

Ablation study (Table 4) comparing Selector-only, Reasoner-only, S+R, and S+R+J variants with two Judger sizes. The article reports the Reasoner gains above and states that "integrating the Judger consistently enhances performance on all three datasets", with the larger Qwen3-32B Judger (J2) yielding the best F1 scores.

> "After incorporating the Reasoner on top of the Selector, the F1 scores are improved by 2.02%, 0.96%, and 1.92% on the S Math, S Bio, and S Phy datasets, respectively."

## Discussion


## Related Claims
- [A dynamic position reward in RL training improves tagging performance and prevents overfitting to Selector outputs](dynamic-position-reward-improves-reasoner.md) — related
- [Applying GRPO alone to LLMs for tagging yields significantly lower performance than supervised fine-tuning](grpo-alone-inferior-to-sft-for-tagging.md) — related
- [SRJudge improves prediction on hard-to-distinguish samples, with larger gains on S Math than on the higher-grade datasets](srjudge-gains-hard-to-distinguish-samples.md) — related
- [SRJudge consistently outperforms state-of-the-art baselines on three knowledge concept tagging datasets](srjudge-outperforms-baselines-three-datasets.md) — related
- [Pruning low-advantage completions during RL improves F1 up to a middle pruning rate while reducing training time](pruning-mechanism-improves-f1-and-training-time.md) — related
- [Fine-tuned SLMs retrieve the correct concept within a top-K shortlist but have limited top-1 accuracy](slm-topk-shortlist-limited-top1-accuracy.md) — related
