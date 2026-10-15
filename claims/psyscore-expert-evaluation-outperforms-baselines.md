---
type: claim
title: Three education experts rate PsyScore feedback significantly higher than all LLM baselines on every dimension (p < .001), with the No-IRT ablation declining in Adaptivity and Accuracy (p < .05)
description: Three education experts rate PsyScore feedback significantly higher than all LLM baselines on every dimension (p < .001), with the No-IRT ablation declining in Adaptivity and Accuracy (p < .05)
id: psyscore-expert-evaluation-outperforms-baselines
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
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Three education experts rate PsyScore feedback significantly higher than all LLM baselines on every dimension (p < .001), with the No-IRT ablation declining in Adaptivity and Accuracy (p < .05)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`

## Subclaims
`q3 i?` In a double-blind expert study of 80 essays, PsyScore outperforms GPT-4o, Llama-4 and Qwen-3 on all five dimensions (p < .001, paired t-test with Bonferroni correction); the No-IRT variant shows marked declines in Adaptivity and Accuracy (p < .05). [→ Wei Xia 2026](#wei-xia-2026)

## Evidence

### Wei Xia 2026

Wei Xia, Jin Wu, Haoran Shi, Xiangyu Wang, Chanjin Zheng. (2026). PsyScore: A Psychometrically-Aware Framework for Trait-Adaptive Essay Scoring and ZPD-Scaffolded Feedback. arXiv preprint. https://arxiv.org/abs/2606.20287 [doi:10.48550/arxiv.2606.20287](https://doi.org/10.48550/arxiv.2606.20287)

`q3 · i?` · `design · r2`

Human expert evaluation: three senior education experts rated a stratified sample of 80 essays with feedback on five dimensions (1–5 Likert); PsyScore mean ratings (e.g., Overall 4.25±.63) exceed baselines, with Fleiss' κ of 0.733 for Specificity.

> "PsyScore significantly outperforms all LLM baselines (GPT-4o, Llama-4, Qwen-3) on every dimension ( p < .001, paired t-test with Bonferroni correction). The ablation variant (PsyScore-No-IRT) exhibits marked declines in Adaptivity and Accuracy( p < .05)"

## Discussion


## Related Claims
- [In pairwise LLM-judge comparisons PsyScore-AEF wins over 90% in Actionability against GPT-4o and Llama, and removing the psychometric module reduces Adaptivity and Tone wins with PsyScore retaining above 75%](psyscore-feedback-actionability-win-rates.md) — possibly the same claim (merge candidate)
- [Removing grid-search initialization of IRT discrimination and difficulty parameters drops scoring performance from QWK 0.747 to 0.705](psyscore-irt-initialization-ablation-qwk-drop.md) — related
- [Ablating expert-informed structural components lowered LLM-judge scores on all dimensions, with largest drops in challenge quality, intent alignment, and domain grounding](ablation-structural-components-lower-judge-scores.md) — related
- [At trait level PsyScore-AES ranks first in 10 of 11 dimensions (mean QWK 0.735), improving Voice scoring from 0.619 to 0.740 while trailing T-MES on Style](psyscore-trait-level-qwk-10-of-11.md) — related
