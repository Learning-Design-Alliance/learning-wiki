---
type: element
status: review
last_edited: 2026-04-07
edited_by: Codex
---

# Adaptive Learning

## Description
Adaptive learning tailors content, pacing, support, or task sequence in response to evidence about a learner's current performance, needs, or prior knowledge.

## Design Implications

### Context
#### Requirements
- Evidence about learner performance, progress, or misconceptions
- A mechanism for changing sequence, support, or difficulty
- Instructional logic that connects adaptation to actual learning goals

#### Constraints
- Adaptation logic can be shallow if it only tracks correctness and not the kind of error or misunderstanding
- Highly adaptive systems can be hard for instructors and learners to interpret
- Personalization should not isolate learners from shared discussion, collaboration, or common goals

### Target Learners
- Learners with heterogeneous readiness levels
- Learners needing more practice or support in specific subskills
- Learners in digital or blended environments where progress data is available continuously

### Target Learning Goals
- Matching instruction more closely to current readiness
- Supporting mastery while reducing unnecessary repetition
- Making it easier to differentiate without fully separating learners

### Affordances
- Supports personalized pacing
- Can route learners to more practice, feedback, or challenge
- Helps instructors manage variation when used transparently

## Related Elements
- [[elements/adaptive-difficulty|Adaptive Difficulty]]
- [[elements/adaptive-mastery-learning|Adaptive Mastery Learning]]
- [[elements/mastery-progression|Mastery Progression]]
- [[elements/provide-guidance|Provide Guidance]]

## Patterns That Use This Element
- [[patterns/game-based-mastery-learning-eg-duolingo-pattern|Game-Based Mastery Learning (e.g., Duolingo Pattern)]]

## Examples
- A tutoring system recommends new tasks based on recent error patterns
- A course platform routes learners to review material when they miss prerequisite concepts
- An instructor changes grouping and support based on ongoing formative evidence

## Key Sources
- Shute, V. J., & Towle, B. (2003). Adaptive e-learning. *Educational Psychologist, 38*(2), 105-114. [https://doi.org/10.1207/S15326985EP3802_4](https://doi.org/10.1207/S15326985EP3802_4)
