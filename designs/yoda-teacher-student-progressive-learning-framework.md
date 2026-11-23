---
type: design
id: yoda-teacher-student-progressive-learning-framework
title: "YODA: teacher-student progressive learning framework with a basic-generalized-harder loop and iterative feedback-refinement"
description: YODA is a dual-agent framework in which a student agent answers questions and refines responses from teacher feedback, while a teacher agent evaluates answers and poses generalized and harder questions.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: jianqiao-lu-2024
    resource: "https://arxiv.org/abs/2401.15670"
    title: "Jianqiao Lu, Wanjun Zhong, Yufei Wang, Zhijiang Guo, Qi Zhu, Wenyong Huang, Yanlin Wang, Fei Mi, Baojun Wang, Yasheng Wang, Lifeng Shang, Xin Jiang, Qun Liu. (2024). YODA: Teacher-Student Progressive Learning for Language Models. arXiv. https://arxiv.org/abs/2401.15670"
    author: Jianqiao Lu, Wanjun Zhong, Yufei Wang, Zhijiang Guo, Qi Zhu, Wenyong Huang, Yanlin Wang, Fei Mi, Baojun Wang, Yasheng Wang, Lifeng Shang, Xin Jiang, Qun Liu
---

# YODA: teacher-student progressive learning framework with a basic-generalized-harder loop and iterative feedback-refinement

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
YODA is a dual-agent framework in which a student agent answers questions and refines responses from teacher feedback, while a teacher agent evaluates answers and poses generalized and harder questions. It "operates on a progressive basic-generalized-harder interactive learning loop": basic problems first, conceptually similar generalized questions to consolidate skills, then progressively more complex problems. The resulting procedural data (question-answer pairs plus full refinement trajectories) trains a smaller model. Both roles were instantiated with the same GPT-4 instance, and the paper notes the teacher need not surpass the student because "evaluation is often easier than task completion".

## Design Implications

### Context
#### Requirements
- An initial unlabeled basic question corpus U as seed problems
- A teacher agent capable of question generalization, question complication, and answer evaluation
- A student agent capable of question answering and answer self-refinement from feedback
#### Constraints
- Evaluated on math reasoning with GPT-4 as both agents and LLaMA2-7B as the trained model; the paper's Limitation section is empty of stated content in the provided text

### Target Learners
- Large language models being fine-tuned for reasoning

### Learning Goals
- Mathematical reasoning and problem-solving skill acquisition from limited seed problems

### Claims

## Related Designs
- 

## Examples
-

## Key Sources
- Jianqiao Lu, Wanjun Zhong, Yufei Wang, Zhijiang Guo, Qi Zhu, Wenyong Huang, Yanlin Wang, Fei Mi, Baojun Wang, Yasheng Wang, Lifeng Shang, Xin Jiang, Qun Liu. (2024). YODA: Teacher-Student Progressive Learning for Language Models. arXiv. https://arxiv.org/abs/2401.15670
