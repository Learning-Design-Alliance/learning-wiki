---
type: theory
title: "Polytomous-DFIT framework: IRT-based parametric DIF/DTF detection with compensatory (C-DIF) and non-compensatory (NC-DIF) indices"
description: "The DFIT framework is an IRT-based, parametric procedure for detecting differential item and test functioning that \"can be used withdichotomous, polytomous, ormultidimensional data.\" For polytomous data it computes ex..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
sources:
  - id: flowers-1996
    resource: "https://eric.ed.gov/?id=ED401319"
    title: "Flowers, C. P., Oshima, C., & Raju, N. (1996). A Description and Demonstration of the Polytomous-DFIT Framework. https://eric.ed.gov/?id=ED401319"
    author: "Flowers, C. P., Oshima, C., & Raju, N"
---

# Polytomous-DFIT framework: IRT-based parametric DIF/DTF detection with compensatory (C-DIF) and non-compensatory (NC-DIF) indices

> **Theory** · [All theories](index.md)

## Description
The DFIT framework is an IRT-based, parametric procedure for detecting differential item and test functioning that "can be used withdichotomous, polytomous, ormultidimensional data." For polytomous data it computes expected item scores and true test scores under the graded response model for each Focal Group examinee treated as both Focal and Reference group members; DTF is the expected squared difference between the two true scores. DIF decomposes into C-DIF, which allows cancellation across items at the test level, and NC-DIF, which assumes all other items are DIF-free. The article demonstrates the framework with Samejima's graded response model in simulation.

## Design Implications

### Context
#### Requirements
- Item parameter estimation and linking of the Reference Group metric to the Focal Group metric (via PARSCALE and EQUATE) before computing DFIT indices
- A critical/cutoff value for DIF indices, established empirically or by chi-square test
#### Constraints
- Results of the demonstration are specific to the conditions simulated
- The DIF embedding method may have provided optimal detection conditions, creating a ceiling effect
- Efficacy should be researched with other IRT models and mixed item formats

### Target Learners
- Psychometricians and test developers evaluating polytomously scored tests for item bias

### Target Learning Objectives
- Detection of differential item and test functioning in polytomously scored assessments

### Claims
- [Polytomous Dfit Effective Dif Detection Simulation](../claims/polytomous-dfit-effective-dif-detection-simulation.md) [+M]
- [Polytomous C Dif Less Stable Than Nc Dif](../claims/polytomous-c-dif-less-stable-than-nc-dif.md) [+M]
- [Polytomous Dfit Nonuniform High A Not Detected](../claims/polytomous-dfit-nonuniform-high-a-not-detected.md) [~M]

## Related Theories
- 

## Examples
-

## Key Sources
- Flowers, C. P., Oshima, C., & Raju, N. (1996). A Description and Demonstration of the Polytomous-DFIT Framework. https://eric.ed.gov/?id=ED401319
