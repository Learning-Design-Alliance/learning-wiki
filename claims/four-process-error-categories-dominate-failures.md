---
type: claim
title: Four process-level error categories account for roughly nine in ten attributed failures in VCoT geometry solving
description: Four process-level error categories account for roughly nine in ten attributed failures in VCoT geometry solving
id: four-process-error-categories-dominate-failures
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

# Four process-level error categories account for roughly nine in ten attributed failures in VCoT geometry solving

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Perception, construction, unused-construction, and reasoning errors account for 93.1% of attributed errors for MathCanvas-7B and 89.7% for CodePlot-CoT-32B. [→ Zhitong Dong 2026](#zhitong-dong-2026)

## Evidence

### Zhitong Dong 2026

Zhitong Dong, Jicai Pan, Yingguo Gao, Jingting Ding, Hao Chen, Jinjie Gu. (2026). Beyond Generation and Accuracy: Diagnosing and Enhancing Visual Chain-of-Thought for Geometry Problem Solving. arXiv preprint. https://arxiv.org/abs/2609.12606

`q2 · i?` · `causal · r2`

Error-attribution analysis of incorrect solutions on GeoVAD-Bench (Figure 3, Section 3.5.2). The article reports the four process-level categories "account for 93.1% of the attributed errors for MathCanvas-7B and 89.7% for CodePlot-CoT-32B", with remaining cases grouped as Others.

> "perception, auxiliary-diagram construction, unused construction, and reasoning errors account for 93.1% of the attributed errors for MathCanvas-7B and 89.7% for CodePlot-CoT-32B, respectively"

## Discussion


## Related Claims
- [Correct final answers are associated with stronger performance on all four process-level metrics, with reasoning-process correctness showing the clearest separation](process-metrics-separate-correct-incorrect-solutions.md) — related
- [In a contrastive audit, visual misreading is the dominant failure mode for non-reasoning models on items reasoning models solve](visual-misread-dominant-non-reasoning-failure.md) — related
- [Step-level credit assignment added to Interleave-RL raises the reasoning score from 46.3% to 66.3% on GeoVAD-Bench](step-level-credit-assignment-boosts-reasoning.md) — related
