---
type: strategy
id: embedding-based-scalable-feedback-and-scaffolding
title: Use error-pattern embeddings to deliver targeted feedback, practice recommendations, and worked examples at scale
description: "The article's design implications describe using the framework's latent vectors to compare submissions and identify similar errors while ignoring superficial differences."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: muntasir-hoq-2025
    resource: "https://arxiv.org/abs/2505.10913"
    title: "Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram. (2025). Automated Identification of Logical Errors in Programs: Advancing Scalable Analysis of Student Misconceptions. arXiv preprint. https://arxiv.org/abs/2505.10913"
    author: Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram
---

# Use error-pattern embeddings to deliver targeted feedback, practice recommendations, and worked examples at scale

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article's design implications describe using the framework's latent vectors to compare submissions and identify similar errors while ignoring superficial differences. This can enable instructors to 'provide targeted feedback at scale' by designing feedback for representative solutions, and to support personalized learning by 'recommending targeted practice problems and instructional materials based on students' errors', including worked examples for novice programmers and dynamic adjustment of learning pathways and problem difficulty.

## Design Implications

### Context
#### Requirements
- A trained SANN embedding model and a repository of similar problems linked to incorrect submissions
#### Constraints
- Evaluated on short Java CS1 programs; uncompilable submissions were excluded, so the scaffolding applies only to compilable code

### Target Learners
- CS1 (introductory programming) university students

### Target Learning Goals
- Remediating logical errors and misconceptions through targeted feedback and practice recommendations

## Claims

- [SANN code vectors outperform explainable baseline code2vec in logical error identification](../claims/sann-beats-code2vec-error-identification.md) [+W]
- [Expert evaluation shows high recall and precision for SANN-identified logical errors across five problems](../claims/sann-high-recall-precision-logical-errors.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram. (2025). Automated Identification of Logical Errors in Programs: Advancing Scalable Analysis of Student Misconceptions. arXiv preprint. https://arxiv.org/abs/2505.10913
