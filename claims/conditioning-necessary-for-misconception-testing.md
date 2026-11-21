---
type: claim
title: "Conditioning predictions on individual students' observed misconceptions differentiates optimal predictions across students with different errors"
description: "Conditioning predictions on individual students' observed misconceptions differentiates optimal predictions across students with different errors"
id: conditioning-necessary-for-misconception-testing
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

# Conditioning predictions on individual students' observed misconceptions differentiates optimal predictions across students with different errors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Given two students with different misconceptions observed in Phase 1, optimal Phase 2 predictions for the same new question differ, so success cannot be achieved through population-level statistics alone. [→ Shashank Sonkar 2025](#shashank-sonkar-2025)

## Evidence

### Shashank Sonkar 2025

Shashank Sonkar, Naiming Liu, Xinghe Chen, Richard G. Baraniuk. (2025). The Imitation Game for Educational AI. arXiv preprint. [doi:10.48550/arXiv.2502.15127](https://doi.org/10.48550/arXiv.2502.15127)

`q1 · i?` · `theoretical · r2`

Formal proof (Theorem 7, Prediction Differentiation) that conditioned predictions maximize P(A′(s, q′) chosen | A(s, q)), which differs based on the Phase 1 misconception. The article argues this forces three capabilities: understanding individual reasoning, generating new questions, and predicting misconception manifestation in new contexts.

> "Given students s1, s2 with different misconceptions m1, m2 observed in Phase 1, optimal predictions for Phase 2 will differ: A′(s1, q′) ̸= A′(s2, q′) even for the same question q′."

## Discussion


## Related Claims
- [Unconditioned single-phase distractor testing converges to the most common misconception and cannot validate understanding of individual student cognition](unconditioned-testing-converges-common-misconception.md) — related
- [Passing the two-phase test implies the AI can identify misconceptions and generate targeted practice problems for at least a (1−ε) fraction of student misconceptions](passing-test-implies-feedback-capability.md) — a broader claim this one bears on
