---
type: claim
title: "Step-level credit assignment added to Interleave-RL raises the reasoning score from 46.3% to 66.3% on GeoVAD-Bench"
description: "Step-level credit assignment added to Interleave-RL raises the reasoning score from 46.3% to 66.3% on GeoVAD-Bench"
id: step-level-credit-assignment-boosts-reasoning
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

# Step-level credit assignment added to Interleave-RL raises the reasoning score from 46.3% to 66.3% on GeoVAD-Bench

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Adding step-level credit assignment on top of Interleave-RL yields the strongest ablation performance, with reasoning increasing from 46.3% to 66.3% and answer accuracy from 60.3% to 62.6%. [→ Zhitong Dong 2026](#zhitong-dong-2026)

## Evidence

### Zhitong Dong 2026

Zhitong Dong, Jicai Pan, Yingguo Gao, Jingting Ding, Hao Chen, Jinjie Gu. (2026). Beyond Generation and Accuracy: Diagnosing and Enhancing Visual Chain-of-Thought for Geometry Problem Solving. arXiv preprint. https://arxiv.org/abs/2609.12606

`q2 · i?` · `causal · r2`

Ablation study on GeoVAD-Bench under the Auto-Aux setting comparing base model, SFT-only, Interleave-RL without SCA, and full model (Table 9). The article reports the Reasoning score "increases from 46.3% to 66.3%" when SCA is added.

> "Adding SCA on top of Interleave-RL yields the strongest overall performance. In particular, the Reasoning score increases from 46.3% to 66.3%, indicating that step-level process supervision effectively directs optimization toward correcting individual reasoning steps."

## Discussion


## Related Claims
- [GeoWeave-8B achieves the highest open-source final-answer accuracy and process average on GeoVAD-Bench, gaining 25.3 and 30.4 percentage points over its base model](geoweave-8b-gains-over-basemodel.md) — related
- [Reasoning with ground-truth auxiliary diagrams consistently outperforms reasoning from the original diagram alone on GeoVAD-Bench](gt-aux-consistently-outperforms-no-aux-geometry.md) — related
- [Four process-level error categories account for roughly nine in ten attributed failures in VCoT geometry solving](four-process-error-categories-dominate-failures.md) — related
