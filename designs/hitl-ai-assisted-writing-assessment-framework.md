---
type: design
id: hitl-ai-assisted-writing-assessment-framework
title: Human-in-the-Loop AI-assisted evaluation framework for high-stakes writing assessment
description: A decision-oriented operational framework integrating LLM-based scoring of the Writing section into a national exam workflow while keeping humans in charge of outcome-determining decisions.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: curi-2026
    resource: "https://arxiv.org/abs/2609.05143"
    title: "Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A. (2026). A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment. arXiv. https://arxiv.org/abs/2609.05143"
    author: Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A
---

# Human-in-the-Loop AI-assisted evaluation framework for high-stakes writing assessment

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A decision-oriented operational framework integrating LLM-based scoring of the Writing section into a national exam workflow while keeping humans in charge of outcome-determining decisions. Its central principle is "ensuring that no final decision affecting test outcomes is made without appropriate human oversight." The workflow (Fig. 8) runs a calibration phase (50–100 texts) to validate the AI model and adapt prompts, scores all responses automatically, applies IRT and Bookmark cut scores, reviews candidates whose pass/fail outcome depends on the Writing section, and recalibrates cut scores after review. Other test sections remain scored by current operational procedures.

## Design Implications

### Context
#### Requirements
- A calibration phase (50–100 texts) to validate the AI model and adapt prompts to the current test topic; IRT and Bookmark cut-score procedures to assign proficiency levels before routing decisions.
#### Constraints
- The study was conducted under offline experimental conditions, and operational deployment may surface additional challenges related to monitoring, drift, and edge cases; the workload reduction varies across editions depending on candidate performance in other test sections.

### Target Learners
- Over-age adults (21+) seeking lower secondary education certification in Uruguay's national Acredita EB assessment

### Learning Goals
- Reliable, fair rubric-based scoring of Spanish argumentative writing for high-stakes pass/fail certification decisions

### Claims
- [Ai Scoring Systematic Under Grading Bias Pass Fail](../claims/ai-scoring-systematic-under-grading-bias-pass-fail.md) [+M]
- [Hitl Workflow Reduces Human Scoring Workload 50 Percent](../claims/hitl-workflow-reduces-human-scoring-workload-50-percent.md) [+W]

## Related Designs

- [Report Assessment & Feedback (RAF) procedure with human-in-the-loop approval of all feedback reports](raf-procedure-human-in-the-loop.md)

## Examples
-

## Key Sources
- Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A. (2026). A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment. arXiv. https://arxiv.org/abs/2609.05143. [doi:10.48550/arxiv.2609.05143](https://doi.org/10.48550/arxiv.2609.05143)
