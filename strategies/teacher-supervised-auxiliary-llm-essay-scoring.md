---
type: strategy
id: teacher-supervised-auxiliary-llm-essay-scoring
title: Use reward-aligned LLM scoring as a teacher-supervised auxiliary tool for preliminary essay scoring at scale
description: "The article positions RACES as \"an auxiliary scoring framework rather than a replacement for human raters\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
sources:
  - id: zhenxin-zhang-2026
    resource: "https://doi.org/10.1186/s41239-026-00607-8"
    title: "Zhenxin Zhang, Ziyu Ding, Mengyun Liu and Haiwei Sang. (2026). RACES: reward-aligned consistent essay scoring with large language models. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00607-8"
    author: Zhenxin Zhang, Ziyu Ding, Mengyun Liu and Haiwei Sang
---

# Use reward-aligned LLM scoring as a teacher-supervised auxiliary tool for preliminary essay scoring at scale

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article positions RACES as "an auxiliary scoring framework rather than a replacement for human raters". Its practical value is improving the stability of preliminary essay scoring in large-scale writing assessment, helping instructors identify borderline or potentially inconsistent cases for further review. Use in realistic higher-education settings "should remain teacher-supervised", with validation still needed for fairness, robustness to prompt injection, interpretability, and subgroup-level consistency.

## Design Implications

### Context
#### Requirements
- Teacher oversight in deployment; additional validation of fairness across writing styles and learner groups before real-world use
#### Constraints
- Before real-world deployment, validation is still required regarding fairness, adversarial robustness, interpretability, subgroup-level consistency, and teacher oversight

### Target Learners
- higher-education instructors grading large volumes of student essays

### Target Learning Goals
- reducing grading workload while maintaining reliable large-scale writing evaluation

### Affordances
- [Races Framework Reward Aligned Essay Scoring](../research-methods/races-reward-aligned-consistent-essay-scoring-framework.md)

## Related Strategies

- [Deploy AI-assisted classroom observation as a complementary first-pass screening and reflection tool, with raters retaining interpretive judgment](ai-assisted-observation-complementary-screening-strategy.md)
- [Use automatic reflection classification for preliminary feedback and workload support, with final assessment retained by educators](automated-reflection-preliminary-feedback-educator-final.md)
- [Use LLM persona simulation only for preliminary experimentation, stress testing, and hypothesis generation, with separate validation for consequential applications](persona-simulation-preliminary-use-only.md)
- [Use current LLMs in the notary domain only as supervised support tools in preliminary drafting or educational contexts](supervised-llm-support-preliminary-legal-drafting.md)
- [Implement AI in assessment as a hybrid support tool for low-stakes, formative stages while humans retain final grading authority](hybrid-ai-human-assessment-implementation.md)

## Examples
-

## Key Sources
- Zhenxin Zhang, Ziyu Ding, Mengyun Liu and Haiwei Sang. (2026). RACES: reward-aligned consistent essay scoring with large language models. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00607-8
