---
type: theory
title: "Latent class forest: a random forest ensemble of latent class trees for model-based clustering of at-risk students"
description: The latent class forest (LCF) embeds latent class analysis within a random forest ensemble, recursively partitioning observations via EM-estimated two-class splits at each internal node, then clustering a pairwise dis...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: pelaez-2019
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/283"
    title: "Pelaez, K., Levine, R. A., Guarcello, M., Laumakis, M., & Fan, J. (2019). Using a Latent Class Forest to Identify At-Risk Students in Higher Education. Journal of Educational Data Mining, 11(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/283"
    author: "Pelaez, K., Levine, R. A., Guarcello, M., Laumakis, M., & Fan, J"
---

# Latent class forest: a random forest ensemble of latent class trees for model-based clustering of at-risk students

> **Theory** · [All theories](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The latent class forest (LCF) embeds latent class analysis within a random forest ensemble, recursively partitioning observations via EM-estimated two-class splits at each internal node, then clustering a pairwise distance matrix built from terminal-node similarity. The authors state: "We introduce a latent class forest, a latent class analysis and a random forest ensemble that will recursively partition observations into groups to help identify at-risk students." It extends RPMM and latent class trees, using bootstrapped samples and random subsets of inputs per split.

## Design Implications

### Context
#### Requirements
- A user-selected number of trees T (at least 500 generally recommended) and a terminal-node minimum size k; the application used a bootstrap proportion of 2/3 and k > 30
#### Constraints
- LCA is computationally expensive and may select a large number of groups when sample size and number of features are large; the EM algorithm guarantees convergence only to a local maximum and assumes local independence

### Target Learners
- higher education students in large enrollment bottleneck courses

### Target Learning Objectives
- early identification of students at risk of failing a course prior to enrollment

### Claims

- [High-risk LCF groups concentrate URM, first-generation, EOP, Compact, commuter, and lower-academic-preparation students](../claims/lcf-high-risk-group-demographic-composition.md) [+W]
- [LCF showed the most differentiated input patterns across risk groups (11 inputs) versus comparison methods](../claims/lcf-most-differentiated-input-patterns.md) [+W]
- [LCF outperformed k-means, RPMM, and SS-RPMM on cluster validity indices in the same PSY 101 data](../claims/lcf-outperforms-comparison-methods-validity-indices.md) [+W]
- [LCF identifies three PSY 101 risk groups with strongly differentiated DFW rates of 28%, 12%, and 6%](../claims/lcf-three-risk-groups-dfw-rates.md) [+W]
- [SI attendance was associated with a significant DFW decrease in the highest-risk group but smaller, non-significant decreases in mid- and low-risk groups](../claims/si-benefit-highest-risk-group.md) [+W]

## Related Theories
- 

## Examples

- [Use LCF risk clusters to target Supplemental Instruction recruitment and resource allocation](../strategies/lcf-clusters-guide-si-resource-allocation.md)

## Key Sources
- Pelaez, K., Levine, R. A., Guarcello, M., Laumakis, M., & Fan, J. (2019). Using a Latent Class Forest to Identify At-Risk Students in Higher Education. Journal of Educational Data Mining, 11(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/283
