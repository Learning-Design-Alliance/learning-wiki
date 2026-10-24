---
type: claim
title: Exam-level AI difficulty correlations with student performance are directionally consistent but weaker and only exploratory
description: Exam-level AI difficulty correlations with student performance are directionally consistent but weaker and only exploratory
id: exam-level-ai-difficulty-correlation-exploratory
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
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

# Exam-level AI difficulty correlations with student performance are directionally consistent but weaker and only exploratory

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2` · `i3` large
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i3` At the exam level, correlations between AI difficulty and normalized student mean performance are negative but weaker than at the problem level (Spearman rho = -0.461 adjusted, rho = -0.594 raw across 11 exams). [→ Hongfei Yan 2026](#hongfei-yan-2026)

## Evidence

### Hongfei Yan 2026

Hongfei Yan, Jiangkai Xiong, Yiqing Li, and Chong Chen. (2026). From Evaluated Models to Evaluation Aids: A Multi-Evidence Study of LLM-Based Difficulty Calibration for Programming Examinations. https://arxiv.org/abs/2608.07523 [doi:10.48550/arxiv.2608.07523](https://doi.org/10.48550/arxiv.2608.07523)

`q2 · i3` · `associational · r2`

Exploratory exam-level correlations across 11 parallel-class exams mixing solved-count and score metrics. Printed effect sizes: Spearman rho = -0.461 (adjusted) and Spearman rho = -0.594 (raw) against normalized student mean. The authors give three reasons for weakness, including the sample of only 11 exams.

> "Table 5 shows that the direction of the exam-level correlation generally matches the expectation that “the higher the AI diﬃculty, the lower the student performance,” but its strength is weaker than at the problem level (see Section 5.4) and can only be interpreted as exploratory evidence."

## Discussion


## Related Claims
- [The AI review ruler's problem-level correlation weakens in an introductory course, where exam-level correlation is near zero and cohort composition dominates](cs101-introductory-course-applicability-boundary.md) — related
- [Review-based AI overall difficulty correlates strongly with problem-level student pass rate across 79 parallel-class exam problems](review-based-ai-difficulty-problem-level-correlation.md) — related
- [The negative AI-difficulty–performance correlation is stable across exposure-discount values 0 to 0.40, and is strongest with no adjustment](exposure-discount-sensitivity-stable-correlation.md) — related
- [AI review difficulty also correlates with problem-level non-attempt rate, providing process evidence beyond pass rate](ai-difficulty-non-attempt-rate-correlation.md) — related
- [The same review ruler supports longitudinal cross-semester problem tracking for one teacher's Data Structures and Algorithms B course](longitudinal-dsa-review-ruler-tracking.md) — related
- Reported GenAI use frequency shows only weak negative associations with OOP assessment performance — related
