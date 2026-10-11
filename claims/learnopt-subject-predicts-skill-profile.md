---
type: claim
title: "Within a syllabus regime, NEET subject predicts a question's skill profile more strongly than year of administration"
description: "Within a syllabus regime, NEET subject predicts a question's skill profile more strongly than year of administration"
id: learnopt-subject-predicts-skill-profile
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: joy-bose-2025
    resource: "https://github.com/learnopt/learnopt"
    title: "Joy Bose, Om Thomas. (2025). LearnOpt: Recovering the Latent Cognitive Structure of Standardized Examinations via Knowledge Graphs and Constrained Optimization. https://github.com/learnopt/learnopt"
    author: Joy Bose, Om Thomas
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Within a syllabus regime, NEET subject predicts a question's skill profile more strongly than year of administration

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Cross-subject KL divergences (0.150-0.420) exceed within-regime year-to-year divergences (max 0.032 pre-shift, 0.060 post-shift). [→ Joy Bose 2025](#joy-bose-2025)

## Evidence

### Joy Bose 2025

Joy Bose, Om Thomas. (2025). LearnOpt: Recovering the Latent Cognitive Structure of Standardized Examinations via Knowledge Graphs and Constrained Optimization. https://github.com/learnopt/learnopt

`q2 · i?` · `associational · r2`

Aggregate skill-distribution analysis by subject across all years of the tagged NEET corpus (Table 4). The article reports pairwise subject divergences "substantially larger than within-regime year-to-year divergence", e.g. Physics dominated by S3 (51.9%) and Biology rich in S5 (34.6%).

> "Pairwise KL divergence between subjects (Biology vs Chemistry: 0.158, Biology vs Physics: 0.420, Chemistry vs Physics: 0.150) is substantially larger than within-regime year-to-year divergence"

## Discussion


## Related Claims
- [Exam tier shapes latent cognitive structure more than subject: JEE Advanced is dominated by Multi-concept Integration (80.9%) versus NEET (33.3%), with JEE-vs-NEET KL divergence 0.505](learnopt-jee-advanced-skill-profile.md) — a narrower finding that bears on this claim
- [NEET's latent skill distribution is piecewise stationary: stable within the 2016-2021 syllabus regime, with a significant shift at the 2023 NCERT rationalization marked by rising Elimination/Negation and falling Direct Recall questions](learnopt-neet-regime-shift-2023.md) — related
