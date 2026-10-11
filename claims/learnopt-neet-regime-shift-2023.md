---
type: claim
title: "NEET's latent skill distribution is piecewise stationary: stable within the 2016-2021 syllabus regime, with a significant shift at the 2023 NCERT rationalization marked by rising Elimination/Negation and falling Direct Recall questions"
description: "NEET's latent skill distribution is piecewise stationary: stable within the 2016-2021 syllabus regime, with a significant shift at the 2023 NCERT rationalization marked by rising Elimination/Negation and falling Direc..."
id: learnopt-neet-regime-shift-2023
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
  - id: joy-bose-2025-2
    resource: "https://github.com/learnopt/learnopt"
    title: "Joy Bose, Om Thomas. (2025). LearnOpt: Recovering the Latent Cognitive Structure of Standardized Examinations via Knowledge Graphs and Constrained Optimization. https://github.com/learnopt/learnopt"
    author: Joy Bose, Om Thomas
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# NEET's latent skill distribution is piecewise stationary: stable within the 2016-2021 syllabus regime, with a significant shift at the 2023 NCERT rationalization marked by rising Elimination/Negation and falling Direct Recall questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1`–`r2` · `q2`

## Subclaims
`q2 i?` Consecutive-year KL divergence within 2016-2021 (0.004-0.032) is non-significant under permutation testing, indicating within-regime stability. [→ Joy Bose 2025](#joy-bose-2025)
`q2 i?` Pooling 2016-2021 vs 2023-2024 gives KL=0.040, p=0.0005, with S5 rising from 19.5-29.3% to 30.7-35.2% and S1 falling from 4.0-6.3% to 1.5-2.6%. [→ Joy Bose 2025 (2)](#joy-bose-2025-2)

## Evidence

### Joy Bose 2025

Joy Bose, Om Thomas. (2025). LearnOpt: Recovering the Latent Cognitive Structure of Standardized Examinations via Knowledge Graphs and Constrained Optimization. https://github.com/learnopt/learnopt

`q2 · i?` · `associational · r2`

Corpus analysis of 1,496 LLM-tagged NEET questions (2016-2024) computing yearly skill distributions and KL divergences with permutation testing. The article reports "consecutive-year KL divergence ranges from 0.004 to 0.032, all non-significant" within the pre-2023 regime.

> "From 2016-2021, the distribution is comparatively stable: consecutive-year KL divergence ranges from 0.004 to 0.032, all non-significant under a 10,000-permutation test (e.g., 2016->2017: p=0.957)."

### Joy Bose 2025 (2)

Joy Bose, Om Thomas. (2025). LearnOpt: Recovering the Latent Cognitive Structure of Standardized Examinations via Knowledge Graphs and Constrained Optimization. https://github.com/learnopt/learnopt

`q2 · i?` · `associational · r1`

Pooled regime-vs-regime permutation test over the tagged NEET corpus, treated by the authors as primary evidence for a structural break. The pooled comparison "gives KL=0.040, p=0.0005"; the text also reports S5 rising to 30.7-35.2% and S1 falling to 1.5-2.6% post-shift.

> "and pooling all pre-shift years (2016-2021, n=1,072) against all post-shift years (2023-2024, n=392) gives KL=0.040, p=0.0005."

## Discussion


## Related Claims
- [Exam tier shapes latent cognitive structure more than subject: JEE Advanced is dominated by Multi-concept Integration (80.9%) versus NEET (33.3%), with JEE-vs-NEET KL divergence 0.505](learnopt-jee-advanced-skill-profile.md) — related
- [Within a syllabus regime, NEET subject predicts a question's skill profile more strongly than year of administration](learnopt-subject-predicts-skill-profile.md) — related
