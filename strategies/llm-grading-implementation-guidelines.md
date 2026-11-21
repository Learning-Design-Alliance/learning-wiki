---
type: strategy
id: llm-grading-implementation-guidelines
title: Implement LLM assignment grading with structured rubrics, TA-graded examples, dry-run validation, the largest feasible open-source model, and a manual-review option
description: "The authors distill their semester-long experience into recommendations 'for incorporating LLMs into assignment grading workflows': develop structured grading rubrics with explanation sections, include graded examples..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: pavlin-g-poliˇcar-2025
    resource: "https://arxiv.org/abs/2501.14499"
    title: "Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. https://arxiv.org/abs/2501.14499"
    author: Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan
---

# Implement LLM assignment grading with structured rubrics, TA-graded examples, dry-run validation, the largest feasible open-source model, and a manual-review option

> **Strategy** · [All strategies](index.md)
> **Evidence** · 7 claims (7 for) · 2 studies (1 causal, 1 design), `q2` · 0 of 2 report an effect size · 7 claims rest on one study

## Description
The authors distill their semester-long experience into recommendations 'for incorporating LLMs into assignment grading workflows': develop structured grading rubrics with explanation sections, include graded examples of student submissions, dry-run new rubrics on manually graded samples to catch systematic errors, select the largest open-source model the hardware supports (prioritizing larger quantized models over smaller full-precision ones), and always allow students to request manual review.

## Design Implications

### Context
#### Requirements
- Structured grading rubrics with explanation sections and graded examples of student submissions must be prepared before deployment
- A dry run on a sample of manually graded submissions should be conducted to identify systematic grading errors, with refinements validated on a new sample to avoid overfitting
- Students must retain the option to request manual review of LLM-assigned grades
#### Constraints
- LLMs still make occasional errors, which motivates the manual-review option
- In an LLM-only grading environment, students might be more inclined to exploit prompt-hacking vulnerabilities, so robust safeguards remain essential

### Target Learners
- master's-level computer science students in large university courses

### Target Learning Goals
- accurate scoring and timely, constructive written feedback on text-based assignment answers

## Claims

- [Prompt composition shifts LLM grading bias: rubric-only prompts yield stricter grading, examples-only prompts more lenient grading, and combining both produces the best results](../claims/rubric-examples-prompt-variant-balances-grading-bias.md) [+W]
- [LLM grading performance generally correlates with parameter count, and 4-bit quantization has negligible effect on grading performance](../claims/llm-grading-performance-scales-with-parameters.md) [+W]
- [Student attitudes toward LLM graders became more positive over the semester, and students strongly felt a manual-review option must remain available](../claims/student-attitudes-toward-llm-graders-improved-over-semester.md) [+W]
- [In a real classroom, all six evaluated LLMs except Llama-8B graded student text answers with classification accuracy between 85% and 90% against TA gold-standard grades](../claims/llm-graders-match-ta-grading-accuracy.md) [+W]
- [LLM grading bias relative to TAs varies with question difficulty: near-zero on trivial and easy questions, mildly stringent on medium, and more generous than TAs on hard questions](../claims/llm-grading-bias-varies-by-question-difficulty.md) [+W]
- [AI-assigned total scores on a handwritten chemistry exam align strongly with TA-assigned totals (R2 = 0.91), while per-problem agreement is lower (R2 = 0.61–0.85)](../claims/ai-total-scores-align-with-ta-grades-chemistry-exam.md) [+W]
- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](../claims/ai-grading-run-to-run-reliability-icc.md) [+W]

## Related Strategies

- [Grade long handwritten submissions page by page, asking the AI to identify where the credited evidence appears](page-by-page-evidence-location-ai-grading.md)

## Examples
-

## Key Sources
- Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. https://arxiv.org/abs/2501.14499
