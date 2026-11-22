---
type: design
id: probing-only-ai-agent-introductory-mechanics
title: Probing-only conversational AI agent for introductory mechanics
description: "A conversational AI agent built as a measurement instrument rather than a tutor: \"It asks a student to commit to a prediction about a concrete everyday situation, explain it without physics vocabulary, and then defend..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: byungmoon-cho-2026
    resource: "https://arxiv.org/abs/2610.22949"
    title: "Byungmoon Cho. (2026). Designing an AI Agent That Does Not Tutor: Design Rules for Socratic Probing in Introductory Physics. https://arxiv.org/abs/2610.22949"
    author: Byungmoon Cho
---

# Probing-only conversational AI agent for introductory mechanics

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 qualitative, 1 design), `q1`–`q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
A conversational AI agent built as a measurement instrument rather than a tutor: "It asks a student to commit to a prediction about a concrete everyday situation, explain it without physics vocabulary, and then defend that explanation against a changed case constructed from the student's own words." It does not teach, hint, confirm, or correct during the conversation and reports nothing until the end. A conversation takes about six minutes, covers Newton's three laws in fixed order, uses a 27-variant question bank selected by class number, and ends with per-law scores, a pointer to course notes, and a machine-readable summary line.

## Design Implications

### Context
#### Requirements
- Replies after correct and wrong answers must be interchangeable, so no reply carries correctness information
- A hard cap of at most two probes per question plus one resolution question
- The model must write down its routing decision before acting on it
#### Constraints
- It cannot authenticate who is typing; a student with someone else supplying answers in real time can score well
- Prompt rules have a reliability ceiling: improvised probes sometimes leave the setting, the agent occasionally exceeds the follow-up cap, and it scores tentative answers somewhat generously
- Scores are formative; nothing in the design is proposed as a basis for grading

### Target Learners
- introductory physics students, including online sections at a two-year college

### Learning Goals
- diagnosing whether students' correct answers reflect robust conceptual understanding of Newton's laws

### Claims

- Cave Detection Four Outcome Scheme [+M]
- [Llm Agents Leak Evaluation Correctness](../claims/llm-agents-leak-evaluation-correctness.md) [+W]
- [In the roller coaster loop dialogue, ChatGPT excelled at providing clear explanations, addressing misconceptions, and promoting active learning through Socratic questioning.](../claims/chatgpt-socratic-roller-coaster-active-learning.md) [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- Byungmoon Cho. (2026). Designing an AI Agent That Does Not Tutor: Design Rules for Socratic Probing in Introductory Physics. https://arxiv.org/abs/2610.22949
