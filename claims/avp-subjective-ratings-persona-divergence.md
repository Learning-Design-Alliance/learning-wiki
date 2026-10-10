---
type: claim
title: Post-session subjective ratings favored the adaptive system for the expressive persona but showed a reversed adaptivity disadvantage for the guarded persona
description: Post-session subjective ratings favored the adaptive system for the expressive persona but showed a reversed adaptivity disadvantage for the guarded persona
id: avp-subjective-ratings-persona-divergence
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
sources:
  - id: angela-chen-2026
    resource: "https://arxiv.org/abs/2606.10051"
    title: "Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). The Empirically Grounded Adaptive Virtual Patient for Psychotherapy Training: Disclosure That Responds to Therapist Micro-Skills. https://arxiv.org/abs/2606.10051"
    author: Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu
    q: 2
    i: 2
    kind: causal
    rigour: 2
  - id: angela-chen-2026-2
    resource: "https://arxiv.org/abs/2606.10051"
    title: "Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). The Empirically Grounded Adaptive Virtual Patient for Psychotherapy Training: Disclosure That Responds to Therapist Micro-Skills. https://arxiv.org/abs/2606.10051"
    author: Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu
    q: 2
    i: 2
    kind: design
    rigour: 2
---

# Post-session subjective ratings favored the adaptive system for the expressive persona but showed a reversed adaptivity disadvantage for the guarded persona

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2` · `i2` medium

## Subclaims
`q2 i2` For the expressive persona (Alex), the adaptive condition significantly outscored static on character consistency (d = 0.40) with a medium realism effect (d = 0.47). [→ Angela Chen 2026](#angela-chen-2026)
`q2 i2` For the guarded persona (Sam), the adaptive condition showed a reversed medium-sized disadvantage in perceived adaptivity (d = −0.50), not statistically significant. [→ Angela Chen 2026 (2)](#angela-chen-2026-2)

## Evidence

### Angela Chen 2026

Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). The Empirically Grounded Adaptive Virtual Patient for Psychotherapy Training: Disclosure That Responds to Therapist Micro-Skills. https://arxiv.org/abs/2606.10051

`q2 · i2` · `causal · r2`

Post-interaction survey with 20 participants rating each condition on 5-point Likert items; for Alex the adaptive condition "received numerically higher ratings on all four dimensions". Printed effect sizes d = 0.40 (consistency) and d = 0.47 (realism) code medium impact.

> "the consistency advantage was significant (W= 0 ,p=.046 ,d= 0.40 ), and realism showed a medium effect (d= 0.47 )."

### Angela Chen 2026 (2)

Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). The Empirically Grounded Adaptive Virtual Patient for Psychotherapy Training: Disclosure That Responds to Therapist Micro-Skills. https://arxiv.org/abs/2606.10051

`q2 · i2` · `design · r2`

Same survey, Sam persona: participants rated perceived adaptivity lower for adaptive (M= 2.70) than static (M= 3.20), p=.077, d=−0.50. The article interprets this as participants reading calibrated restraint as unresponsiveness within a ≈10-turn window.

> "a reversed medium-sized disadvantage in perceived adaptivity (M= 2.70 adaptive vs.M= 3.20 static;W= 36 , p=.077 , d=−0.50 )"

## Discussion


## Related Claims
- [The adaptive virtual patient produces a steadily climbing disclosure trajectory across a session while a prompt-only baseline with the same LLM and persona stays flat](avp-climbing-disclosure-vs-static-flat.md) — related
- [In the AVP, per-turn disclosure change responds to trainee exploration but not measurably to trainee empathy, and the static baseline shows no significant joint response](avp-exploration-drives-disclosure-change.md) — related
