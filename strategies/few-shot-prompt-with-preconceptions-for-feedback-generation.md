---
type: strategy
id: few-shot-prompt-with-preconceptions-for-feedback-generation
title: Design GPT feedback prompts with few-shot examples covering each response category and documented student preconceptions as context
description: "The article's prompt-engineering recipe combines few-shot prompting with physics education research knowledge."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: tong-wan-and-zhongzhou-chen-2023
    resource: "https://arxiv.org/abs/2311.06180"
    title: "Tong Wan and Zhongzhou Chen. (2023). Exploring Generative AI assisted feedback writing for students' written responses to a physics conceptual question with prompt engineering and few-shot learning. https://arxiv.org/abs/2311.06180"
    author: Tong Wan and Zhongzhou Chen
---

# Design GPT feedback prompts with few-shot examples covering each response category and documented student preconceptions as context

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 3 studies (2 design, 1 causal), `q2` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
The article's prompt-engineering recipe combines few-shot prompting with physics education research knowledge. After initial GPT outputs "had some obvious mistakes that resemble some of the common preconceptions identified in the PER literature," the authors added those preconceptions to the prompt context and provided one response-feedback example pair from each manually categorized response type. The prompt also includes the problem, an expert response, numbered physics principles, and feedback instructions.

## Design Implications

### Context
#### Requirements
- Manually categorize student responses and write human feedback for a small set of examples, one per category, to include in the prompt
- Include documented common preconceptions from the discipline's research literature as contextual information in the prompt
#### Constraints
- The manual categorization process is described as very time consuming and impractical if LLMs are to be used as a grading assistant at scale
- LLM output is probabilistic, so hallucinations cannot be completely eradicated

### Target Learners
- introductory physics students in large-enrollment courses

### Target Learning Goals
- improving conceptual understanding and reasoning through feedback on free-response conceptual questions

## Claims

- [Instructors rated approximately 70% of GPT-generated feedback statements as needing only minor or no modification, with an average rating of 2.06 on a 0-3 scale](../claims/instructors-rate-70-percent-gpt-feedback-minor-editing.md) [+W]
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons](../claims/in-context-examples-improve-bloom-classification.md) [+W]
- [Prompting with category information or few-shot examples yields limited improvement in distribution alignment, with zero-shot closest for most models](../claims/prompting-strategies-limited-alignment-gain.md) [~W]

## Related Strategies

- [Instructors should review and edit all AI-generated feedback before sending it to students](human-in-the-loop-review-of-ai-feedback.md)
- [Development strategies targeting AI virtual patient limitations: expert-reviewed content, iterative prompt engineering, behavioral rules, few-shot prompting, and conversational memory](ai-virtual-patient-mitigation-strategies.md)
- [Use iterative prompt engineering mirroring human coders' labeling processes to refine LLM classification prompts](iterative-prompt-engineering-mirroring-human-coder-refinement.md)
- [Rule-constrained GPT-4 prompt for interest-based problem contextualization](rule-constrained-gpt4-contextualization-prompt.md)
- [Use a simulated multiagent prompt combining role, instruction-based, chain, and few-shot prompting to generate OSCE stations with an LLM](simulated-multiagent-prompting-for-osce-generation.md)
- [Improve LLM feedback quality via JSON-schema prompts with hidden scoring keys and preprocessing code into structured dictionaries](llm-prompt-schema-and-preprocessing-strategy.md)
- [Craft educational LLM prompts using iterative refinement, role-playing, and constraints with suitable context](three-pillar-educational-prompting-strategy.md)
- [Constrain LLM feedback prompts to physics content with a rubric and ideal-answer example](llm-feedback-prompt-constraints-strategy.md)

## Examples
-

## Key Sources
- Tong Wan and Zhongzhou Chen. (2023). Exploring Generative AI assisted feedback writing for students' written responses to a physics conceptual question with prompt engineering and few-shot learning. https://arxiv.org/abs/2311.06180
