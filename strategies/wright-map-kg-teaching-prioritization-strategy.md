---
type: strategy
id: wright-map-kg-teaching-prioritization-strategy
title: Use Wright maps and knowledge graph centrality to allocate teaching time, in-class assessment, and review priorities to specific knowledge points
description: The article demonstrates a concrete procedure for translating psychometric and network outputs into teaching decisions.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
sources:
  - id: cao-zhen-yu-2024
    resource: "https://doi.org/10.1186/s12909-024-05401-6"
    title: "Cao Zhen-Yu, Lin Feng, Feng Chun. (2024). Interpretation of course conceptual structure and student self-efficacy: an integrated strategy of knowledge graphs with item response modeling. BMC Medical Education. https://doi.org/10.1186/s12909-024-05401-6"
    author: Cao Zhen-Yu, Lin Feng, Feng Chun
---

# Use Wright maps and knowledge graph centrality to allocate teaching time, in-class assessment, and review priorities to specific knowledge points

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 associational), `q3` · 1 of 1 report an effect size · 5 claims rest on one study

## Description
The article demonstrates a concrete procedure for translating psychometric and network outputs into teaching decisions. Wright maps place each student's theta alongside item difficulties, delineating "areas of competence (below the θ value) and incompetence (above the θ value)", so instructors can pinpoint KPs warranting focused review per student. KPs with higher difficulty should receive more teaching time and resources, while highly discriminative KPs such as kp.31 should receive more in-class assessments and feedback. Network centrality identifies necessary points like kp.46 that should be prioritized for mastery because failing them risks comprehension of associated items.

## Design Implications

### Context
#### Requirements
- A fitted IRT model providing theta values and item difficulty and discrimination parameters
- A knowledge graph backbone with centrality measures (hub score, betweenness, Laplacian centrality) for knowledge points
#### Constraints
- A majority of KPs fell within a similar difficulty range, posing a challenge in distinguishing between individuals with high and low abilities
- Items excluded from the IRT model lack difficulty parameters, so assessing their difficulty remains an open problem the article acknowledges

### Target Learners
- Higher education students in rehabilitation/physical therapy courses

### Target Learning Goals
- Prioritizing review of personally challenging knowledge points and allocating teaching resources to difficult, discriminative, and structurally necessary KPs

### Affordances
- [Irt Kg Integrated Kp Assessment Framework](../research-methods/integrated-irt-and-knowledge-graph-modeling-framework-for-quantitatively-assessing-course.md)

## Claims

- [The three-parameter logistic model was selected for estimating SEL and knowledge-point difficulty because lower-scoring students showed more Guttman errors, indicating guessing](../claims/3plm-selected-guessing-parameter.md) [+W]
- [The knowledge graph backbone's main component comprised 58 knowledge points, and IRT difficulty levels could not replace knowledge-point position parameters in the graph](../claims/kg-backbone-position-distinct-from-irt-difficulty.md) [+W]
- [Knowledge point kp.46 (Indications for joint mobility techniques) occupied the most critical position in the knowledge graph backbone while featuring prominently in the IRT model](../claims/kp46-hub-necessary-point.md) [+W]
- [A 50-knowledge-point Mokken scale extracted from a difficulty-rating questionnaire shows high internal consistency for measuring student self-efficacy for learning](../claims/mokken-scale-50-kp-sel-high-reliability.md) [+W]
- [Self-efficacy for learning estimated by IRT was not significantly correlated with one-time exam scores or full-range GPA, but showed a weak positive correlation with GPA among students with positive SEL](../claims/sel-gpa-positive-range-correlation.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Cao Zhen-Yu, Lin Feng, Feng Chun. (2024). Interpretation of course conceptual structure and student self-efficacy: an integrated strategy of knowledge graphs with item response modeling. BMC Medical Education. https://doi.org/10.1186/s12909-024-05401-6
