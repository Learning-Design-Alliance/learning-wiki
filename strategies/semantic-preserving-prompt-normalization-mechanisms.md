---
type: strategy
id: semantic-preserving-prompt-normalization-mechanisms
title: Normalize prompts via domain-consistent terminology substitution and clinical narrative restructuring that add no new information
description: Qualitative analysis of PET rewrites identifies two concrete normalization mechanisms.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: lier-jin-2026
    resource: "https://arxiv.org/abs/2608.08942"
    title: "Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942"
    author: Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin
---

# Normalize prompts via domain-consistent terminology substitution and clinical narrative restructuring that add no new information

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Qualitative analysis of PET rewrites identifies two concrete normalization mechanisms. First, domain-consistent terminology: an informal phrase like 3 HIV medicines is rewritten as three-drug antiretroviral regimen, improving linguistic precision without introducing new medical information. Second, clinical information restructuring: a long unstructured narrative is reorganized into semantically equivalent sections. Overall, these examples suggest that PET improves accessibility primarily by enhancing the presentation of existing information rather than altering its content.

## Design Implications

### Context
#### Requirements
- Rewrites must preserve the original meaning and may not modify or introduce clinical facts; only presentation and organization of existing information change.
#### Constraints
- Mechanisms are illustrated with two representative medical question-answering examples rather than tested as separate experimental conditions.

### Target Learners
- users who describe clinical concerns in informal everyday language
- users submitting long, unstructured narratives to AI systems

### Target Learning Goals
- expressing the same clinical question in terminology consistent with clinical literature and LLM training data
- making diagnostically relevant evidence more salient to the language model

### Affordances
- Prompt Privilege Prompt Equity Framework

## Claims

- [After PET normalization, no statistically significant performance differences remain between user cohorts](../claims/pet-eliminates-significant-accessibility-disparities.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942
