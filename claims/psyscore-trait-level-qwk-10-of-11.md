---
type: claim
title: At trait level PsyScore-AES ranks first in 10 of 11 dimensions (mean QWK 0.735), improving Voice scoring from 0.619 to 0.740 while trailing T-MES on Style
description: At trait level PsyScore-AES ranks first in 10 of 11 dimensions (mean QWK 0.735), improving Voice scoring from 0.619 to 0.740 while trailing T-MES on Style
id: psyscore-trait-level-qwk-10-of-11
status: draft
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

# At trait level PsyScore-AES ranks first in 10 of 11 dimensions (mean QWK 0.735), improving Voice scoring from 0.619 to 0.740 while trailing T-MES on Style

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` PsyScore-AES ranks first on 10 of 11 trait dimensions with mean QWK 0.735, including a Voice improvement from 0.619 (ArTS) to 0.740, though it trails T-MES on Style (0.683 vs 0.721). [→ Wei Xia 2026](#wei-xia-2026)

## Evidence

### Wei Xia 2026

Wei Xia, Jin Wu, Haoran Shi, Xiangyu Wang, Chanjin Zheng. (2026). PsyScore: A Psychometrically-Aware Framework for Trait-Adaptive Essay Scoring and ZPD-Scaffolded Feedback. arXiv preprint. https://arxiv.org/abs/2606.20287 [doi:10.48550/arxiv.2606.20287](https://doi.org/10.48550/arxiv.2606.20287)

`q2 · i?` · `design · r2`

Trait-level comparison in Table 2 of the ASAP++ evaluation: the model leads "10 out of 11 evaluated dimensions" with mean QWK 0.735; Voice rises from 0.619 to 0.740, while Style trails T-MES (0.683 vs 0.721).

> "At the trait level, PsyScore-AES ranks first in 10 out of 11 evaluated dimensions, achieving a mean QWK of 0.735. In the Voice dimension, which is typically more subjective, the model improves the QWK from 0.619 (ArTS) to 0.740."

## Discussion


## Related Claims
- [PsyScore-AES achieves a state-of-the-art average QWK of 0.747 on ASAP++, surpassing the strongest baseline SaMRL-large (0.722) and ranking first on 6 of 8 prompts](psyscore-aes-sota-qwk-0-747-asap.md) — related
- [Removing grid-search initialization of IRT discrimination and difficulty parameters drops scoring performance from QWK 0.747 to 0.705](psyscore-irt-initialization-ablation-qwk-drop.md) — related
- [Three education experts rate PsyScore feedback significantly higher than all LLM baselines on every dimension (p < .001), with the No-IRT ablation declining in Adaptivity and Accuracy (p < .05)](psyscore-expert-evaluation-outperforms-baselines.md) — related
