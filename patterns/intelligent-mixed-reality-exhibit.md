---
type: pattern
id: intelligent-mixed-reality-exhibit
title: Intelligent Mixed-Reality Exhibit
description: A free-choice, hands-on exhibit augmented with computer-vision sensing and an animated character that runs a predict-observe-explain cycle over contrasting physical cases, then fades guidance into open-ended construction.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
author: Yannier, N., Crowley, K., Do, Y., Hudson, S. E., & Koedinger, K. R.
grain_size: unit
sources:
  - id: yannier-et-al-2022
    resource: "https://doi.org/10.1080/10508406.2022.2032071"
    title: "Yannier, N., Crowley, K., Do, Y., Hudson, S. E., & Koedinger, K. R. (2022). Intelligent science exhibits: Transforming hands-on exhibits into mixed-reality learning experiences. Journal of the Learning Sciences, 31(3), 335-368."
    author: "Yannier, N., Crowley, K., Do, Y., Hudson, S. E., & Koedinger, K. R."
---

# Intelligent Mixed-Reality Exhibit

> **Pattern** · [All patterns](index.md)

## Description
An informal-learning exhibit combines a tangible physical interface (an earthquake table and building blocks, in the source study) with a depth camera and vision algorithm that detects the learner's physical actions — where blocks are placed, whether and how a tower falls — and an animated on-screen character that runs a predict-observe-explain cycle in response: the learner predicts an outcome, the system runs the physical event, and a curated menu of explanations (not free-form text) prompts the learner to explain what happened, with immediate confirmation or correction. The system presents a sequence of physically contrasting cases that each isolate one physics principle (height, symmetry, base width, or center of mass) before shifting to an open "test my tower" mode where the learner builds freely and the system only reports pass/fail — guidance fades as the learner gains agency. This differs from a classroom intelligent tutoring system chiefly in setting and stakes: it operates in a self-paced, optional, free-choice museum context, embeds the "problem" in tangible physical construction rather than a screen-only or symbolic task, and uses intrinsic play (an animated gorilla character, a physical build) rather than grades to sustain engagement.

## Implications

### Context
#### Requirements
- A physical, hands-on task with an outcome that can be reliably sensed by computer vision (in the source study, a moment-of-inertia signature at tower-fall, robust to lighting changes)
- A curated menu of plausible explanations to choose from, rather than open-ended text input, so the system can give immediate, accurate feedback
- A sequence of case pairs, each engineered to differ on exactly one physics principle, so the contrast — not just the outcome — carries the instructional content
#### Constraints
- Requires nontrivial engineering investment (custom computer-vision detection, a curated case library, an authored feedback/character layer) — not a low-cost retrofit of an existing static exhibit
- Demonstrated for a specific physical-mechanics domain (structural stability); transfer to less physically-sensable domains is untested
#### Grain Size
Unit (a single self-paced museum session, roughly 15 minutes in the source study)

### Target Goals
- [AI-mediated feedback in hands-on exhibits improves learning and engagement](../claims/ai-mediated-feedback-in-hands-on-exhibits-improves-learning-and-engagement.md)

### Target Learners
- Museum visitors and other free-choice, informal learners, studied here with elementary-school-aged children (median grade 2)

### Theory
#### Supporting
- Intelligent tutoring systems — AI-mediated, contingent feedback during exploration
- Predict-observe-explain (White & Gunstone, 1992)
- Contrasting cases / perceptual learning (Gibson & Gibson, 1955) — paired cases differing on one dimension sharpen what learners notice
- Guided discovery (de Jong & Lazonder, 2014) — structure and prompts guide exploration without eliminating the learner's own cognitive effort

### Claims
#### Supporting
- [AI-mediated feedback in hands-on exhibits improves learning and engagement](../claims/ai-mediated-feedback-in-hands-on-exhibits-improves-learning-and-engagement.md) [+S]

## Design

### Sequence
1. **Guided-discovery mode begins**: the system selects a pair of towers that contrast on exactly one stability principle.
2. **Predict**: "Which tower will fall first?" — learner predicts before the physical event runs.
3. **Observe**: the earthquake table shakes; the system's vision algorithm detects the fall outcome.
4. **Explain**: the system prompts "Why did this tower fall?" with a fixed menu of physics-principle options (e.g., "it's taller," "it has a thinner base," "it has more weight on top than bottom," "it's not symmetrical"); the learner selects one and the animated character confirms or corrects it, with an emotionally expressive response (celebratory for success, surprised for error).
5. **Repeat** across a sequence of contrasting pairs covering the full set of stability principles.
6. **Fade to open exploration**: the learner enters "test my tower" mode, building any tower and testing it on the shaking table; the system now gives only pass/fail feedback, withdrawing the guided prediction/explanation scaffold as the learner exercises independent construction and troubleshooting.

### Affordances
- [Immediate Feedback](../elements/immediate-feedback.md)
- [Guided Discovery](../elements/guided-discovery.md)
- [Comparing Cases](../elements/comparing-cases.md)

### Personalization
- (not addressed in the source study — no adaptive difficulty or individual-differences variation was tested)

## Related Patterns
- (none yet linked)

## Examples
- A museum "leaning tower" exhibit pairing an earthquake table with wooden/Lego/magnetic building blocks and an animated gorilla character, tested against an unfacilitated version of the same physical materials with only static signage.

## Key Sources
- Yannier, N., Crowley, K., Do, Y., Hudson, S. E., & Koedinger, K. R. (2022). Intelligent science exhibits: Transforming hands-on exhibits into mixed-reality learning experiences. *Journal of the Learning Sciences, 31*(3), 335-368. [https://doi.org/10.1080/10508406.2022.2032071](https://doi.org/10.1080/10508406.2022.2032071)
- White, R., & Gunstone, R. (1992). *Probing Understanding*. Falmer Press.
- de Jong, T., & Lazonder, A. W. (2014). The guided discovery learning principle. In R. E. Mayer (Ed.), *The Cambridge Handbook of Multimedia Learning*.
