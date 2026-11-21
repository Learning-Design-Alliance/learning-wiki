---
type: claim
title: Passing the two-phase test implies the AI can identify misconceptions and generate targeted practice problems for at least a (1−ε) fraction of student misconceptions
description: Passing the two-phase test implies the AI can identify misconceptions and generate targeted practice problems for at least a (1−ε) fraction of student misconceptions
id: passing-test-implies-feedback-capability
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

# Passing the two-phase test implies the AI can identify misconceptions and generate targeted practice problems for at least a (1−ε) fraction of student misconceptions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` An AI system that passes the two-phase test can, with probability at least (1−2δ), identify underlying misconceptions, generate new questions testing the same concept, and predict student responses, enabling targeted practice generation for at least a (1−ε) fraction of misconceptions. [→ Shashank Sonkar 2025](#shashank-sonkar-2025)

## Evidence

### Shashank Sonkar 2025

Shashank Sonkar, Naiming Liu, Xinghe Chen, Richard G. Baraniuk. (2025). The Imitation Game for Educational AI. arXiv preprint. [doi:10.48550/arXiv.2502.15127](https://doi.org/10.48550/arXiv.2502.15127)

`q1 · i?` · `theoretical · r2`

Formal result (Theorem 5, Feedback Capability): the proof chains Phase 1 observation, Phase 2 success, and the Misconception Concentration theorem to argue that generating targeted new questions demonstrates feedback capability through practice problem generation.

> "An AI system that passes our two-phase test can both identify and generate targeted practice problems for at least a (1 − ϵ) fraction of student misconceptions with probability at least (1 − 2δ)."

## Discussion


## Related Claims
- [Conditioning predictions on individual students' observed misconceptions differentiates optimal predictions across students with different errors](conditioning-necessary-for-misconception-testing.md) — a narrower finding that bears on this claim
- [Unconditioned single-phase distractor testing converges to the most common misconception and cannot validate understanding of individual student cognition](unconditioned-testing-converges-common-misconception.md) — related
- [Adding a whole-number-strategy misconception to a fraction tutor's student model improved its fit to the data and gave per-student misconception estimates that tracked pre-test errors](misconception-kc-improves-fraction-student-model.md) — related
- [Equal accuracy on fraction comparison items can mask fundamentally different misconceptions](fraction-accuracy-masks-distinct-misconceptions.md) — related
