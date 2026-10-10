---
type: design
id: iterative-llm-refinement-item-generation
title: Iterative LLM refinement strategy for generating course-tailored exam questions
description: "A two-stage generation procedure, similar to Self-Refine, in which an LLM generator produces multiple-choice questions from instructor-provided course materials and an AI judge labels each question \"good\" or \"bad\"; la..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: calvin-isley-2025
    resource: "https://arxiv.org/abs/2508.08314"
    title: "Calvin Isley, Joshua Gilbert, Evangelos Kassos, Michaela Kocher, Allen Nie, Emma Brunskill, Ben Domingue, Jake Hofman, Joscha Legewie, Teddy Svoronos, Charlotte Tuminelli, Sharad Goel. (2025). Assessing the Quality of AI-Generated Exams: A Large-Scale Field Study. https://arxiv.org/abs/2508.08314"
    author: Calvin Isley, Joshua Gilbert, Evangelos Kassos, Michaela Kocher, Allen Nie, Emma Brunskill, Ben Domingue, Jake Hofman, Joscha Legewie, Teddy Svoronos, Charlotte Tuminelli, Sharad Goel
---

# Iterative LLM refinement strategy for generating course-tailored exam questions

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A two-stage generation procedure, similar to Self-Refine, in which an LLM generator produces multiple-choice questions from instructor-provided course materials and an AI judge labels each question "good" or "bad"; labeled questions are fed back into the generator's prompt as few-shot examples, and the loop repeats until 20 judge-approved questions exist. A final judging round assesses difficulty, appropriateness, and answer correctness, and the 10 hardest approved questions become the class-specific exam. All generation and judging used OpenAI's o3-mini model, with five 2012 AP Statistics practice questions as "good" examples in every prompt.

## Design Implications

### Context
#### Requirements
- Instructor-provided course materials (course description, syllabus, prior homework or exams) converted to plain text as context for both generator and judge
- An AI judge applying appropriateness criteria such as no syllabus-logistics questions, mentally solvable calculations, and no duplicated concepts
#### Constraints
- Question generation was limited to multiple-choice questions solvable in about 1-2 minutes each
- If final judging removed more than 10 questions, an additional 20 questions had to be generated and the full group of 40 re-evaluated

### Target Learners
- college students in STEM and quantitative courses

### Learning Goals
- assessment of course-specific conceptual understanding

### Claims
- [Ai Items Slightly More Discriminating](../claims/ai-items-slightly-more-discriminating.md) [+M]
- [Ai Exam Items Easier Than Standardized](../claims/ai-exam-items-easier-than-standardized.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Calvin Isley, Joshua Gilbert, Evangelos Kassos, Michaela Kocher, Allen Nie, Emma Brunskill, Ben Domingue, Jake Hofman, Joscha Legewie, Teddy Svoronos, Charlotte Tuminelli, Sharad Goel. (2025). Assessing the Quality of AI-Generated Exams: A Large-Scale Field Study. https://arxiv.org/abs/2508.08314
