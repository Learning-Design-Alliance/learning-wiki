---
type: strategy
id: repeated-attempt-llm-evaluation-strategy
title: Evaluate LLMs for educational use with repeated-attempt consistency testing rather than single-attempt performance only
description: The article recommends evaluating LLM reliability through repeated administration of the same assessment.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
sources:
  - id: wang-shuo-2026
    resource: "https://doi.org/10.1186/s12909-026-08704-y"
    title: "Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao. (2026). Large language models in Chinese anesthesiology residency examinations: a comparative analysis of performance, reliability and clinical reasoning. BMC Medical Education. https://doi.org/10.1186/s12909-026-08704-y"
    author: Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao
---

# Evaluate LLMs for educational use with repeated-attempt consistency testing rather than single-attempt performance only

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 4 studies (2 design, 1 causal, 1 associational), `q2`–`q3` · 0 of 4 report an effect size · 4 claims rest on one study

## Description
The article recommends evaluating LLM reliability through repeated administration of the same assessment. The authors ran each of the 210 questions through each model 30 times, initiating "a new conversation window was initiated for every test instance" to limit carryover, and measured consistency as the proportion of questions answered correctly in all 30 attempts. They argue this repeated-measures design "revealed granular differences in LLM reliability" that single-attempt studies miss.

## Design Implications

### Context
#### Requirements
- A large number of repeated iterations (the article used 30, citing normality of distributions) and standardized question input formats with answer-format instructions
#### Constraints
- The authors note the short-interval repeated testing may have introduced a learning effect, and proprietary models prevented verifying whether server-side caching influenced outputs

### Target Learners
- education researchers and program administrators evaluating AI tools for residency training

### Target Learning Goals
- reliability assessment of AI educational tools before deployment

## Claims

- [LLM-based essay grading is not fully reproducible: repeated ChatGPT sessions on the same submissions show only moderate consistency (Krippendorff's alpha 0.625)](../claims/llm-grading-session-variability-limited-reproducibility.md) [+W]
- [Pooling Repeated LLM Grades Does Not Improve Agreement on Short Answers](../claims/pooling-repeated-llm-grades-does-not-improve-agreement.md) [~W]
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](../claims/within-judge-stability-llm-rubric.md) [+W]
- [Gemini 1.5 Pro shows the highest response consistency across 30 repeated exam attempts, significantly exceeding GPT-4o but statistically comparable to Claude](../claims/gemini-highest-response-consistency-repeated-attempts.md) [+W]

## Related Strategies

- [Evaluate LLM examination performance with a standardised simulation framework using repeated independent runs and Monte Carlo confidence intervals](standardised-llm-exam-simulation-framework-strategy.md)
- [Build infrastructure-level mechanisms to monitor, benchmark, and control LLM response behavior across model transitions in conversation-based assessment](infrastructure-mechanisms-for-llm-response-consistency.md)

## Examples
-

## Key Sources
- Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao. (2026). Large language models in Chinese anesthesiology residency examinations: a comparative analysis of performance, reliability and clinical reasoning. BMC Medical Education. https://doi.org/10.1186/s12909-026-08704-y
