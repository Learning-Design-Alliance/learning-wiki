---
type: claim
title: Applying GRPO alone to LLMs for tagging yields significantly lower performance than supervised fine-tuning
description: Applying GRPO alone to LLMs for tagging yields significantly lower performance than supervised fine-tuning
id: grpo-alone-inferior-to-sft-for-tagging
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: zhiwei-yang-2026
    resource: "https://doi.org/10.48550/arxiv.2609.36982"
    title: "Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan. (2026). SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging. arXiv preprint. https://arxiv.org/abs/2609.36982 [doi:10.48550/arxiv.2609.36982](https://doi.org/10.48550/arxiv.2609.36982)"
    author: Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Applying GRPO alone to LLMs for tagging yields significantly lower performance than supervised fine-tuning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` LLMs trained with GRPO alone obtain F1 scores of only 0.6600, 0.5674, and 0.5388 on S Math, S Bio, and S Phy, significantly inferior to the same LLMs trained with SFT. [→ Zhiwei Yang 2026](#zhiwei-yang-2026)

## Evidence

### Zhiwei Yang 2026

Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan. (2026). SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging. arXiv preprint. https://arxiv.org/abs/2609.36982 [doi:10.48550/arxiv.2609.36982](https://doi.org/10.48550/arxiv.2609.36982)

`q2 · i?` · `causal · r1`

Baseline comparison (Table 3) applying GRPO to sub-8B LLMs (Qwen2.5-7B-Instruct, LLaMA-3.1-8B-Instruct, DS-R1-Qwen-7B) versus SFT on the same models. The article attributes the gap to GRPO's extensive exploration of the search space, causing sparse rewards and convergence challenges.

> "While LLMs can benefit fromGRPOin knowledge concept tagging, their performance remains significantly inferior to that achieved with the SFT strategy, obtaining F1 scores of only 0.6600, 0.5674, and 0.5388 on the S Math, S Bio, and S Phy datasets, respectively."

## Discussion


## Related Claims
- [Each SRJudge component contributes: the Reasoner and Judger add measurable F1 gains over the Selector alone](srjudge-ablation-components-contribute.md) — related
- [SRJudge consistently outperforms state-of-the-art baselines on three knowledge concept tagging datasets](srjudge-outperforms-baselines-three-datasets.md) — related
- [SRJudge improves prediction on hard-to-distinguish samples, with larger gains on S Math than on the higher-grade datasets](srjudge-gains-hard-to-distinguish-samples.md) — related
- [Pruning low-advantage completions during RL improves F1 up to a middle pruning rate while reducing training time](pruning-mechanism-improves-f1-and-training-time.md) — related
- [GRPO with an SFS-aligned reward yields more consistent improvements than DPO, achieving the highest SFS overall](grpo-sfs-reward-beats-dpo.md) — related
- [GRPO with the Proficiency Alignment Reward improves alignment over SFT across every writing trait and essay prompt](grpo-par-improves-alignment-across-all-traits.md) — related
- [A dynamic position reward in RL training improves tagging performance and prevents overfitting to Selector outputs](dynamic-position-reward-improves-reasoner.md) — related
- [Reinforcement learning with a learned alignment reward substantially improves question-concept alignment after supervised fine-tuning, while answerability remains high throughout training](alignment-rl-improves-concept-alignment.md) — reports the opposite
- [GRPO pedagogical alignment of a reasoning LLM lowers actual student learning while raising judge-rated helpfulness (a multi-dimensional alignment tax)](grpo-pedagogical-alignment-tax-lowers-learning.md) — related
- [GRPO-with-PAR gains over SFT transfer to independent evaluators never used during policy optimization](par-gains-transfer-to-independent-evaluators.md) — related
