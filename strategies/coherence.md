---
type: strategy
id: coherence
title: Coherence
description: Removing extraneous words, images, sounds, and decorative material from instruction so that working memory is spent on the essential content.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Coherence

> **Strategy** · [All strategies](index.md)

## Description
Coherence is the design strategy of excluding material that is interesting but irrelevant to the learning goal — decorative images, background music, seductive details, tangential anecdotes, and verbose text. It is carried out by auditing instructional materials and cutting anything that does not support the stated objective, then structuring what remains around the core content.

## Design Implications

Coherence directly counters the well-replicated finding that interesting-but-irrelevant material consumes working memory and diverts attention from essential content, degrading learning [Irrelevant seductive details and decorative media hurt learning outcomes.](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [+S]. The underlying mechanism is capacity limitation: when extraneous material occupies attention and working memory, less capacity remains for building a mental model of the target content [Overload of working memory degrades learning outcomes.](../claims/cognitive-overload-degrades-learning.md) [+S]. Designers should resist the intuition that adding interesting material increases engagement and learning; the evidence consistently favors leaner presentations.

### Context
#### Requirements
- Explicit learning objectives against which every content element can be judged
- A draft or existing material set to audit for extraneous elements
- Willingness to cut "engaging" content that does not serve the objective ([Clear Structure](../principles/clear-structure-presentation.md))

#### Constraints
- Over-trimming can strip materials of motivating context for learners who lack the background to see why content matters [~M] — coherence must be balanced against [Activation](../principles/activation.md) of prior knowledge and relevance framing
- Seductive details hurt novices most but can be less harmful — occasionally even useful for elaboration — for learners with high prior knowledge [~M]
- Removing all narrative and imagery can produce dry materials that learners disengage from voluntarily, particularly in self-paced settings [-W]

#### Implementation Variability
- **Text:** delete tangential sentences and interesting-but-off-topic anecdotes; shorten verbose passages to essential wording
- **Graphics:** remove decorative images that do not support the explanation; keep graphics that clarify structure
- **Audio/video:** eliminate background music and environmental sounds; cut filler narration
- **Signaling alternative:** where extraneous material cannot be removed, use emphasis and cueing to direct attention to essentials

### Target Learners
- Novices, who lack the prior knowledge to filter out irrelevant material efficiently [Irrelevant seductive details and decorative media hurt learning outcomes.](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [+S]
- Learners with limited working memory capacity or high element interactivity in the domain [Overload of working memory degrades learning outcomes.](../claims/cognitive-overload-degrades-learning.md) [+S]
- Less critical for experts, who can ignore extraneous material — and may find stripped-down materials unengaging [~M]

### Target Learning Goals
- Retention and understanding of explanatory content (science, history, procedures)
- Transfer of principles to new problems, which seductive details particularly disrupt
- Efficient learning under time constraints

### Instructions
1. State the learning objective and identify the essential content ([Clear Structure](../principles/clear-structure-presentation.md)).
2. Audit each text passage, image, sound, and anecdote: does it directly support the objective? If not, cut it.
3. Replace decorative graphics with explanatory ones ([Multimedia](../principles/cognitive-load-management.md)).
4. Shorten verbose text to concise, essential wording; break what remains into digestible units ([Chunking](../principles/chunking.md)).
5. Pilot with novices and check whether any cut material was actually load-bearing for understanding; restore only what proves necessary.

## Related Strategies
- [Signaling](signaling.md) — the complementary strategy: instead of removing material, cue attention to what matters
- [Segmenting](segmenting.md) — pacing content in learner-controlled pieces to manage load
- [Seductive Details Removal](seductive-details-removal.md) — the specific case of cutting interesting-but-irrelevant text

## Examples
- **Mayer's multimedia lessons** — In controlled experiments, versions of a lightning-formation and brakes lesson with added music, decorative video, and expanded text produced worse retention and transfer than the lean versions ([Mayer, 2021](https://doi.org/10.1017/9781316941355)).
- **Textbook revision** — Replacing an anecdote-laden biology passage with a concise causal explanation of the same process, keeping one illustrative example tied directly to the mechanism.
- **Corporate e-learning** — Removing stock photography and background music from compliance modules; narration restated on-screen text is also cut rather than duplicated.

## Key Sources
- Mayer, R. E. (2021). *Multimedia learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Mayer, R. E., Heiser, J., & Lonn, S. (2001). Cognitive constraints on multimedia learning: When presenting more material results in less understanding. *Journal of Educational Psychology, 93*(1), 187–198. [doi:10.1037/0022-0663.93.1.187](https://doi.org/10.1037/0022-0663.93.1.187)
- Garner, R., Gillingham, M. G., & White, C. S. (1989). Effects of "seductive details" on macroprocessing and microprocessing in adults and children. *Cognition and Instruction, 6*(1), 41–57. [doi:10.1207/s1532690xci0601_2](https://doi.org/10.1207/s1532690xci0601_2)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)