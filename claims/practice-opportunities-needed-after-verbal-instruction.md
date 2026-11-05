---
type: claim
title: After up-front instruction, students start practice at about 65% correct and need about seven opportunities per knowledge component to reach 80%
description: Across 27 datasets from online practice systems used after lectures and readings, the typical student began practice at about 65% correct and needed about seven practice opportunities with feedback on a knowledge component to reach 80% correct.
id: practice-opportunities-needed-after-verbal-instruction
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

# After up-front instruction, students start practice at about 65% correct and need about seven opportunities per knowledge component to reach 80%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r3` · `q2` · n=6,946 students in 27 datasets
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

Mastery here is the authors' criterion of 80% correct on first attempts; an opportunity is one attempt at a task that exercises the knowledge component, with feedback and help available.

## Subclaims
`q2 i?` Despite lectures and readings before practice, the median initial accuracy across 27 datasets was 0.638 log odds, about 65.42% correct (mean 61.79%, 95% CI [56.77%, 66.82%]). [→ Koedinger et al. 2023](#koedinger-et-al-2023)

`q2 i?` The median overall learning rate was 0.09 log odds per opportunity (mean 0.15, 95% CI [0.08, 0.22]), about 2.5 percentage points per opportunity from a 65% start, and the median number of opportunities to reach 80% correct was 7.24 (mean 12.27, 95% CI [7.09, 17.45]). [→ Koedinger et al. 2023](#koedinger-et-al-2023)

`q2 i?` Counting practice opportunities on a knowledge component predicted performance better than elapsed calendar time: the time-based model fit best in only one of the 20 datasets with suitable time logs. [→ Koedinger et al. 2023](#koedinger-et-al-2023)

## Evidence

### Koedinger et al. 2023

Koedinger, K. R., Carvalho, P. F., Liu, R., & McLaughlin, E. A. (2023). An astonishing regularity in student learning rate. *Proceedings of the National Academy of Sciences, 120*(13), e2221311120. [doi:10.1073/pnas.2221311120](https://doi.org/10.1073/pnas.2221311120)

`q2 · secondary analysis of observational log data with statistical models` · `i? · no standardised effect size; accuracy reported in log odds and percent correct` · `n=6,946 students in 27 datasets` · `associational · r3`

The authors fitted mixed-effects logistic regression growth models to 27 datasets (1.3 million first-attempt observations, 6,946 learners, 12 courses in mathematics, science and language, late elementary school to college) from intelligent tutoring systems, educational games and online courses held in LearnLab's DataShop. In these courses, lectures and assigned readings typically came before the technology-based [practice](../elements/practice.md), which gave immediate [feedback](../elements/feedback.md), explanatory help on request and repeated opportunities on each knowledge component. A response counted as correct only on a first attempt without a hint. The number of opportunities to mastery was computed from each dataset's overall intercept and learning rate. Two datasets whose initial success rate was above 80% were excluded, as they left little room to observe learning. The authors note that their datasets do not represent feedback such as peer interaction or classroom dialogue.

## Discussion

The authors read the modest starting accuracy as evidence that verbal instruction alone rarely brings students to mastery, and that substantial learning comes from practice with feedback. The figure of about seven opportunities is a median across datasets; the mean was 12.27, and a student with low initial knowledge needed about 13 opportunities (see [the companion claim](students-differ-in-initial-knowledge-not-learning-rate.md)).

## Learner Variables
- [Prior Knowledge](../learner-variables/prior-knowledge.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [Students in online practice systems differ widely in initial knowledge but very little in learning rate per practice opportunity](students-differ-in-initial-knowledge-not-learning-rate.md) — the same study
- [In the authors' kindergarten efficacy trial, classrooms with higher rates of student practice opportunities produced substantively important mathematics gains](higher-practice-opportunity-rates-linked-to-gains.md) — related
