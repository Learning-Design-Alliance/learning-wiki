---
type: design
id: five-part-llm-prompt-template-saq-grading
title: Five-part LLM prompt template for AI-assisted grading of short-answer questions
description: "The approach gives large-language models instructor-guided few-shot prompt templates for grading: \"The prompt includes the text of the SAQ, the instructor’s criteria for a good answer, multiple examples of student res..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-06
sources:
  - id: heinrich-tobias-2025
    resource: "https://doi.org/10.1371/journal.pone.0328041"
    title: "Heinrich Tobias, Baily Spencer, Chen Kuan-Wu, DeOliveira Jack, Park Sanghoon, Wang Navida Chun-Han (2025). AI-assisted grading and personalized feedback in large political science classes: Results from randomized controlled trials. PLOS One. https://doi.org/10.1371/journal.pone.0328041"
    author: Heinrich Tobias, Baily Spencer, Chen Kuan-Wu, DeOliveira Jack, Park Sanghoon, Wang Navida Chun-Han
---

# Five-part LLM prompt template for AI-assisted grading of short-answer questions

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The approach gives large-language models instructor-guided few-shot prompt templates for grading: "The prompt includes the text of the SAQ, the instructor’s criteria for a good answer, multiple examples of student responses paired with the instructor’s grades and personalized feedback, and a new, ungraded student answer." In all classes instructors implemented the approach with OpenAI's GPT-4, and generated grades and feedback were entered into the course's learning platform.

## Design Implications

### Context
#### Requirements
- Instructors must develop a prompt template per SAQ containing the question text, a rubric distinguishing strong from weak answers, and about ten randomly chosen instructor-graded gold answers with feedback
#### Constraints
- GPT-4 was chosen over an open-source model, prioritizing ease of use and stronger performance over replicability and transparency, since model parameters are not public

### Target Learners
- undergraduate students in large-enrollment political science courses

### Learning Goals
- critical thinking through short-answer questions with personalized instructor feedback

### Claims
- [Ai Grading Pooled Discrimination Null](../claims/ai-grading-pooled-discrimination-null.md) [+M]
- [Ai Graded Saqs Fewer Regrade Requests](../claims/ai-graded-saqs-fewer-regrade-requests.md) [+M]
- [Human Grading Raises Perceived Feedback Helpfulness](../claims/human-grading-raises-perceived-feedback-helpfulness.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Heinrich Tobias, Baily Spencer, Chen Kuan-Wu, DeOliveira Jack, Park Sanghoon, Wang Navida Chun-Han (2025). AI-assisted grading and personalized feedback in large political science classes: Results from randomized controlled trials. PLOS One. https://doi.org/10.1371/journal.pone.0328041
