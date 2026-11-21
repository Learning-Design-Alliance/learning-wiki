---
type: design
id: ai-practice-exam-system-confidence-explanations
title: AI-powered practice exam system combining GPT-4o feedback, textbook links, and required confidence ratings and explanations
description: The article presents a practice exam system deployed in a 1002-student biology course, built with Laravel 11.34 and Vue.js on AWS.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: mak-ahmad-2025
    resource: "https://doi.org/10.1145/3698205.3729542"
    title: "Mak Ahmad, Prerna Ravi, David Karger, and Marc Facciotti. 2025. How Adding Metacognitive Requirements in Support of AI Feedback in Practice Exams Transforms Student Learning Behaviors. In Proceedings of the Twelfth ACM Conference on Learning @ Scale (L@S '25). https://doi.org/10.1145/3698205.3729542"
    author: Mak Ahmad, Prerna Ravi, David Karger, and Marc Facciotti
---

# AI-powered practice exam system combining GPT-4o feedback, textbook links, and required confidence ratings and explanations

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 3 claims rest on one study

## Description
The article presents a practice exam system deployed in a 1002-student biology course, built with Laravel 11.34 and Vue.js on AWS. Students answer multiple-choice questions while "students must indicate a confidence level and provide an explanation for their choice", then receive condition-specific feedback in review mode. GPT-4o generates 5-7 sentence feedback conditioned on the student's answer, explanation, and confidence, with validated learning-objective summaries constraining responses to reduce hallucination risk.

## Design Implications

### Context
#### Requirements
- A validated question bank with learning-objective mappings and instructor-validated textbook summaries; the article reports data preparation took over 30 hours
- Students must provide both a confidence rating and written explanation for each answer before proceeding
#### Constraints
- When API responses fail or take too long, the system degrades to simpler feedback modes, changing the experimental condition
- Some students found the AI-generated text too dense and difficult to read in the small feedback window

### Target Learners
- First-year undergraduate general biology students in large-enrollment courses

### Learning Goals
- Midterm exam preparation across approximately 400 multiple-choice questions covering course learning objectives
- Metacognitive self-assessment and self-regulated study behaviors

### Claims
- [No Significant Difference Four Feedback Conditions Practice Exams](../claims/no-significant-difference-four-feedback-conditions-practice-exams.md) [+M]
- [Confidence Ratings Predict Exam Performance](../claims/confidence-ratings-predict-exam-performance.md) [+M]
- [High Satisfaction Voluntary Adoption Practice Tool](../claims/high-satisfaction-voluntary-adoption-practice-tool.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Mak Ahmad, Prerna Ravi, David Karger, and Marc Facciotti. 2025. How Adding Metacognitive Requirements in Support of AI Feedback in Practice Exams Transforms Student Learning Behaviors. In Proceedings of the Twelfth ACM Conference on Learning @ Scale (L@S '25). https://doi.org/10.1145/3698205.3729542
