---
type: strategy
id: concise-concrete-elaboration-on-confusion-strategy
title: Configure AI tutors to respond to detected confusion with concise, concrete elaboration rather than warmth or added length
description: "The article's implications for practice state that AI tutoring designers should incorporate \"concrete elaborations, such as analogies, comparisons, and worked examples\" when student confusion is detected, and that ins..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: shayla-sharmin-2026
    resource: "https://huggingface.co/datasets/wmcnicho/StudyChat"
    title: "Shayla Sharmin, Mohammad Fahim Abrar, Roghayeh Leila Barmaki. (2026). Micro-level AI Feedback Features and Student Responses in Consecutive LLM Tutoring Interactions. https://huggingface.co/datasets/wmcnicho/StudyChat"
    author: Shayla Sharmin, Mohammad Fahim Abrar, Roghayeh Leila Barmaki
---

# Configure AI tutors to respond to detected confusion with concise, concrete elaboration rather than warmth or added length

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 1 study (1 associational), `q2` · 1 of 1 report an effect size · 4 claims rest on one study

## Description
The article's implications for practice state that AI tutoring designers should incorporate "concrete elaborations, such as analogies, comparisons, and worked examples" when student confusion is detected, and that instructional designers should configure AI tutors to provide concise explanations during confused turns. This follows from the findings that elaboration predicted next-turn understanding while length predicted lower understanding. The authors also suggest prompting for "a short, targeted explanation built around a single analogy or example before adding further detail."

## Design Implications

### Context
#### Requirements
- A mechanism for detecting student confusion in the conversation to trigger the targeted explanatory support
#### Constraints
- The supporting evidence is correlational, from one undergraduate AI course and one tutoring system; generalization to other subjects, levels, or models is unknown

### Target Learners
- undergraduate students in an AI course using an LLM tutor

### Target Learning Goals
- resolving student confusion about course concepts in programming and AI topics

## Claims

- [Concrete elaboration in an AI tutor response is a significant positive predictor of the confused student's understanding in the next interaction](../claims/concrete-elaboration-predicts-next-turn-understanding.md) [+W]
- [Concrete elaboration is associated with lower re-confusion in the next interaction, significant in chi-square tests but only marginally significant in the GEE model](../claims/concrete-elaboration-lower-re-confusion-mixed.md) [+W]
- [Longer AI tutor responses are independently associated with lower understanding in the confused student's next interaction](../claims/long-responses-lower-next-turn-understanding.md) [+W]
- [Affective language in AI tutor responses shows no significant association with next-turn understanding or re-confusion](../claims/affective-language-no-immediate-effect.md) [-W]

## Related Strategies

- [Adapt tutor responses to detected learner affect: leading hints for frustration, engaging hooks for boredom, and timed intervention for confusion](affect-sensitive-autotutor-responses.md)

## Examples
-

## Key Sources
- Shayla Sharmin, Mohammad Fahim Abrar, Roghayeh Leila Barmaki. (2026). Micro-level AI Feedback Features and Student Responses in Consecutive LLM Tutoring Interactions. https://huggingface.co/datasets/wmcnicho/StudyChat
