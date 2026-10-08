---
type: theory
title: "L*: a modified L statistic that restores a zero chance value when self-transitions are excluded"
description: "L* is a modified version of D'Mello's L statistic intended for use when self-transitions are excluded."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: jeffrey-matayoshi-and-shamya-karumbaiah-2020
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/478"
    title: "Jeffrey Matayoshi and Shamya Karumbaiah. (2020). Adjusting the L Statistic when Self-Transitions are Excluded in Affect Dynamics. Journal of Educational Data Mining, Volume 12, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/478"
    author: Jeffrey Matayoshi and Shamya Karumbaiah
---

# L*: a modified L statistic that restores a zero chance value when self-transitions are excluded

> **Theory** · [All theories](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
L* is a modified version of D'Mello's L statistic intended for use when self-transitions are excluded. It restricts computation to transitions in T_A, the set where the next state is not A, and normalizes the base rates so that, per Theorem 1, "the value of L∗ at chance is equal to zero" when conditional independence holds. The article proves this result and compares L*'s properties to L. L* is equivalent to the λ statistic of Bosch and Paquette (2020) when base rates are computed per sequence, but distinct when averaged over a sample.

## Design Implications

### Context
#### Requirements
- Requires full affect sequences including all self-transitions, from which transitions to A are then excluded
- Assumes P(Bnext|TA) < 1 for the chance-value theorem to apply
#### Constraints
- The article states its current work does not apply to situations where arbitrary non-self transition pairs are impossible, such as systems requiring a correct answer before advancing

### Target Learners
- students in adaptive and digital learning environments

### Target Learning Objectives
- measuring affective state transitions during learning for affect-sensitive interventions

### Claims

- [L Chance Value Nonzero Self Transitions Excluded](../claims/l-chance-value-nonzero-self-transitions-excluded.md) [+M]
- [Theoretical ranges differ sharply: L with self-transitions removed is bounded below by −1 (individual base rates) or −2 (averaged), while L* is bounded by −k+1 (individual) or has no finite lower bound (averaged)](../claims/l-and-l-star-theoretical-value-ranges.md) [+W]
- [Simulations show L* values at chance stay centered at zero even when one affective state's base rate is disproportionately high](../claims/l-star-chance-zero-nonuniform-base-rates-simulation.md) [+W]
- [Simulations with two dominant base rates also show L* at chance centered at zero](../claims/l-star-chance-zero-two-dominant-base-rates.md) [+W]
- [On real student data, L with self-transitions removed makes all transitions from flow appear positive and significant, while L* gives a mix of signs with the only significant value negative](../claims/l-star-student-data-more-coherent-than-l.md) [+W]

## Related Theories
- 

## Examples

- [Recommended procedure for applying L* to sequences of affective states](../strategies/procedure-for-applying-l-star.md)

## Key Sources
- Jeffrey Matayoshi and Shamya Karumbaiah. (2020). Adjusting the L Statistic when Self-Transitions are Excluded in Affect Dynamics. Journal of Educational Data Mining, Volume 12, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/478
