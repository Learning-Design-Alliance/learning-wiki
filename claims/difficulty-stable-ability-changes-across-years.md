---
type: claim
title: Question difficulty estimates are highly stable across successive years (correlation 0.98) while student ability estimates correlate only moderately (0.54)
description: Question difficulty estimates are highly stable across successive years (correlation 0.98) while student ability estimates correlate only moderately (0.54)
id: difficulty-stable-ability-changes-across-years
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: erva-nihan-kandemir-2024
    resource: "https://doi.org/10.1145/3636555.3636858"
    title: "Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus. (2024). Adaptation of the Multi-Concept Multivariate Elo Rating System to Medical Students' Training Data. The 14th Learning Analytics and Knowledge Conference (LAK '24). https://doi.org/10.1145/3636555.3636858"
    author: Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: erva-nihan-kandemir-2024-2
    resource: "https://doi.org/10.1145/3636555.3636858"
    title: "Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus. (2024). Adaptation of the Multi-Concept Multivariate Elo Rating System to Medical Students' Training Data. The 14th Learning Analytics and Knowledge Conference (LAK '24). https://doi.org/10.1145/3636555.3636858"
    author: Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Question difficulty estimates are highly stable across successive years (correlation 0.98) while student ability estimates correlate only moderately (0.54)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For shared questions, logistic regression difficulty estimates correlate at 0.98 across the 2019-2020 and 2020-2021 years. [→ Erva Nihan Kandemir 2024](#erva-nihan-kandemir-2024)
`q2 i?` Student ability estimates across the same two years correlate at only 0.54, suggesting abilities changed between years. [→ Erva Nihan Kandemir 2024 (2)](#erva-nihan-kandemir-2024-2)

## Evidence

### Erva Nihan Kandemir 2024

Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus. (2024). Adaptation of the Multi-Concept Multivariate Elo Rating System to Medical Students' Training Data. The 14th Learning Analytics and Knowledge Conference (LAK '24). https://doi.org/10.1145/3636555.3636858

`q2 · i?` · `associational · r2`

Comparison of logistic regression estimates across the 2019-2020 and 2020-2021 educational years (Figure 5). For shared questions the article reports "a robust positive correlation of 0.98" for difficulty; no standardized effect size beyond the correlation coefficient is printed.

> "Specifically, for shared questions, we observe a robust positive correlation of 0.98, indicating that the difficulty levels of these questions remain relatively consistent over time."

### Erva Nihan Kandemir 2024 (2)

Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus. (2024). Adaptation of the Multi-Concept Multivariate Elo Rating System to Medical Students' Training Data. The 14th Learning Analytics and Knowledge Conference (LAK '24). https://doi.org/10.1145/3636555.3636858

`q2 · i?` · `associational · r2`

Same two-year logistic regression comparison (Figure 5, right panel): user ability per specialty correlates at 0.54 across years, which the authors read as students' abilities in various specialties having changed over the years, as they anticipated.

> "However, when it comes to students' abilities, the correlation, albeit positive at 0.54, is not as strong."

## Discussion


## Related Claims
- [Elo and logistic regression converge to strongly correlated estimates of question difficulty (r = 0.97) and user ability (r = 0.86) on the same-year data](elo-logistic-regression-estimate-correlation.md) — related
- [Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)](llm-difficulty-magnitude-error-varies-across-models.md) — related
- [Simulated guessing and copying rapidly degrade item difficulty estimates beyond about one-third occurrence, while discrimination and ability estimates remain robust past two-thirds, with no graceful degradation](guessing-copying-robustness-difficulty-vs-discrimination.md) — related
