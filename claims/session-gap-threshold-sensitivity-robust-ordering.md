---
type: claim
title: "Exercise-level indicators are robust to the session-gap threshold: exercise ordering is essentially unchanged across 10, 15, 20, and 30 minute caps with a fixed 15-minute closure tail."
description: "Exercise-level indicators are robust to the session-gap threshold: exercise ordering is essentially unchanged across 10, 15, 20, and 30 minute caps with a fixed 15-minute closure tail."
id: session-gap-threshold-sensitivity-robust-ordering
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: juuso-jaakola-2026
    resource: "https://doi.org/10.48550/arXiv.2610.09499"
    title: "Juuso Jaakola, Vlad Stirbu, Teiko Heinosaari. (2026). Using Learning Analytics to Study Novice Learners’ Work on Quantum Circuit Simulator Tasks. arXiv preprint. [doi:10.48550/arXiv.2610.09499](https://doi.org/10.48550/arXiv.2610.09499)"
    author: Juuso Jaakola, Vlad Stirbu, Teiko Heinosaari
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Exercise-level indicators are robust to the session-gap threshold: exercise ordering is essentially unchanged across 10, 15, 20, and 30 minute caps with a fixed 15-minute closure tail.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Varying the session-gap cap across 10, 15, 20, and 30 minutes leaves the exercise ordering essentially unchanged and produces small value changes. [→ Juuso Jaakola 2026](#juuso-jaakola-2026)

## Evidence

### Juuso Jaakola 2026

Juuso Jaakola, Vlad Stirbu, Teiko Heinosaari. (2026). Using Learning Analytics to Study Novice Learners’ Work on Quantum Circuit Simulator Tasks. arXiv preprint. [doi:10.48550/arXiv.2610.09499](https://doi.org/10.48550/arXiv.2610.09499)

`q2 · i?` · `design · r2`

Sensitivity analysis (Table III) comparing session-gap caps of 10, 15, 20, and 30 minutes against the 15-minute reference, with Spearman ρ reporting ordering stability and Δ reporting average indicator change.

> "The exercise ordering is essentially unchanged across the tested caps, and the corresponding value changes remain small when the closure tail is held fixed at 15 minutes."

## Discussion


## Related Claims
- [The second-use participation benefit holds under every conversation-duration threshold from four to ten minutes](caisey-benefit-robust-to-duration-threshold.md) — a broader claim this one bears on
- [Adding a quadratic achievement term leaves the negative contextual-mean effect essentially unchanged](curvature-adjustment-does-not-eliminate-bflpe.md) — related
- [Pooled gamification effects remain stable when high-risk-of-bias studies are excluded and in leave-one-out and fixed-effect sensitivity analyses](gamification-sensitivity-analyses-stable-pooled-effects.md) — a broader claim this one bears on
- [Across most exercises the attempt-count distribution is dense at low values with a long thin upper tail, distinguishing exercises needing targeted scaffolding for a struggling minority from uniformly hard ones.](long-tail-attempt-distributions-targeted-scaffolding.md) — related
