---
type: claim
title: Unconditioned single-phase distractor testing converges to the most common misconception and cannot validate understanding of individual student cognition
description: Unconditioned single-phase distractor testing converges to the most common misconception and cannot validate understanding of individual student cognition
id: unconditioned-testing-converges-common-misconception
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: shashank-sonkar-2025
    resource: "https://doi.org/10.48550/arXiv.2502.15127"
    title: "Shashank Sonkar, Naiming Liu, Xinghe Chen, Richard G. Baraniuk. (2025). The Imitation Game for Educational AI. arXiv preprint. [doi:10.48550/arXiv.2502.15127](https://doi.org/10.48550/arXiv.2502.15127)"
    author: Shashank Sonkar, Naiming Liu, Xinghe Chen, Richard G. Baraniuk
    q: 1
    i: "?"
    kind: theoretical
    rigour: 2
---

# Unconditioned single-phase distractor testing converges to the most common misconception and cannot validate understanding of individual student cognition

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In an unconditioned test where distractors are generated without observing prior student responses, both AI and human generators rationally converge to targeting the most common misconception, reducing the test to population-level pattern matching. [→ Shashank Sonkar 2025](#shashank-sonkar-2025)

## Evidence

### Shashank Sonkar 2025

Shashank Sonkar, Naiming Liu, Xinghe Chen, Richard G. Baraniuk. (2025). The Imitation Game for Educational AI. arXiv preprint. [doi:10.48550/arXiv.2502.15127](https://doi.org/10.48550/arXiv.2502.15127)

`q1 · i?` · `theoretical · r2`

Formal derivation (Theorem 6) showing expected selection rate is maximized by targeting the most common misconception, "with equality achieved only when targeting m∗." The authors call the resulting problem "False Equivalence": an AI could pass by learning population-level statistics without modeling individual reasoning.

> "Given a question q with misconception set M (q) = {m1, ..., mk} where P (mi) represents the probability of misconception mi in the student population, both AI and human experts will rationally converge to targeting m∗ = arg maxmi∈M (q) P (mi)."

## Discussion


## Related Claims
- [Conditioning predictions on individual students' observed misconceptions differentiates optimal predictions across students with different errors](conditioning-necessary-for-misconception-testing.md) — related
- [Passing the two-phase test implies the AI can identify misconceptions and generate targeted practice problems for at least a (1−ε) fraction of student misconceptions](passing-test-implies-feedback-capability.md) — related
- [Statistical sampling theory shows high-confidence validation of misconception tracking is feasible with approximately 100 students and roughly 25 questions per student](sampling-theory-feasible-validation-student-counts.md) — related
- [LLMs predict common distractors above chance but fall 15 percentage points below chance at predicting which errors students rarely select](llm-distractor-prediction-asymmetry.md) — related
- [Candidate selection is a second bottleneck: an oracle ranker over proposed candidates substantially raises proportional match, and plausibility checks reject some valid distractors](candidate-selection-loss-oracle-ranker.md) — related
