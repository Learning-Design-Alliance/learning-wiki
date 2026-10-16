---
type: claim
title: "The outcome data met t-test assumptions: Lilliefors normality (Lo < Lt for both classes) and variance homogeneity (F count 0.579 < F table 1.84)"
description: "The outcome data met t-test assumptions: Lilliefors normality (Lo < Lt for both classes) and variance homogeneity (F count 0.579 < F table 1.84)"
id: normality-homogeneity-prerequisites-met
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
sources:
  - id: hakiki-2023
    resource: "https://doi.org/10.25082/AMLER.2023.02.013"
    title: "Hakiki, M., Fadli, R., Samala, A. D., Fricticarani, A., Dayurni, P., Rahmadani, K., Astiti, A. D., & Sabir, A. (2023). Exploring the impact of using Chat-GPT on student learning outcomes in technology learning: The comprehensive experiment. Advances in Mobile Learning Educational Research, 3(2), 859-872. https://doi.org/10.25082/AMLER.2023.02.013"
    author: "Hakiki, M., Fadli, R., Samala, A. D., Fricticarani, A., Dayurni, P., Rahmadani, K., Astiti, A. D., & Sabir, A."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: hakiki-2023-2
    resource: "https://doi.org/10.25082/AMLER.2023.02.013"
    title: "Hakiki, M., Fadli, R., Samala, A. D., Fricticarani, A., Dayurni, P., Rahmadani, K., Astiti, A. D., & Sabir, A. (2023). Exploring the impact of using Chat-GPT on student learning outcomes in technology learning: The comprehensive experiment. Advances in Mobile Learning Educational Research, 3(2), 859-872. https://doi.org/10.25082/AMLER.2023.02.013"
    author: "Hakiki, M., Fadli, R., Samala, A. D., Fricticarani, A., Dayurni, P., Rahmadani, K., Astiti, A. D., & Sabir, A."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# The outcome data met t-test assumptions: Lilliefors normality (Lo < Lt for both classes) and variance homogeneity (F count 0.579 < F table 1.84)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`

## Subclaims
`q2 i?` Lilliefors tests showed both classes' final-test data were normally distributed (Lo < Lt = 0.159). [→ Hakiki 2023](#hakiki-2023)
`q2 i?` An F test showed the two classes had homogeneous variances (F count = 0.579 < F table = 1.84). [→ Hakiki 2023 (2)](#hakiki-2023-2)

## Evidence

### Hakiki 2023

Hakiki, M., Fadli, R., Samala, A. D., Fricticarani, A., Dayurni, P., Rahmadani, K., Astiti, A. D., & Sabir, A. (2023). Exploring the impact of using Chat-GPT on student learning outcomes in technology learning: The comprehensive experiment. Advances in Mobile Learning Educational Research, 3(2), 859-872. https://doi.org/10.25082/AMLER.2023.02.013

`q2 · i?` · `causal · r1`

Prerequisite normality testing of final-test scores for both classes (N = 31 each) using the Lilliefors test at a 5% significance level. Table 3 prints Lt = 0.159 with Lo = 0.142 (control) and Lo = 0.150 (experimental), described as "Lo < Lt".

> "Based on the Lilliefors test for the experimental and control classes, L o < Lt, it can be concluded that the data is normally distributed."

### Hakiki 2023 (2)

Hakiki, M., Fadli, R., Samala, A. D., Fricticarani, A., Dayurni, P., Rahmadani, K., Astiti, A. D., & Sabir, A. (2023). Exploring the impact of using Chat-GPT on student learning outcomes in technology learning: The comprehensive experiment. Advances in Mobile Learning Educational Research, 3(2), 859-872. https://doi.org/10.25082/AMLER.2023.02.013

`q2 · i?` · `causal · r1`

Variance homogeneity testing via F test at α = 0.05 with dk = 30, comparing the experimental and control classes' variances. The article reports "The Fcount value is 0.579 while the Ftable value is 1.84", concluding homogeneous variances and justifying the pooled variance t-test.

> "The Fcount value is 0.579 while the Ftable value is 1.84. Thus, it can be concluded that the value of Fcount< Ftable, which indicates that the two groups tested are homogeneous."

## Discussion


## Related Claims
- [Q-Q plots, CDF curves, and residual checks support the joint normality assumption underlying the multivariate true score model for the course-specific tests.](course-specific-norms-normality-supported.md) — related
- [Normality assumptions of the true score model appeared reasonable for the course-specific tests](normality-assumption-reasonable-course-specific.md) — related
- [The multivariate normality assumption of the norming model was judged met for all domains and grades, despite some tail deviations in Q-Q plots](normality-assumption-met-foundational-skills-norming.md) — related
- [The multivariate normality assumption of the true score model was judged reasonable for all domains and grades](spanish-foundational-skills-normality-assumption-met.md) — related
