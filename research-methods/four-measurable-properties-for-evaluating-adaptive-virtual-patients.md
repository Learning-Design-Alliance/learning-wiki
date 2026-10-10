---
type: research-method
id: four-measurable-properties-for-evaluating-adaptive-virtual-patients
title: Four measurable properties for evaluating adaptive virtual patients
description: "The article proposes four measurable properties an adaptive virtual patient should satisfy, each with its own metric: P1 Responsiveness (state changes in the direction the data predicts), P2 Gradual Build-up (the state \"climbs steadily across the session and only as the user earns it\"), P3 Faithful "
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Four measurable properties for evaluating adaptive virtual patients

> **Research Method** · [All research methods](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article proposes four measurable properties an adaptive virtual patient should satisfy, each with its own metric: P1 Responsiveness (state changes in the direction the data predicts), P2 Gradual Build-up (the state "climbs steadily across the session and only as the user earns it"), P3 Faithful Realization (generated text matches the intended state), and P4 Skill Sensitivity (different users get visibly different sessions). Each property comes with its own metric, so evaluators can locate exactly where a system fails rather than collapse the question into one number.

## Accounts
<!-- How each source describes or uses the method -->
- **Four measurable properties for evaluating adaptive virtual patients: responsiveness, gradual build-up, faithful realization, and skill sensitivity**: The article proposes four measurable properties an adaptive virtual patient should satisfy, each with its own metric: P1 Responsiveness (state changes in the direction the data predicts), P2 Gradual Build-up (the state "climbs steadily across the session and only as the user earns it"), P3 Faithful Realization (generated text matches the intended state), and P4 Skill Sensitivity (different users get visibly different sessions). Each property comes with its own metric, so evaluators can locate exactly where a system fails rather than collapse the question into one number. (Angela Chen et al. (2026))

### Claims
- [The adaptive virtual patient produces a steadily climbing disclosure trajectory across a session while a prompt-only baseline with the same LLM and persona stays flat](../claims/avp-climbing-disclosure-vs-static-flat.md) [+M]
- [In the AVP, per-turn disclosure change responds to trainee exploration but not measurably to trainee empathy, and the static baseline shows no significant joint response](../claims/avp-exploration-drives-disclosure-change.md) [+M]
- [The AVP's generated text matches its intended internal disclosure level about twice as often as the static baseline (0.651 vs. 0.311 agreement)](../claims/avp-faithful-realization-alignment.md) [+M]
- [Higher-skill trainees elicit faster-climbing AVP disclosure trajectories, directionally supporting skill sensitivity, though the formal interaction test is underpowered](../claims/avp-skill-sensitivity-directional.md) [+M]

## Related Research Methods
-

## Key Sources
- Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). The Empirically Grounded Adaptive Virtual Patient for Psychotherapy Training: Disclosure That Responds to Therapist Micro-Skills. https://arxiv.org/abs/2606.10051
