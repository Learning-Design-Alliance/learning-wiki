---
type: claim
title: In the AVP, per-turn disclosure change responds to trainee exploration but not measurably to trainee empathy, and the static baseline shows no significant joint response
description: In the AVP, per-turn disclosure change responds to trainee exploration but not measurably to trainee empathy, and the static baseline shows no significant joint response
id: avp-exploration-drives-disclosure-change
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
    kind: design
    rigour: 2
---

# In the AVP, per-turn disclosure change responds to trainee exploration but not measurably to trainee empathy, and the static baseline shows no significant joint response

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` OLS regression of per-turn disclosure change found exploration drove AVP state change while the empathy coefficient was effectively zero; in the static VP exploration was only marginal and the joint model not significant. [→ Angela Chen 2026](#angela-chen-2026)

## Evidence

### Angela Chen 2026

Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). The Empirically Grounded Adaptive Virtual Patient for Psychotherapy Training: Disclosure That Responds to Therapist Micro-Skills. https://arxiv.org/abs/2606.10051

`q2 · i?` · `design · r2`

OLS regression with cluster-robust SEs on session (530 turn-pairs, 40 AVP sessions; 423 turn-pairs, 40 SVP sessions) of evaluated disclosure change on empathy total and exploration. The quote shows "exploration drives the change ( ˆβexp = +0.281"; the unstandardized coefficients are not standardized effect sizes, so impact is null.

> "In A VP, exploration drives the change ( ˆβexp = +0.281 , p<10 −6) while the empathy coefficient is effectively zero (ˆβemp = +0.004,p=.87 )"

## Discussion


## Related Claims
- [The adaptive virtual patient produces a steadily climbing disclosure trajectory across a session while a prompt-only baseline with the same LLM and persona stays flat](avp-climbing-disclosure-vs-static-flat.md) — related
- [The AVP's generated text matches its intended internal disclosure level about twice as often as the static baseline (0.651 vs. 0.311 agreement)](avp-faithful-realization-alignment.md) — related
- [Higher-skill trainees elicit faster-climbing AVP disclosure trajectories, directionally supporting skill sensitivity, though the formal interaction test is underpowered](avp-skill-sensitivity-directional.md) — related
- [The deployed empirically motivated weight vector outperforms equal, empathy-only, and exploration-only weightings in evaluator agreement, with exploration carrying most of the adaptive signal](avp-weight-ablation-exploration-dominant.md) — related
- [Post-session subjective ratings favored the adaptive system for the expressive persona but showed a reversed adaptivity disadvantage for the guarded persona](avp-subjective-ratings-persona-divergence.md) — related
- [Expert evaluation found the virtual patient realistic and immediate ACT feedback increased therapists' awareness of intervention choices](expert-evaluation-realism-and-feedback-awareness.md) — related
- [In a self-selected survey, students favored delayed disclosure and agency, but 39.3% found the system too indirect and 42.9% reported repetition](staged-feedback-survey-perceptions.md) — related
