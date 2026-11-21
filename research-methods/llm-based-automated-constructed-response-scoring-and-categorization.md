---
type: research-method
id: llm-based-automated-constructed-response-scoring-and-categorization
title: LLM-based automated constructed-response scoring and categorization
description: "A Jupyter-Notebook pipeline calls OpenAI's GPT-4o API to grade students' written claim-evidence-reasoning responses to three EMCS questions, one question at a time."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# LLM-based automated constructed-response scoring and categorization

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
A Jupyter-Notebook pipeline calls OpenAI's GPT-4o API to grade students' written claim-evidence-reasoning responses to three EMCS questions, one question at a time. The prompt combines role prompting ("...experienced physics educator...") with chain-of-thought scoring ("Before assigning scores, think through the student’s response step by step"), outputs a .csv with claim, evidence/reasoning, and overall correctness flags, and generates emergent categories.

## Accounts
<!-- How each source describes or uses the method -->
- **GPT-4o grading-and-categorization pipeline for written physics explanations**: A Jupyter-Notebook pipeline calls OpenAI's GPT-4o API to grade students' written claim-evidence-reasoning responses to three EMCS questions, one question at a time. The prompt combines role prompting ("...experienced physics educator...") with chain-of-thought scoring ("Before assigning scores, think through the student’s response step by step"), outputs a .csv with claim, evidence/reasoning, and overall correctness flags, and generates emergent categories. (Sean Savage (2025))

### Claims
- [GPT-4o grades students' written explanations on EMCS conceptual physics questions with accuracy comparable to a human grader (0-3% discrepancy, mean Cohen's kappa 0.77)](../claims/gpt4o-grades-written-physics-explanations-comparable-to-human-graders.md) [+M]
- [LLM-generated categories of incorrect explanations do not align with the multiple-choice distractors of the original EMCS questions](../claims/llm-incorrect-explanation-categories-differ-from-mc-distractors.md) [+M]
- [LLM-generated incorrect-explanation categories persisted across multiple API runs, indicating consistent grading performance](../claims/llm-categories-persist-across-runs.md) [+M]

## Related Research Methods
-

## Key Sources
- Sean Savage, N. Sanjay Rebello. (2025). Using an LLM to Investigate Students’ Explanations on Conceptual Physics Questions. https://arxiv.org/abs/2508.14823
