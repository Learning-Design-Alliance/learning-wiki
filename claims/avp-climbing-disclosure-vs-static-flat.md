---
type: claim
title: The adaptive virtual patient produces a steadily climbing disclosure trajectory across a session while a prompt-only baseline with the same LLM and persona stays flat
description: The adaptive virtual patient produces a steadily climbing disclosure trajectory across a session while a prompt-only baseline with the same LLM and persona stays flat
id: avp-climbing-disclosure-vs-static-flat
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: angela-chen-2026
    resource: "https://arxiv.org/abs/2606.10051"
    title: "Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). The Empirically Grounded Adaptive Virtual Patient for Psychotherapy Training: Disclosure That Responds to Therapist Micro-Skills. https://arxiv.org/abs/2606.10051"
    author: Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The adaptive virtual patient produces a steadily climbing disclosure trajectory across a session while a prompt-only baseline with the same LLM and persona stays flat

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` In a within-subjects human study, AVP disclosure climbed from guarded toward medium over the session while the static prompt-only VP remained nearly flat. [→ Angela Chen 2026](#angela-chen-2026)

## Evidence

### Angela Chen 2026

Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). The Empirically Grounded Adaptive Virtual Patient for Psychotherapy Training: Disclosure That Responds to Therapist Micro-Skills. https://arxiv.org/abs/2606.10051

`q2 · i?` · `causal · r2`

Within-subjects evaluation (20 clinicians and trainees, 80 sessions, 1,033 turns) comparing AVP and a static prompt-only VP; decile-averaged evaluator-coded disclosure showed "the A VP climbs from ≈1.0 (Guarded)" while the SVP stayed near its starting level. No standardized effect size is printed for this trajectory contrast.

> "the A VP climbs from ≈1.0 (Guarded) at the start of a session to ≈2.0 (Medium Disclosure) by the 80% mark, while the SVP starts already at≈1.7 and remains nearly flat."

## Discussion


## Related Claims
- [Higher-skill trainees elicit faster-climbing AVP disclosure trajectories, directionally supporting skill sensitivity, though the formal interaction test is underpowered](avp-skill-sensitivity-directional.md) — related
- [Post-session subjective ratings favored the adaptive system for the expressive persona but showed a reversed adaptivity disadvantage for the guarded persona](avp-subjective-ratings-persona-divergence.md) — related
- [The AVP's generated text matches its intended internal disclosure level about twice as often as the static baseline (0.651 vs. 0.311 agreement)](avp-faithful-realization-alignment.md) — related
- [In the AVP, per-turn disclosure change responds to trainee exploration but not measurably to trainee empathy, and the static baseline shows no significant joint response](avp-exploration-drives-disclosure-change.md) — related
- [The deployed empirically motivated weight vector outperforms equal, empathy-only, and exploration-only weightings in evaluator agreement, with exploration carrying most of the adaptive signal](avp-weight-ablation-exploration-dominant.md) — related
- [AURA's within-session reinforcement learning improved composite response quality over non-adaptive baselines (p = 0.044, d = 0.66), with fewer specification prompts and more validation behavior](aura-rl-improves-response-quality.md) — related
- [Standalone LLM tutors replicate Phase II's profile: strong single-interaction intelligence without systematic control over the learning trajectory](standalone-llm-tutors-lack-trajectory-control.md) — related
- [Expert evaluation found the virtual patient realistic and immediate ACT feedback increased therapists' awareness of intervention choices](expert-evaluation-realism-and-feedback-awareness.md) — related
