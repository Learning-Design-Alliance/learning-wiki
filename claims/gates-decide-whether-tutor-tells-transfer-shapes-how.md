---
type: claim
title: The binary reward gates govern whether the tutor tells while the masked near-transfer post-test shapes how it teaches
description: The binary reward gates govern whether the tutor tells while the masked near-transfer post-test shapes how it teaches
id: gates-decide-whether-tutor-tells-transfer-shapes-how
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

# The binary reward gates govern whether the tutor tells while the masked near-transfer post-test shapes how it teaches

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Removing the gates lowers whole-dialog pedagogy (3.66→2.80) and raises handover, while removing near-transfer yields the lowest MathDial win rate (56%) and lowers the Eedi win rate from 72.4% to 65.0%. [→ Jakub Macina 2026](#jakub-macina-2026)

## Evidence

### Jakub Macina 2026

Jakub Macina, Manu Kapur, Mrinmaya Sachan. (2026). The Assistance Dilemma: Learning to Teach via Multi-Turn Reinforcement Learning. [doi:10.48550/arXiv.2610.06446](https://doi.org/10.48550/arXiv.2610.06446)

`q1 · i?` · `causal · r2`

Leave-one-out ablation at 4B (Section 5.2, Table 2), a simulation with a frozen LLM student: "Near-transfer governs out-of-domain transfer", with Ped-RM on MathDial falling from 7.92 to 6.10 without the gates and to 5.25 without near-transfer.

> "Near-transfer governs out-of-domain transfer: without it, the policy has the lowest MathDial win rate (56%), and its Eedi win rate drops from 72.4% to 65.0%."

## Discussion


## Related Claims
- [EDUARDO-27B attains the highest MathTutorBench pedagogical reward-model score and win rate over human teachers on MathDial among all tested tutors, including frontier models, with fewer thinking tokens](eduardo-27b-highest-mathtutorbench-pedagogy-win-rate.md) — related
- [A learning-gain reward alone does not separate teaching from telling: a policy trained without the binary gates hands over the solution in 61% of dialogs at the same simulated gain](learning-gain-reward-alone-does-not-separate-teaching-from-telling.md) — related
- [Adding gate-failure penalties based on predefined pedagogical criteria harms teaching performance and generalization, while training on student improvement alone allows broader capabilities to emerge](gate-penalties-harm-generalization-student-improvement-reward.md) — related
- [Leakage is held, not reduced, for the Qwen3.5/3.8 family, and reduced substantially only for Qwen3-14B](leakage-held-not-reduced-qwen-family-eduardo.md) — related
