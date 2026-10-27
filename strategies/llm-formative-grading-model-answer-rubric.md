---
type: strategy
id: llm-formative-grading-model-answer-rubric
title: "Use LLM grading with an instructor's model answer and rubric for formative assessment of writing in large science classes"
description: "The article recommends deploying LLMs to grade student science writing at scale, supplying the instructor's model answer and rubric in the prompt, since this prompt condition produced the closest agreement with instru..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: chris-impey-2024
    resource: "https://doi.org/10.21203/rs.3.rs-3962175/v1"
    title: "Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer. (2024). Using Large Language Models for Automated Grading of Student Writing about Science. Preprint. https://doi.org/10.21203/rs.3.rs-3962175/v1"
    author: Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer
---

# Use LLM grading with an instructor's model answer and rubric for formative assessment of writing in large science classes

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article recommends deploying LLMs to grade student science writing at scale, supplying the instructor's model answer and rubric in the prompt, since this prompt condition produced the closest agreement with instructor grades. The authors plan this first for formative assessment in large General Education science classes, where "the grading burden of evaluating student writing is severe." Later, feedback could use the claim, evidence, reasoning framework.

## Design Implications

### Context
#### Requirements
- An instructor's model answer and rubric must be supplied in the prompt; a rubric alone gave poor results.
#### Constraints
- Performance is markedly worse for open-ended or speculative questions; the study is a pilot in MOOC settings with lifelong adult learners, and scaling to tens of thousands of learners remains untested.

### Target Learners
- Lifelong adult learners in MOOCs
- Undergraduates in large introductory science classes

### Target Learning Goals
- Scientific writing
- Formative assessment of science writing

## Claims

- [GPT-4 grading agrees best with the instructor when the prompt includes the instructor's model answer with a rubric, and worst with an AI-generated rubric alone](../claims/prompt-design-model-answer-plus-rubric-best.md) [+W]
- [Assignments at the first five levels of Bloom's taxonomy are suited to LLM grading, while Create-level assignments are more challenging for LLMs to assess](../claims/bloom-levels-limit-llm-grading-suitability.md) [+W]
- [For individual students, GPT-4 grades match instructor grades more closely than peer grades do, with smaller dispersion](../claims/gpt4-individual-student-grading-beats-peer-grading.md) [+W]
- [GPT-4 generally outperforms GPT-3.5 in matching instructor grades, with lower internal variance](../claims/gpt4-outperforms-gpt35-grading-instructor-agreement.md) [+W]
- [In three astronomy MOOCs, GPT-3.5 and GPT-4 grades are closer to instructor grades with lower dispersion than peer grades](../claims/llm-grading-closer-to-instructor-than-peer-grading.md) [+W]

## Related Strategies

- [Reserve LLM grading for short, well-structured tasks with explicit rubrics or exemplar answers, newer models, and stable API pipelines](reserve-llm-grading-for-structured-rubric-tasks.md)

## Examples
-

## Key Sources
- Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer. (2024). Using Large Language Models for Automated Grading of Student Writing about Science. Preprint. https://doi.org/10.21203/rs.3.rs-3962175/v1
