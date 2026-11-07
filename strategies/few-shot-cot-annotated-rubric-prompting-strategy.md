---
type: strategy
id: few-shot-cot-annotated-rubric-prompting-strategy
title: Use few-shot prompting with chain-of-thought and annotated rubric examples for LLM-based scoring of learner-generated clinical text
description: "The article identifies an effective prompting technique for LLM-based scoring that included \"an LLM role description, the scoring rubric, the VP case context, scoring examples with corresponding cases, step-by-step ra..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-03
sources:
  - id: stadler-p-2026
    resource: "https://doi.org/10.2196/94666"
    title: "Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J. (2026). Test-Retest Reliability of Large Language Models and Their Concordance With Human Experts in Rubric-Based Scoring of Clinical Summary Statements: Experimental Comparative Study. JMIR Medical Education. https://doi.org/10.2196/94666"
    author: Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J
---

# Use few-shot prompting with chain-of-thought and annotated rubric examples for LLM-based scoring of learner-generated clinical text

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article identifies an effective prompting technique for LLM-based scoring that included "an LLM role description, the scoring rubric, the VP case context, scoring examples with corresponding cases, step-by-step rationales for those examples, an explicit CoT initiator, and a placeholder for the learner's summary statement." This strategy achieved the highest overall accuracy across all tested models. The authors recommend that future studies systematically examine which elements are essential and how many examples are optimal.

## Design Implications

### Context
#### Requirements
- Manually picked summary statements annotated with human expert ratings to serve as scoring examples
#### Constraints
- Prompt refinement may be necessary when transferring the approach to new contexts

### Target Learners
- medical students

### Target Learning Goals
- clinical reasoning
- formative feedback

## Claims

- [Few-shot with chain-of-thought prompting achieves the best concordance with human expert ratings for all tested LLMs](../claims/few-shot-cot-best-concordance-human-experts.md) [+W]
- [Large closed-weights LLMs show high test-retest reliability when scoring clinical summary statements across repeated runs](../claims/llm-high-test-retest-reliability-summary-statement-scoring.md) [+W]

## Related Strategies

- [Translate deductive coding rubrics into structured zero-shot prompts to compare LLM coding against human coding](zero-shot-prompt-codebook-translation-strategy.md)
- [Guide student instruction with chain-of-thought decomposition, few-shot worked examples, and self-consistency over multiple LLM queries](cot-fewshot-selfconsistency-student-guidance.md)
- [Use a simulated multiagent prompt combining role, instruction-based, chain, and few-shot prompting to generate OSCE stations with an LLM](simulated-multiagent-prompting-for-osce-generation.md)
- [Improve LLM performance on TCM examinations by incorporating TCM texts into training, developing specialized TCM LLMs, and using chain-of-thought prompting](specialized-tcm-llm-training-and-chain-of-thought-strategy.md)

## Examples
-

## Key Sources
- Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J. (2026). Test-Retest Reliability of Large Language Models and Their Concordance With Human Experts in Rubric-Based Scoring of Clinical Summary Statements: Experimental Comparative Study. JMIR Medical Education. https://doi.org/10.2196/94666
