---
type: claim
title: "The causal forest estimate of the average effect of intensified ELA enrollment is approximately 0.064 SD, with a 95% confidence interval that includes zero"
description: "The causal forest estimate of the average effect of intensified ELA enrollment is approximately 0.064 SD, with a 95% confidence interval that includes zero"
id: causal-forest-ate-0064-ci-includes-zero
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
    i: "?"
    kind: associational
    rigour: 2
---

# The causal forest estimate of the average effect of intensified ELA enrollment is approximately 0.064 SD, with a 95% confidence interval that includes zero

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Averaging its heterogeneous effect estimates, the causal forest yields an average treatment effect of approximately 0.064 SD whose 95% confidence interval includes zero. [→ Nabit Bajwa 2026](#nabit-bajwa-2026)

## Evidence

### Nabit Bajwa 2026

Nabit Bajwa, Seth B. Hunter, and Sanmay Das. (2026). Actionable Insights from Observational Data: The Case of Advanced Classes in K-12 Education. [doi:10.1145/3846167.3848599](https://doi.org/10.1145/3846167.3848599)

`q2 · i?` · `associational · r2`

Causal forest DML on the same trimmed sample, reported as a secondary robustness check computed as the average of heterogeneous treatment effect estimates. The effect is "approximately 0.064 standard deviations, with a 95% confidence interval that includes zero", comparable in magnitude to the other estimators.

> "The causal forest estimate of the average effect is approximately 0.064 standard deviations, with a 95% confidence interval that includes zero."

## Discussion


## Related Claims
- [Predicted benefits of intensified ELA coursework vary with prior achievement, estimated highest among students near or slightly above average proficiency](cate-heterogeneity-prior-ela-achievement.md) — related
- [Double machine learning confirms a positive, statistically significant average effect of intensified ELA enrollment of approximately 0.07 SD in the common-support trimmed sample](dml-robustness-007-sd-ela-ate.md) — related
- [Enrolling in opt-in intensified middle-school ELA coursework is associated with a modest positive effect on end-of-year ELA achievement of approximately 0.06-0.09 standard deviations](intensified-ela-enrollment-006-009-sd-ela-gain.md) — related
- [Estimated gains from intensified ELA coursework are systematically smaller for FRL-eligible, English-learner, and disabled students, and larger for gifted-identified students](cate-smaller-underrepresented-subgroups.md) — related
