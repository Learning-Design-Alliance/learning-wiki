---
type: research-method
id: latent-class-forest
title: Latent class forest
description: The latent class forest (LCF) embeds latent class analysis within a random forest ensemble, recursively partitioning observations via EM-estimated two-class splits at each internal node, then clustering a pairwise distance matrix built from terminal-node similarity.
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: pelaez-2019
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/283"
    title: "Pelaez, K., Levine, R. A., Guarcello, M., Laumakis, M., & Fan, J. (2019). Using a Latent Class Forest to Identify At-Risk Students in Higher Education. Journal of Educational Data Mining, 11(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/283"
    author: "Pelaez, K., Levine, R. A., Guarcello, M., Laumakis, M., & Fan, J"
---

# Latent class forest

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
The latent class forest (LCF) embeds latent class analysis within a random forest ensemble, recursively partitioning observations via EM-estimated two-class splits at each internal node, then clustering a pairwise distance matrix built from terminal-node similarity. The authors state: "We introduce a latent class forest, a latent class analysis and a random forest ensemble that will recursively partition observations into groups to help identify at-risk students." It extends RPMM and latent class trees, using bootstrapped samples and random subsets of inputs per split.

## Accounts
<!-- How each source describes or uses the method -->
- **Latent class forest: a random forest ensemble of latent class trees for model-based clustering of at-risk students**: The latent class forest (LCF) embeds latent class analysis within a random forest ensemble, recursively partitioning observations via EM-estimated two-class splits at each internal node, then clustering a pairwise distance matrix built from terminal-node similarity. The authors state: "We introduce a latent class forest, a latent class analysis and a random forest ensemble that will recursively partition observations into groups to help identify at-risk students." It extends RPMM and latent class trees, using bootstrapped samples and random subsets of inputs per split. (Pelaez et al. (2019))

### Claims

## Related Research Methods
-

## Key Sources
- Pelaez, K., Levine, R. A., Guarcello, M., Laumakis, M., & Fan, J. (2019). Using a Latent Class Forest to Identify At-Risk Students in Higher Education. Journal of Educational Data Mining, 11(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/283

<!-- merged 2026-10-10 from theories/latent-class-forest-method ("Latent class forest: a random forest ensemble of latent class trees for model-based clustering of at-risk students"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

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


## Related Theories
- 

## Examples

- [Use LCF risk clusters to target Supplemental Instruction recruitment and resource allocation](../strategies/lcf-clusters-guide-si-resource-allocation.md)

## Key Sources
- Pelaez, K., Levine, R. A., Guarcello, M., Laumakis, M., & Fan, J. (2019). Using a Latent Class Forest to Identify At-Risk Students in Higher Education. Journal of Educational Data Mining, 11(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/283
-->
