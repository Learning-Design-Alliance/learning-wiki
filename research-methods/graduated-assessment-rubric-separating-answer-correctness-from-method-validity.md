---
type: research-method
id: graduated-assessment-rubric-separating-answer-correctness-from-method-validity
title: Graduated assessment rubric separating answer correctness from method validity
description: The rubric adapts the mathematical assessment distinction between the answer mark (correct output) and the method mark (valid reasoning) to automated diagnosis.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Graduated assessment rubric separating answer correctness from method validity

> **Research Method** · [All research methods](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 2 studies (2 causal), `q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The rubric adapts the mathematical assessment distinction between the answer mark (correct output) and the method mark (valid reasoning) to automated diagnosis. For correct-answer cases it distinguishes four categories: clear reasoning, needs clarification, misconception detected, and wrong answer. The paper argues a binary formulation "collapses Options 2 and 3, either falsely accusing students whose explanations are merely brief, or losing the routing signal that distinguishes unclear from flawed reasoning." It grounds the design in Black and Wiliam's formative assessment steps.

## Accounts
<!-- How each source describes or uses the method -->
- **Graduated assessment rubric separating answer correctness from method validity**: The rubric adapts the mathematical assessment distinction between the answer mark (correct output) and the method mark (valid reasoning) to automated diagnosis. For correct-answer cases it distinguishes four categories: clear reasoning, needs clarification, misconception detected, and wrong answer. The paper argues a binary formulation "collapses Options 2 and 3, either falsely accusing students whose explanations are merely brief, or losing the routing signal that distinguishes unclear from flawed reasoning." It grounds the design in Black and Wiliam's formative assessment steps. (Moiz Imran (2026))
- **Three-way KG-grounded diagnosis of student proof steps (optimal, valid-alternative, incorrect)**: The article's organizing evaluation framework classifies each student next step into three pedagogically distinct categories using a knowledge graph encoding all valid inference paths for each problem. The article states that "Unlike prior benchmarks relying on binary correctness, our KG encodes all valid inference paths, enabling three-way diagnosis." A step is Optimal if it follows an expert-authored path and strictly reduces distance to the conclusion, Valid-alternative if it is a valid inference that does not reduce distance, and Incorrect if it is not derivable under any valid rule. Edge-level annotation of rules and parent statements enables verification of both what was derived and how the derivation is justified. (Tahreem Yasir et al. (2026))

### Claims

- [Model performance is robust to minor prompt wording changes but sensitive to holistic rubric redesign](../claims/rubric-structure-part-of-assessment-construct.md) [+M]
- [Including a mark scheme in the prompt does not change misconception detection but significantly reduces false positives against correct-reasoning students](../claims/mark-scheme-reduces-false-positives.md) [+M]
- [LLM feedback agents classify optimal logic proof steps near-ceiling but perform poorly on valid-alternative and incorrect solutions](../claims/llm-tutors-near-ceiling-optimal-poor-valid-alternative-incorrect.md) [+M]
- [Model selection, not feedback condition, explains LLM diagnostic accuracy in three-way logic proof classification](../claims/model-selection-dominates-feedback-condition-diagnosis.md) [+M]
- [LLM feedback agents show model-specific over-rejection of valid-alternative reasoning and over-validation of incorrect solutions](../claims/llm-over-rejection-over-validation-patterns.md) [~W]

## Related Research Methods
-

## Key Sources
- Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143
- Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes. (2026). Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most. arXiv:2605.16207. https://arxiv.org/abs/2605.16207
