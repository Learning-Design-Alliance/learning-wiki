---
type: element
title: Pedagogical Agent Signaling for Feedback Salience
description: An embodied on-screen agent that points and gazes directly at feedback text when it appears, using social cueing rather than a generic arrow to pull elementary students' attention to feedback they would otherwise skip.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
sources:
  - id: tarning-et-al-2020
    resource: "https://doi.org/10.1080/10508406.2020.1770092"
    title: "Tärning, B., Lee, Y. J., Andersson, R., Månsson, K., Gulz, A., & Haake, M. (2020). Assessing the black box of feedback neglect in a digital educational game for elementary school. Journal of the Learning Sciences, 29(4-5), 511-549."
    author: "Tärning, B., Lee, Y. J., Andersson, R., Månsson, K., Gulz, A., & Haake, M."
---

# Pedagogical Agent Signaling for Feedback Salience

## Description
An embodied pedagogical agent already central to the learning task (e.g., a teachable agent whose in-game success depends on the student's help) turns to face and points at a feedback text box the moment it appears, using gaze and gesture rather than a purely directional cue like an animated arrow. The mechanism is social: gaze and pointing recruit reflexive joint-attention responses and load the pointed-at content with the implicit message "this matters," in a way a non-social directional cue does not.

## Design Implications

### Context
#### Requirements
- An embodied agent already integrated into the task in a socially meaningful role (e.g., a teachable agent), not a cosmetic add-on
- Feedback text that appears at a fixed, predictable location the agent can reliably gaze/point toward
#### Constraints
- The effect is confined to the noticing and reading stages of feedback processing — see [Critical Constructive Feedback Processing](../theories/critical-constructive-feedback-processing.md); it does not, by itself, increase whether students act on feedback or improve as a result
- A generic directional cue (e.g., an arrow) does not reproduce the effect — the benefit appears to depend on the social cues (gaze, gesture) an embodied agent provides, not on directionality alone

### Target Learners
- Elementary-age students in digital learning environments who are not otherwise inclined to notice or read constructive feedback

### Target Learning Goals
- Increasing the proportion of feedback instances that are noticed and read, as a precondition for feedback to have any effect on learning

### Affordances
- [Critical Constructive Feedback Processing](../theories/critical-constructive-feedback-processing.md)

## Related Elements
- [Feedback](feedback.md)
- [Immediate Feedback](immediate-feedback.md)

## Examples
- A digital history game ("Guardian of History") in which a teachable agent named Timy points and gazes at feedback text after a student's wrong answer, tested against an arrow-signaling condition and a no-signaling control.

## Key Sources
- Tärning, B., Lee, Y. J., Andersson, R., Månsson, K., Gulz, A., & Haake, M. (2020). Assessing the black box of feedback neglect in a digital educational game for elementary school. *Journal of the Learning Sciences, 29*(4-5), 511-549. [https://doi.org/10.1080/10508406.2020.1770092](https://doi.org/10.1080/10508406.2020.1770092)
