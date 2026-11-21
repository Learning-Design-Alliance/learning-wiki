---
type: claim
title: Weeks with LLM-generated multiple-choice retrieval practice produced significantly higher quiz scores than weeks without retrieval practice in college data science courses (r = 0.5860)
description: Weeks with LLM-generated multiple-choice retrieval practice produced significantly higher quiz scores than weeks without retrieval practice in college data science courses (r = 0.5860)
id: llm-generated-retrieval-practice-higher-quiz-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: an-2025
    resource: "https://doi.org/10.48550/arXiv.2507.05629"
    title: "An, Y., Liu, J., Acharya, N., and Hashmi, R. (2025). Enhancing Student Learning with LLM-Generated Retrieval Practice Questions: An Empirical Study in Data Science Courses. arXiv:2507.05629v2 [cs.AI]. [doi:10.48550/arXiv.2507.05629](https://doi.org/10.48550/arXiv.2507.05629)"
    author: An, Y., Liu, J., Acharya, N., and Hashmi, R.
    q: 2
    i: 3
    kind: causal
    rigour: 1
  - id: an-2025-2
    resource: "https://doi.org/10.48550/arXiv.2507.05629"
    title: "An, Y., Liu, J., Acharya, N., and Hashmi, R. (2025). Enhancing Student Learning with LLM-Generated Retrieval Practice Questions: An Empirical Study in Data Science Courses. arXiv:2507.05629v2 [cs.AI]. [doi:10.48550/arXiv.2507.05629](https://doi.org/10.48550/arXiv.2507.05629)"
    author: An, Y., Liu, J., Acharya, N., and Hashmi, R.
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Weeks with LLM-generated multiple-choice retrieval practice produced significantly higher quiz scores than weeks without retrieval practice in college data science courses (r = 0.5860)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person
> **Design limits** · An 2025: groups were assigned but students were analysed as independent · An 2025 (2): groups were assigned but students were analysed as independent (read from the study by two models, 2026-11-21)

## Subclaims
`q2 i3` Students performed significantly better on Quiz 1 than on Quiz 2, with a large positive rank-biserial correlation (r = 0.5860). [→ An 2025](#an-2025)
`q2 i?` The advantage occurred when students practiced with LLM-generated MCQs during instruction, compared to a time when they did not perform any retrieval practice. [→ An 2025 (2)](#an-2025-2)

## Evidence

### An 2025

An, Y., Liu, J., Acharya, N., and Hashmi, R. (2025). Enhancing Student Learning with LLM-Generated Retrieval Practice Questions: An Empirical Study in Data Science Courses. arXiv:2507.05629v2 [cs.AI]. [doi:10.48550/arXiv.2507.05629](https://doi.org/10.48550/arXiv.2507.05629)

`q2 · i3` · `causal · r1`

Mann-Whitney U test on merged quiz scores from two college data science courses in a quasi-experimental non-equivalent groups design; the article reports rank-biserial r = 0.5860 and concludes 'students performed significantly better on Quiz 1 than on Quiz 2'.

> "the large positive rank-biserial correlation (r = 0.5860), and the descriptive statistics showing a much higher median and mean for Quiz 1, provides very strong evidence that students performed significantly better on Quiz 1 than on Quiz 2."

### An 2025 (2)

An, Y., Liu, J., Acharya, N., and Hashmi, R. (2025). Enhancing Student Learning with LLM-Generated Retrieval Practice Questions: An Empirical Study in Data Science Courses. arXiv:2507.05629v2 [cs.AI]. [doi:10.48550/arXiv.2507.05629](https://doi.org/10.48550/arXiv.2507.05629)

`q2 · i?` · `causal · r1`

Statistical comparison of Quiz 1 (LLM retrieval practice condition) and Quiz 2 (no retrieval practice) scores: students 'achieved significantly better learning outcomes if they practiced with LLM-generated MCQs, compared to a time when they did not perform any retrieval practice'.

> "The statistical analysis on scores from Quiz 1 and Quiz 2 revealed that the students achieved significantly better learning outcomes if they practiced with LLM-generated MCQs, compared to a time when they did not perform any retrieval practice."

## Discussion


## Related Claims
- [LLM-assigned difficulty labels fail to predict empirical item difficulty in classroom retrieval practice (ρ=0.06), as do co-generated Bloom levels (ρ=0.02)](llm-difficulty-labels-fail-to-predict-empirical-item-difficulty.md) — related
- [A course section that reviewed with Kahoot no-stakes quizzes differed significantly in high-stakes multiple-choice exam scores from a section that reviewed with a study guide and lecture, a difference the authors report as improvement without printing group means](kahoot-testing-effect-higher-exam-scores.md) — related
- [LLM-generated retrieval practice was practical to deploy and well received, but high correctness rates (about 70% of items at p=1.0) restricted score variance](llm-generated-retrieval-practice-deployable-but-high-accuracy-limits-variance.md) — related
- [Classroom quizzing delivered by clickers, computer software, or paper improves student performance on classroom exams in middle school and college courses](classroom-quizzing-improves-exam-performance-across-grades-and-content.md) — a broader claim this one bears on
- [Only one statistically significant group difference emerged across the 21 post-intervention assessments, on a Week 6 LLM quiz](single-residual-llm-quiz-gap.md) — related
