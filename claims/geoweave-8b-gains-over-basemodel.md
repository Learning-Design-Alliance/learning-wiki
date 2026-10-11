---
type: claim
title: GeoWeave-8B achieves the highest open-source final-answer accuracy and process average on GeoVAD-Bench, gaining 25.3 and 30.4 percentage points over its base model
description: GeoWeave-8B achieves the highest open-source final-answer accuracy and process average on GeoVAD-Bench, gaining 25.3 and 30.4 percentage points over its base model
id: geoweave-8b-gains-over-basemodel
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: zhitong-dong-2026
    resource: "https://arxiv.org/abs/2609.12606"
    title: "Zhitong Dong, Jicai Pan, Yingguo Gao, Jingting Ding, Hao Chen, Jinjie Gu. (2026). Beyond Generation and Accuracy: Diagnosing and Enhancing Visual Chain-of-Thought for Geometry Problem Solving. arXiv preprint. https://arxiv.org/abs/2609.12606"
    author: Zhitong Dong, Jicai Pan, Yingguo Gao, Jingting Ding, Hao Chen, Jinjie Gu
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: zhitong-dong-2026-2
    resource: "https://arxiv.org/abs/2609.12606"
    title: "Zhitong Dong, Jicai Pan, Yingguo Gao, Jingting Ding, Hao Chen, Jinjie Gu. (2026). Beyond Generation and Accuracy: Diagnosing and Enhancing Visual Chain-of-Thought for Geometry Problem Solving. arXiv preprint. https://arxiv.org/abs/2609.12606"
    author: Zhitong Dong, Jicai Pan, Yingguo Gao, Jingting Ding, Hao Chen, Jinjie Gu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GeoWeave-8B achieves the highest open-source final-answer accuracy and process average on GeoVAD-Bench, gaining 25.3 and 30.4 percentage points over its base model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` GeoWeave-8B reaches 62.6% answer accuracy and 82.9% process average, improving over SenseNova-U1-8B by 25.3 and 30.4 percentage points, with coordinated gains across all four process metrics. [→ Zhitong Dong 2026](#zhitong-dong-2026)
`q2 i?` GeoWeave-8B outperforms MathCanvas-7B on all four conventional mathematical reasoning benchmarks and achieves higher Math-VR PS and AC than both compared methods. [→ Zhitong Dong 2026 (2)](#zhitong-dong-2026-2)

## Evidence

### Zhitong Dong 2026

Zhitong Dong, Jicai Pan, Yingguo Gao, Jingting Ding, Hao Chen, Jinjie Gu. (2026). Beyond Generation and Accuracy: Diagnosing and Enhancing Visual Chain-of-Thought for Geometry Problem Solving. arXiv preprint. https://arxiv.org/abs/2609.12606

`q2 · i?` · `design · r2`

Main comparison on GeoVAD-Bench under Auto-Aux (Table 7, Section 6.2). The article reports GeoWeave-8B "achieves the highest final-answer accuracy, reaching 62.6%" and 82.9% process average, with per-dimension gains of 5.8, 51.0, 22.0, and 43.0 percentage points.

> "Among the open-source models, GeoWeave-8B achieves the highest final-answer accuracy, reaching 62.6%. It improves over the SenseNova-U1-8B baseline by 25.3 percentage points and surpasses every other open-source model listed in Table 7."

### Zhitong Dong 2026 (2)

Zhitong Dong, Jicai Pan, Yingguo Gao, Jingting Ding, Hao Chen, Jinjie Gu. (2026). Beyond Generation and Accuracy: Diagnosing and Enhancing Visual Chain-of-Thought for Geometry Problem Solving. arXiv preprint. https://arxiv.org/abs/2609.12606

`q2 · i?` · `design · r2`

Generalization evaluation on public benchmarks (Table 8, Section 6.3). The article reports GeoWeave-8B "outperforms MathCanvas-7B on all four conventional mathematical reasoning benchmarks" and higher Math-VR PS (64.7) and AC (41.4) than both compared methods.

> "GeoWeave-8B outperforms MathCanvas-7B on all four conventional mathematical reasoning benchmarks. On Math-VR, GeoWeave-8B also achieves higher PS and AC than both MathCanvas-7B and CodePlot-CoT-32B."

## Discussion


## Related Claims
- [Reasoning with ground-truth auxiliary diagrams consistently outperforms reasoning from the original diagram alone on GeoVAD-Bench](gt-aux-consistently-outperforms-no-aux-geometry.md) — related
- [Step-level credit assignment added to Interleave-RL raises the reasoning score from 46.3% to 66.3% on GeoVAD-Bench](step-level-credit-assignment-boosts-reasoning.md) — related
- [Correct final answers are associated with stronger performance on all four process-level metrics, with reasoning-process correctness showing the clearest separation](process-metrics-separate-correct-incorrect-solutions.md) — related
