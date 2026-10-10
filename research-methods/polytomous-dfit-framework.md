---
type: research-method
id: polytomous-dfit-framework
title: Polytomous DFIT framework
description: "The DFIT framework is an IRT-based, parametric procedure for detecting differential item and test functioning that \"can be used withdichotomous, polytomous, ormultidimensional data.\" For polytomous data it computes expected item scores and true test scores under the graded response model for each Fo"
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: flowers-1996
    resource: "https://eric.ed.gov/?id=ED401319"
    title: "Flowers, C. P., Oshima, C., & Raju, N. (1996). A Description and Demonstration of the Polytomous-DFIT Framework. https://eric.ed.gov/?id=ED401319"
    author: "Flowers, C. P., Oshima, C., & Raju, N"
  - id: flowers-1997
    resource: "https://eric.ed.gov/?id=ED410300"
    title: "Flowers, C. P., Oshima, T. C., & Raju, N. S. (1997). The Relationship between Polytomous DFIT and Other Polytomous DIF Procedures. Paper presented at the NCME Annual Meeting, Chicago. https://eric.ed.gov/?id=ED410300"
    author: "Flowers, C. P., Oshima, T. C., & Raju, N. S"
---

# Polytomous DFIT framework

> **Research Method** · [All research methods](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 2 studies (2 causal), `q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The DFIT framework is an IRT-based, parametric procedure for detecting differential item and test functioning that "can be used withdichotomous, polytomous, ormultidimensional data." For polytomous data it computes expected item scores and true test scores under the graded response model for each Focal Group examinee treated as both Focal and Reference group members; DTF is the expected squared difference between the two true scores. DIF decomposes into C-DIF, which allows cancellation across items at the test level, and NC-DIF, which assumes all other items are DIF-free. The article demonstrates the framework with Samejima's graded response model in simulation.

## Accounts
<!-- How each source describes or uses the method -->
- **Polytomous-DFIT framework: IRT-based parametric DIF/DTF detection with compensatory (C-DIF) and non-compensatory (NC-DIF) indices**: The DFIT framework is an IRT-based, parametric procedure for detecting differential item and test functioning that "can be used withdichotomous, polytomous, ormultidimensional data." For polytomous data it computes expected item scores and true test scores under the graded response model for each Focal Group examinee treated as both Focal and Reference group members; DTF is the expected squared difference between the two true scores. DIF decomposes into C-DIF, which allows cancellation across items at the test level, and NC-DIF, which assumes all other items are DIF-free. The article demonstrates the framework with Samejima's graded response model in simulation. (Flowers et al. (1996))
- **Polytomous DFIT framework for differential item and test functioning**: An IRT-based parametric procedure proposed by Raju, van der Linden, and Fleer (1995) for detecting differential item functioning and differential test functioning in polytomously scored data. It computes expected item scores as weighted sums of item category response functions and sums them into true test scores; the article explains that "the difference between the dichotomous and polytomous DFIT framework is the calculation of the item true score," after which the framework is identical to the dichotomous case. It yields compensatory (CDIF) and noncompensatory (NCDIF) DIF indices, the latter assuming all other items are DIF-free. (Flowers et al. (1997))

### Claims
- [The polytomous-DFIT framework effectively identified DTF and DIF in polytomously scored data under the simulated conditions](../claims/polytomous-dfit-effective-dif-detection-simulation.md) [+M]
- [C-DIF was less stable than NC-DIF across simulated conditions](../claims/polytomous-c-dif-less-stable-than-nc-dif.md) [+M]
- [Type of DIF affected detection: nonuniform DIF items with higher a-parameters were not detected whereas lower a-parameter items were](../claims/polytomous-dfit-nonuniform-high-a-not-detected.md) [~M]
- [The polytomous DFIT framework shows Type I error rates close to nominal alpha except when the number of DIF items and DIF magnitude are highest](../claims/polytomous-dfit-type-i-error-near-alpha.md) [+M]
- [DIF detection rates for all indices are higher with larger samples, equivalent distributions, fewer DIF items, greater DIF magnitude, and larger a-parameters](../claims/polytomous-dif-detection-rate-factors.md) [+M]

## Related Research Methods
-

## Key Sources
- Flowers, C. P., Oshima, C., & Raju, N. (1996). A Description and Demonstration of the Polytomous-DFIT Framework. https://eric.ed.gov/?id=ED401319
- Flowers, C. P., Oshima, T. C., & Raju, N. S. (1997). The Relationship between Polytomous DFIT and Other Polytomous DIF Procedures. Paper presented at the NCME Annual Meeting, Chicago. https://eric.ed.gov/?id=ED410300

<!-- merged 2026-10-10 from theories/polytomous-dfit-framework-polytomous-extension ("Polytomous-DFIT framework: IRT-based parametric DIF/DTF detection with compensatory (C-DIF) and non-compensatory (NC-DIF) indices"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.
- Flowers, C. P., Oshima, T. C., & Raju, N. S. (1997). The Relationship between Polytomous DFIT and Other Polytomous DIF Procedures. Paper presented at the NCME Annual Meeting, Chicago. https://eric.ed.gov/?id=ED410300

# Polytomous-DFIT framework: IRT-based parametric DIF/DTF detection with compensatory (C-DIF) and non-compensatory (NC-DIF) indices

> **Theory** · [All theories](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

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
-->

<!-- merged 2026-10-10 from theories/polytomous-dfit-framework ("Polytomous DFIT framework for differential item and test functioning"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Polytomous DFIT framework for differential item and test functioning

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
An IRT-based parametric procedure proposed by Raju, van der Linden, and Fleer (1995) for detecting differential item functioning and differential test functioning in polytomously scored data. It computes expected item scores as weighted sums of item category response functions and sums them into true test scores; the article explains that "the difference between the dichotomous and polytomous DFIT framework is the calculation of the item true score," after which the framework is identical to the dichotomous case. It yields compensatory (CDIF) and noncompensatory (NCDIF) DIF indices, the latter assuming all other items are DIF-free.

## Design Implications

### Context
#### Requirements
- Requires IRT ability and item parameter estimation and an equating procedure, as with Lord's chi-square
#### Constraints
- Statistical significance testing of NCDIF is overly sensitive at large sample sizes, so empirical cutoff values are recommended
- The DTF (CDIF) procedure was not examined in this study

### Target Learners
- Psychometricians and test developers working with polytomously scored assessments

### Target Learning Objectives
- Detecting differential item functioning in polytomous test data

### Claims
- [Polytomous Dfit Type I Error Near Alpha](../claims/polytomous-dfit-type-i-error-near-alpha.md) [+M]
- [Polytomous Dif Detection Rate Factors](../claims/polytomous-dif-detection-rate-factors.md) [+M]

## Related Theories
- 

## Examples
-

## Key Sources
- Flowers, C. P., Oshima, T. C., & Raju, N. S. (1997). The Relationship between Polytomous DFIT and Other Polytomous DIF Procedures. Paper presented at the NCME Annual Meeting, Chicago. https://eric.ed.gov/?id=ED410300
-->
