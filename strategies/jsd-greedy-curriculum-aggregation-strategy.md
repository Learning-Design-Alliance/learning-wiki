---
type: strategy
id: jsd-greedy-curriculum-aggregation-strategy
title: Greedy JSD-based aggregation procedure for constructing standard single- and double-field curricula
description: A curriculum-design recipe that starts from five maximum-credit seed courses per discipline, then iteratively adds candidate courses sorted by weight sum in the course-projected network, accepting a candidate only if...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: gahyoun-gim-2025
    resource: "https://arxiv.org/abs/2502.17841"
    title: "Gahyoun Gim, Jinhyuk Yun and Sang Hoon Lee. (2025). Quantifying interdisciplinary synergy in higher STEM education. arXiv. https://arxiv.org/abs/2502.17841"
    author: Gahyoun Gim, Jinhyuk Yun and Sang Hoon Lee
---

# Greedy JSD-based aggregation procedure for constructing standard single- and double-field curricula

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
A curriculum-design recipe that starts from five maximum-credit seed courses per discipline, then iteratively adds candidate courses sorted by weight sum in the course-projected network, accepting a candidate only if it reduces the average Jensen-Shannon divergence between the model and the real departmental curricula. The article states: "The addition of the candidate course in the model is accepted if ⟨J⟩D ≤ 0, and rejected if ⟨J⟩D > 0." Aggregation terminates when total credits reach at least 80, matching typical Korean four-year major requirements. The same procedure with a two-discipline average JSD criterion builds integrated double-field curricula.

## Design Implications

### Context
#### Requirements
- A standardized course set with credit weights and a course-projected weighted network
- Seed courses chosen as the five with maximum credit assigned to the discipline
#### Constraints
- Designed under Korean national constraints of roughly 80 major credits over four years; the article notes credit-requirement discrepancies might matter more in countries with more flexible curricula

### Target Learners
- Undergraduate STEM students in four-year programs

### Target Learning Goals
- Constructing standard curricula for single disciplines and integrated two-field majors

## Claims

- [An LLM-based pipeline standardizes 126,347 raw Korean STEM course entries into 24,476 standardized courses](../claims/llm-course-standardization-24476-courses.md) [+W]
- [Curriculum synergy scores are highest among closely related engineering disciplines, and science disciplines pair better with their engineering counterparts than with each other](../claims/css-higher-within-engineering-science-engineering-pairs.md) [+W]
- [Engineering disciplines form multiple cores and basic natural science disciplines the periphery in the curriculum synergy network](../claims/css-network-engineering-core-science-periphery.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Gahyoun Gim, Jinhyuk Yun and Sang Hoon Lee. (2025). Quantifying interdisciplinary synergy in higher STEM education. arXiv. https://arxiv.org/abs/2502.17841
