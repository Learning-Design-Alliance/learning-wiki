---
type: design
id: learning-in-blocks-framework
title: "Learning in Blocks: HeteroMAD-scored conversational assessment driving mastery-based progression and spaced review"
description: Learning in Blocks is an adaptive language-learning framework that links progression and review to evidence from open-ended conversations scored with CEFR-aligned rubrics by heterogeneous multi-agent debate.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: nicy-scaria-2026
    resource: "https://arxiv.org/abs/2604.22770"
    title: "Nicy Scaria, Silvester John Joseph Kennedy, and Deepak Subramani. (2026). Learning in Blocks: A Multi Agent Debate Assisted Personalized Adaptive Learning Framework for Language Learning. Preprint, to appear in International Conference on Artificial Intelligence in Education (LNAI). https://arxiv.org/abs/2604.22770"
    author: Nicy Scaria, Silvester John Joseph Kennedy, and Deepak Subramani
---

# Learning in Blocks: HeteroMAD-scored conversational assessment driving mastery-based progression and spaced review

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 3 claims rest on one study

## Description
Learning in Blocks is an adaptive language-learning framework that links progression and review to evidence from open-ended conversations scored with CEFR-aligned rubrics by heterogeneous multi-agent debate. HeteroMAD operates in two stages — a scoring stage where role-specialized agents evaluate Grammar, Vocabulary, and Interactive Communication and debate conflicting judgments before a judge synthesizes consensus scores, and a recommendation stage that identifies grammar skills and vocabulary topics for targeted review. Progression to the next Concept Block is gated: "if they achieve at least 70% in every GVC contained in CB t, at which point progression to CBt+1 is unlocked". Unmastered skills are logged into per-block review lesson groups re-tested at spaced intervals, and diagnostic bridge assessments personalize subsequent blocks when learners demonstrate untaught skills.

## Design Implications

### Context
#### Requirements
- Conversations must be scored against CEFR-aligned rubrics validated against expert judgment
- Agents must be conditioned on the cumulative set of skills and vocabulary the learner has been exposed to
#### Constraints
- Mastery-based progression slows advancement through the block sequence relative to ungated progression
- Benchmarked and studied only at CEFR A2 in an 8-week period

### Target Learners
- English learners working toward CEFR A2 proficiency

### Learning Goals
- Grammar accuracy
- Vocabulary precision
- Interactive Communication in spoken interaction

### Claims
- [Heteromad Best Score Agreement Cefr A2](../claims/heteromad-best-score-agreement-cefr-a2.md) [+M]
- [Heteromad Recommendation Acceptability 90 91](../claims/heteromad-recommendation-acceptability-90-91.md) [+M]
- [Learning In Blocks Cohort Largest Gains](../claims/learning-in-blocks-cohort-largest-gains.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Nicy Scaria, Silvester John Joseph Kennedy, and Deepak Subramani. (2026). Learning in Blocks: A Multi Agent Debate Assisted Personalized Adaptive Learning Framework for Language Learning. Preprint, to appear in International Conference on Artificial Intelligence in Education (LNAI). https://arxiv.org/abs/2604.22770
