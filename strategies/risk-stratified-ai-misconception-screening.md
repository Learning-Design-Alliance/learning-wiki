---
type: strategy
id: risk-stratified-ai-misconception-screening
title: "Deploy AI misconception screening in a risk-stratified way: revise vulnerable question values at authoring time, pair AI screening with mark-scheme-style reference reasoning, and use follow-up probing questions rather than binary classification"
description: "The paper's implications-for-practice section recommends \"risk-stratified deployment rather than uniform automation\"."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: moiz-imran-and-sahan-bulathwela-2026
    resource: "https://arxiv.org/abs/2605.23925"
    title: "Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925"
    author: Moiz Imran and Sahan Bulathwela
---

# Deploy AI misconception screening in a risk-stratified way: revise vulnerable question values at authoring time, pair AI screening with mark-scheme-style reference reasoning, and use follow-up probing questions rather than binary classification

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The paper's implications-for-practice section recommends "risk-stratified deployment rather than uniform automation". Question authors should check at design time whether known errors yield the correct answer for chosen values and revise the values if so. Because even the best model produces roughly 4.3 false alarms per genuine detection, the authors suggest follow-up questions probing understanding and note that "providing mark-scheme-style reference reasoning to frontier models can improve TM detection", pairing AI screening with structured references for safer deployment.

## Design Implications

### Context
#### Requirements
- Frontier-model access for screening, since locally runnable fine-tuned models under-detect TM cases
- Structured reference reasoning or follow-up probing questions to control false alarms
#### Constraints
- Fully automated stand-alone screening is not viable on its own at natural TM prevalence; in unstructured classroom settings with lower TM prevalence the false alarm problem would be worse

### Target Learners
- school mathematics students whose responses are screened by AI tutors

### Target Learning Goals
- reliable detection of misconceptions hidden behind correct answers

### Affordances
- Correct Answer Trap Coincidental Correctness

## Related Strategies
- 

## Examples
-

## Key Sources
- Moiz Imran and Sahan Bulathwela. (2026). Catching TheCorrectAnswerTrap: Characterising AI Tutor Blind Spots When Analysing Student Reasoning. arXiv preprint. https://arxiv.org/abs/2605.23925
