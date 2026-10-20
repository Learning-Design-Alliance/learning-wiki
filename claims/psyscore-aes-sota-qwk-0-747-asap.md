---
type: claim
title: PsyScore-AES achieves a state-of-the-art average QWK of 0.747 on ASAP++, surpassing the strongest baseline SaMRL-large (0.722) and ranking first on 6 of 8 prompts
description: PsyScore-AES achieves a state-of-the-art average QWK of 0.747 on ASAP++, surpassing the strongest baseline SaMRL-large (0.722) and ranking first on 6 of 8 prompts
id: psyscore-aes-sota-qwk-0-747-asap
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: wei-xia-2026
    resource: "https://doi.org/10.48550/arxiv.2606.20287"
    title: "Wei Xia, Jin Wu, Haoran Shi, Xiangyu Wang, Chanjin Zheng. (2026). PsyScore: A Psychometrically-Aware Framework for Trait-Adaptive Essay Scoring and ZPD-Scaffolded Feedback. arXiv preprint. https://arxiv.org/abs/2606.20287 [doi:10.48550/arxiv.2606.20287](https://doi.org/10.48550/arxiv.2606.20287)"
    author: Wei Xia, Jin Wu, Haoran Shi, Xiangyu Wang, Chanjin Zheng
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# PsyScore-AES achieves a state-of-the-art average QWK of 0.747 on ASAP++, surpassing the strongest baseline SaMRL-large (0.722) and ranking first on 6 of 8 prompts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the ASAP++ benchmark, PsyScore-AES attains an average QWK of 0.747 across prompts, exceeding SaMRL-large's 0.722 and ranking first on 6 of 8 prompts. [→ Wei Xia 2026](#wei-xia-2026)

## Evidence

### Wei Xia 2026

Wei Xia, Jin Wu, Haoran Shi, Xiangyu Wang, Chanjin Zheng. (2026). PsyScore: A Psychometrically-Aware Framework for Trait-Adaptive Essay Scoring and ZPD-Scaffolded Feedback. arXiv preprint. https://arxiv.org/abs/2606.20287 [doi:10.48550/arxiv.2606.20287](https://doi.org/10.48550/arxiv.2606.20287)

`q2 · i?` · `design · r2`

Benchmark comparison on the ASAP++ dataset (6:2:2 split, 5-fold ensemble of bert-base-uncased) reported in Table 1: PsyScore-AES reaches "a new state-of-the-art average Quadratic Weighted Kappa (QWK) of 0.747" versus 0.722 for SaMRL-large.

> "PsyScore-AES achieves a new state-of-the-art average Quadratic Weighted Kappa (QWK) of 0.747, surpassing the strongest baseline (SaMRL-large, 0.722) and ranking first in 6 out of 8 prompts."

## Discussion


## Related Claims
- [At trait level PsyScore-AES ranks first in 10 of 11 dimensions (mean QWK 0.735), improving Voice scoring from 0.619 to 0.740 while trailing T-MES on Style](psyscore-trait-level-qwk-10-of-11.md) — related
- [Removing grid-search initialization of IRT discrimination and difficulty parameters drops scoring performance from QWK 0.747 to 0.705](psyscore-irt-initialization-ablation-qwk-drop.md) — related
- [GRPO with the Proficiency Alignment Reward improves alignment over SFT across every writing trait and essay prompt](grpo-par-improves-alignment-across-all-traits.md) — related
- [Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation](sft-improves-proficiency-alignment-over-prompting.md) — related
- [Rubric-grounded prompting alone provides limited proficiency control, aligning far better on content-oriented traits than on form-oriented traits](prompting-limited-uneven-proficiency-control-writing-simulation.md) — related
- [Three education experts rate PsyScore feedback significantly higher than all LLM baselines on every dimension (p < .001), with the No-IRT ablation declining in Adaptivity and Accuracy (p < .05)](psyscore-expert-evaluation-outperforms-baselines.md) — related
