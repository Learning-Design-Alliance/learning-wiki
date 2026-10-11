---
type: claim
title: "Static Knowledge Grounding and Dynamic Personal Memory are complementary: removing both yields the largest quality degradation"
description: "Static Knowledge Grounding and Dynamic Personal Memory are complementary: removing both yields the largest quality degradation"
id: skg-dpm-complementary-ablation-deeptutor
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: bingxi-zhao-2026
    resource: "https://arxiv.org/abs/2604.26962"
    title: "Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang. (2026). DeepTutor: Towards Agentic Personalized Tutoring. Technical Report, The University of Hong Kong. https://arxiv.org/abs/2604.26962"
    author: Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# Static Knowledge Grounding and Dynamic Personal Memory are complementary: removing both yields the largest quality degradation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`

## Subclaims
`q2 i?` Ablation shows removing SKG mainly weakens grounding metrics while removing DPM mainly weakens Personalization and Fitness, and removing both yields the largest overall degradation. [→ Bingxi Zhao 2026](#bingxi-zhao-2026)

## Evidence

### Bingxi Zhao 2026

Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang. (2026). DeepTutor: Towards Agentic Personalized Tutoring. Technical Report, The University of Hong Kong. https://arxiv.org/abs/2604.26962

`q2 · i?` · `causal · r?`

Component ablation (Figure 9) of SKG, DPM, or both from the full pipeline. The article reports SKG removal drops Groundedness most, while DPM removal most sharply declines Personalization and Fitness; no standardized effect sizes are printed.

> "Removing DPMmainly weakens adaptation.PersonalizationandFitnessdecline most sharply, showing that the learner profile is central to gap-aware explanation and difficulty-calibrated practice; the smaller drop inGroundedness"

## Discussion


## Related Claims
- [Ablating expert-informed structural components lowered LLM-judge scores on all dimensions, with largest drops in challenge quality, intent alignment, and domain grounding](ablation-structural-components-lower-judge-scores.md) — related
- [DeepTutor's interactive tutoring gains are stable across five university-level domains, varying only 0.16 points in overall quality](deeptutor-gains-stable-across-five-domains.md) — related
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](cognitive-load-module-largest-ablation-drop.md) — related
- [Pipeline components play complementary roles: hierarchical generation has the largest effect, grounding improves specificity and factual accuracy, and cluster-informed TOC planning improves structure and audience fit](pipeline-components-complementary-ablation.md) — related
- [Knowledge and behavior profile components provide complementary signals: removing either hurts metrics tied to the other](knowledge-behavior-profile-complementary-signals.md) — related
