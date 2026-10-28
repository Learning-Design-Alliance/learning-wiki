---
type: design
id: mixed-initiative-field-trip-planning
title: "Mixed-initiative interaction for field trip planning: user control combined with delegated scheduling support"
description: "The article's organizing framework applies Horvitz's mixed-initiative interaction to field trip organization: the teacher leads every design step and selects places and activities, while the system takes over burdenso..."
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

# Mixed-initiative interaction for field trip planning: user control combined with delegated scheduling support

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article's organizing framework applies Horvitz's mixed-initiative interaction to field trip organization: the teacher leads every design step and selects places and activities, while the system takes over burdensome computations such as consistency checks and itinerary optimization. Unlike most personalized tour planners that autonomously generate optimized itineraries and let users only critique complete solutions, this approach combines information filtering with automated scheduling so that "the user [is] in full control of the design process, delegating the system to manage difficult and burdensome tasks such as consistency checks and itinerary optimization". The framework treats PoIs as complex entities aggregating activities, and separates information filtering from itinerary optimization, which is solved as a Travelling Salesman Problem rather than a utility-maximizing Tourist Trip Design Problem.

## Design Implications

### Context
#### Requirements
- An underlying itinerary generation service that computes the schedule taking the shortest time, so feasibility annotations rest on an optimized partial schedule
#### Constraints
- The approach excludes automated planning where the system leads the construction of the itinerary, and does not focus on fine-grained routing or reactive itinerary adaptation during trip execution

### Target Learners
- Teachers of any school level organizing field trips for whole classes

### Learning Goals
- Design of out-of-school learning itineraries aligned with didactic objectives and time constraints

### Claims
- [Fieldtriporganizer Support Autonomy Anxiety Motivation](../claims/fieldtriporganizer-support-autonomy-anxiety-motivation.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Noemi Mauro, Liliana Ardissono, Federica Cena, Livio Scarpinati, Gianluca Torta. (2024). An Intelligent Support System to Help Teachers Plan Field Trips. Int J Artif Intell Educ 34, 793–824. https://doi.org/10.1007/s40593-023-00366-x
