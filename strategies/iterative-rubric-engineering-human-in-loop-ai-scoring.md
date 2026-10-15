---
type: strategy
id: iterative-rubric-engineering-human-in-loop-ai-scoring
title: Implement AI scoring of OEQs through iterative rubric engineering with humans in the loop checking validity, reliability, reproducibility, and bias
description: The article offers a roadmap in which prior exams are used to evaluate the reliability of generative AI scores and adjust scoring rubrics before live use.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: olvet-dm-2026
    resource: "https://doi.org/10.1007/s40670-026-02638-2"
    title: "Olvet DM, Kruidering M, Fulton TB, Truong B, Endo K, Lucito R, Willey JM. (2026). Can Generative Artificial Intelligence Reliably Score Open-Ended Question Assessments in Undergraduate Medical Education? Medical Science Educator 36:1539–1552. https://doi.org/10.1007/s40670-026-02638-2"
    author: Olvet DM, Kruidering M, Fulton TB, Truong B, Endo K, Lucito R, Willey JM
---

# Implement AI scoring of OEQs through iterative rubric engineering with humans in the loop checking validity, reliability, reproducibility, and bias

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article offers a roadmap in which prior exams are used to evaluate the reliability of generative AI scores and adjust scoring rubrics before live use. Faculty conduct error pattern analysis using GPT-4's feedback, refine the rubric, and re-score across iterations. As the authors state, "It is essential that humans remain in the loop to check for validity (i.e., is AI providing accurate information), reliability (i.e., is AI scoring comparable to faculty scoring?), reproducibility (i.e., is AI providing consistent scores?), and bias (i.e., is AI providing biased information?)". Safeguards include faculty scoring a subset of exams, having AI re-score the same exam multiple times, and reviewing AI feedback for accuracy.

## Design Implications

### Context
#### Requirements
- Up-front time investment to establish reliability through multiple scoring iterations with faculty error pattern review
- Faculty content experts available to adjudicate gold standard scores and refine rubrics
#### Constraints
- If scoring an entire exam is not feasible, the article suggests reserving AI for more analytic and straightforward questions and faculty scoring for more complex reasoning questions
- Reliability may not remain robust on future generations of AI models

### Target Learners
- medical students in undergraduate medical education

### Target Learning Goals
- accurate scoring of open-ended assessment of medical knowledge
- timely personalized feedback on exam performance

## Related Strategies

- [Integrate GPT models into LA-supported feedback systems with an iterative instructor-student validation loop to improve reliability](iterative-validation-loop-gpt-feedback-systems.md)

## Examples
-

## Key Sources
- Olvet DM, Kruidering M, Fulton TB, Truong B, Endo K, Lucito R, Willey JM. (2026). Can Generative Artificial Intelligence Reliably Score Open-Ended Question Assessments in Undergraduate Medical Education? Medical Science Educator 36:1539–1552. https://doi.org/10.1007/s40670-026-02638-2
