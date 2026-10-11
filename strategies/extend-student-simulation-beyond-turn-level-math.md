---
type: strategy
id: extend-student-simulation-beyond-turn-level-math
title: Future student-simulation work should extend beyond turn-level math dialogue and address history-selection and faithfulness gaps
description: "The authors lay out forward-looking directions: studying how to include a student's entire learning history in context, potentially \"by leveraging interaction embeddings optimized for student simulation or using intel..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: zhangqi-duan-2026
    resource: "https://arxiv.org/abs/2605.30051"
    title: "Zhangqi Duan, Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Simon Woodhead, Andrew Lan. (2026). Who Am I? History-Aware Profiles for Student Simulation in Tutoring Dialogues. arXiv preprint. https://arxiv.org/abs/2605.30051"
    author: Zhangqi Duan, Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Simon Woodhead, Andrew Lan
---

# Future student-simulation work should extend beyond turn-level math dialogue and address history-selection and faithfulness gaps

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The authors lay out forward-looking directions: studying how to include a student's entire learning history in context, potentially "by leveraging interaction embeddings optimized for student simulation or using intelligent context retrieval"; extending simulation beyond dialogue turns to predicting selected options or help requests; examining faithfulness in fully simulated dialogues with new metrics; and testing the task in other domains including programming and language learning. They also plan evaluation on the ASSISTments tutoring chat log dataset to test generalizability beyond their private math data.

## Design Implications

### Context
#### Requirements
- New metrics to compare fully simulated tutor-student dialogues against ground-truth dialogues
#### Constraints
- Current evaluation covers a single private dataset in the math domain and only turn-level simulation

### Target Learners
- Math students, with planned extension to programming and language learners

### Target Learning Goals
- Faithful simulation of student behavior for evaluating and training LLM tutors

### Affordances
- [History Conditioned Student Simulation Framework](../research-methods/history-conditioned-student-simulation-two-component-profile-generator-plus-simulator-fram.md)

## Related Strategies

- [Future Directions for Dialogue Knowledge Tracing](future-directions-for-dialogue-knowledge-tracing.md)

## Examples
-

## Key Sources
- Zhangqi Duan, Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Simon Woodhead, Andrew Lan. (2026). Who Am I? History-Aware Profiles for Student Simulation in Tutoring Dialogues. arXiv preprint. https://arxiv.org/abs/2605.30051
