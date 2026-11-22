---
type: claim
title: "A learning-gain reward alone does not separate teaching from telling: a policy trained without the binary gates hands over the solution in 61% of dialogs at the same simulated gain"
description: "A learning-gain reward alone does not separate teaching from telling: a policy trained without the binary gates hands over the solution in 61% of dialogs at the same simulated gain"
id: learning-gain-reward-alone-does-not-separate-teaching-from-telling
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: jakub-macina-2026
    resource: "https://doi.org/10.48550/arXiv.2610.06446"
    title: "Jakub Macina, Manu Kapur, Mrinmaya Sachan. (2026). The Assistance Dilemma: Learning to Teach via Multi-Turn Reinforcement Learning. [doi:10.48550/arXiv.2610.06446](https://doi.org/10.48550/arXiv.2610.06446)"
    author: Jakub Macina, Manu Kapur, Mrinmaya Sachan
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# A learning-gain reward alone does not separate teaching from telling: a policy trained without the binary gates hands over the solution in 61% of dialogs at the same simulated gain

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Under a masked near-transfer post-test, telling no longer raises the reward, yet the tutor keeps telling: without the binary gates the policy hands over the solution in 61% of dialogs with learning gain unchanged. [→ Jakub Macina 2026](#jakub-macina-2026)

## Evidence

### Jakub Macina 2026

Jakub Macina, Manu Kapur, Mrinmaya Sachan. (2026). The Assistance Dilemma: Learning to Teach via Multi-Turn Reinforcement Learning. [doi:10.48550/arXiv.2610.06446](https://doi.org/10.48550/arXiv.2610.06446)

`q1 · i?` · `causal · r2`

Leave-one-out ablation at 4B in the RL training environment (n=494 held-out problems), a simulation with a frozen LLM student, reported in Section 5.2: "All four arms lie within0.03on∆ transfer" so handover is reward-neutral and only the gates make it costly.

> "All four arms lie within0.03on∆ transfer (+0.23to+0.25), even though the policy hands over the solution in 61% of dialogs without the gates (vs. 31%) and in 47% without near-transfer."

## Discussion


## Related Claims
- [The binary reward gates govern whether the tutor tells while the masked near-transfer post-test shapes how it teaches](gates-decide-whether-tutor-tells-transfer-shapes-how.md) — related
- [Leakage is held, not reduced, for the Qwen3.5/3.8 family, and reduced substantially only for Qwen3-14B](leakage-held-not-reduced-qwen-family-eduardo.md) — related
- [An analytical chapter identifies reward hacking, engagement optimization over learning, and scaffolding dependency as risks of RL policies with poorly specified rewards](rl-reward-misalignment-failure-modes.md) — a broader claim this one bears on
- [An engagement-optimized RL tutor exhibits reward hacking, achieving the highest cumulative reward while producing minimal learning and a 70.8% behavioral-safety violation rate](engagement-optimized-rl-tutor-reward-hacking.md) — related
- [In a simulated tutoring agent, removing the behavioral-safety constraint (C3) appears to cause collapse to near-single-action policies, which the authors read as C3 being the most influential safeguard, though its ablation does not differ significantly from removing C1 in RHSI](c3-ablation-policy-collapse.md) — related
- [Adding gate-failure penalties based on predefined pedagogical criteria harms teaching performance and generalization, while training on student improvement alone allows broader capabilities to emerge](gate-penalties-harm-generalization-student-improvement-reward.md) — related
- [Optimizing immediate task success trades off against pedagogical support: pushing solve rate raises answer leakage](solve-rate-pedagogy-tradeoff-answer-leakage.md) — related
