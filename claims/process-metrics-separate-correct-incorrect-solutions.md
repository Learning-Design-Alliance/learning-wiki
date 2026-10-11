---
type: claim
title: Correct final answers are associated with stronger performance on all four process-level metrics, with reasoning-process correctness showing the clearest separation
description: Correct final answers are associated with stronger performance on all four process-level metrics, with reasoning-process correctness showing the clearest separation
id: process-metrics-separate-correct-incorrect-solutions
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
    kind: causal
    rigour: 2
---

# Correct final answers are associated with stronger performance on all four process-level metrics, with reasoning-process correctness showing the clearest separation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Correct solutions outperform incorrect solutions on perception, auxiliary quality, utilization, and reasoning for both evaluated models, with the largest deltas in reasoning (46.9 and 53.5 percentage points). [→ Zhitong Dong 2026](#zhitong-dong-2026)

## Evidence

### Zhitong Dong 2026

Zhitong Dong, Jicai Pan, Yingguo Gao, Jingting Ding, Hao Chen, Jinjie Gu. (2026). Beyond Generation and Accuracy: Diagnosing and Enhancing Visual Chain-of-Thought for Geometry Problem Solving. arXiv preprint. https://arxiv.org/abs/2609.12606

`q2 · i?` · `causal · r2`

Stage-wise diagnostic comparison of L1-L4 metrics between incorrect and correct solutions (Table 5). The article reports "Correct solutions outperform incorrect solutions on all four process-level metrics"; printed deltas include +46.9 (MathCanvas-7B) and +53.5 (CodePlot-CoT-32B) for reasoning.

> "Correct solutions outperform incorrect solutions on all four process-level metrics for both models."

## Discussion


## Related Claims
- [Four process-level error categories account for roughly nine in ten attributed failures in VCoT geometry solving](four-process-error-categories-dominate-failures.md) — related
- [Reasoning with ground-truth auxiliary diagrams consistently outperforms reasoning from the original diagram alone on GeoVAD-Bench](gt-aux-consistently-outperforms-no-aux-geometry.md) — related
- [GeoWeave-8B achieves the highest open-source final-answer accuracy and process average on GeoVAD-Bench, gaining 25.3 and 30.4 percentage points over its base model](geoweave-8b-gains-over-basemodel.md) — related
