---
type: strategy
id: human-in-the-loop-review-of-ai-feedback
title: Instructors should review and edit all AI-generated feedback before sending it to students
description: Because LLM outputs are probabilistic and can contain hallucinations or bias, the article recommends a human-in-the-loop procedure in which the instructor checks every AI-generated feedback statement and edits as need...
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

# Instructors should review and edit all AI-generated feedback before sending it to students

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 3 studies (1 quant-synthesis, 1 review, 1 theoretical), `q1`–`q2` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
Because LLM outputs are probabilistic and can contain hallucinations or bias, the article recommends a human-in-the-loop procedure in which the instructor checks every AI-generated feedback statement and edits as needed before delivery. The article's proposed grading-assistant workflow makes instructor editing the third step: all response-feedback pairs are presented to the instructor, who edits feedback, which takes significantly less time than generating all feedback from scratch.

## Design Implications

### Context
#### Requirements
- Instructor time to review all response-feedback pairs before sending corrected feedback to students
#### Constraints
- AI-generated feedback could be potentially biased because LLMs are pre-trained on data from sources including the internet and social media
- LLMs could also generate incoherent chains of argument or factually incorrect information, termed hallucination

### Target Learners
- introductory physics students in large-enrollment courses

### Target Learning Goals
- receiving correct, personalized feedback on written responses

## Claims

- [AI systems can produce biased or inaccurate diagnostic outputs, requiring critical teacher evaluation before integration](../claims/ai-biased-inaccurate-outputs-require-critical-evaluation.md) [+W]
- [Reviewed literature reports risks of overreliance, AI errors in complex tasks, and students' uncritical acceptance of AI-generated outputs](../claims/ai-math-risks-overreliance-errors-uncritical-trust.md) [+W]
- [Recurring risks of GenAI in STEAM education include hallucination, bias, superficial completion strategies, and compromised assessment validity](../claims/genai-steam-risks-hallucination-bias.md) [+W]

## Related Strategies

- [Design GPT feedback prompts with few-shot examples covering each response category and documented student preconceptions as context](few-shot-prompt-with-preconceptions-for-feedback-generation.md)
- [Add human-in-the-loop capabilities so practitioners can edit or choose among LLM-generated tutoring script components](human-in-the-loop-cts-authoring-strategy.md)
- [Human-in-the-loop evaluation of LLM assessment conversations for fairness, bias, and explainability](human-in-the-loop-llm-cba-fairness-evaluation.md)
- [Incorporate pre-delivery LLM-based evaluation approaches into GenAI-powered personalised SRL scaffolding systems to mitigate hallucinations](pre-delivery-llm-evaluation-mitigate-hallucinations.md)
- [Validate ChatGPT-generated learning content through instructor review before giving it to residents](instructor-validation-of-chatgpt-content.md)
- [Integrate GPT models into LA-supported feedback systems with an iterative instructor-student validation loop to improve reliability](iterative-validation-loop-gpt-feedback-systems.md)
- [Human-in-the-loop quality control for AI-generated educational content](human-in-the-loop-ai-content-quality-control.md)
- [Integrate a teacher or instructor interface to review and correct AI-generated content alongside AI feedback](hybrid-ai-human-feedback-instructor-interface.md)
- [Structure AI-assisted feedback to prioritize instructor-authored content, then instructor-edited AI suggestions, with pure AI comments only filling gaps](instructor-authored-feedback-priority.md)
- [Use hybrid AI feedback combining directive guidance with reflective prompts in large-enrolment and online courses](hybrid-ai-feedback-large-courses-strategy.md)
- [Extend feedback coverage by having instructors verify LLM-generated feedback for uncovered error patterns ad hoc](instructor-verified-llm-feedback-uncovered-errors.md)

## Examples
-

## Key Sources
- Tong Wan and Zhongzhou Chen. (2023). Exploring Generative AI assisted feedback writing for students' written responses to a physics conceptual question with prompt engineering and few-shot learning. https://arxiv.org/abs/2311.06180
