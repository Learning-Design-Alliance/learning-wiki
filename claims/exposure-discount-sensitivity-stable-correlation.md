---
type: claim
title: The negative AI-difficulty–performance correlation is stable across exposure-discount values 0 to 0.40, and is strongest with no adjustment
description: The negative AI-difficulty–performance correlation is stable across exposure-discount values 0 to 0.40, and is strongest with no adjustment
id: exposure-discount-sensitivity-stable-correlation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: hongfei-yan-2026
    resource: "https://doi.org/10.48550/arxiv.2608.07523"
    title: "Hongfei Yan, Jiangkai Xiong, Yiqing Li, and Chong Chen. (2026). From Evaluated Models to Evaluation Aids: A Multi-Evidence Study of LLM-Based Difficulty Calibration for Programming Examinations. https://arxiv.org/abs/2608.07523 [doi:10.48550/arxiv.2608.07523](https://doi.org/10.48550/arxiv.2608.07523)"
    author: Hongfei Yan, Jiangkai Xiong, Yiqing Li, and Chong Chen
    q: 2
    i: 3
    kind: associational
    rigour: 2
---

# The negative AI-difficulty–performance correlation is stable across exposure-discount values 0 to 0.40, and is strongest with no adjustment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2` · `i3` large
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i3` Across discount levels 0, 0.10, 0.25, and 0.40, the Spearman rho between adjusted AI difficulty and pass rate ranges from rho = -0.780 to rho = -0.871, weakening monotonically as the discount increases. [→ Hongfei Yan 2026](#hongfei-yan-2026)

## Evidence

### Hongfei Yan 2026

Hongfei Yan, Jiangkai Xiong, Yiqing Li, and Chong Chen. (2026). From Evaluated Models to Evaluation Aids: A Multi-Evidence Study of LLM-Based Difficulty Calibration for Programming Examinations. https://arxiv.org/abs/2608.07523 [doi:10.48550/arxiv.2608.07523](https://doi.org/10.48550/arxiv.2608.07523)

`q2 · i3` · `associational · r2`

Four-level sensitivity analysis of the exposure-discount coefficient on the 79-problem sample. Printed effect sizes: Spearman rho = -0.780 to rho = -0.871 across discount levels. The authors note this is "contrary to the assumption that “the exposure discount improves explanatory power,”" suggesting the raw difficulty already corresponds well to student performance.

> "across the four discount levels, the Spearman ρ between adjusted AI diﬃculty and pass rate ranges from -0.780 to -0.871. Notably, the correlation is strongest when the discount is 0 (i.e., no adjustment), and it weakens monotonically as the discount increases;"

## Discussion


## Related Claims
- [AI review difficulty also correlates with problem-level non-attempt rate, providing process evidence beyond pass rate](ai-difficulty-non-attempt-rate-correlation.md) — related
- [The AI review ruler's problem-level correlation weakens in an introductory course, where exam-level correlation is near zero and cohort composition dominates](cs101-introductory-course-applicability-boundary.md) — related
- [Exam-level AI difficulty correlations with student performance are directionally consistent but weaker and only exploratory](exam-level-ai-difficulty-correlation-exploratory.md) — related
- [Review-based AI overall difficulty correlates strongly with problem-level student pass rate across 79 parallel-class exam problems](review-based-ai-difficulty-problem-level-correlation.md) — a narrower finding that bears on this claim
- [The same review ruler supports longitudinal cross-semester problem tracking for one teacher's Data Structures and Algorithms B course](longitudinal-dsa-review-ruler-tracking.md) — related
- [LLM-generated difficulty ratings show only moderate rank alignment with empirical student performance on basic arithmetic items](llm-difficulty-moderate-rank-alignment-arithmetic.md) — related
