---
type: strategy
id: instructor-in-the-loop-visualization-tuning
title: Involve the course instructor in rating and tuning visualization and model parameters
description: "This strategy embeds the domain expert (the course instructor) in the analysis loop: the expert rates candidate visualizations for usefulness, favouring those that both confirm known patterns and contain novel but pla..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: pardos-2018
    resource: "https://github.com/CAHLR/d3-scatterplot"
    title: "Pardos, Z. A., & Horodyskyj, L. (2018). Analysis of Student Behaviour in Habitable Worlds Using Continuous Representation Visualization. https://github.com/CAHLR/d3-scatterplot"
    author: "Pardos, Z. A., & Horodyskyj, L"
---

# Involve the course instructor in rating and tuning visualization and model parameters

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
This strategy embeds the domain expert (the course instructor) in the analysis loop: the expert rates candidate visualizations for usefulness, favouring those that both confirm known patterns and contain novel but plausible ones, then interprets the chosen visualization. The article states that "Involving instructors in the tuning of the visualization and model parameters produces analyses with a desirable mixture of expected and unexpected, but explainable, patterns." The rationale is that if a visualization depicts patterns the expert knows to be true, other aspects of it may also be true but not yet known. In the study, the co-creator rated 21 visualizations on a five-point scale.

## Design Implications

### Context
#### Requirements
- Access to a subject matter expert with implicit knowledge of the course
- A set of visualizations produced across a range of hyperparameter values for the expert to rate
#### Constraints
- The article flags the laborious tuning effort as an obstacle for instructors without researcher support and notes it is an open question whether analytical data fluency or light professional development suffices for independent use

### Target Learners
- online higher education students

### Target Learning Goals
- surfacing behavioural patterns to improve course design and instruction

### Affordances
- [Skip Gram Clickstream Representation Visualization](../research-methods/skip-gram-representation-learning-of-clickstream-behaviour-with-t-sne-visualization.md)

## Claims

- [The highest-rated skip-gram visualization of Habitable Worlds used a window size of five and vector size of twelve, with low vector sizes yielding overly sequential plots](../claims/skip-gram-hyperparameter-tuning-results.md) [+W]

## Related Strategies

- [Use learning analytics with human-in-the-loop evaluation to disassemble the data jigsaw from VR training systems](la-human-in-the-loop-vrts-evaluation-strategy.md)
- [Human-in-the-loop generative pipeline for synthetic classroom training data with domain-expert validation](generative-synthetic-classroom-data-pipeline-strategy.md)
- [Center co-design with teachers and students throughout AI tool R&D, using human-in-the-loop workflows as a primary risk mitigation](co-design-human-in-the-loop-ai-edtech-strategy.md)
- [Position the instructor as human-in-the-loop reviewer of AI-generated difficulty reports before any feedback reaches students](instructor-in-loop-ai-difficulty-reports.md)

## Examples
-

## Key Sources
- Pardos, Z. A., & Horodyskyj, L. (2018). Analysis of Student Behaviour in Habitable Worlds Using Continuous Representation Visualization. https://github.com/CAHLR/d3-scatterplot
