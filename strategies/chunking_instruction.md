---
type: strategy
id: chunking_instruction
title: Chunking Instruction
description: Breaking instructional content into small, coherent units that each fit within working memory limits before being integrated into larger wholes.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Chunking Instruction

> **Strategy** · [All strategies](index.md)

## Description
Chunking instruction means dividing content into small, self-contained units — a concept, step, rule, or example — sized so that each can be processed in working memory before moving on. Units are sequenced so that each new chunk builds on previously consolidated ones, and learners are given time or practice to consolidate each chunk before the load accumulates. The strategy treats segmenting, sequencing, and pacing as primary design decisions rather than afterthoughts.

## Design Implications

Working memory can hold only a few novel elements at once; instruction that presents more than this in a single pass overloads the learner and degrades learning [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+S]. Chunking works by keeping each instructional segment within these limits and by grouping related elements so they are encoded as single units [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]. As expertise grows, learners can handle larger chunks, so segment size should scale with prior knowledge rather than staying fixed [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M].

### Context
#### Requirements
- A task or content analysis that identifies the natural conceptual units and their dependencies
- A sequence ordered so prerequisite chunks precede dependent ones ([Clear Structure](../principles/clear-structure.md))
- A consolidation activity after each chunk — a check, brief [Practice](../elements/practice.md), or recall prompt — before introducing the next
- Meaningful grouping: chunks must be coherent units, not arbitrary slices of a continuous stream

#### Constraints
- Over-segmentation fragments the material and destroys the relational structure learners need; learners who must mentally reassemble many tiny pieces lose the overview [-M]
- Chunks that cut across natural conceptual boundaries (e.g., splitting a worked example mid-step) increase, rather than reduce, load [~M]
- For learners with high prior knowledge, small chunks with heavy scaffolding feel slow and redundant and can depress performance [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [-M]
- Chunking alone does not create understanding; isolated chunks without integration activities produce fragmented knowledge [-M]

#### Implementation Variability
- **Segmented video**: short videos with interactive controls that stop between segments (Mayer's segmenting principle)
- **Step-sequenced tasks**: complex tasks introduced as progressively more complete wholes, as in [4C/ID](../patterns/4cid-four-component-instructional-design.md)
- **Microlearning**: standalone small units (e.g., Duolingo lessons), which trade integration for scheduling flexibility
- **Learner pacing**: giving learners a "continue" control rather than fixing segment boundaries externally [~M]

### Target Learners
- Novices, who lack the schemas needed to compress large amounts of novel information [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]
- Learners with limited working memory capacity or high element interactivity material (e.g., statistics, chemistry, programming)
- Less beneficial for experts, for whom fine-grained segmentation adds redundant processing [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Procedural skill acquisition: learning multi-step processes one stage at a time
- Conceptual understanding of high-element-interactivity material
- Retention and schema formation, since consolidated chunks are the raw material for larger schemas

### Instructions
1. Analyze the content to identify its constituent concepts, steps, or rules and their prerequisite relationships.
2. Group elements into coherent chunks that can each be explained and practiced within a single short segment.
3. Order chunks so each depends only on chunks already taught ([Clear Structure](../principles/clear-structure.md)).
4. Present each chunk with an advance organizer showing where it fits in the whole ([Advance Organizers](../elements/advance-organizers.md)).
5. Follow each chunk with immediate consolidation — practice, self-explanation, or a check ([Practice](../elements/practice.md)).
6. Increase chunk size and reduce support as learners gain expertise, merging chunks into larger wholes ([Fading](../elements/fading.md)).

## Related Strategies
- [Segmenting](segmenting.md) — the multimedia-learning counterpart: letting learners control pacing across segments
- [Spiral Curriculum](../elements/spiral-curriculum.md) — revisits chunks over time to build integration and retention
- [Mastery Learning](mastery-learning.md) — gates progression on consolidation of each chunk

## Examples
- **Khan Academy** (https://www.khanacademy.org) — lessons split into short videos and practice sets, each covering one concept, with mastery checks gating progression to the next chunk.
- **Duolingo** (https://www.duolingo.com) — language content broken into small lesson units of a few items each, sequenced by prerequisite structure.
- **4C/ID in medical education** — complex clinical procedures taught as sequenced learning tasks of increasing whole-task complexity rather than presented all at once.

## Key Sources
- Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81–97. [doi:10.1037/h0043158](https://doi.org/10.1037/h0043158)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251–296. [doi:10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
- Mayer, R. E. (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)