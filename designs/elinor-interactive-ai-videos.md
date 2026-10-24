---
type: design
id: elinor-interactive-ai-videos
title: AI-powered interactive Elinor Wonders Why videos with contingent dialogue
description: "Interactive science videos built with PBS KIDS on two Elinor Wonders Why episodes (aerodynamics and reptile molting), in which \"the main character, powered by artificial intelligence (AI), engaged in conversation with..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-24
sources:
  - id: ying-xu-2023
    resource: "https://osf.io/j7upd"
    title: "Ying Xu, Kunlei He, Julian Levine, Daniel Ritchie, Zexuan Pan, Andres Bustamante, and Mark Warschauer. (2023). Artificial Intelligence Enhances Children's Science Learning from Television Shows. https://osf.io/j7upd"
    author: Ying Xu, Kunlei He, Julian Levine, Daniel Ritchie, Zexuan Pan, Andres Bustamante, and Mark Warschauer
---

# AI-powered interactive Elinor Wonders Why videos with contingent dialogue

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
Interactive science videos built with PBS KIDS on two Elinor Wonders Why episodes (aerodynamics and reptile molting), in which "the main character, powered by artificial intelligence (AI), engaged in conversation with children by asking them questions and providing responsive feedback". They use "automatic speech recognition and intent detection, powered by Google's cloud services"; when the AI did not comprehend an answer, Elinor rephrased the question in simpler language, e.g. converting an open-ended question to multiple choice. Questions and feedback were based on the Next Generation Science Standards and vetted by PBS KIDS' science learning advisory board.

## Design Implications

### Context
#### Requirements
- Automatic speech recognition and intent detection (Google cloud services) to classify children's utterances by semantic intent
- Questions and feedback aligned to the Next Generation Science Standards and vetted by a science learning advisory board
#### Constraints
- Speech data may need to be shared with third-party services, raising privacy concerns; COPPA does not explicitly cover AI technologies
- Speech recognition performance may vary with children's linguistic profiles per related phonemic-recognition research

### Target Learners
- Children aged 3–7, predominantly bilingual English–Spanish, preschool and early elementary

### Learning Goals
- Science concepts (aerodynamics, reptile molting)
- Observation, prediction, pattern finding, and problem solving

### Claims
- [Ai Interactive Video Science Learning Gain](../claims/ai-interactive-video-science-learning-gain.md) [+M]
- [Contingency Beats Pseudo Interactive Learning](../claims/contingency-beats-pseudo-interactive-learning.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Ying Xu, Kunlei He, Julian Levine, Daniel Ritchie, Zexuan Pan, Andres Bustamante, and Mark Warschauer. (2023). Artificial Intelligence Enhances Children's Science Learning from Television Shows. https://osf.io/j7upd
