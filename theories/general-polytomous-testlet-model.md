---
type: theory
title: "General polytomous testlet model: a bifactor-style IRT model extending the general testlet model to mixed dichotomous and polytomous testlet items via a generalized partial credit model"
description: The general polytomous testlet model is an item response theory model for testlet-based tests containing both dichotomously and polytomously scored items.
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

# General polytomous testlet model: a bifactor-style IRT model extending the general testlet model to mixed dichotomous and polytomous testlet items via a generalized partial credit model

> **Theory** · [All theories](index.md)
> **Evidence** · 6 claims (4 for, 1 mixed, 1 against) · 2 studies, `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The general polytomous testlet model is an item response theory model for testlet-based tests containing both dichotomously and polytomously scored items. It extends the general testlet model of Li, Bolt, and Fu (2006), which the report notes "is essentially the same as the bifactor model", by using a generalized partial credit model for the polytomous items. Each item loads on a general ability dimension and on a secondary dimension associated with its testlet, with separate discrimination parameters for the two factors. According to the report, "This model not only takes into account local dependence within the testlets but also provides more information about how items within a testlet are influenced by the testlet factor."

## Design Implications

### Context
#### Requirements
- Data from testlet-based tests in which items share common stimuli and some items are polytomously scored
- Estimation via marginal maximum likelihood, implemented in the study with the SAS NLMIXED procedure using Gauss-Hermite quadrature and a dual quasi-Newton algorithm
#### Constraints
- The report states one drawback is that more item parameters need to be estimated, and thus the fit of the model may not be good
- Computational time was quite long (about 20-35 hours), which the report says limits its use in extensive data analyses

### Target Learners
- Examinees of large-scale English language assessments with reading testlets

### Target Learning Objectives
- Accurate measurement of reading ability from testlet-based assessments

### Claims

- [Polytomous Testlet Model Good Parameter Recovery](../claims/polytomous-testlet-model-good-parameter-recovery.md) [+M]
- [Mirt Ss Fits Testlet Data Better](../claims/mirt-ss-fits-testlet-data-better.md) [-M]
- [In simulation, ignoring local dependence overestimates reliability, and the overestimation grows with the size of the testlet effect (17.0%-21.8% decrease under the larger testlet effect vs. 4.8%-7.4% under the small)](../claims/ignored-local-dependence-overestimates-reliability-simulation.md) [+W]
- [In operational reading-test data, item parameter estimates from a standard 2PL/GPCM that ignores local dependence closely match those from the testlet model (average correlations 0.9893 and 0.9978)](../claims/local-dependence-small-impact-item-parameters-real-data.md) [+W]
- [In operational reading-test data, ignoring local dependence inflates reliability estimates, with passage-based alpha 2.3%-4.9% lower than item-based alpha across six test forms](../claims/real-data-reliability-overestimated-2-3-to-4-9-percent.md) [+W]
- [The proportionality restrictions that the testlet model imposes on the bifactor model were implausible in the applied dataset, as specific-to-general loading quotients varied far from constant within testlets](../claims/testlet-proportionality-restrictions-implausible.md) [~W]

## Related Theories
- 

## Examples

- [SAS NLMIXED implementation of the general polytomous testlet model, 2PL/GPCM, and MIRT-SS models](../elements/sas-nlmixed-irt-testlet-implementation.md)

## Key Sources
- Yanmei Li, Shuhong Li, and Lin Wang. (2010). Application of a General Polytomous Testlet Model to the Reading Section of a Large-Scale English Language Assessment. ETS Research Report RR-10-21. http://www.ets.org/research/contact.html
