---
type: claim
title: "Exam tier shapes latent cognitive structure more than subject: JEE Advanced is dominated by Multi-concept Integration (80.9%) versus NEET (33.3%), with JEE-vs-NEET KL divergence 0.505"
description: "Exam tier shapes latent cognitive structure more than subject: JEE Advanced is dominated by Multi-concept Integration (80.9%) versus NEET (33.3%), with JEE-vs-NEET KL divergence 0.505"
id: learnopt-jee-advanced-skill-profile
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
    rigour: 1
  - id: joy-bose-2025-2
    resource: "https://github.com/learnopt/learnopt"
    title: "Joy Bose, Om Thomas. (2025). LearnOpt: Recovering the Latent Cognitive Structure of Standardized Examinations via Knowledge Graphs and Constrained Optimization. https://github.com/learnopt/learnopt"
    author: Joy Bose, Om Thomas
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Exam tier shapes latent cognitive structure more than subject: JEE Advanced is dominated by Multi-concept Integration (80.9%) versus NEET (33.3%), with JEE-vs-NEET KL divergence 0.505

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`

## Subclaims
`q2 i?` The JEE-vs-NEET divergence (0.505) exceeds NEET's largest cross-subject divergence (0.420), which exceeds its largest within-regime cross-year divergence (0.060). [→ Joy Bose 2025](#joy-bose-2025)
`q2 i?` The same pattern holds within subjects: JEE Advanced Chemistry and Physics are 63.3% and 77.8% S3 versus 34.9% and 51.9% in NEET. [→ Joy Bose 2025 (2)](#joy-bose-2025-2)

## Evidence

### Joy Bose 2025

Joy Bose, Om Thomas. (2025). LearnOpt: Recovering the Latent Cognitive Structure of Standardized Examinations via Knowledge Graphs and Constrained Optimization. https://github.com/learnopt/learnopt

`q2 · i?` · `associational · r1`

Cross-exam comparison applying the identical tagging pipeline to the 110 single-correct MCQs of JEEBench (2016-2023). The article reports JEE Advanced at 80.9% S3 with effectively zero S1, and the three-axis ordering of divergences quoted above.

> "The JEE-vs-NEET divergence (0.505) exceeds NEET's largest cross-subject divergence (Biology vs Physics, 0.420, Section 4.3 Table 4), which in turn exceeds NEET's largest within-regime cross-year divergence (0.060, 2023-2024)."

### Joy Bose 2025 (2)

Joy Bose, Om Thomas. (2025). LearnOpt: Recovering the Latent Cognitive Structure of Standardized Examinations via Knowledge Graphs and Constrained Optimization. https://github.com/learnopt/learnopt

`q2 · i?` · `associational · r1`

Same-subject cross-exam comparison (Table 7) on the JEEBench MCQ subset versus the NEET corpus. The article reports per-subject S3 percentages quoted verbatim, with Chemistry KL=0.234 and Physics KL=0.267 for JEE vs NEET.

> "JEE Advanced Mathematics is 92.5% S3; JEE Advanced Chemistry and Physics are 63.3% and 77.8% S3 respectively, versus 34.9% and 51.9% for the same subjects in NEET."

## Discussion


## Related Claims
- [Within a syllabus regime, NEET subject predicts a question's skill profile more strongly than year of administration](learnopt-subject-predicts-skill-profile.md) — a broader claim this one bears on
- [NEET's latent skill distribution is piecewise stationary: stable within the 2016-2021 syllabus regime, with a significant shift at the 2023 NCERT rationalization marked by rising Elimination/Negation and falling Direct Recall questions](learnopt-neet-regime-shift-2023.md) — related
- [A pilot human annotation surfaces a framing discrepancy: a NEET aspirant labeled all 10 sampled questions as Recall, including the five the LLM tagged as Elimination/Negation](learnopt-pilot-recall-framing.md) — related
