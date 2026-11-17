---
type: research-method
id: hierarchical-irt-hirt
title: Hierarchical IRT (HIRT)
description: "HIRT augments one-parameter IRT, in which the probability a student s answers item i correctly is f(θs−βi), with knowledge of item groups: \"Each item i is associated with a group j(i) whose diﬃculty is distributed normally around a per-group mean\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
---

# Hierarchical IRT (HIRT)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
HIRT augments one-parameter IRT, in which the probability a student s answers item i correctly is f(θs−βi), with knowledge of item groups: "Each item i is associated with a group j(i) whose diﬃculty is distributed normally around a per-group mean". Group means carry a hyperprior, expressing the belief that items in the same group (e.g., a shared template or skill) have similar difficulty. The article fits HIRT by MAP ascent of the modified log posterior and evaluates it on online response prediction, where it was the best-performing model overall.

## Accounts
<!-- How each source describes or uses the method -->
- **Hierarchical IRT: a Bayesian extension of one-parameter IRT that models item difficulty as grouped around per-group means**: HIRT augments one-parameter IRT, in which the probability a student s answers item i correctly is f(θs−βi), with knowledge of item groups: "Each item i is associated with a group j(i) whose diﬃculty is distributed normally around a per-group mean". Group means carry a hyperprior, expressing the belief that items in the same group (e.g., a shared template or skill) have similar difficulty. The article fits HIRT by MAP ascent of the modified log posterior and evaluates it on online response prediction, where it was the best-performing model overall. (Kevin H. Wilson et al. (2016))

### Claims
- [Hierarchical IRT, which exploits item grouping structure, was the best-performing model across the board except on one metric](../claims/hirt-best-performing-item-grouping.md) [+M]

## Related Research Methods
-

## Key Sources
- Kevin H. Wilson, Yan Karklin, Bojian Han, Chaitanya Ekanadham. (2016). Back to the basics: Bayesian extensions of IRT outperform neural networks for proficiency estimation. arXiv:1604.02336v2 [cs.AI]. https://arxiv.org/abs/1604.02336
