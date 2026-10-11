---
type: claim
title: "Post-training alignment methods may induce sycophancy that deteriorates GenAI models' ability to disagree and push back"
description: "Post-training alignment methods may induce sycophancy that deteriorates GenAI models' ability to disagree and push back"
id: sycophancy-limits-genai-pushback
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: mutlu-cukurova-2025
    resource: "https://arxiv.org/abs/2511.19580"
    title: "Mutlu Cukurova, Wannapon Suraworachet, Qi Zhou, and Sahan Bulathwela. (2025). Towards Synergistic Teacher-AI Interactions with Generative Artificial Intelligence. https://arxiv.org/abs/2511.19580"
    author: Mutlu Cukurova, Wannapon Suraworachet, Qi Zhou, and Sahan Bulathwela
    q: 1
    i: "?"
---

# Post-training alignment methods may induce sycophancy that deteriorates GenAI models' ability to disagree and push back

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q1` argument or single case

## Subclaims
`q1 i?` The chapter argues that post-training methods like RLHF and DPO arguably lead to emergent sycophancy, deteriorating models' ability to disagree with users, and that probabilistic GenAI models lack an internal epistemic stance for authentic push back. [→ Mutlu Cukurova 2025](#mutlu-cukurova-2025)

## Evidence

### Mutlu Cukurova 2025

Mutlu Cukurova, Wannapon Suraworachet, Qi Zhou, and Sahan Bulathwela. (2025). Towards Synergistic Teacher-AI Interactions with Generative Artificial Intelligence. https://arxiv.org/abs/2511.19580

`q1 · i?`

Theoretical argument, not an empirical test: the chapter reasons that semantic relationship mining and probabilistic models limit authentic push back because there is no internal epistemic stance, and that push-back capacity is double-edged, risking disregard of valid feedback without governance mechanisms.

> "While these have benefits for human alignment, it is arguable that they also lead to emergent features like sycophancy which causes the deterioration of models' ability to disagree andpush backwhen engaging with human users"

## Discussion


## Related Claims
- [GRPO with an SFS-aligned reward yields more consistent improvements than DPO, achieving the highest SFS overall](grpo-sfs-reward-beats-dpo.md) — related
- [Sycophantic failure manifests as indiscriminate correct flips rather than explicit sycophantic agreement, and SFT shifts behavior toward pushback and maintain under non-targeted feedback](sycophancy-via-correct-flip-not-verbal-agreement.md) — related
- [The sycophancy-focused intervention significantly reduced the assistant's positional mirroring of incorrect user rankings and rank-order alignment](intervention-reduced-positional-mimicry.md) — related
- [Supervised fine-tuning on misconception-faithful demonstrations sharply improves SFS (up to +0.555 on Malrule for Qwen3-4B)](sft-improves-selective-update-behavior.md) — related
- [Both RL stages are needed: removing DPO and GRPO training causes the largest performance drop in student simulation](rl-stages-needed-faithful-student-simulation.md) — related
