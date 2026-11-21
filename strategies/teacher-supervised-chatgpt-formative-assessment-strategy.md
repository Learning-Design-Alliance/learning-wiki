---
type: strategy
id: teacher-supervised-chatgpt-formative-assessment-strategy
title: Use ChatGPT as a teacher-supervised complementary tool for formative assessment of laboratory reports, not as an automated grader
description: "The article recommends integrating AI-generated evaluations as \"new forms of interaction that can provide feedback practices in the physics laboratory\" rather than replacements for human judgment."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: abreu-m-2025
    resource: "https://arxiv.org/abs/2510.16137"
    title: "Abreu M, Suárez A, Stari C and Martí A C. (2025). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. https://arxiv.org/abs/2510.16137"
    author: Abreu M, Suárez A, Stari C and Martí A C
---

# Use ChatGPT as a teacher-supervised complementary tool for formative assessment of laboratory reports, not as an automated grader

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (3 for, 1 mixed, 2 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
The article recommends integrating AI-generated evaluations as "new forms of interaction that can provide feedback practices in the physics laboratory" rather than replacements for human judgment. Teachers and students should engage critically with such feedback, and the model may support routine checks of structure and presentation plus aggregated analysis of recurring student difficulties, always under teacher supervision to ensure conceptual validity.

## Design Implications

### Context
#### Requirements
- Structured prompts and standardized interaction protocols, including a teaching role, checklist of tasks, the instructor evaluation guide, and a required output format
#### Constraints
- The complete automation of grading remains unrealistic given the complexity of validating scientific reasoning and content; AI evaluation of technical reasoning and data interpretation is less reliable

### Target Learners
- undergraduate physics students in Experimental Physics courses

### Target Learning Goals
- scientific writing and report structure
- experimental reasoning and interpretation of uncertainty

## Claims

- [API-based evaluation is efficient for large-scale processing but struggles with graphical content, while customized ChatGPT gives more contextualized feedback with lower reproducibility](../claims/api-versus-custom-gpt-complementary-tradeoff.md) [~W]
- [API-based evaluation fails on graphical and mathematical content because the model cannot parse images, tables, graphs and embedded equations](../claims/chatgpt-api-cannot-parse-figures-equations.md) [-W]
- [In API-based evaluation, ChatGPT consistently assesses the formal and structural aspects of physics laboratory reports](../claims/chatgpt-api-consistent-formal-assessment.md) [+W]
- [In API-based evaluation, ChatGPT's assessment of technical and conceptual content is irregular and often inaccurate](../claims/chatgpt-api-unreliable-technical-assessment.md) [-W]
- [The customized Physics Instructor GPT gives balanced formal feedback and can offer conceptually nuanced technical observations, but with greater variability](../claims/custom-gpt-balanced-context-sensitive-feedback.md) [+W]
- [The customized ChatGPT can accurately process graphical information when images are submitted directly through the interface](../claims/custom-gpt-direct-image-submission-accurate.md) [+W]

## Related Strategies

- [Implement AI in assessment as a hybrid support tool for low-stakes, formative stages while humans retain final grading authority](hybrid-ai-human-assessment-implementation.md)
- [Use automatic reflection classification for preliminary feedback and workload support, with final assessment retained by educators](automated-reflection-preliminary-feedback-educator-final.md)
- [Deploy AI-assisted classroom observation as a complementary first-pass screening and reflection tool, with raters retaining interpretive judgment](ai-assisted-observation-complementary-screening-strategy.md)
- [Use LLMs as faculty-supervised adjuncts for automated MCQ pretesting and formative feedback](llm-faculty-supervised-mcq-pretesting-feedback.md)
- [Integrate AI chatbots into dental education as supervised supplementary tools for exam preparation and formative self-assessment](supervised-chatbot-supplementary-dental-education.md)
- [Use LLMs cautiously as supplementary learning tools in dental education, with output verification and professional supervision](cautious-llm-supplementary-tools-dental-education.md)
- [Allocate human and AI effort by dimension type: automate explicit-criteria dimensions, retain human review for pedagogical judgment](human-ai-division-of-labor-mcq-generation.md)
- [Use LLM grading for programmatic assessment and triage, not for unreviewed student-facing feedback](llm-grading-programmatic-assessment-triage.md)

## Examples
-

## Key Sources
- Abreu M, Suárez A, Stari C and Martí A C. (2025). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. https://arxiv.org/abs/2510.16137
