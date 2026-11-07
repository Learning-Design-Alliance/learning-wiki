---
type: strategy
id: stepwise-addition-of-linkage-variables
title: Improve deterministic linkage rates by progressively adding shared administrative variables to break duplicates
description: "When datasets lack a shared personal identifier, the article's implementable recipe is to link first on the few shared variables (school board ID, gender, birth month and year), omit duplicates, then add further share..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
sources:
  - id: sinclair-jeanne-2023
    resource: "https://doi.org/10.23889/ijpds.v8i1.1843"
    title: "Sinclair Jeanne, Davies Scott, Janus Magdalena. (2023). Student achievement trajectories in Ontario: Creating and validating a province-wide, multi-cohort and longitudinal database. International Journal of Population Data Science. https://doi.org/10.23889/ijpds.v8i1.1843"
    author: Sinclair Jeanne, Davies Scott, Janus Magdalena
---

# Improve deterministic linkage rates by progressively adding shared administrative variables to break duplicates

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
When datasets lack a shared personal identifier, the article's implementable recipe is to link first on the few shared variables (school board ID, gender, birth month and year), omit duplicates, then add further shared variables in stages. Acquiring Toronto District School Board school-level data allowed school identification numbers to be used, which "reduced the number of duplicates and added 51,000 new links," and English learner status and French Immersion participation were then used to resolve remaining duplicate entries.

## Design Implications

### Context
#### Requirements
- Both datasets must contain a set of shared deidentified administrative variables (district ID, gender, birth date) and, ideally, additional shared variables such as school ID, English learner status, and program participation
#### Constraints
- Initial link rates on three variables alone ranged from only 8.6% to 14.9% because large boards contain many same-gender, same-birthday students; students whose data do not link on all variables are excluded

### Target Learners
- Provincial populations of public school students

### Target Learning Goals
- Maximizing linked-case coverage in longitudinal achievement databases built without common personal identifiers

## Claims

- [A deterministic linkage protocol without a common personal identifier linked 50% of Ontario EDI cases to EQAO achievement data across grades](../claims/deterministic-linkage-linked-half-of-edi-cases.md) [+W]
- [Linked and unlinked cases showed negligible differences on demographic variables, supporting generalization to Ontario's student population](../claims/negligible-demographic-differences-linked-unlinked.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Sinclair Jeanne, Davies Scott, Janus Magdalena. (2023). Student achievement trajectories in Ontario: Creating and validating a province-wide, multi-cohort and longitudinal database. International Journal of Population Data Science. https://doi.org/10.23889/ijpds.v8i1.1843
