---
type: strategy
id: intra-rater-kappa-repeated-llm-runs-strategy
title: Measure LLM grading reliability via intra-rater Kappa across repeated runs
description: "The article operationalises LLM evaluation quality by comparing evaluations between two independent runs of the LLM with the same prompt and data, using weighted Cohen's Kappa (with linear weights) as an intra-rater r..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: mrityunjay-kumar-2025
    resource: "https://arxiv.org/abs/2510.06997"
    title: "Mrityunjay Kumar. (2025). The Limits of Goal-Setting Theory in LLM-Driven Assessment. arXiv. https://arxiv.org/abs/2510.06997"
    author: Mrityunjay Kumar
---

# Measure LLM grading reliability via intra-rater Kappa across repeated runs

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 4 studies (3 causal, 1 design), `q2` · 0 of 4 report an effect size · 5 claims rest on one study

## Description
The article operationalises LLM evaluation quality by comparing evaluations between two independent runs of the LLM with the same prompt and data, using weighted Cohen's Kappa (with linear weights) as an intra-rater reliability metric. Mean Kappa represents performance and SD Kappa represents performance variance. Practitioners can adopt this method: run the same evaluation prompt multiple times, compute pairwise weighted Kappa across run pairs, and inspect both the mean and spread.

## Design Implications

### Context
#### Requirements
- Multiple independent evaluation runs per prompt type (six in the study, yielding 15 pairwise comparisons per type)
#### Constraints
- Kappa here measures run-to-run agreement, not agreement with a human rater

### Target Learners
- Instructors and researchers evaluating LLM grading reliability

### Target Learning Goals
- Assessing consistency and stability of AI-driven assessment

## Claims

- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](../claims/ai-grading-run-to-run-reliability-icc.md) [+W]
- [ChatGPT's grading consistency does not improve with increased prompt specificity in essay evaluation](../claims/chatgpt-grading-consistency-not-improved-by-prompt-specificity.md) [+W]
- [Prompt specificity does not reduce ChatGPT's performance variance in essay evaluation](../claims/prompt-specificity-does-not-reduce-chatgpt-variance.md) [+W]
- [Pooling Repeated LLM Grades Does Not Improve Agreement on Short Answers](../claims/pooling-repeated-llm-grades-does-not-improve-agreement.md) [+W]
- [Mistral 7B shows high ICCs but low Fleiss kappa when scoring summary statements](../claims/mistral-7b-high-icc-low-fleiss-kappa.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Mrityunjay Kumar. (2025). The Limits of Goal-Setting Theory in LLM-Driven Assessment. arXiv. https://arxiv.org/abs/2510.06997
