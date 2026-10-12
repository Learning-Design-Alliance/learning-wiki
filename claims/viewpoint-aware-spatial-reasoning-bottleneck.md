---
type: claim
title: Viewpoint-aware spatial reasoning is a persistent bottleneck with poor calibration of spatial uncertainty
description: Viewpoint-aware spatial reasoning is a persistent bottleneck with poor calibration of spatial uncertainty
id: viewpoint-aware-spatial-reasoning-bottleneck
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: luyao-zhu-2026
    resource: "https://arxiv.org/abs/2609.19088"
    title: "Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng. (2026). MUSE: Benchmarking Large Vision-Language Models on Multi-modal Understanding in Situated Education. arXiv preprint. https://arxiv.org/abs/2609.19088"
    author: Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Viewpoint-aware spatial reasoning is a persistent bottleneck with poor calibration of spatial uncertainty

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On a Relative Position failure case, 90.0% of models predict a definite lateral relation and 73.3% predict a definite vertical relation despite ground truth specifying none; only 43.3% correctly identify depth, and no model resolves all three dimensions correctly. [→ Luyao Zhu 2026](#luyao-zhu-2026)

## Evidence

### Luyao Zhu 2026

Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng. (2026). MUSE: Benchmarking Large Vision-Language Models on Multi-modal Understanding in Situated Education. arXiv preprint. https://arxiv.org/abs/2609.19088

`q2 · i?` · `design · r2`

Case-based error analysis of Relative Position responses across the evaluated models (Figure 10b). The article reports a strong forced-relation bias and states that models oscillate between asserting definite relations under ambiguous evidence and predicting None while missing valid depth cues, revealing weak viewpoint-aware spatial reasoning.

> "Although the ground truth specifies no definite lateral or vertical relation, 90.0% and 73.3% of models, respectively, predict one; depth reasoning is also unreliable, with only 43.3% correctly identifying the girl as in front of the boy."

## Discussion


## Related Claims
- [Ground-truth validation found the detector identified 55% of human-coded interactions, with misses driven by visual constraints such as teachers outside boundary boxes or obscured](detector-recall-55-percent-visual-constraints.md) — related
- [Generative AI generates responses based on probability and pattern prediction, not reasoning or understanding](genai-probabilistic-prediction-not-reasoning.md) — a broader claim this one bears on
- [LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth](llama-prediction-range-compression.md) — related
- [Reasoning with ground-truth auxiliary diagrams consistently outperforms reasoning from the original diagram alone on GeoVAD-Bench](gt-aux-consistently-outperforms-no-aux-geometry.md) — related
- [All evaluated models struggle with spatial reasoning and precise visual replication on Turtle Graphics tasks](vlms-struggle-spatial-reasoning-visual-precision.md) — a narrower finding that bears on this claim
