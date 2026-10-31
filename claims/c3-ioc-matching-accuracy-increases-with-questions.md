---
type: claim
title: "C3-IoC job role matching accuracy increases monotonically with the number of questionnaire questions answered, reaching about 80% accuracy with four questions and nearly 100% with 24"
description: "C3-IoC job role matching accuracy increases monotonically with the number of questionnaire questions answered, reaching about 80% accuracy with four questions and nearly 100% with 24"
id: c3-ioc-matching-accuracy-increases-with-questions
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
    rigour: 3
  - id: adán-josé-garcía-2023-2
    resource: "https://doi.org/10.1007/s40593-022-00317-y"
    title: "Adán José-García, Alison Sneyd, Ana Melro, Anaïs Ollagnier, Georgina Tarling, Haiyang Zhang, Mark Stevenson, Richard Everson, Rudy Arthur. (2023). C3-IoC: A Career Guidance System for Assessing Student Skills using Machine Learning and Network Visualisation. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00317-y"
    author: Adán José-García, Alison Sneyd, Ana Melro, Anaïs Ollagnier, Georgina Tarling, Haiyang Zhang, Mark Stevenson, Richard Everson, Rudy Arthur
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# C3-IoC job role matching accuracy increases monotonically with the number of questionnaire questions answered, reaching about 80% accuracy with four questions and nearly 100% with 24

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2`–`r3` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Community assignment accuracy for dummy user profiles increases from about 80% with four questions to nearly 100% with 24 questions answered. [→ Adán José-García 2023](#adan-jose-garcia-2023)
`q2 i?` Success rate of placing the true job role in the top 10 matches increases rapidly with more questions; a percentage equal to or higher than 90% is obtained from 10 questions onwards. [→ Adán José-García 2023 (2)](#adan-jose-garcia-2023-2)

## Evidence

### Adán José-García 2023

Adán José-García, Alison Sneyd, Ana Melro, Anaïs Ollagnier, Georgina Tarling, Haiyang Zhang, Mark Stevenson, Richard Everson, Rudy Arthur. (2023). C3-IoC: A Career Guidance System for Assessing Student Skills using Machine Learning and Network Visualisation. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00317-y

`q2 · i?` · `design · r3`

Validation experiment constructing a dummy user for each of the 381 general job corpus job roles and varying answered questions Q from 4 to 24. The article reports the accuracy increase "from about 80% when answering four questions to nearly 100%" with 24 questions; no standardised effect size is printed.

> "In general, it is evident that the performance of the assignment of dummy user profiles to the correct communities continually increases as more questions are answered. The accuracy increases from about 80% when answering four questions to nearly 100% when the number of questions answered increases to 24 questions."

### Adán José-García 2023 (2)

Adán José-García, Alison Sneyd, Ana Melro, Anaïs Ollagnier, Georgina Tarling, Haiyang Zhang, Mark Stevenson, Richard Everson, Rudy Arthur. (2023). C3-IoC: A Career Guidance System for Assessing Student Skills using Machine Learning and Network Visualisation. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00317-y

`q2 · i?` · `design · r2`

Numerical evaluation of Success Rate Percentage SRP(k) for k = 1, 5 and 10 over dummy users for Q = 4 to 24. The article reports the top-5/top-10 success rate "increases rapidly with the number of questions answered"; no effect size printed.

> "As expected, the success rate for matching the true job in the top 5 or 10 best matches increases rapidly with the number of questions answered. However, when the exact match k = 1 is required, the success rate is initially proportional to Q"

## Discussion


## Related Claims
- [Exact-match (k=1) job role prediction requires approximately 24 questionnaire questions to achieve an average success rate of 90%, while at least six questions yield a top-10 success rate above 70%](c3-ioc-exact-match-needs-24-questions.md) — related
- [On MedQA, GPT-5.4-mini's accuracy increases monotonically with prompt sophistication across semantically equivalent questions, with generated Low Literacy prompt variants scoring significantly below Prompt Engineer variants](prompt-privilege-monotonic-accuracy-gap-medqa.md) — related
- [User trial participants rated the C3-IoC system positively for usability, with the Job roles map and Job roles overview the highest-rated components](c3-ioc-user-trial-usability-positive.md) — related
