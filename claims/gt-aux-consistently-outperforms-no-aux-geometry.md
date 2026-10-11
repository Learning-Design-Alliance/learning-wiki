---
type: claim
title: Reasoning with ground-truth auxiliary diagrams consistently outperforms reasoning from the original diagram alone on GeoVAD-Bench
description: Reasoning with ground-truth auxiliary diagrams consistently outperforms reasoning from the original diagram alone on GeoVAD-Bench
id: gt-aux-consistently-outperforms-no-aux-geometry
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

# Reasoning with ground-truth auxiliary diagrams consistently outperforms reasoning from the original diagram alone on GeoVAD-Bench

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Across evaluated models, final-answer accuracy under GT-Aux consistently exceeds No-Aux, with reference-diagram gains of 3.0 to 7.0 percentage points as printed in Table 4. [→ Zhitong Dong 2026](#zhitong-dong-2026)

## Evidence

### Zhitong Dong 2026

Zhitong Dong, Jicai Pan, Yingguo Gao, Jingting Ding, Hao Chen, Jinjie Gu. (2026). Beyond Generation and Accuracy: Diagnosing and Enhancing Visual Chain-of-Thought for Geometry Problem Solving. arXiv preprint. https://arxiv.org/abs/2609.12606

`q2 · i?` · `causal · r2`

Benchmark evaluation on GeoVAD-Bench comparing final-answer accuracy under three controlled auxiliary conditions (Table 4). The article reports "GT-Aux consistently outperforms No-Aux"; printed reference gains are +3.3 (GPT-5.4 + GPT-image2), +3.0 (Qwen3-VL-8B + Qwen-image-edit), and +7.0 (SenseNova-U1-8B) percentage points.

> "Across the evaluated models, GT-Aux consistently outperforms No-Aux, showing that validated auxiliary diagrams provide useful information for geometry problem solving."

## Discussion


## Related Claims
- [GeoWeave-8B achieves the highest open-source final-answer accuracy and process average on GeoVAD-Bench, gaining 25.3 and 30.4 percentage points over its base model](geoweave-8b-gains-over-basemodel.md) — related
- [Step-level credit assignment added to Interleave-RL raises the reasoning score from 46.3% to 66.3% on GeoVAD-Bench](step-level-credit-assignment-boosts-reasoning.md) — related
- [Step-linked visual grounding externalizes spatial reasoning: synchronized diagrams that reveal auxiliary lines step by step reduce split-attention effort](step-linked-visualization-externalizes-reasoning.md) — related
- [Correct final answers are associated with stronger performance on all four process-level metrics, with reasoning-process correctness showing the clearest separation](process-metrics-separate-correct-incorrect-solutions.md) — related
