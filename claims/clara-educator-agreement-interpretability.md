---
type: claim
title: CLARA annotations align with blinded educator judgments, with 0.81 pairwise agreement and highest-rated educational interpretability
description: CLARA annotations align with blinded educator judgments, with 0.81 pairwise agreement and highest-rated educational interpretability
id: clara-educator-agreement-interpretability
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: sijing-yin-2026
    resource: "https://arxiv.org/abs/2610.05783"
    title: "Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu. (2026). CLARA: Can AI Assess Developmental Appropriateness in Children's Stories?. https://arxiv.org/abs/2610.05783"
    author: Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: sijing-yin-2026-2
    resource: "https://arxiv.org/abs/2610.05783"
    title: "Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu. (2026). CLARA: Can AI Assess Developmental Appropriateness in Children's Stories?. https://arxiv.org/abs/2610.05783"
    author: Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# CLARA annotations align with blinded educator judgments, with 0.81 pairwise agreement and highest-rated educational interpretability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` In blinded human evaluation, average pairwise annotation agreement across three educators per story reaches 0.81, and educational interpretability receives the highest average criterion score. [→ Sijing Yin 2026](#sijing-yin-2026)
`q2 i?` Educators rate educational interpretability highest among criteria, indicating the annotation space provides meaningful developmental explanations beyond direct age prediction. [→ Sijing Yin 2026 (2)](#sijing-yin-2026-2)

## Evidence

### Sijing Yin 2026

Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu. (2026). CLARA: Can AI Assess Developmental Appropriateness in Children's Stories?. https://arxiv.org/abs/2610.05783

`q2 · i?` · `design · r2`

Blinded human evaluation with eight early-childhood educators on 60 randomly sampled stories, each independently evaluated by three educators (180 instances). The article reports "the average pairwise annotation agreement across the three evaluators per story reaches 0.81".

> "the average pairwise annotation agreement across the three evaluators per story reaches 0.81, supporting the reliability of the proposed developmental annotation framework."

### Sijing Yin 2026 (2)

Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu. (2026). CLARA: Can AI Assess Developmental Appropriateness in Children's Stories?. https://arxiv.org/abs/2610.05783

`q2 · i?` · `design · r2`

Same blinded educator evaluation (Table 7), rated on 1-5 Likert criteria including COG, LAN, and SEL label quality. The article reports "educational interpretabil- ity receives the highest average score", indicating educators found the annotation space educationally meaningful beyond direct age prediction.

> "As shown in Table 7, educational interpretabil- ity receives the highest average score, suggesting that the proposed annotation space provides mean- ingful developmental explanations beyond direct age prediction alone."

## Discussion


## Related Claims
- [Developmental representations remain relatively stable across translated bilingual narratives](clara-bilingual-translation-consistency.md) — related
- [CLARA achieves the highest agreement with blinded human developmental ranking judgments compared with readability and prompting baselines](clara-highest-human-ranking-agreement.md) — related
- [Structured developmental annotation (CLARA) achieves stronger alignment with developmental references than readability-based and direct prompting baselines](clara-outperforms-readability-and-prompting-baselines.md) — related
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md) — related
- [Making trustworthiness metrics and visualizations explicit increased inter-rater reliability among learning engineers evaluating LLM responses](trustworthiness-metrics-visualizations-increase-expert-agreement.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [In disagreement cases, blinded educators more frequently prefer CLARA developmental estimates over publisher recommendations](educators-prefer-clara-over-publisher-labels.md) — related
- [Students who experienced annotation subjectivity firsthand most frequently requested ways to reduce disagreement, indicating they had not internalised disagreement as meaningful signal](students-request-eliminating-disagreement.md) — related
