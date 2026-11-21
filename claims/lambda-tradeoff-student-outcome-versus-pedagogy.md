---
type: claim
title: Increasing the reward weight λ raises predicted student correctness while generally lowering rubric score, with the tradeoff saturating between λ = 0.75 and 1.0
description: Increasing the reward weight λ raises predicted student correctness while generally lowering rubric score, with the tradeoff saturating between λ = 0.75 and 1.0
id: lambda-tradeoff-student-outcome-versus-pedagogy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: alexander-scarlatos-2025
    resource: "https://doi.org/10.1007/978-3-031-98414-3_18"
    title: "Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)"
    author: Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: alexander-scarlatos-2025-2
    resource: "https://doi.org/10.1007/978-3-031-98414-3_18"
    title: "Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)"
    author: Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Increasing the reward weight λ raises predicted student correctness while generally lowering rubric score, with the tradeoff saturating between λ = 0.75 and 1.0

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Increasing λ from 0 to 1 generally increases student correctness prediction performance while generally decreasing the rubric score. [→ Alexander Scarlatos 2025](#alexander-scarlatos-2025)
`q2 i?` Changing λ from 0.75 to 1.0 does not increase student outcome performance, and the authors interpret a small correctness reward signal as implicitly helping pedagogical effectiveness. [→ Alexander Scarlatos 2025 (2)](#alexander-scarlatos-2025-2)

## Evidence

### Alexander Scarlatos 2025

Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)

`q2 · i?` · `design · r2`

Numerical experiment varying λ ∈ {0.00, 0.25, 0.50, 0.75, 1.00} in DPO training, evaluated on a subset of 500 turn pairs; results shown in Figure 2 indicate the stated general trend in both metrics.

> "We see that, as expected, increasing λ from 0 to 1 generally increases student correctness prediction performance while generally decreasing the rubric score."

### Alexander Scarlatos 2025 (2)

Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)

`q2 · i?` · `design · r2`

The same λ experiment reports a saturation point: performance does not rise between 0.75 and 1.0, and dropping below 0.25 hurts pedagogy, which the authors read as mutual reinforcement of the two objectives.

> "Perhaps surprisingly, changing λ from 0.75 to 1.0 does not increase student outcome performance, while decreasing λ from 0.25 to 0.0 decreases pedagogical performance."

## Discussion


## Related Claims
- [Responsiveness and helpfulness trade off: always-answer adapters score lowest on helpfulness while withholding adapters score highest](educlaw-bench-responsiveness-helpfulness-tradeoff.md) — related
