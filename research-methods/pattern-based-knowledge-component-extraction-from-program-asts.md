---
type: research-method
id: pattern-based-knowledge-component-extraction-from-program-asts
title: Pattern-based knowledge component extraction from program ASTs
description: "The framework defines knowledge components as \"recurring, semantically meaningful structural patterns based on important subtrees from program Abstract Syntax Trees (ASTs)\"."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Pattern-based knowledge component extraction from program ASTs

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The framework defines knowledge components as "recurring, semantically meaningful structural patterns based on important subtrees from program Abstract Syntax Trees (ASTs)". Discovery proceeds in four steps: SANN-guided subtree extraction trained on topic labels, normalization that anonymizes identifiers and canonicalizes syntactic alternatives, context-aware encoding of normalized subtree sequences with a β-VAE, and K-means clustering of latent vectors into KCs. Activities are then mapped to IDF-weighted knowledge vectors and compared by cosine similarity, yielding finer-grained, implementation-level signals such as guarded loop traversals and accumulator updates.

## Accounts
<!-- How each source describes or uses the method -->
- **Pattern-based knowledge component framework for representing programming learning activities**: The framework defines knowledge components as "recurring, semantically meaningful structural patterns based on important subtrees from program Abstract Syntax Trees (ASTs)". Discovery proceeds in four steps: SANN-guided subtree extraction trained on topic labels, normalization that anonymizes identifiers and canonicalizes syntactic alternatives, context-aware encoding of normalized subtree sequences with a β-VAE, and K-means clustering of latent vectors into KCs. Activities are then mapped to IDF-weighted knowledge vectors and compared by cosine similarity, yielding finer-grained, implementation-level signals such as guarded loop traversals and accumulator updates. (Muntasir Hoq et al. (2026))

### Claims
- [Pattern-based KC similarity retrieves bundle-aligned programming learning items better than code-embedding and other KC baselines in both retrieval directions](../claims/pattern-kc-retrieval-outperforms-baselines.md) [+M]

## Related Research Methods
-

## Key Sources
- Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram. (2026). Automated Recommendation of Programming Learning Content Using Pattern-based Knowledge Components. CSEDM'26: 10th Educational Data Mining in Computer Science Education Workshop. https://educationaldatamining.org
