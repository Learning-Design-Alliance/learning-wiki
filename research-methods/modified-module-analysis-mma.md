---
type: research-method
id: modified-module-analysis-mma
title: Modified Module Analysis (MMA)
description: Modified Module Analysis (MMA) is a network-analytic method for multiple-choice concept inventory data that builds the response network from the correlation matrix of incorrect answers rather than the raw adjacency matrix, sparsifies it by statistical significance and a correlation threshold, and ap
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
---

# Modified Module Analysis (MMA)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
Modified Module Analysis (MMA) is a network-analytic method for multiple-choice concept inventory data that builds the response network from the correlation matrix of incorrect answers rather than the raw adjacency matrix, sparsifies it by statistical significance and a correlation threshold, and applies bootstrapped community detection to find stable groups of incorrect answers. The article proposes it as a modification of MAMCR that "investigates the community structure of the correlation matrix".

## Accounts
<!-- How each source describes or uses the method -->
- **Modified Module Analysis (MMA): correlation-matrix network method with bootstrapped community detection for concept inventory responses**: Modified Module Analysis (MMA) is a network-analytic method for multiple-choice concept inventory data that builds the response network from the correlation matrix of incorrect answers rather than the raw adjacency matrix, sparsifies it by statistical significance and a correlation threshold, and applies bootstrapped community detection to find stable groups of incorrect answers. The article proposes it as a modification of MAMCR that "investigates the community structure of the correlation matrix". (James Wells et al. (2019))
- **Modified Module Analysis (MMA): a network-analytic method for identifying communities of incorrect responses on multiple-choice conceptual inventories**: MMA adapts the Module Analysis of Multiple-Choice Responses method for large datasets by building a network whose nodes are incorrect responses and whose edge weights are correlations between responses. As the article states, "In MMA, the edge weight is the correlation coeﬃcient between the two responses." Edges below r > 0.2 or non-significant at α = 0.05 with Bonferroni correction are removed, and a fast-greedy community detection algorithm with 1000 bootstrapped replications identifies communities of responses preferentially selected together. This study applies MMA to the FMCE and compares results to Study 1's FCI analysis. (James Wells et al. (2020))

### Claims
- [MAMCR fails to replicate for large FCI samples: Infomap with LANS sparsification consistently identified only one large community of incorrect answers](../claims/mamcr-fails-large-fci-samples.md) [+M]
- [Modified Module Analysis identified 9 groups of incorrect FCI answers on the pretest and 11 on the post-test, in most cases mappable to common misconceptions](../claims/mma-identifies-incorrect-answer-groups.md) [+M]
- [Modified Module Analysis applied to the FMCE at a 20% node-retention threshold identifies incorrect-answer communities associated with only four misconceptions, consistent with previously identified item groups](../claims/mma-fmce-four-misconceptions-20-percent.md) [+M]

## Related Research Methods
-

## Key Sources
- James Wells, Rachel Henderson, John Stewart, Gay Stewart, Jie Yang, and Adrienne Traxler. (2019). Exploring the Structure of Misconceptions in the Force Concept Inventory with Modified Module Analysis. https://arxiv.org/abs/1905.06176
- James Wells, Rachel Henderson, Adrienne Traxler, Paul Miller, and John Stewart. (2020). Exploring the Structure of Misconceptions in the Force and Motion Conceptual Evaluation with Modified Module Analysis. https://arxiv.org/abs/2001.00967
