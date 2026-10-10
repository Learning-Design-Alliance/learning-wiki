---
type: claim
title: "The AVP's generated text matches its intended internal disclosure level about twice as often as the static baseline (0.651 vs. 0.311 agreement)"
description: "The AVP's generated text matches its intended internal disclosure level about twice as often as the static baseline (0.651 vs."
id: avp-faithful-realization-alignment
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

# The AVP's generated text matches its intended internal disclosure level about twice as often as the static baseline (0.651 vs. 0.311 agreement)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Agreement between the system's intended disclosure level and an independent evaluator's judgment of the generated utterance was 0.651 for the AVP versus 0.311 for the static VP. [→ Angela Chen 2026](#angela-chen-2026)

## Evidence

### Angela Chen 2026

Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). The Empirically Grounded Adaptive Virtual Patient for Psychotherapy Training: Disclosure That Responds to Therapist Micro-Skills. https://arxiv.org/abs/2606.10051

`q2 · i?` · `design · r2`

Evaluation of state-output alignment using an independent LLM disclosure-labeler as ground truth across the 80 recorded sessions; "Adaptive overall agreement is 0.651 vs. Static’s 0.311". Per-level precision for AVP H-level was low (.326), printed in Table 7.

> "Figure 3 shows the confusion matrices behind the alignment metric: Adaptive overall agreement is 0.651 vs. Static’s 0.311."

## Discussion


## Related Claims
- [The adaptive virtual patient produces a steadily climbing disclosure trajectory across a session while a prompt-only baseline with the same LLM and persona stays flat](avp-climbing-disclosure-vs-static-flat.md) — related
- [In the AVP, per-turn disclosure change responds to trainee exploration but not measurably to trainee empathy, and the static baseline shows no significant joint response](avp-exploration-drives-disclosure-change.md) — related
- [The deployed empirically motivated weight vector outperforms equal, empathy-only, and exploration-only weightings in evaluator agreement, with exploration carrying most of the adaptive signal](avp-weight-ablation-exploration-dominant.md) — related
