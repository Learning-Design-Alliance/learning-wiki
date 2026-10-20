---
type: claim
title: "In pairwise LLM-judge comparisons PsyScore-AEF wins over 90% in Actionability against GPT-4o and Llama, and removing the psychometric module reduces Adaptivity and Tone wins with PsyScore retaining above 75%"
description: "In pairwise LLM-judge comparisons PsyScore-AEF wins over 90% in Actionability against GPT-4o and Llama, and removing the psychometric module reduces Adaptivity and Tone wins with PsyScore retaining above 75%"
id: psyscore-feedback-actionability-win-rates
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
  - id: wei-xia-2026-2
    resource: "https://arxiv.org/abs/2606.20287"
    title: "Wei Xia, Jin Wu, Haoran Shi, Xiangyu Wang, Chanjin Zheng. (2026). PsyScore: A Psychometrically-Aware Framework for Trait-Adaptive Essay Scoring and ZPD-Scaffolded Feedback. arXiv preprint. https://arxiv.org/abs/2606.20287"
    author: Wei Xia, Jin Wu, Haoran Shi, Xiangyu Wang, Chanjin Zheng
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In pairwise LLM-judge comparisons PsyScore-AEF wins over 90% in Actionability against GPT-4o and Llama, and removing the psychometric module reduces Adaptivity and Tone wins with PsyScore retaining above 75%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Against general-purpose models (GPT-4o, Llama), PsyScore-AEF exceeds 90% win rate in Actionability. [→ Wei Xia 2026](#wei-xia-2026)
`q2 i?` In the no-diagnosis ablation, removing the psychometric module substantially reduces Adaptivity and Tone wins, with PsyScore retaining a win rate above 75%. [→ Wei Xia 2026 (2)](#wei-xia-2026-2)

## Evidence

### Wei Xia 2026

Wei Xia, Jin Wu, Haoran Shi, Xiangyu Wang, Chanjin Zheng. (2026). PsyScore: A Psychometrically-Aware Framework for Trait-Adaptive Essay Scoring and ZPD-Scaffolded Feedback. arXiv preprint. https://arxiv.org/abs/2606.20287 [doi:10.48550/arxiv.2606.20287](https://doi.org/10.48550/arxiv.2606.20287)

`q2 · i?` · `design · r2`

Pairwise preference evaluation (Figure 3) on a stratified sample of 400 essays, judged double-blind by GPT-5 and Gemini-3-pro with position swapping; win rates "exceeding 90% in the Actionability dimension" against GPT-4o and Llama.

> "When compared to general-purpose models such as GPT-4o and Llama-3, PsyScore-AEF achieves win rates exceeding 90% in the Actionability dimension."

### Wei Xia 2026 (2)

Wei Xia, Jin Wu, Haoran Shi, Xiangyu Wang, Chanjin Zheng. (2026). PsyScore: A Psychometrically-Aware Framework for Trait-Adaptive Essay Scoring and ZPD-Scaffolded Feedback. arXiv preprint. https://arxiv.org/abs/2606.20287

`q2 · i?` · `design · r2`

Ablation arm of the same pairwise evaluation (Figure 3d, PsyScore-AEF vs No IRT): removing the psychometric module reduces Adaptivity and Tone wins, with PsyScore "retaining a win rate above 75%".

> "Abla- tion analysis (Figure 3) demonstrates that removing the psychometric module results in a substantial re- duction in bothAdaptivityandTone, with PsyScore retaining a win rate above 75%."

## Discussion


## Related Claims
- [Three education experts rate PsyScore feedback significantly higher than all LLM baselines on every dimension (p < .001), with the No-IRT ablation declining in Adaptivity and Accuracy (p < .05)](psyscore-expert-evaluation-outperforms-baselines.md) — possibly the same claim (merge candidate)
- [Teacher-agent comparisons show backbone-dependent patterns consistent with ZPD-informed adaptation](teacher-agent-backbone-dependent-zpd-patterns.md) — related
