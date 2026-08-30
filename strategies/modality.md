---
type: strategy
title: Modality
description: Presenting words as spoken narration rather than on-screen text when accompanying graphics, to balance verbal and visual channels of working memory.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Modality

## Description
The modality strategy presents verbal information as spoken audio (narration) rather than written on-screen text when the same screen also displays graphics, animation, or video. It is grounded in the assumption that working memory has partially separate visual and auditory channels; distributing words and pictures across these channels increases effective capacity [Cognitive overload degrades learning when channels are overloaded.](../claims/cognitive-overload-degrades-learning.md) [+S].

## Design Implications

When learners must read text and simultaneously view an animation, both compete for the visual channel; converting the text to narration frees visual resources for the graphic [Pairing graphics with spoken narration improves learning over graphics with on-screen text.](../claims/modality-principle-spoken-narration-beats-on-screen-text.md) [+S]. This is one of the most consistently supported effects in multimedia learning research, with meta-analytic support across lab and classroom studies [Ginns, 2005]. The strategy is a core application of [Cognitive Load Management](../principles/cognitive-load-management.md) within [Cognitive Load Theory](../theories/cognitive-load-theory.md) and Mayer's Cognitive Theory of Multimedia Learning.

### Context
#### Requirements
- A graphic, animation, or video that carries essential content
- Narration that is concise and conversational, synchronized with the visual
- Audio quality and playback control (pause, replay) so learners can manage pacing

#### Constraints
- Ineffective when the graphic is static and the learner can self-pace; reading text next to a still image imposes little channel competition [~S]
- Narration is transient — if the material is complex or unfamiliar, spoken-only presentation can overload auditory memory, and adding redundant on-screen text or allowing learner pacing helps [~M]
- Fails when learners cannot hear well, are in noisy environments, or lack the language proficiency to follow fast speech; on-screen text is then the accessible option [-M]
- Not applicable when the words are instructions to be referenced repeatedly (e.g., a checklist), where persistence matters more than channel balance

#### Implementation Variability
- Narrated animation (classic case): voice-over explains an animated process
- Agent-delivered narration: on-screen pedagogical agent speaks the explanation; benefits come from the audio, not the agent's presence [Coherence principle — irrelevant material hurts learning.](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [+M]
- Audio-plus-persistent-keywords: narration supplemented by minimal on-screen labels for terms that must be retained
- Learner-paced audio: segmenting the narration into user-controlled chunks mitigates transience [Segmenting reduces overload for complex multimedia.](../claims/segmenting-principle-improves-multimedia-learning.md) [+M]

### Target Learners
- Novices with low prior knowledge, who lack schemas to compensate for split attention [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — the modality effect shrinks or reverses for experts
- Learners with adequate listening comprehension and hearing ability in the language of instruction
- Not suited as a sole format for deaf or hard-of-hearing learners; captions or text alternatives are required ([Accommodations](../elements/accommodations.md))

### Target Learning Goals
- Understanding dynamic processes and causal systems explained alongside animation or video
- Reducing extraneous load during complex multimedia explanations
- Retention of verbal material integrated with visual representations ([Dual Coding Theory](../theories/dual-coding-theory.md))

### Instructions
1. Identify the essential graphic or animation and the words that explain it.
2. Convert explanatory text to concise, conversational narration; avoid verbatim duplication of on-screen text (redundancy harms learning) [Redundant on-screen text with narration hurts learning.](../claims/redundancy-principle-hurts-learning.md) [+S].
3. Synchronize narration with the corresponding visual events.
4. Segment the presentation so learners can pause or replay ([Chunking](../principles/chunking.md)).
5. Provide captions or a transcript for accessibility and noisy contexts.
6. For static, self-paced content, prefer text-and-graphics layout over forced audio.

## Related Strategies
- [Segmenting](../strategies/segmenting.md) — controls pacing of transient narration
- [Redundancy Avoidance](../strategies/redundancy-avoidance.md) — the complementary rule: don't duplicate narration as on-screen text
- [Signaling](../strategies/signaling.md) — directs attention within the narrated visual
- [Coherence](../strategies/coherence.md) — removes extraneous material that competes for the freed channel

## Examples
- **[Khan Academy](https://www.khanacademy.org)** — narrated problem-solving videos with handwritten-style visuals; words are spoken, not displayed as paragraphs.
- **[PhET Interactive Simulations](https://phet.colorado.edu)** — simulations paired with spoken guidance in guided activities, keeping the visual channel focused on the simulation itself.
- **Anatomy and physiology courses using narrated animation** — e.g., narrated cardiac-cycle animations replacing text-heavy slides, the canonical setting for modality-effect experiments (Mayer & Moreno, 1998).

## Key Sources
- Mayer, R. E., & Moreno, R. (1998). A split-attention effect in multimedia learning: Evidence for dual processing systems in working memory. *Journal of Educational Psychology, 90*(2), 312–320. [doi:10.1037/0022-0663.90.2.312](https://doi.org/10.1037/0022-0663.90.2.312)
- Ginns, P. (2005). Meta-analysis of the modality effect. *Learning and Instruction, 15*(4), 313–331. [doi:10.1016/j.learninstruc.2005.07.001](https://doi.org/10.1016/j.learninstruc.2005.07.001)
- Mayer, R. E. (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Moreno, R., & Mayer, R. E. (1999). Cognitive principles of multimedia learning: The role of modality and contiguity. *Journal of Educational Psychology, 91*(2), 358–368. [doi:10.1037/0022-0663.91.2.358](https://doi.org/10.1037/0022-0663.91.2.358)