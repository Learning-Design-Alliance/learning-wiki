---
type: strategy
id: llm-written-explanation-assessment-at-scale-strategy
title: "Use appropriately prompted LLMs to assess students' written explanations at scale in large-enrollment courses"
description: Supplement multiple-choice assessment in large courses by having students write claim-evidence-reasoning explanations and grading them with an appropriately prompted LLM.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: sean-savage-2025
    resource: "https://arxiv.org/abs/2508.14823"
    title: "Sean Savage, N. Sanjay Rebello. (2025). Using an LLM to Investigate Students’ Explanations on Conceptual Physics Questions. https://arxiv.org/abs/2508.14823"
    author: Sean Savage, N. Sanjay Rebello
---

# Use appropriately prompted LLMs to assess students' written explanations at scale in large-enrollment courses

> **Strategy** · [All strategies](index.md)
> **Evidence** · 7 claims (3 for, 4 mixed) · 3 studies (1 causal, 1 review, 1 design), `q1`–`q2` · 0 of 3 report an effect size · 7 claims rest on one study

## Description
Supplement multiple-choice assessment in large courses by having students write claim-evidence-reasoning explanations and grading them with an appropriately prompted LLM. The article states LLM assessment "can potentially facilitate educators to uncover areas of weakness in students’ understanding" and that LLMs identify reasoning resources absent from MC options. Implementation follows the article's pipeline: role prompting, chain-of-thought scoring, emergent categorization, and validation against a human-graded sample.

## Design Implications

### Context
#### Requirements
- Students must be able to produce written claim-evidence-reasoning responses, which the article says students were prepared for through recitation instruction in the framework
- A human-graded validation sample to gauge the LLM's accuracy against human grading
#### Constraints
- Validated only on three of 25 EMCS questions due to concern for student fatigue
- The LLM was less likely to mark a student as completely correct than the human grader

### Target Learners
- first-semester calculus-based physics undergraduates in large-enrollment courses (N > 1,000)

### Target Learning Goals
- assessing conceptual understanding of energy and momentum, including students' written explanations and conceptual resources

## Claims

- [Students can reach the correct claim via incorrect explanations, so MC scoring alone masks unproductive conceptual resources](../claims/correct-claim-incorrect-explanation-masked-by-mc.md) [+M]
- [GPT-4o grades students' written explanations on EMCS conceptual physics questions with accuracy comparable to a human grader (0-3% discrepancy, mean Cohen's kappa 0.77)](../claims/gpt4o-grades-written-physics-explanations-comparable-to-human-graders.md) [+M]
- [LLM-generated incorrect-explanation categories persisted across multiple API runs, indicating consistent grading performance](../claims/llm-categories-persist-across-runs.md) [+M]
- [LLM-generated categories of incorrect explanations do not align with the multiple-choice distractors of the original EMCS questions](../claims/llm-incorrect-explanation-categories-differ-from-mc-distractors.md) [~M]
- [The LLM was less likely than the human grader to mark a student as completely correct](../claims/llm-less-likely-to-mark-completely-correct.md) [~M]
- [Phase VI AI-enabled systems face six documented challenges: explainability, hallucination risk, prompt sensitivity, computational cost, validation complexity, and limited large-scale evidence](../claims/phase-vi-ai-systems-six-challenges.md) [~W]
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](../claims/llm-competency-error-patterns-four-types.md) [~M]

## Related Strategies

- [Ask students to explain why wrong multiple-choice answers are wrong and why they chose their answer, then have an AI bot analyze the explanations](ai-analyzed-explanation-strategy.md)
- [Use LLM grading with an instructor's model answer and rubric for formative assessment of writing in large science classes](llm-formative-grading-model-answer-rubric.md)
- [Design CT rubrics and prompts to explicitly operationalize integrated constructs and demand parameter-interaction reasoning](explicit-rubrics-for-integrated-ct-constructs.md)
- [Improve LLM grading alignment through LLM-optimized guidelines, calibration examples, and median-of-parallels grading](llm-grading-alignment-optimization-strategies.md)

## Examples
-

## Key Sources
- Sean Savage, N. Sanjay Rebello. (2025). Using an LLM to Investigate Students’ Explanations on Conceptual Physics Questions. https://arxiv.org/abs/2508.14823
