---
type: design
id: learnopt-framework-theory
title: "LearnOpt framework: exam preparation as constrained optimization over an LLM-built exam knowledge graph with BKT mastery updates"
description: "LearnOpt reframes exam preparation as a constrained optimization problem: it ingests historical question papers, LLM-tags each question with chapter, topic, difficulty and skill via a chain-of-evidence prompt, builds..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: joy-bose-2025
    resource: "https://github.com/learnopt/learnopt"
    title: "Joy Bose, Om Thomas. (2025). LearnOpt: Recovering the Latent Cognitive Structure of Standardized Examinations via Knowledge Graphs and Constrained Optimization. https://github.com/learnopt/learnopt"
    author: Joy Bose, Om Thomas
---

# LearnOpt framework: exam preparation as constrained optimization over an LLM-built exam knowledge graph with BKT mastery updates

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
LearnOpt reframes exam preparation as a constrained optimization problem: it ingests historical question papers, LLM-tags each question with chapter, topic, difficulty and skill via a chain-of-evidence prompt, builds a knowledge graph in FalkorDB with prerequisite edges, and "produces a ranked, time-bounded study plan specifying which concept subgroups to study, in what sequence, and with what expected score gain." Mastery is initialized from self-report and updated via standard BKT; the objective is solved with Google OR-Tools CP-SAT and re-run after each study session. Its substantive extension over the Embibe PAJ precedent is a skill-weighted objective coupling the exam's empirical cognitive-operation distribution into the reward signal.

## Design Implications

### Context
#### Requirements
- Historical question papers in PDF format, an official syllabus, and a student mastery vector as inputs; full question text including options for reliable skill tagging
#### Constraints
- Validated on MCQ exams; transfer to subjective or coding assessments requires further work
- Mastery vectors initialized from self-report introduce subjective bias; optimization evaluation is simulation-based with no measured student outcomes

### Target Learners
- NEET and JEE aspirants preparing for standardized examinations

### Learning Goals
- Efficient allocation of limited preparation time across topics and cognitive skills to maximize expected exam score

### Claims
- [Learnopt Neet Regime Shift 2023](../claims/learnopt-neet-regime-shift-2023.md) [+M]
- [Learnopt Jee Advanced Skill Profile](../claims/learnopt-jee-advanced-skill-profile.md) [+M]

## Related Designs

- [Chain-of-Concept: topic-graph organisation of past assessments replacing similarity-based retrieval](chain-of-concept-topic-graph-memory.md)

## Examples
-

## Key Sources
- Joy Bose, Om Thomas. (2025). LearnOpt: Recovering the Latent Cognitive Structure of Standardized Examinations via Knowledge Graphs and Constrained Optimization. https://github.com/learnopt/learnopt
