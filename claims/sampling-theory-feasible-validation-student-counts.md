---
type: claim
title: Statistical sampling theory shows high-confidence validation of misconception tracking is feasible with approximately 100 students and roughly 25 questions per student
description: Statistical sampling theory shows high-confidence validation of misconception tracking is feasible with approximately 100 students and roughly 25 questions per student
id: sampling-theory-feasible-validation-student-counts
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
  - id: shashank-sonkar-2025-2
    resource: "https://doi.org/10.48550/arXiv.2502.15127"
    title: "Shashank Sonkar, Naiming Liu, Xinghe Chen, Richard G. Baraniuk. (2025). The Imitation Game for Educational AI. arXiv preprint. [doi:10.48550/arXiv.2502.15127](https://doi.org/10.48550/arXiv.2502.15127)"
    author: Shashank Sonkar, Naiming Liu, Xinghe Chen, Richard G. Baraniuk
    q: 1
    i: "?"
    kind: theoretical
    rigour: 2
---

# Statistical sampling theory shows high-confidence validation of misconception tracking is feasible with approximately 100 students and roughly 25 questions per student

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · theoretical `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Because misconceptions cluster around common patterns, the required sample size grows with the number of common misconceptions and the inverse of the minimum misconception probability, making validation practical with modest samples. [→ Shashank Sonkar 2025](#shashank-sonkar-2025)
`q1 i?` Covering all common misconceptions with questions requires on the order of k/t ln(k/δ) questions, illustrated by roughly 2,500 total responses in the article's worked example. [→ Shashank Sonkar 2025 (2)](#shashank-sonkar-2025-2)

## Evidence

### Shashank Sonkar 2025

Shashank Sonkar, Naiming Liu, Xinghe Chen, Richard G. Baraniuk. (2025). The Imitation Game for Educational AI. arXiv preprint. [doi:10.48550/arXiv.2502.15127](https://doi.org/10.48550/arXiv.2502.15127)

`q1 · i?` · `theoretical · r2`

Analytical result (Theorems 1 and 2): a small subset of misconceptions accounts for most errors, and N = O(k log(1/δ)/pmin) students suffice; the article's worked parameter values yield approximately 100 students.

> "for typical values (k = 10 common misconceptions, δ = 0.05 for 95% confidence level, and pmin = 0.05 assuming even the rarest common misconception occurs in 1% of students), this requires approximately 100 students, making testing feasible in practice."

### Shashank Sonkar 2025 (2)

Shashank Sonkar, Naiming Liu, Xinghe Chen, Richard G. Baraniuk. (2025). The Imitation Game for Educational AI. arXiv preprint. [doi:10.48550/arXiv.2502.15127](https://doi.org/10.48550/arXiv.2502.15127)

`q1 · i?` · `theoretical · r2`

Analytical result (Theorem 3, Question Coverage): Q = O(k/t ln(k/δ)) questions cover k misconceptions with probability at least 1−δ; the article's remark computes the illustrative workload of about 25 questions per student.

> "For typical values (k = 10, t = 2, pmin = 0.01, δ = 0.05), this requires approximately 2, 500 total responses, or about 25 questions per student across 100 students."

## Discussion


## Related Claims
- [Adding a whole-number-strategy misconception to a fraction tutor's student model improved its fit to the data and gave per-student misconception estimates that tracked pre-test errors](misconception-kc-improves-fraction-student-model.md) — related
- [Unconditioned single-phase distractor testing converges to the most common misconception and cannot validate understanding of individual student cognition](unconditioned-testing-converges-common-misconception.md) — related
