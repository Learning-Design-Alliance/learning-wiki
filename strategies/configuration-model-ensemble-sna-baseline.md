---
type: strategy
id: configuration-model-ensemble-sna-baseline
title: Use configuration-model ensembles to statistically contextualize whole-network SNA metrics
description: Because standard hypothesis tests assume independence that social network data violate, the article generates ensembles of random networks matched to the reference network and compares metric values against them.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: emily-bolger-2024
    resource: "https://arxiv.org/abs/2407.00193"
    title: "Emily Bolger, Marius Nwobi, and Marcos D. Caballero. (2024). Characterizing Faculty Online Learning Community Interactions Using Social Network Analysis. https://arxiv.org/abs/2407.00193"
    author: Emily Bolger, Marius Nwobi, and Marcos D. Caballero
---

# Use configuration-model ensembles to statistically contextualize whole-network SNA metrics

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Because standard hypothesis tests assume independence that social network data violate, the article generates ensembles of random networks matched to the reference network and compares metric values against them. The authors "implement the Configuration Model," which "preserves the strength distribution of the reference network as our distribution to generate random networks," then compute the proportion of ensemble networks with a lower metric value; extreme proportions indicate the observed value differs from chance.

## Design Implications

### Context
#### Requirements
- An ensemble generation method that preserves the reference network's strength distribution, with enough generated networks to balance computation time and statistical accuracy
#### Constraints
- The choice of network generation method can lead to false conclusions, especially with smaller amounts of data

### Target Learners
- Researchers and community leaders evaluating faculty online learning communities

### Target Learning Goals
- Evaluating whether community communication patterns meet community goals

## Claims

- [Weighted reciprocity is low in PICUP Slack channel networks despite exceeding comparable random networks](../claims/picup-slack-low-weighted-reciprocity.md) [+W]

## Related Strategies

- [Future SNA e-learning studies should include a quantitative approach exploiting the statistical power of SNA to explain complex systems](sna-elearning-future-quantitative-approach.md)
- [Advance the use of structural-configurational methods such as SNA and ENA toward empirically testable models](structural-configurational-methods-toward-testable-models.md)

## Examples
-

## Key Sources
- Emily Bolger, Marius Nwobi, and Marcos D. Caballero. (2024). Characterizing Faculty Online Learning Community Interactions Using Social Network Analysis. https://arxiv.org/abs/2407.00193
