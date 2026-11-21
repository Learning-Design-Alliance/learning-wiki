---
type: claim
title: Learners studying top-ranked resources performed significantly better than those studying third-ranked resources
description: Learners studying top-ranked resources performed significantly better than those studying third-ranked resources
id: alignment-ranked-resources-predict-learning-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: molavi-2025
    resource: "https://doi.org/10.48550/arXiv.2512.13658"
    title: "Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor. (2025). Embedding-Based Rankings of Educational Resources based on Learning Outcome Alignment: Benchmarking, Expert Validation, and Learner Performance. [doi:10.48550/arXiv.2512.13658](https://doi.org/10.48550/arXiv.2512.13658)"
    author: Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: molavi-2025-2
    resource: "https://doi.org/10.48550/arXiv.2512.13658"
    title: "Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor. (2025). Embedding-Based Rankings of Educational Resources based on Learning Outcome Alignment: Benchmarking, Expert Validation, and Learner Performance. [doi:10.48550/arXiv.2512.13658](https://doi.org/10.48550/arXiv.2512.13658)"
    author: Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Learners studying top-ranked resources performed significantly better than those studying third-ranked resources

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In a three-group experiment with 360 learners, the Kruskal–Wallis test showed a significant difference in scores between groups assigned resources ranked first, second, or third by Voyage. [→ Molavi 2025](#molavi-2025)
`q2 i?` Dunn's post-hoc tests showed learners who studied the top-ranked resource scored significantly higher than those studying the third-ranked resource, while adjacent-group differences did not meet the Bonferroni-corrected threshold. [→ Molavi 2025 (2)](#molavi-2025-2)

## Evidence

### Molavi 2025

Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor. (2025). Embedding-Based Rankings of Educational Resources based on Learning Outcome Alignment: Benchmarking, Expert Validation, and Learner Performance. [doi:10.48550/arXiv.2512.13658](https://doi.org/10.48550/arXiv.2512.13658)

`q2 · i?` · `causal · r2`

Randomized three-group experiment on Prolific with 360 participants without prior programming or IT experience (2 domains × 6 topics × 3 groups × 10 learners); ten minutes of study followed by an expert-designed multiple-choice question. "The overall test indicated a significant difference between groups."

> "Scores were analyzed using theKruskal–Wallis H test, followed byDunn's post-hoc testswithBonferroni correction. The overall test indicated a significant difference between groups, 𝜒 2(2,𝑁= 360)= 15.39,𝑝<. 001."

### Molavi 2025 (2)

Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor. (2025). Embedding-Based Rankings of Educational Resources based on Learning Outcome Alignment: Benchmarking, Expert Validation, and Learner Performance. [doi:10.48550/arXiv.2512.13658](https://doi.org/10.48550/arXiv.2512.13658)

`q2 · i?` · `causal · r2`

Dunn's post-hoc comparisons (α=.017): Group 1 vs. Group 3 was significant (p<.001), with mean ranks 203.0 vs. 158.0; Group 1 vs. Group 2 and Group 2 vs. Group 3 were not significant (p=.049). Performance scores followed the resource ranking directionally.

> "learners who studied the top-ranked resource scored significantly higher than those studying the third-ranked resource, providing clear evidence that our ranking predicts learning effectiveness."

## Discussion


## Related Claims
- [In SIDRA and R-G-SIDRA cohorts, higher in-system MCQ scores (by tertile) predicted higher final exam grades, but in the RB-G-SIDRA cohort the tertile groups did not differ significantly.](mcq-tertiles-predict-final-exam-by-cohort.md) — related
- [The Voyage text-embedding model outperforms other embedding models and the YouTube baseline in ranking educational resources by alignment with intended learning outcomes](voyage-embedding-best-alignment-ranking-accuracy.md) — related
