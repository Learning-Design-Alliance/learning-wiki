---
type: strategy
id: llm-grading-programmatic-assessment-triage
title: Use LLM grading for programmatic assessment and triage, not for unreviewed student-facing feedback
description: The article recommends deploying the LLM pipeline as a class-wide programmatic tool rather than as an automated grader of individual student work.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: savage-2026
    resource: "https://arxiv.org/abs/2605.07036"
    title: "Savage, S., Bralin, A., Hur, P., & Rebello, N. S. (2026). Using Large Language Models to Analyze Engagement in Computational Thinking via Computational Physics Essays. https://arxiv.org/abs/2605.07036"
    author: "Savage, S., Bralin, A., Hur, P., & Rebello, N. S"
---

# Use LLM grading for programmatic assessment and triage, not for unreviewed student-facing feedback

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article recommends deploying the LLM pipeline as a class-wide programmatic tool rather than as an automated grader of individual student work. It states the pipeline "serves as a highly effective tool for programmatic assessment" and "can successfully triage superficial notebooks for targeted human review", providing instructors rapid baseline metrics on class-wide CT integration in large-enrollment courses. The authors explicitly caution against returning automated, unreviewed grades or formative feedback directly to students given the model's vulnerability in parsing subjective sensemaking contexts.

## Design Implications

### Context
#### Requirements
- Human review must remain in the loop for notebooks flagged or for subjective epistemic judgments
#### Constraints
- The model exhibits positive scoring bias in subjective categories and was calibrated on a localized dataset, so algorithmic bias across diverse populations must be investigated

### Target Learners
- instructors of large-enrollment introductory physics courses

### Target Learning Goals
- scalable programmatic assessment of computational thinking

## Claims

- [LLM agreement with human raters is lower for holistic CT quality scores (71% exact agreement, MAE 0.29) than for binary sub-practices](../claims/llm-71-percent-holistic-quality-agreement.md) [+W]
- [A multimodal LLM achieves 84% exact agreement with human consensus in detecting 20 binary computational-thinking sub-practices in student essays](../claims/llm-84-percent-agreement-ct-subpractices.md) [+W]
- [The LLM shows a severe positive bias on the subjective sub-practice Choosing Effective Computational Tools, mistaking tool mention for justification](../claims/llm-positive-bias-tool-justification.md) [+W]

## Related Strategies

- [Use automatic reflection classification for preliminary feedback and workload support, with final assessment retained by educators](automated-reflection-preliminary-feedback-educator-final.md)
- [Deploy the predictive model as a mid-semester triage tool with capacity-aligned thresholds, recalibration, non-punitive governance, and bias auditing](mid-semester-triage-deployment-strategy.md)
- [Deploy AI-assisted classroom observation as a complementary first-pass screening and reflection tool, with raters retaining interpretive judgment](ai-assisted-observation-complementary-screening-strategy.md)
- [Use LLM grading with an instructor's model answer and rubric for formative assessment of writing in large science classes](llm-formative-grading-model-answer-rubric.md)
- [Use ChatGPT as a teacher-supervised complementary tool for formative assessment of laboratory reports, not as an automated grader](teacher-supervised-chatgpt-formative-assessment-strategy.md)
- [Allocate human and AI effort by dimension type: automate explicit-criteria dimensions, retain human review for pedagogical judgment](human-ai-division-of-labor-mcq-generation.md)

## Examples
-

## Key Sources
- Savage, S., Bralin, A., Hur, P., & Rebello, N. S. (2026). Using Large Language Models to Analyze Engagement in Computational Thinking via Computational Physics Essays. https://arxiv.org/abs/2605.07036. [doi:10.48550/arxiv.2605.07036](https://doi.org/10.48550/arxiv.2605.07036)
