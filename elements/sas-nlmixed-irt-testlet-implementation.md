---
type: element
id: sas-nlmixed-irt-testlet-implementation
title: SAS NLMIXED implementation of the general polytomous testlet model, 2PL/GPCM, and MIRT-SS models
description: The report implements all three models (the general polytomous testlet model, the 2PL/GPCM, and the multidimensional IRT model with simple structure) using the SAS NLMIXED procedure, which fits nonlinear mixed models...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
sources:
  - id: yanmei-li-2010
    resource: "http://www.ets.org/research/contact.html"
    title: "Yanmei Li, Shuhong Li, and Lin Wang. (2010). Application of a General Polytomous Testlet Model to the Reading Section of a Large-Scale English Language Assessment. ETS Research Report RR-10-21. http://www.ets.org/research/contact.html"
    author: Yanmei Li, Shuhong Li, and Lin Wang
---

# SAS NLMIXED implementation of the general polytomous testlet model, 2PL/GPCM, and MIRT-SS models

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
The report implements all three models (the general polytomous testlet model, the 2PL/GPCM, and the multidimensional IRT model with simple structure) using the SAS NLMIXED procedure, which fits nonlinear mixed models by maximizing an approximation to the likelihood integrated over the random effects. The report states "The general polytomous testlet model was estimated using the SAS NLMIXED procedure" and demonstrates "the flexibility of SAS NLMIXED in fitting IRT models." An appendix provides sample SAS code for fitting each of the three models.

## Design Implications

### Context
#### Requirements
- SAS software with the NLMIXED procedure; the study used Gauss-Hermite quadrature and the dual quasi-Newton algorithm
#### Constraints
- The report states the computational time was quite long (about 20-35 hours), which limits its use in extensive data analyses, and that alternative software needs to be explored in the future

### Target Learners
- Psychometricians and researchers calibrating testlet-based assessments

### Target Learning Goals
- Estimating item parameters under models that account for local dependence among testlet items

### Affordances
- [General Polytomous Testlet Model](../theories/general-polytomous-testlet-model.md)

## Related Elements
- 

## Examples
-

## Key Sources
- Yanmei Li, Shuhong Li, and Lin Wang. (2010). Application of a General Polytomous Testlet Model to the Reading Section of a Large-Scale English Language Assessment. ETS Research Report RR-10-21. http://www.ets.org/research/contact.html
