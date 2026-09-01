---
type: element
id: quizzes
title: Quizzes
description: Short, low-stakes assessments that reinforce learning and provide feedback.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Quizzes

> **Element** · [All elements](index.md)

## Description
Quizzes are short, low-stakes assessments used during learning rather than at its end. Their primary function is not measurement but learning: answering questions forces retrieval from memory, and the feedback that follows corrects and consolidates what was retrieved.

## Design Implications

Quizzes are one of the most robustly supported instructional elements: testing itself improves long-term retention, often more than restudying the same material [Rowland, 2014 meta-analysis] [+S]. The benefit comes from the act of retrieval, not merely from re-exposure to content, so quiz questions should require learners to produce or select answers from memory rather than simply reread. Feedback is essential — retrieval without corrective feedback can entrench errors, especially for high-confidence wrong answers [High-confidence errors improve retention when corrected.](../claims/high-confidence-errors-improve-retention.md) [~M]. Distributing quizzes over time multiplies the effect, since spaced retrieval produces markedly better retention than massed testing [Spaced retrieval outperforms massed.](../claims/spaced-repetition-improves-retention.md) [+S].

### Context
#### Requirements
- Questions that target retrieval, not recognition of recently seen text (avoid verbatim repetition of study material)
- Immediate or rapid feedback with correct answers and brief explanations
- Low or no stakes, so errors are treated as learning events rather than failures
- Distribution across time, aligned with a [Spaced Repetition](spaced-repetition.md) schedule

#### Constraints
- Quizzes that only test recall of isolated facts can narrow study behavior toward memorization at the expense of deeper understanding [~M] — learners study to the test format
- Testing without feedback risks reinforcing errors; learners may confidently re-retrieve wrong answers [-S]
- Frequent identical re-testing produces diminishing returns once material is mastered; question difficulty must adapt or rotate [~M]
- High-stakes framing undermines the benefit — anxiety and grade pressure shift attention from learning to performance [~M]

### Target Learners
- Effective across ages and subject domains, including young children and medical students [Rowland, 2014 meta-analysis] [+S]
- Particularly valuable in digital environments where automated question delivery and feedback are cheap and scalable
- Benefits learners with weaker prior knowledge especially, because retrieval success builds a foundation for later integration [+M]

### Target Learning Goals
- Retention of factual and conceptual knowledge over weeks and months
- Formative diagnosis: identifying gaps for both learner and instructor
- Fluency building: automating prerequisite knowledge to free working memory for complex tasks

### Affordances
- [Retrieval Practice](retrieval-practice.md) — a quiz is the operational form of retrieval practice; the testing effect is the mechanism behind the element
- [Formative Assessment](../principles/formative-assessment.md) — low-stakes quizzes generate evidence of understanding that can trigger instructional adjustment before summative assessment
- [Cognitive Load Theory](../principles/cognitive-load-theory.md) — successful retrieval of prerequisite knowledge automates it, reducing working-memory load during subsequent complex learning
- [Mastery Learning](../principles/mastery-learning.md) — quizzes provide the checkpoint mechanism: learners advance only after demonstrating criterion performance
- [Spaced Repetition](spaced-repetition.md) — quiz scheduling is the delivery vehicle for spacing; systems resurface items at expanding intervals

## Related Elements
- [Retrieval Practice](retrieval-practice.md) — the underlying mechanism; a quiz is retrieval practice with assessment structure
- [Formative Assessment](formative-assessment.md) — the broader function quizzes serve when results inform teaching
- [Spaced Repetition](spaced-repetition.md) — the scheduling principle that determines when quizzes should occur
- [Feedback](feedback.md) — the component that converts retrieval into corrected knowledge
- [Assess Performance](assess-performance.md) — Gagné's event that quizzes operationalize

## Patterns That Use This Element
- [Formative Assessment](../patterns/formative-assessment.md) — quizzes as the recurring evidence-gathering loop
- [Mastery Learning](../patterns/mastery-learning.md) — quizzes as criterion-referenced checkpoints gating progression
- [Competency-Based Learning](../patterns/competency-based-learning.md) — quizzes as evidence of demonstrated competency
- [Flipped Classroom](../patterns/flipped-classroom.md) — pre-class quizzes hold learners accountable for first-exposure material

## Examples

**[Duolingo](https://www.duolingo.com)** — Short, frequent, gamified quizzes with adaptive item resurfacing; a mass-market implementation of spaced retrieval.

**[Anki](https://apps.ankiweb.net)** — Spaced-repetition flashcard system that schedules retrieval attempts at expanding intervals based on self-rated difficulty.

**[Khan Academy](https://www.khanacademy.org)** — Practice exercises with immediate feedback and mastery tracking; quizzes gate progression through skill levels.

**[Retrieval practice guides](https://www.retrievalpractice.org)** — Agarwal and Bain's teacher-facing resources translating testing-effect research into classroom quiz routines (e.g., "brain dumps," two-things exit tickets).

## Key Sources
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/medu.12141](https://doi.org/10.1111/medu.12141)
- Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin, 140*(6), 1432–1463. [doi:10.1037/a0037559](https://doi.org/10.1037/a0037559)
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. [doi:10.1080/0969595980050102](https://doi.org/10.1080/0969595980050102)
- Butler, A. C., & Roediger, H. L. (2008). Feedback enhances the positive effects and reduces the negative effects of multiple-choice testing. *Memory & Cognition, 36*(3), 604–616. [doi:10.3758/MC.36.3.604](https://doi.org/10.3758/MC.36.3.604)