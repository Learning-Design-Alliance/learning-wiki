---
type: claim
title: Brute-force search over all possible course sets is computationally infeasible for specialisations with large course catalogues
description: Brute-force search over all possible course sets is computationally infeasible for specialisations with large course catalogues
id: brute-force-course-set-search-infeasible
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: luis-alberto-pinos-ullauri-2025
    resource: "https://doi.org/10.1007/s40593-025-00463-z"
    title: "Luis Alberto Pinos Ullauri, Alexis Lebis, Abir Karami, Mathieu Vermeulen, Anthony Fleury, Wim Van den Noortgate. (2025). A Recommender System of Postgraduate Courses Based on Soft Skills: A Psychometric-inspired Approach. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00463-z"
    author: Luis Alberto Pinos Ullauri, Alexis Lebis, Abir Karami, Mathieu Vermeulen, Anthony Fleury, Wim Van den Noortgate
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Brute-force search over all possible course sets is computationally infeasible for specialisations with large course catalogues

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Computing fitness for 10000 course sets took approximately 49.27 seconds on the authors' hardware, implying roughly 131.83 days to exhaustively test all course sets of a single Specialisation 4 student taking 11 of 40 courses. [→ Luis Alberto Pinos Ullauri 2025](#luis-alberto-pinos-ullauri-2025)

## Evidence

### Luis Alberto Pinos Ullauri 2025

Luis Alberto Pinos Ullauri, Alexis Lebis, Abir Karami, Mathieu Vermeulen, Anthony Fleury, Wim Van den Noortgate. (2025). A Recommender System of Postgraduate Courses Based on Soft Skills: A Psychometric-inspired Approach. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00463-z

`q1 · i?` · `design · r2`

Timing measurement on a Python implementation (Intel Core i7-10810U, 32 GB RAM) reported in the Searching for the Optimal Course Set section. The article's linear extrapolation yields "≈ 131.83 days" for one Specialisation 4 student, motivating genetic algorithms.

> "it took approximately 49.27 seconds to compute the fitness of 10000 course sets. This means that with a linear extrapolation, it would take approximately 2.31180144e9(49.27) ∗e−4 = 1.33e10 s ≈ 131.83 days non-stop to try all possible course sets of a single student of Specialisation 4"

## Discussion


## Related Claims
- [Across all score functions and aggregation types, recommended course sets have on average higher fitness than the courses students actually took](recommendations-higher-fitness-than-actual-courses.md) — related
- [Recommended course sets satisfy significantly more soft skill targets than the courses students actually took](recommendations-satisfy-more-soft-skill-targets.md) — related
