---
type: claim
title: Leakage is held, not reduced, for the Qwen3.5/3.8 family, and reduced substantially only for Qwen3-14B
description: Leakage is held, not reduced, for the Qwen3.5/3.8 family, and reduced substantially only for Qwen3-14B
id: leakage-held-not-reduced-qwen-family-eduardo
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jakub-macina-2026
    resource: "https://doi.org/10.48550/arXiv.2610.06446"
    title: "Jakub Macina, Manu Kapur, Mrinmaya Sachan. (2026). The Assistance Dilemma: Learning to Teach via Multi-Turn Reinforcement Learning. [doi:10.48550/arXiv.2610.06446](https://doi.org/10.48550/arXiv.2610.06446)"
    author: Jakub Macina, Manu Kapur, Mrinmaya Sachan
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Leakage is held, not reduced, for the Qwen3.5/3.8 family, and reduced substantially only for Qwen3-14B

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Eduardo-27B leaks in 9% of dialogs, the same as its base, while training reduces leakage substantially only for Qwen3-14B, whose base hands over the solution in 98% of dialogs, reduced to 32%. [→ Jakub Macina 2026](#jakub-macina-2026)

## Evidence

### Jakub Macina 2026

Jakub Macina, Manu Kapur, Mrinmaya Sachan. (2026). The Assistance Dilemma: Learning to Teach via Multi-Turn Reinforcement Learning. [doi:10.48550/arXiv.2610.06446](https://doi.org/10.48550/arXiv.2610.06446)

`q1 · i?` · `design · r2`

Training-environment and evaluation analysis in Section 5.1 (Table 1) reporting dialog leakage rates: "Eduardo-27B leaks in 9% of dialogs, the same as its base" and Eduardo-4B and 9B leak in 25–31%, about four times the frontier rate of 5–7%.

> "Training reduces leakage substantially only for Qwen3-14B, whose base hands over the solution in 98% of dialogs (to 32%)."

## Discussion


## Related Claims
- [EDUARDO-27B is the strongest TutorMoments tutor under a plain prompt, but frontier models overtake it when given the evaluation-aware rubric prompt](eduardo-strongest-plain-prompt-frontier-overtake-with-rubric.md) — related
- [Supervised fine-tuning on SocraticEdu provides the largest single-step SE gain (+0.200) but still leaks target terms in 26.7% of dialogues](sft-largest-single-step-gain-but-still-leaks.md) — related
- [A learning-gain reward alone does not separate teaching from telling: a policy trained without the binary gates hands over the solution in 61% of dialogs at the same simulated gain](learning-gain-reward-alone-does-not-separate-teaching-from-telling.md) — related
- [GRPO alignment without the directness reward raises Socratic scaffolding effectiveness from 0.300 to 0.633 and cuts keyword leakage from 30.0% to 13.3% against the prompt-only base on held-out questions](grpo-without-directness-raises-socratic-scaffolding-effectiveness.md) — related
- [The leakage manipulation fires: ConvTutor leaks far more than PedTutor on the primary base, while probe accuracy saturates and cannot distinguish conditions](leakage-manipulation-check-probe-ceiling.md) — related
- [EDUARDO-27B attains the highest MathTutorBench pedagogical reward-model score and win rate over human teachers on MathDial among all tested tutors, including frontier models, with fewer thinking tokens](eduardo-27b-highest-mathtutorbench-pedagogy-win-rate.md) — related
- [The binary reward gates govern whether the tutor tells while the masked near-transfer post-test shapes how it teaches](gates-decide-whether-tutor-tells-transfer-shapes-how.md) — related
- [Ped. Think Reward achieves the best tutoring performance among trained models, and Thinking Reward is most effective when combined with pedagogical prompting](thinking-reward-needs-pedagogical-prompting.md) — related
