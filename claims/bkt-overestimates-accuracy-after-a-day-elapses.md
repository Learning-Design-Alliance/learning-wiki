---
type: claim
title: "The survey reports, citing Qiu et al., that BKT consistently overestimates the accuracy of students' answers when a day or more has elapsed since their previous responses."
description: "The survey reports, citing Qiu et al., that BKT consistently overestimates the accuracy of students' answers when a day or more has elapsed since their previous responses."
id: bkt-overestimates-accuracy-after-a-day-elapses
status: review
generated:
  by: claude/unspecified
  at: 2026-09-24
evidence_strength: weak
newest_evidence: 2021
sources:
  - id: shuanghong-shen-2021
    resource: "https://doi.org/10.48550/arxiv.2105.15106"
    title: "Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106 [doi:10.48550/arxiv.2105.15106](https://doi.org/10.48550/arxiv.2105.15106)"
    author: Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# The survey reports, citing Qiu et al., that BKT consistently overestimates the accuracy of students' answers when a day or more has elapsed since their previous responses.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The review attributes to Qiu et al. the finding that BKT overestimates answer accuracy after a gap of a day or more. [→ Shuanghong Shen 2021](#shuanghong-shen-2021)

## Evidence

### Shuanghong Shen 2021

Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106 [doi:10.48550/arxiv.2105.15106](https://doi.org/10.48550/arxiv.2105.15106)

`q2 · i?` · `review · r2`

Narrative review attributing this to Qiu et al., who "discover that BKT consistently overestimates the accuracy of students’ answers when a day or more had elapsed"; the survey explains BKT assumes performance stays the same regardless of elapsed time, motivating the BKT-Forget model.

> "Qiu et al. [88] discover that BKT consistently overestimates the accuracy of students’ answers when a day or more had elapsed since their previous responses."

## Discussion

## Related Claims

- [The survey reports, citing Pavlik et al., that no single knowledge tracing model was always the best, and that a better model must consider multiple student features and the learning context.](no-single-knowledge-tracing-model-is-always-best.md) — the general claim this finding bears on, with the studies behind it

- [The survey states that deep learning knowledge tracing models exhibit superior performance to Bayesian and logistic models but have significant room for improvement in interpretability.](deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability.md) — the general claim this finding bears on, with the studies behind it
- MS-BKT mastery estimates fluctuate less than classic BKT and avoid over-high estimates after long incorrect runs, in fictitious-student comparisons — related
- [The survey reports, citing Lee and Brunskill, that individualized BKT in an intelligent tutoring system reduced by about half the questions required for 20% of students to achieve mastery.](individualized-bkt-reduces-questions-needed-for-mastery.md) — related
- [The survey reports, citing Desmarais and Baker, that students using the BKT-sequence recommendation algorithm solved more difficult exercises, obtained higher performance and spent more time in the system than students using the traditional approach.](bkt-sequence-recommendation-students-solved-harder-exercises.md) — related
- [BKT is recommended as the knowledge estimation approach for SPOL learning awareness and intervention because it balances explanatory power against predicting accuracy](bkt-recommended-knowledge-state-estimation-spol.md) — reports the opposite
