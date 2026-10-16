---
type: claim
title: A dynamic position reward in RL training improves tagging performance and prevents overfitting to Selector outputs
description: A dynamic position reward in RL training improves tagging performance and prevents overfitting to Selector outputs
id: dynamic-position-reward-improves-reasoner
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

# A dynamic position reward in RL training improves tagging performance and prevents overfitting to Selector outputs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` SRJudge with position rewards consistently outperforms one without position rewards, and dynamic adjustment across positions and training steps yields additional improvements over a static position reward. [→ Zhiwei Yang 2026](#zhiwei-yang-2026)

## Evidence

### Zhiwei Yang 2026

Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan. (2026). SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging. arXiv preprint. https://arxiv.org/abs/2609.36982 [doi:10.48550/arxiv.2609.36982](https://doi.org/10.48550/arxiv.2609.36982)

`q2 · i?` · `design · r2`

Ablation on position reward strategies (Table 5) comparing no reward, a static reward (R position = 3), and the dynamic reward of Equation (5). Dynamic yields the highest F1 (e.g., 0.7491 on S Math vs 0.7372 without). The article says the dynamic reward "helps sustain active exploration and improve RL efficiency" as training progresses.

> "SRJudge with position rewards consistently outperforms one without position rewards, which shows that introducing position rewards to the LLM Reasoner can prevent it from overfitting to the Selector's outputs."

## Discussion


## Related Claims
- [Each SRJudge component contributes: the Reasoner and Judger add measurable F1 gains over the Selector alone](srjudge-ablation-components-contribute.md) — related
- [Pruning low-advantage completions during RL improves F1 up to a middle pruning rate while reducing training time](pruning-mechanism-improves-f1-and-training-time.md) — related
- [SRJudge consistently outperforms state-of-the-art baselines on three knowledge concept tagging datasets](srjudge-outperforms-baselines-three-datasets.md) — related
