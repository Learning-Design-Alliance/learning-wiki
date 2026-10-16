---
type: design
id: rag-gpt4o-tutor-training-lesson-generator
title: RAG-based GPT-4o lesson generation system with task-decomposition prompting for tutor training lessons
description: A two-step system in which a lesson designer first retrieves research articles on effective tutoring practices, then uses them to prompt the GPT-4o model (gpt-4o-2024-05-13) to generate scenario-based lessons for trai...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: jionghao-lin-2025
    resource: "https://arxiv.org/abs/2506.17356"
    title: "Jionghao Lin, Jiarui Rao, Sandy Yiyang Zhao, Yuting Wang, Ashish Gurung, Amanda Barany, Jaclyn Ocumpaugh, Ryan S. Baker, and Kenneth R. Koedinger. (2025). Automatic Large Language Models Creation of Interactive Learning Lessons. arXiv preprint. https://arxiv.org/abs/2506.17356"
    author: Jionghao Lin, Jiarui Rao, Sandy Yiyang Zhao, Yuting Wang, Ashish Gurung, Amanda Barany, Jaclyn Ocumpaugh, Ryan S. Baker, and Kenneth R. Koedinger
---

# RAG-based GPT-4o lesson generation system with task-decomposition prompting for tutor training lessons

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A two-step system in which a lesson designer first retrieves research articles on effective tutoring practices, then uses them to prompt the GPT-4o model (gpt-4o-2024-05-13) to generate scenario-based lessons for training novice tutors of middle school mathematics online. The article states "The strength of RAG lies in its ability to produce contextually accurate content by incorporating the generated output into factual data." Lessons follow a five-section structure (Title Page, Scenario I, Instruction, Scenario II, Conclusion) and can be generated in one to five segments.

## Design Implications

### Context
#### Requirements
- A lesson designer retrieves articles related to specific tutoring practices, providing the foundational knowledge on effective instructional strategies
- The lesson follows the structured five-section tutor training format
#### Constraints
- Even with RAG integrating academic papers containing verified references, the model still produced references that did not exist

### Target Learners
- novice human tutors teaching middle school mathematics online

### Learning Goals
- effective tutoring practices
- scenario-based tutoring skills

### Claims
- [Three Segment Decomposition Highest Rated Llm Lessons](../claims/three-segment-decomposition-highest-rated-llm-lessons.md) [+M]
- [Rag Does Not Ensure Citation Authenticity](../claims/rag-does-not-ensure-citation-authenticity.md) [-M]

## Related Designs
- 

## Examples
-

## Key Sources
- Jionghao Lin, Jiarui Rao, Sandy Yiyang Zhao, Yuting Wang, Ashish Gurung, Amanda Barany, Jaclyn Ocumpaugh, Ryan S. Baker, and Kenneth R. Koedinger. (2025). Automatic Large Language Models Creation of Interactive Learning Lessons. arXiv preprint. https://arxiv.org/abs/2506.17356
