---
type: claim
title: Pruning low-advantage completions during RL improves F1 up to a middle pruning rate while reducing training time
description: Pruning low-advantage completions during RL improves F1 up to a middle pruning rate while reducing training time
id: pruning-mechanism-improves-f1-and-training-time
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: zhiwei-yang-2026
    resource: "https://arxiv.org/abs/2609.36982"
    title: "Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan. (2026). SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging. arXiv preprint. https://arxiv.org/abs/2609.36982"
    author: Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Pruning low-advantage completions during RL improves F1 up to a middle pruning rate while reducing training time

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` As the RL pruning rate increases, F1 first improves then declines (staying above the no-pruning setting), while training time consistently decreases. [→ Zhiwei Yang 2026](#zhiwei-yang-2026)

## Evidence

### Zhiwei Yang 2026

Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan. (2026). SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging. arXiv preprint. https://arxiv.org/abs/2609.36982

`q2 · i?` · `design · r2`

Numerical results across pruning-rate settings (Table 6): F1 peaks at the 0.50 pruning rate (0.7491 on S Math, 0.6925 on S Bio, 0.6629 on S Phy) and training time falls from 14.1 to 5.5 hours on S Math between rates 0.00 and 0.75. The article attributes this to filtering out low-quality completions with marginal advantages.

> "As the pruning rate increases, F1 scores exhibit a trend of initial improvement followed by a decline (while exceeding the no-pruning setting). Meanwhile, training time consistently decreases as the pruning rate increases."

## Discussion


## Related Claims
- [Applying GRPO alone to LLMs for tagging yields significantly lower performance than supervised fine-tuning](grpo-alone-inferior-to-sft-for-tagging.md) — related
- [Reinforcement learning with a learned alignment reward substantially improves question-concept alignment after supervised fine-tuning, while answerability remains high throughout training](alignment-rl-improves-concept-alignment.md) — related
- [A dynamic position reward in RL training improves tagging performance and prevents overfitting to Selector outputs](dynamic-position-reward-improves-reasoner.md) — related
- [Over eight weeks, university learners receiving reinforcement learning-optimized oral practice sequencing attained normalized learning gains approximately 2.2 times higher than learners following fixed curricula](rl-sequencing-beats-fixed-oral-curriculum.md) — related
- [Each SRJudge component contributes: the Reasoner and Judger add measurable F1 gains over the Selector alone](srjudge-ablation-components-contribute.md) — related
