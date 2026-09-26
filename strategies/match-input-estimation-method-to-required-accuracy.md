---
type: strategy
id: match-input-estimation-method-to-required-accuracy
title: Match the input-parameter estimation method (managerial estimates vs. time study) to the accuracy the simulation purpose requires
description: The report advises choosing how to determine simulation input parameters according to the purpose of the run.
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
sources:
  - id: cohen-1975
    resource: "https://eric.ed.gov/?id=CE005601"
    title: "Cohen, Malcolm S. (1975). A Study of On-Line Use of Job Information in Employment Service Local Offices. Volume II: A Simulation Study. https://eric.ed.gov/?id=CE005601"
    author: Cohen, Malcolm S
---

# Match the input-parameter estimation method (managerial estimates vs. time study) to the accuracy the simulation purpose requires

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The report advises choosing how to determine simulation input parameters according to the purpose of the run. For a manager seeking better understanding of minor changes, estimating values from his own experience may suffice; "When a high degree of accuracy is needed; e.g., if thesimulation is being used to develop budget estimates, a timestudy may be necessary." A descriptive model of the proposed configuration should be developed before the time study, which can then both estimate parameters and validate the model, including statistically testing assumptions such as whether interview length depends on the applicant's occupation.

## Design Implications

### Context
#### Requirements
- A detailed descriptive model of the proposed office configuration should be developed prior to conducting a time study
#### Constraints
- If the proposed office configuration is sufficiently different from the present one, a time study may not be possible, and accuracy is then limited by the predictive technique used

### Target Learners
- Employment Service planners and managers conducting simulation studies

### Target Learning Goals
- Estimating simulation input parameters at an appropriate level of accuracy and cost

### Affordances
- [Descriptive Simulation Modeling Framework Es Office](../theories/descriptive-simulation-modeling-framework-es-office.md)

## Related Strategies

- [Use simulation as a non-threatening alternative to direct experimentation when testing office reorganizations](simulation-as-non-threatening-experimentation-alternative.md)
- [Initialize BKT parameters from simulated student data when no human data is available](initialize-bkt-parameters-from-simulated-data.md)
- [Estimate a skill's minimum BKT-BF RSS a priori from dim, n, and percent_correct before running the full grid search](estimate-minimum-rss-from-skill-variables.md)

## Examples
-

## Key Sources
- Cohen, Malcolm S. (1975). A Study of On-Line Use of Job Information in Employment Service Local Offices. Volume II: A Simulation Study. https://eric.ed.gov/?id=CE005601
