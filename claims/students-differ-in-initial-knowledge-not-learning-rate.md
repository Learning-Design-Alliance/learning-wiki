---
type: claim
title: Students in online practice systems differ widely in initial knowledge but very little in learning rate per practice opportunity
description: Across 27 datasets from online practice systems, students' starting accuracy varied by about 20 percentage points between the lower and upper halves, while their gain per practice opportunity varied by about one percentage point.
id: students-differ-in-initial-knowledge-not-learning-rate
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: koedinger-et-al-2023
    resource: "https://doi.org/10.1073/pnas.2221311120"
    title: "Koedinger, K. R., Carvalho, P. F., Liu, R., & McLaughlin, E. A. (2023). An astonishing regularity in student learning rate. *Proceedings of the National Academy of Sciences, 120*(13), e2221311120. [doi:10.1073/pnas.2221311120](https://doi.org/10.1073/pnas.2221311120)"
    author: "Koedinger, K. R., Carvalho, P. F., Liu, R., & McLaughlin, E. A."
    q: 2
    i: "?"
    n: 6,946 students in 27 datasets
    kind: associational
    rigour: 3
---

# Students in online practice systems differ widely in initial knowledge but very little in learning rate per practice opportunity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r3` · `q2` · n=6,946 students in 27 datasets
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

The finding is about learning rate measured per practice opportunity on a knowledge component, in educational technologies that give immediate feedback and on-demand instruction. It is not about how fast students progress through a course in calendar time, which also depends on how many opportunities each student gets.

## Subclaims
`q2 i?` Students varied substantially in initial knowledge: the median standard deviation of student intercepts across 27 datasets was 0.651 log odds, and students in the lower half of initial knowledge started at about 55% correct against about 75% for the upper half (medians 55.21% and 75.17%). [→ Koedinger et al. 2023](#koedinger-et-al-2023)

`q2 i?` Student learning rate varied little: the median standard deviation of student learning rates was 0.015 log odds per opportunity (interquartile range 0.018), against 0.102 (interquartile range 0.132) for the learning rates of knowledge components, so the per-opportunity gain ran from about 1.70% at the 25th percentile of students to 2.56% at the 75th. [→ Koedinger et al. 2023](#koedinger-et-al-2023)

`q2 i?` In opportunities to reach 80% correct, a typical slower learner needed about one more opportunity than a typical faster learner (medians 7.89 and 6.94), whereas a student in the lower half of initial knowledge needed about ten more than one in the upper half (13.13 and 3.66). [→ Koedinger et al. 2023](#koedinger-et-al-2023)

`q2 i?` Student learning-rate variation was detectable in some datasets: the model with a learning rate per student fit better than the one without it in 21 of 27 datasets by AIC and 15 of 27 by BIC, and the variation it detected was small. It was larger in the six language datasets (median interquartile range 0.045 log odds) than in the 16 mathematics (0.017) and five science (0.008) datasets. [→ Koedinger et al. 2023](#koedinger-et-al-2023)

## Evidence

### Koedinger et al. 2023

Koedinger, K. R., Carvalho, P. F., Liu, R., & McLaughlin, E. A. (2023). An astonishing regularity in student learning rate. *Proceedings of the National Academy of Sciences, 120*(13), e2221311120. [doi:10.1073/pnas.2221311120](https://doi.org/10.1073/pnas.2221311120)

`q2 · secondary analysis of observational log data with statistical models` · `i? · no standardised effect size; variation reported in log odds and percent correct` · `n=6,946 students in 27 datasets` · `associational · r3`

The authors fitted mixed-effects logistic regression growth models to 27 datasets from LearnLab's DataShop repository: 1.3 million first-attempt observations from 6,946 learners in 12 courses in mathematics, science and language, from late elementary school to college, collected in intelligent tutoring systems, educational games and online courses. Each model combined a refined knowledge component model of the domain with an intercept (initial knowledge) and a slope (learning rate) per student and per knowledge component, counting practice opportunities on each component. Students started the practice at very different levels but improved at nearly the same rate per opportunity, while knowledge components differed markedly in their rates. Simulated data with high student learning-rate variation showed the model can detect such variation when it is present, and the low variation held when knowledge-component learning rates were dropped from the model (interquartile range 0.021 instead of 0.018) and when only hard or only easy components were analysed. The authors note that the systems studied provided favourable conditions (immediate feedback, explanatory instruction on demand, tasks designed by cognitive task analysis), that forms of feedback such as peer interaction and classroom dialogue are not well represented, and that poorer knowledge-component models lower the estimated learning rates and make student variation even harder to see.

## Discussion

The authors read the result as a challenge to accounts of large individual differences in learning ability, and suggest that differences in achievement come mainly from differences in prior and current learning opportunities. Their explanation of the large differences in initial knowledge (different amounts of domain-relevant experience before the course) and of the small differences in rate (a "disjunctive learning path" hypothesis) are proposals, not results of this study. The analysis is observational: students were not assigned to different amounts of practice.

## Learner Variables
- [Prior Knowledge](../learner-variables/prior-knowledge.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [After up-front instruction, students start practice at about 65% correct and need about seven opportunities per knowledge component to reach 80%](practice-opportunities-needed-after-verbal-instruction.md) — the same study
- [Individualizing the initial knowledge parameter reliably improves prediction of real-world data](individualizing-initial-knowledge-improves-prediction.md) — related
- [Split-half stability analysis shows fitted learning-rate parameters are meaningful, with Spearman correlations between 0.5 and 0.7 across independent data halves](split-half-learning-rate-stability.md) — related
- [Opportunity gaps in incoming chemistry content knowledge are present: prequiz scores varied widely and were predicted by coursework, PEER/first-generation status, and gender](prequiz-opportunity-gaps-chemistry-knowledge.md) — related
