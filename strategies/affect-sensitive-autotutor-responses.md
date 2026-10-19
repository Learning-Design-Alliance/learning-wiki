---
type: strategy
id: affect-sensitive-autotutor-responses
title: "Adapt tutor responses to detected learner affect: leading hints for frustration, engaging hooks for boredom, and timed intervention for confusion"
description: The authors propose programming AutoTutor to respond appropriately to affective states exhibited by learners, on the expectation that learning improves when the tutor adapts to confusion, frustration, and boredom in a...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
sources:
  - id: scotty-d-craig-2008
    resource: "https://doi.org/10.1080/02699930701516759"
    title: "Scotty D. Craig, Sidney D'Mello, Amy Witherspoon, and Art Graesser. (2008). Emote aloud during learning with AutoTutor: Applying the Facial Action Coding System to cognitive/affective states during learning. Cognition and Emotion, 22(5), 777-788. https://doi.org/10.1080/02699930701516759"
    author: "Scotty D. Craig, Sidney D'Mello, Amy Witherspoon, and Art Graesser"
---

# Adapt tutor responses to detected learner affect: leading hints for frustration, engaging hooks for boredom, and timed intervention for confusion

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (2 for, 2 against) · 2 studies (1 associational, 1 theoretical), `q1`–`q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The authors propose programming AutoTutor to respond appropriately to affective states exhibited by learners, on the expectation that learning improves when the tutor adapts to confusion, frustration, and boredom in addition to cognitive states. The article specifies concrete responses: "If the learner is frustrated, then AutoTutor should give a leading hint to put the student back on track. If the learner is bored, some engaging hooks are needed." For confusion, the authors flag an open pedagogical question about how long a student should remain confused and thinking deeply before the tutor intervenes.

## Design Implications

### Context
#### Requirements
- Automatic detection of the learner's affective states, e.g. via non-intrusive sensing of dialogue history logs, facial expressions, posture, and speech intonation
#### Constraints
- The appropriate intervention timing for confusion is an open question the article does not resolve

### Target Learners
- college students learning with AutoTutor

### Target Learning Goals
- computer literacy learning supported by adaptive affect-sensitive tutoring

## Claims

- [Confusion during learning is associated with facial action units 4, 7, and 12, with tightened lids tending to trigger a lowered brow](../claims/confusion-facial-action-units-4-7-12.md) [+W]
- [The emote-aloud procedure is limited by non-reporting and floor effects: 2 of 7 participants did not verbalise affective states and four states were removed from analysis](../claims/emote-aloud-floor-effects-limitation.md) [-W]
- [Frustration during learning is associated with facial action units 1, 2, and 14, with a mutual trigger rule between the inner and outer brow raises](../claims/frustration-facial-action-units-1-2-14.md) [+W]
- [Generalizable detectors of students' affective states in DLPs remain an unsolved problem](../claims/no-generalizable-affective-detectors.md) [-W]

## Related Strategies

- [Affect-aware CPS systems should monitor local trajectories of confusion and disengagement over time rather than responding to isolated affective signals](monitor-local-affect-trajectories-in-cps-systems.md)

## Examples
-

## Key Sources
- Scotty D. Craig, Sidney D'Mello, Amy Witherspoon, and Art Graesser. (2008). Emote aloud during learning with AutoTutor: Applying the Facial Action Coding System to cognitive/affective states during learning. Cognition and Emotion, 22(5), 777-788. https://doi.org/10.1080/02699930701516759
