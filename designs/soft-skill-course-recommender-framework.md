---
type: design
id: soft-skill-course-recommender-framework
title: Soft-skill-based course recommender system framework (psychometric model + fitness functions + genetic algorithm)
description: "A recommender system that takes a student's course set as input, predicts expected soft skill proficiency with an ensemble of psychometric models, compares it to a targeted soft skill profile via score functions, aggr..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
sources:
  - id: luis-alberto-pinos-ullauri-2025
    resource: "https://doi.org/10.1007/s40593-025-00463-z"
    title: "Luis Alberto Pinos Ullauri, Alexis Lebis, Abir Karami, Mathieu Vermeulen, Anthony Fleury, Wim Van den Noortgate. (2025). A Recommender System of Postgraduate Courses Based on Soft Skills: A Psychometric-inspired Approach. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00463-z"
    author: Luis Alberto Pinos Ullauri, Alexis Lebis, Abir Karami, Mathieu Vermeulen, Anthony Fleury, Wim Van den Noortgate
---

# Soft-skill-based course recommender system framework (psychometric model + fitness functions + genetic algorithm)

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A recommender system that takes a student's course set as input, predicts expected soft skill proficiency with an ensemble of psychometric models, compares it to a targeted soft skill profile via score functions, aggregates the per-skill scores into a single fitness value, and uses genetic algorithms to search for the course set with the highest fitness. The article's stated aim is "to propose a recommender system framework, leveraging psychometric approaches in order to reduce the soft skills gap". It was illustrated on real data from three cohorts, producing recommendations for 172 different course sets.

## Design Implications

### Context
#### Requirements
- A targeted soft skill profile per specialisation
- Trained psychometric models predicting per-category probabilities for each soft skill
- A fitness function combining score functions and an aggregation method
#### Constraints
- Designed for short-term small-size datasets from higher education, where CF/CBF approaches lack sufficient interaction data
- Genetic algorithm hyper-parameters were chosen empirically through preliminary tests

### Target Learners
- postgraduate students choosing specialisation courses

### Learning Goals
- reaching targeted soft skill proficiency by the end of the program

### Claims
- [Recommendations Higher Fitness Than Actual Courses](../claims/recommendations-higher-fitness-than-actual-courses.md) [+M]
- [Recommendations Satisfy More Soft Skill Targets](../claims/recommendations-satisfy-more-soft-skill-targets.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Luis Alberto Pinos Ullauri, Alexis Lebis, Abir Karami, Mathieu Vermeulen, Anthony Fleury, Wim Van den Noortgate. (2025). A Recommender System of Postgraduate Courses Based on Soft Skills: A Psychometric-inspired Approach. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00463-z
