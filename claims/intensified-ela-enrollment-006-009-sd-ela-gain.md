---
type: claim
title: Enrolling in opt-in intensified middle-school ELA coursework is associated with a modest positive effect on end-of-year ELA achievement of approximately 0.06-0.09 standard deviations
description: Enrolling in opt-in intensified middle-school ELA coursework is associated with a modest positive effect on end-of-year ELA achievement of approximately 0.06-0.09 standard deviations
id: intensified-ela-enrollment-006-009-sd-ela-gain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: nabit-bajwa-2026
    resource: "https://doi.org/10.1145/3846167.3848599"
    title: "Nabit Bajwa, Seth B. Hunter, and Sanmay Das. (2026). Actionable Insights from Observational Data: The Case of Advanced Classes in K-12 Education. [doi:10.1145/3846167.3848599](https://doi.org/10.1145/3846167.3848599)"
    author: Nabit Bajwa, Seth B. Hunter, and Sanmay Das
    q: 2
    i: 0
    kind: associational
    rigour: 2
  - id: nabit-bajwa-2026-2
    resource: "https://doi.org/10.1145/3846167.3848599"
    title: "Nabit Bajwa, Seth B. Hunter, and Sanmay Das. (2026). Actionable Insights from Observational Data: The Case of Advanced Classes in K-12 Education. [doi:10.1145/3846167.3848599](https://doi.org/10.1145/3846167.3848599)"
    author: Nabit Bajwa, Seth B. Hunter, and Sanmay Das
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Enrolling in opt-in intensified middle-school ELA coursework is associated with a modest positive effect on end-of-year ELA achievement of approximately 0.06-0.09 standard deviations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2` · `i0` negligible
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i0` After full controls, enrollment in intensified ELA coursework is associated with approximately 0.06-0.09 SD higher end-of-year Grade 7 ELA achievement relative to observably comparable non-enrolled students. [→ Nabit Bajwa 2026](#nabit-bajwa-2026)
`q2 i?` A regression controlling only for prior ELA achievement yields a much larger coefficient of approximately 0.20 SD, showing the extent of selection bias addressed by the additional controls. [→ Nabit Bajwa 2026 (2)](#nabit-bajwa-2026-2)

## Evidence

### Nabit Bajwa 2026

Nabit Bajwa, Seth B. Hunter, and Sanmay Das. (2026). Actionable Insights from Observational Data: The Case of Advanced Classes in K-12 Education. [doi:10.1145/3846167.3848599](https://doi.org/10.1145/3846167.3848599)

`q2 · i0` · `associational · r2`

Value-added style regression on the district's Grade 7 cohort conditioning on prior achievement, concurrent math performance, math pathway, and demographics. Enrollment in intensified ELA is associated with higher end-of-year ELA achievement of "approximately 0.06-0.09 standard deviations", statistically significant and stable across specifications.

> "the estimates imply that a student who enrolls in intensified ELA coursework scores approximately 0.06-0.09 standard deviations (equivalent to about 2–3 months of additional learning) higher in end-of-year ELA achievement, on average, relative to an observably comparable student who remains in the baseline course."

### Nabit Bajwa 2026 (2)

Nabit Bajwa, Seth B. Hunter, and Sanmay Das. (2026). Actionable Insights from Observational Data: The Case of Advanced Classes in K-12 Education. [doi:10.1145/3846167.3848599](https://doi.org/10.1145/3846167.3848599)

`q2 · i?` · `associational · r2`

Comparison specification within the same value-added analysis: with only prior ELA achievement as a control the coefficient is "approximately 0.20 SD (p< 0.01)" — substantially larger than fully controlled estimates, indicating the selection bias the fuller specifications address; no standardized effect size is printed for this contrast.

> "a regression including only prior ELA achievement and advanced enrollment yields an estimated coefficient of approximately 0.20 SD (p< 0.01), substantially larger than the fully controlled estimates."

## Discussion


## Related Claims
- [Estimated gains from intensified ELA coursework are systematically smaller for FRL-eligible, English-learner, and disabled students, and larger for gifted-identified students](cate-smaller-underrepresented-subgroups.md) — related
- [The causal forest estimate of the average effect of intensified ELA enrollment is approximately 0.064 SD, with a 95% confidence interval that includes zero](causal-forest-ate-0064-ci-includes-zero.md) — related
- [Double machine learning confirms a positive, statistically significant average effect of intensified ELA enrollment of approximately 0.07 SD in the common-support trimmed sample](dml-robustness-007-sd-ela-ate.md) — related
- [Predicted benefits of intensified ELA coursework vary with prior achievement, estimated highest among students near or slightly above average proficiency](cate-heterogeneity-prior-ela-achievement.md) — related
- [High- and medium-ability Black and Hispanic students from lower-SES backgrounds enroll in intensified ELA at substantially lower rates than similarly prepared peers](under-enrollment-black-hispanic-low-ses-high-ability.md) — related
- [Enrollment in intensified ELA rises sharply with prior achievement, and higher-SES students are more likely to enroll at nearly every achievement level](enrollment-rises-sharply-prior-achievement-ses-gap.md) — related
