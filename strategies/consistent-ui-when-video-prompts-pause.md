---
type: strategy
id: consistent-ui-when-video-prompts-pause
title: Keep the video player user interface consistent when pausing for self-explanation prompts to avoid extraneous reorientation
description: "The discussion identifies a design contributor to extraneous load: prompts changed the screen layout, presenting video in a smaller frame beside a question-and-answer area and then restoring full screen after answering."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-18
sources:
  - id: beege-2025
    resource: "https://doi.org/10.1007/s11251-024-09693-5"
    title: "Beege, M., & Ploetzner, R. (2025). Learning from interactive video: the influence of self-explanations, navigation, and cognitive load. Instructional Science. https://doi.org/10.1007/s11251-024-09693-5"
    author: "Beege, M., & Ploetzner, R"
---

# Keep the video player user interface consistent when pausing for self-explanation prompts to avoid extraneous reorientation

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The discussion identifies a design contributor to extraneous load: prompts changed the screen layout, presenting video in a smaller frame beside a question-and-answer area and then restoring full screen after answering. The article states "A consistent user interface could help to keep extraneous load low." Implementers of in-video prompts should therefore avoid layout switches between watching and answering phases, keeping the video presentation stable while prompts are open.

## Design Implications

### Context
#### Requirements
- Self-explanation prompts that pause or overlay the video should preserve the learner's visual frame of reference across the prompt interaction
#### Constraints
- The recommendation addresses perceived extraneous load under this article's specific screen-design change and interrupts the flow of information regardless

### Target Learners
- novice learners watching instructional videos with embedded prompts

### Target Learning Goals
- minimizing extraneous cognitive load during prompted video learning

## Claims

- [Self-explanation prompts increase intrinsic and extraneous cognitive load but not germane load in instructional video learning](../claims/self-explanation-prompts-increase-intrinsic-extraneous-load.md) [+M]
- [Self-explanation prompts in an instructional video do not improve retention or comprehension when learning time is controlled](../claims/self-explanation-prompts-no-learning-benefit-controlled-time.md) [~M]

## Related Strategies

- [Predictability: Environment & Structure](predictability-environment-structure.md)
- [Reducing Distractions](reducing-distractions.md)
- [Reducing Visual Clutter](reducing_visual_clutter.md)

## Examples
-

## Key Sources
- Beege, M., & Ploetzner, R. (2025). Learning from interactive video: the influence of self-explanations, navigation, and cognitive load. Instructional Science. https://doi.org/10.1007/s11251-024-09693-5
