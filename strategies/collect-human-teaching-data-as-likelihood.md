---
type: strategy
id: collect-human-teaching-data-as-likelihood
title: Promote a non-pedagogical learner into a pedagogical one by collecting human teaching data and using a computational model of it as the likelihood
description: "The article's design recommendation for pedagogical machine learning: \"one can collect data on how human teachers generate examples for a domain and use a computational model of this process as the likelihood in Bayes..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: long-ouyang-2017
    resource: "https://arxiv.org/abs/1711.09401"
    title: "Long Ouyang, Michael C. Frank (2017). Pedagogical learning. 31st Conference on Neural Information Processing Systems (NIPS 2017). https://arxiv.org/abs/1711.09401"
    author: Long Ouyang, Michael C. Frank
---

# Promote a non-pedagogical learner into a pedagogical one by collecting human teaching data and using a computational model of it as the likelihood

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
The article's design recommendation for pedagogical machine learning: "one can collect data on how human teachers generate examples for a domain and use a computational model of this process as the likelihood in Bayesian inference", thereby promoting a non-pedagogical learner into a pedagogical one that can mine the signal in helpful examples.

## Design Implications

### Context
#### Requirements
- Behavioral data on how human teachers generate examples for the target domain
- An existing non-pedagogical Bayesian learner whose likelihood can be replaced by the teaching model
#### Constraints
- Pedagogical learning is computationally challenging because the teaching model must repeatedly call the non-pedagogical learner as a subroutine
- Errors in teaching examples might be particularly damaging when learners expect teachers to be helpful
- The near miss and minimal pair teaching patterns might not be possible for regression problems

### Target Learners
- adult learners inferring rule-based concepts from labeled examples

### Target Learning Goals
- inferring complex concepts from a few well-chosen examples

### Affordances
- Pedagogical Learning Bayesian Recursion

## Claims

- [Human learners can infer complex rules from teachers' example corpora, which were verified as helpful evidence](../claims/human-learners-guess-regex-from-corpora.md) [+W]
- [Teachers of regular expressions produce minimal-pair clustering structure, editing positive examples into near-boundary negative examples](../claims/minimal-pair-clustering-regex-teaching.md) [+W]
- [In a synthetic comparison, the pedagogical learner L1 generally outperforms the non-pedagogical learner L0 on human teaching data, though they are on par in some parameter regimes](../claims/pedagogical-learner-outperforms-non-pedagogical.md) [+W]
- [Polarity balance of teacher corpora varies by rule: more negatives for zip-code, more positives for suffix-s](../claims/polarity-balance-varies-by-rule.md) [+W]
- [Unconstrained teacher corpora ranged from 1 to 13 examples with a low but nonzero labeling error rate of 6.6%](../claims/teaching-corpus-size-and-error-rate.md) [+W]
- [Teacher corpora have internal temporal structure: the first example in a cluster tends to be positive and clusters occur in contiguous spans](../claims/temporal-cluster-structure-teaching-corpora.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Long Ouyang, Michael C. Frank (2017). Pedagogical learning. 31st Conference on Neural Information Processing Systems (NIPS 2017). https://arxiv.org/abs/1711.09401
