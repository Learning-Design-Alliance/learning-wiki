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
> **Evidence** · 4 claims (4 for) · 2 studies (2 design), `q2` · 1 of 2 report an effect size · 4 claims rest on one study

## Description
A Jupyter-Notebook pipeline calls OpenAI's GPT-4o API to grade students' written claim-evidence-reasoning responses to three EMCS questions, one question at a time. The prompt combines role prompting ("...experienced physics educator...") with chain-of-thought scoring ("Before assigning scores, think through the student’s response step by step"), outputs a .csv with claim, evidence/reasoning, and overall correctness flags, and generates emergent categories.

## Accounts
<!-- How each source describes or uses the method -->
- **GPT-4o grading-and-categorization pipeline for written physics explanations**: A Jupyter-Notebook pipeline calls OpenAI's GPT-4o API to grade students' written claim-evidence-reasoning responses to three EMCS questions, one question at a time. The prompt combines role prompting ("...experienced physics educator...") with chain-of-thought scoring ("Before assigning scores, think through the student’s response step by step"), outputs a .csv with claim, evidence/reasoning, and overall correctness flags, and generates emergent categories. (Sean Savage (2025))
- **Automatic LLM-based evaluation metric for bug descriptions using point-wise matching, precision, recall and F1**: The paper proposes "an automatic evaluation metric that leverages LLMs to assess generated bug descriptions in a structured manner". Learners' generated descriptions are produced point by point; an LLM judge determines whether each generated description and ground-truth description "refer to the same bug in logic", returning 1 or 0, and set-level Precision, Recall and F1 (B-Precision, B-Recall, B-F1) are computed over samples. The metric aims to reduce the burden of time-consuming manual evaluation and to assess descriptions at a fine-grained level. (Zhenlong Dai et al. (2026))

### Claims
- [GPT-4o grades students' written explanations on EMCS conceptual physics questions with accuracy comparable to a human grader (0-3% discrepancy, mean Cohen's kappa 0.77)](../claims/gpt4o-grades-written-physics-explanations-comparable-to-human-graders.md) [+M]
- [LLM-generated categories of incorrect explanations do not align with the multiple-choice distractors of the original EMCS questions](../claims/llm-incorrect-explanation-categories-differ-from-mc-distractors.md) [+M]
- [LLM-generated incorrect-explanation categories persisted across multiple API runs, indicating consistent grading performance](../claims/llm-categories-persist-across-runs.md) [+M]
- [The automatic bug-description evaluation metric agrees strongly with human evaluators](../claims/automatic-bug-description-metric-human-agreement.md) [+M]

## Related Research Methods
-

## Key Sources
- Sean Savage, N. Sanjay Rebello. (2025). Using an LLM to Investigate Students’ Explanations on Conceptual Physics Questions. https://arxiv.org/abs/2508.14823
- Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen. (2026). Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement. https://arxiv.org/abs/2601.08545
