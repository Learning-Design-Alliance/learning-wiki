---
type: strategy
title: Segmenting
description: Breaking continuous instructional material (especially animation, video, or narration) into learner-paced segments to manage cognitive load.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Segmenting

> **Strategy** · [All strategies](index.md)

## Description
Segmenting divides continuous instructional material — animation, video, narrated slides, complex diagrams — into discrete, meaningful parts that learners can process one at a time, typically with a "continue" button or pause point between parts. It is one of Mayer's multimedia design principles, grounded in the observation that a continuous presentation forces learners to hold and integrate many pieces of information in working memory simultaneously [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+S].

## Design Implications

Segmenting works because working memory is severely limited; when a continuous animation or narration streams past, essential processing on one part competes with representation of the next, and learning suffers [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+S]. Segment boundaries should fall at conceptual breaks — the end of a causal step, a sub-process, or a scene — not at arbitrary time intervals, so that each segment is a coherent unit [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]. Segmenting is most powerful when combined with learner control: letting learners pace their progression through segments allows re-viewing of poorly understood parts and prevents advancing before integration is complete.

### Context
#### Requirements
- Content with identifiable conceptual structure — steps, stages, or sub-processes that can serve as natural segment boundaries
- A pacing mechanism (continue button, pause prompts, chaptered video) rather than a single continuous stream
- Segment-sized units small enough to be processed in one working-memory pass, but not so small that the whole's structure is lost

#### Constraints
- Segmenting material that is already low in element interactivity (simple, familiar content) adds navigation overhead without load benefit [~M]
- Over-fine segmentation can fragment a coherent causal narrative, harming schema formation — learners may see the trees and lose the process
- Learner pacing without guidance invites skipping or shallow re-viewing; segmenting alone does not guarantee active processing [-W]

#### Implementation Variability
- **Hard segmentation**: content is pre-cut into fixed segments with continue buttons (typical in Mayer's experiments)
- **Learner-controlled pausing**: continuous media with explicit prompts to pause and summarize before continuing
- **Segmented with questions**: each segment followed by a short retrieval question, combining pacing with [Practice](../elements/practice.md)
- **Chaptered video**: platforms like YouTube chapters or Coursera's segmented lecture videos apply the same principle at course scale

### Target Learners
- Novices with low prior knowledge, who lack schemas to hold incoming material efficiently [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+S]
- Learners with lower working memory capacity, who benefit most from externally imposed pacing
- Less beneficial for experts, who can self-pace mentally and may find forced pauses disruptive [~W]

### Target Learning Goals
- Understanding dynamic, multi-step processes (mechanical, biological, computational)
- Transfer of procedural knowledge explained through animation or narrated demonstration
- Retention of complex narrated explanations where integration across moments in time is required

### Instructions
1. Map the content's conceptual structure and mark natural boundaries — one step, stage, or sub-process per segment ([Chunking](../principles/chunking.md))
2. Produce or re-cut the media so each segment is a self-contained unit, ending at a completion point rather than mid-explanation
3. Add a pacing control (continue button, pause prompt) so learners decide when to advance
4. Optionally append a brief question or summary prompt after each segment to enforce active processing ([Practice](../elements/practice.md))
5. Check that the full sequence still communicates the whole process — add an advance organizer or overview if segmentation obscures global structure ([Advance Organizers](../elements/advance-organizers.md))

## Related Strategies
- [Pre-training](pre-training.md) — teaching names and characteristics of key concepts before the segmented presentation reduces load further; the two principles are complementary
- [Signaling](signaling.md) — cues highlight what matters *within* each segment; segmenting manages load *between* segments
- [Modality](modality.md) — narrating segments offloads visual working memory; frequently combined with segmenting in multimedia design

## Examples
- **Mayer & Chandler (2001)** — the canonical experiment: a lightning-formation animation split into user-paced segments produced substantially better transfer than the continuous version.
- **[Khan Academy](https://www.khanacademy.org)** — short, single-concept videos (typically under 10 minutes) rather than full lectures; each video is effectively one segment in a paced sequence.
- **[Coursera](https://www.coursera.org)** — lecture videos broken into 5–10 minute segments with in-video quiz prompts at segment boundaries.
- **PhET simulations** ([https://phet.colorado.edu](https://phet.colorado.edu)) — complex phenomena explored through discrete, learner-paced manipulations rather than a continuous animation.

## Key Sources
- Mayer, R. E., & Chandler, P. (2001). When learning is just a click away: Does simple user interaction foster deeper understanding of multimedia messages? *Journal of Educational Psychology, 93*(2), 390–397. [doi:10.1037/0022-0663.93.2.390](https://doi.org/10.1037/0022-0663.93.2.390)
- Mayer, R. E. (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Moreno, R. (2007). Optimizing learning from animations by minimizing cognitive load: Cognitive and affective consequences of spacing and segmentation strategies. *Journal of Educational Psychology, 99*(2), 265–277. [doi:10.1002/acp.1348](https://doi.org/10.1002/acp.1348)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)