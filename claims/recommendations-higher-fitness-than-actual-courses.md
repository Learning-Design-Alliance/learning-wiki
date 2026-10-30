---
type: claim
title: Across all score functions and aggregation types, recommended course sets have on average higher fitness than the courses students actually took
description: Across all score functions and aggregation types, recommended course sets have on average higher fitness than the courses students actually took
id: recommendations-higher-fitness-than-actual-courses
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: luis-alberto-pinos-ullauri-2025
    resource: "https://doi.org/10.1007/s40593-025-00463-z"
    title: "Luis Alberto Pinos Ullauri, Alexis Lebis, Abir Karami, Mathieu Vermeulen, Anthony Fleury, Wim Van den Noortgate. (2025). A Recommender System of Postgraduate Courses Based on Soft Skills: A Psychometric-inspired Approach. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00463-z"
    author: Luis Alberto Pinos Ullauri, Alexis Lebis, Abir Karami, Mathieu Vermeulen, Anthony Fleury, Wim Van den Noortgate
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Across all score functions and aggregation types, recommended course sets have on average higher fitness than the courses students actually took

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Recommended course sets yield a positive average fitness increase over actual course histories, ranging from 2.2% (Quadratic, Specialisation 1) to 21.9% (Logistic, Specialisation 4) in compensatory terms and from 23.1% to 997.2% in partially compensatory terms. [→ Luis Alberto Pinos Ullauri 2025](#luis-alberto-pinos-ullauri-2025)

## Evidence

### Luis Alberto Pinos Ullauri 2025

Luis Alberto Pinos Ullauri, Alexis Lebis, Abir Karami, Mathieu Vermeulen, Anthony Fleury, Wim Van den Noortgate. (2025). A Recommender System of Postgraduate Courses Based on Soft Skills: A Psychometric-inspired Approach. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00463-z

`q2 · i?` · `design · r2`

Numerical optimisation results summarised in Table 7 from genetic algorithm runs on the test set of students at stage 2. The article reports the average fitness increase of recommendations over actual courses, e.g. "2.2% in Quadratic in Specialisation 1 to 21.9% in Logistic in Specialisation 4". All students in the test set benefited from a higher fitness.

> "It can be seen that across all score functions and aggregation types, the average increase in the fitness is positive. This increase varies from 2.2% in Quadratic in Specialisation 1 to 21.9% in Logistic in Specialisation 4 in compensatory terms."

## Discussion


## Related Claims
- [Brute-force search over all possible course sets is computationally infeasible for specialisations with large course catalogues](brute-force-course-set-search-infeasible.md) — related
- [Fitness increases vary across the 10 soft skills, with some skills showing small negative increases under compensatory aggregation](fitness-increases-vary-across-soft-skills.md) — related
- [Recommended course sets satisfy significantly more soft skill targets than the courses students actually took](recommendations-satisfy-more-soft-skill-targets.md) — related
