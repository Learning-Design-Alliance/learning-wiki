---
type: claim
title: "Exact-match (k=1) job role prediction requires approximately 24 questionnaire questions to achieve an average success rate of 90%, while at least six questions yield a top-10 success rate above 70%"
description: "Exact-match (k=1) job role prediction requires approximately 24 questionnaire questions to achieve an average success rate of 90%, while at least six questions yield a top-10 success rate above 70%"
id: c3-ioc-exact-match-needs-24-questions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: adán-josé-garcía-2023
    resource: "https://doi.org/10.1007/s40593-022-00317-y"
    title: "Adán José-García, Alison Sneyd, Ana Melro, Anaïs Ollagnier, Georgina Tarling, Haiyang Zhang, Mark Stevenson, Richard Everson, Rudy Arthur. (2023). C3-IoC: A Career Guidance System for Assessing Student Skills using Machine Learning and Network Visualisation. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00317-y"
    author: Adán José-García, Alison Sneyd, Ana Melro, Anaïs Ollagnier, Georgina Tarling, Haiyang Zhang, Mark Stevenson, Richard Everson, Rudy Arthur
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: adán-josé-garcía-2023-2
    resource: "https://doi.org/10.1007/s40593-022-00317-y"
    title: "Adán José-García, Alison Sneyd, Ana Melro, Anaïs Ollagnier, Georgina Tarling, Haiyang Zhang, Mark Stevenson, Richard Everson, Rudy Arthur. (2023). C3-IoC: A Career Guidance System for Assessing Student Skills using Machine Learning and Network Visualisation. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00317-y"
    author: Adán José-García, Alison Sneyd, Ana Melro, Anaïs Ollagnier, Georgina Tarling, Haiyang Zhang, Mark Stevenson, Richard Everson, Rudy Arthur
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Exact-match (k=1) job role prediction requires approximately 24 questionnaire questions to achieve an average success rate of 90%, while at least six questions yield a top-10 success rate above 70%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2`–`r3` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When the exact match k = 1 is required, about 24 questions are needed to achieve an average success rate of 90%. [→ Adán José-García 2023](#adan-jose-garcia-2023)
`q2 i?` The article suggests users answer at least six questions out of 24 for C3-IoC to generate a 70% success rate in the 10 most similar jobs. [→ Adán José-García 2023 (2)](#adan-jose-garcia-2023-2)

## Evidence

### Adán José-García 2023

Adán José-García, Alison Sneyd, Ana Melro, Anaïs Ollagnier, Georgina Tarling, Haiyang Zhang, Mark Stevenson, Richard Everson, Rudy Arthur. (2023). C3-IoC: A Career Guidance System for Assessing Student Skills using Machine Learning and Network Visualisation. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00317-y

`q2 · i?` · `design · r2`

Dummy-user SRP evaluation (Fig. 9) with Q varied from 4 to 24. The article states "approximately 24 questions are needed to achieve an average success rate of 90%" for exact matches; percentages are printed with no effect size.

> "However, when the exact match k = 1 is required, the success rate is initially proportional to Q , but approximately 24 questions are needed to achieve an average success rate of 90%."

### Adán José-García 2023 (2)

Adán José-García, Alison Sneyd, Ana Melro, Anaïs Ollagnier, Georgina Tarling, Haiyang Zhang, Mark Stevenson, Richard Everson, Rudy Arthur. (2023). C3-IoC: A Career Guidance System for Assessing Student Skills using Machine Learning and Network Visualisation. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00317-y

`q2 · i?` · `design · r3`

Authors' analysis of the k = 10 SRP curve in the discussion of the first dummy-user experiment, stating users "must answer at least six questionnaire questions" for above 70% prediction; printed percentages only, no effect size.

> "Under this setting, it was observed that the user must answer at least six questionnaire questions to obtain a prediction percentage higher than 70%. From 10 questions onwards, a percentage equal to or higher than 90% is obtained."

## Discussion


## Related Claims
- [C3-IoC job role matching accuracy increases monotonically with the number of questionnaire questions answered, reaching about 80% accuracy with four questions and nearly 100% with 24](c3-ioc-matching-accuracy-increases-with-questions.md) — related
- [User trial participants rated the C3-IoC system positively for usability, with the Job roles map and Job roles overview the highest-rated components](c3-ioc-user-trial-usability-positive.md) — related
