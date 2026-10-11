---
type: claim
title: Without step-level supervision, neither the student model nor the tutor model can acquire misconceptions regardless of training data size
description: Without step-level supervision, neither the student model nor the tutor model can acquire misconceptions regardless of training data size
id: step-level-supervision-essential-misconception-acquisition
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: naiming-liu-2026
    resource: "https://arxiv.org/abs/2604.00818"
    title: "Naiming Liu, Xinghe Chen, Richard Baraniuk, Mrinmaya Sachan, and Shashank Sonkar. (2026). Misconception Acquisition Dynamics in Large Language Models. https://arxiv.org/abs/2604.00818"
    author: Naiming Liu, Xinghe Chen, Richard Baraniuk, Mrinmaya Sachan, and Shashank Sonkar
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Without step-level supervision, neither the student model nor the tutor model can acquire misconceptions regardless of training data size

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Training on final incorrect answers alone leaves MA below 30% across all three base models even with up to 1600 (student) or 800 (tutor) samples. [→ Naiming Liu 2026](#naiming-liu-2026)

## Evidence

### Naiming Liu 2026

Naiming Liu, Xinghe Chen, Richard Baraniuk, Mrinmaya Sachan, and Shashank Sonkar. (2026). Misconception Acquisition Dynamics in Large Language Models. https://arxiv.org/abs/2604.00818

`q2 · i?` · `causal · r2`

No-steps ablation repeating the acquisition experiments with final answers only; several misconceptions (M3, M5, M8) achieved less than 1% accuracy, and for the tutor model without steps OCA also degraded as training progressed.

> "Across all three base models and all misconceptions, MA remained below 30% even with substantial training data (up to 1600 samples for the student model, 800 for the tutor model)."

## Discussion


## Related Claims
- [On the PRM800K validation dataset, detection rates dropped by 10.5 percentage points when final answers were correct, consistent with the correct answer trap extending beyond the Eedi data](cat-extends-to-prm800k-validation.md) — related
- [Classroom-scale data (5-80 samples per misconception) is insufficient for reliable tutor-model misconception acquisition](tutor-model-sample-efficiency-classroom-insufficient.md) — related
- [Tutor models trained on ten misconceptions simultaneously learn each misconception while overall correct accuracy remains stable or improves (93% to 98%)](tutor-model-multi-misconception-no-accuracy-tradeoff.md) — related
