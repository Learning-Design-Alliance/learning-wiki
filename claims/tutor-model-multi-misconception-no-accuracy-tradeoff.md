---
type: claim
title: "Tutor models trained on ten misconceptions simultaneously learn each misconception while overall correct accuracy remains stable or improves (93% to 98%)"
description: "Tutor models trained on ten misconceptions simultaneously learn each misconception while overall correct accuracy remains stable or improves (93% to 98%)"
id: tutor-model-multi-misconception-no-accuracy-tradeoff
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

# Tutor models trained on ten misconceptions simultaneously learn each misconception while overall correct accuracy remains stable or improves (93% to 98%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` With sufficient samples (100-800 per misconception), tutor-model MA increases while OCA remains stable or improves across all three base models. [→ Naiming Liu 2026](#naiming-liu-2026)

## Evidence

### Naiming Liu 2026

Naiming Liu, Xinghe Chen, Richard Baraniuk, Mrinmaya Sachan, and Shashank Sonkar. (2026). Misconception Acquisition Dynamics in Large Language Models. https://arxiv.org/abs/2604.00818 [doi:10.48550/arxiv.2604.00818](https://doi.org/10.48550/arxiv.2604.00818)

`q2 · i?` · `causal · r2`

Tutor-model instruction-tuning on ten misconceptions (Mset of M1, M2, M6, M8, M11, M12, M19, M20, M21, M22) across Llama-3.1-8B, Phi-4, and Qwen-3; the article reports OCA rising from 93% to 98% with no effect size printed.

> "whentrainedwithsufficientsamples(100–800),thetutormodelexhibitsincreasing MA while OCA remains stable or evenimproves, rising from 93% to 98% across all three models (Llama, Phi, Qwen)."

## Discussion


## Related Claims
- [Mixing correct examples into student-model training resolves the misconception-accuracy trade-off, with correct examples as low as 25% preserving both properties](mixing-correct-examples-resolves-student-model-tradeoff.md) — related
- [Classroom-scale data (5-80 samples per misconception) is insufficient for reliable tutor-model misconception acquisition](tutor-model-sample-efficiency-classroom-insufficient.md) — related
- [Without step-level supervision, neither the student model nor the tutor model can acquire misconceptions regardless of training data size](step-level-supervision-essential-misconception-acquisition.md) — related
- [Instruction-tuning a student model on a single misconception overgeneralizes the error across problems and degrades correct-solving accuracy](student-model-misconception-overgeneralization-degrades-accuracy.md) — related
