---
type: design
id: visual-feasibility-annotation-time-constraints
title: "Visual feasibility annotation of options against the itinerary's time constraints"
description: This lesson/task-level design pattern keeps the planner constantly aware of the temporal feasibility of each candidate item while an itinerary is built incrementally.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
sources:
  - id: noemi-mauro-2024
    resource: "https://doi.org/10.1007/s40593-023-00366-x"
    title: "Noemi Mauro, Liliana Ardissono, Federica Cena, Livio Scarpinati, Gianluca Torta. (2024). An Intelligent Support System to Help Teachers Plan Field Trips. Int J Artif Intell Educ 34, 793–824. https://doi.org/10.1007/s40593-023-00366-x"
    author: Noemi Mauro, Liliana Ardissono, Federica Cena, Livio Scarpinati, Gianluca Torta
---

# Visual feasibility annotation of options against the itinerary's time constraints

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
This lesson/task-level design pattern keeps the planner constantly aware of the temporal feasibility of each candidate item while an itinerary is built incrementally. Each PoI and activity is annotated with "a green or red semaphore depending on whether the item can be included in the itinerary without exceeding the available time or not", alongside a continuously updated display of spare time. If the user disregards the indication and causes a scheduling error, the application explains the problem. In the study's thematic analysis, most participants considered awareness of the remaining time very useful, and some missed this functionality in the baseline planner.

## Design Implications

### Context
#### Requirements
- An itinerary generator invoked after each item addition or removal so the next feasibility estimate relies on a refreshed, optimized schedule
#### Constraints
- The heuristic feasibility estimation may generate false negatives because it does not optimize the schedule of the revised itinerary and may overestimate displacement time

### Target Learners
- Teachers planning multi-stop itineraries under fixed time budgets

### Learning Goals
- Informed selection of places and activities that fit the trip's temporal constraints

### Claims
- [Fieldtriporganizer Higher Usability Than Baseline](../claims/fieldtriporganizer-higher-usability-than-baseline.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Noemi Mauro, Liliana Ardissono, Federica Cena, Livio Scarpinati, Gianluca Torta. (2024). An Intelligent Support System to Help Teachers Plan Field Trips. Int J Artif Intell Educ 34, 793–824. https://doi.org/10.1007/s40593-023-00366-x
