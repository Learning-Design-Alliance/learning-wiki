---
type: claim
title: Classroom-scale data (5-80 samples per misconception) is insufficient for reliable tutor-model misconception acquisition
description: Classroom-scale data (5-80 samples per misconception) is insufficient for reliable tutor-model misconception acquisition
id: tutor-model-sample-efficiency-classroom-insufficient
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: naiming-liu-2026
    resource: "https://doi.org/10.48550/arxiv.2604.00818"
    title: "Naiming Liu, Xinghe Chen, Richard Baraniuk, Mrinmaya Sachan, and Shashank Sonkar. (2026). Misconception Acquisition Dynamics in Large Language Models. https://arxiv.org/abs/2604.00818 [doi:10.48550/arxiv.2604.00818](https://doi.org/10.48550/arxiv.2604.00818)"
    author: Naiming Liu, Xinghe Chen, Richard Baraniuk, Mrinmaya Sachan, and Shashank Sonkar
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Classroom-scale data (5-80 samples per misconception) is insufficient for reliable tutor-model misconception acquisition

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` In the small-sample regime, only one of ten misconceptions reaches MA above 90% at 80 samples per misconception. [→ Naiming Liu 2026](#naiming-liu-2026)

## Evidence

### Naiming Liu 2026

Naiming Liu, Xinghe Chen, Richard Baraniuk, Mrinmaya Sachan, and Shashank Sonkar. (2026). Misconception Acquisition Dynamics in Large Language Models. https://arxiv.org/abs/2604.00818 [doi:10.48550/arxiv.2604.00818](https://doi.org/10.48550/arxiv.2604.00818)

`q2 · i?` · `causal · r2`

Small-sample regime experiments (nm in {5,10,20,40,80}) training tutor models on ten misconceptions simultaneously; OCA remained stable but average MA failed to reach the 90% threshold for most misconceptions.

> "With only 80 samples per misconception, only one out of ten misconceptions achieves MA above 90%."

## Discussion


## Related Claims
- [Without step-level supervision, neither the student model nor the tutor model can acquire misconceptions regardless of training data size](step-level-supervision-essential-misconception-acquisition.md) — related
- [Tutor models trained on ten misconceptions simultaneously learn each misconception while overall correct accuracy remains stable or improves (93% to 98%)](tutor-model-multi-misconception-no-accuracy-tradeoff.md) — related
- [Current GenAI tools are not designed to support active learning and their apparent domain expertise is brittle](genai-tools-not-designed-for-active-learning.md) — related
