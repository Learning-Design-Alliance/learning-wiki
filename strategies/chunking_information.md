---
type: strategy
title: Chunking Information
description: Organize content into small, meaningful units so each fits within working memory limits before being consolidated into larger schemas.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Chunking Information

## Description
Chunking organizes content into small, meaningful units — each small enough to be processed as a single item in working memory — and sequences those units so learners can consolidate them into larger schemas before the next load arrives. It is carried out by segmenting text, video, diagrams, or instruction into coherent parts, labeling each part, and ordering them from simple to complex.

## Design Implications

Working memory can hold only a handful of meaningful units at once; chunking respects that limit by ensuring each instructional step presents one coherent unit rather than an undifferentiated stream [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]. The unit of chunking should be *meaningful*, not merely small — a chunk is a familiar pattern that can be retrieved as one item, so labels, headings, and advance organizers help learners perceive the boundaries [Miller, 1956](https://doi.org/10.1037/h0043158) [+S]. Segmentation works best when learners control pacing, since consolidation time varies widely across individuals [Mayer, 2009](https://doi.org/10.1017/CBO9780511811678) [+M].

### Context
#### Requirements
- Analysis of the content to identify natural conceptual boundaries (steps, sub-procedures, causal episodes)
- Explicit labels or headings that mark each chunk so learners can encode it as a unit
- Sequencing that builds each new chunk on previously consolidated ones ([Advance Organizers](../elements/advance-organizers.md))
- Learner pacing control for segmented media (pause, replay, next)

#### Constraints
- Over-fragmentation destroys the coherence learners need; micro-chunks that break causal or procedural connections force learners to re-integrate the pieces themselves, adding extraneous load [~M]
- Chunk boundaries that don't match the learner's prior knowledge produce arbitrary segments — novices and experts carve up material differently [Gobet et al., 2001](https://doi.org/10.1016/S1364-6613(00)01662-4) [~M]
- For learners with high prior knowledge, heavy segmentation is redundant and slows them down (expertise reversal) [~M]
- Chunking presentation alone does not guarantee encoding; without [Practice](../elements/practice.md) or [Self-Explanation](../claims/self-explanation-improves-conceptual-understanding.md) [+S], chunks remain isolated facts

#### Implementation Variability
- **Segmented video**: short segments with interactive continuation prompts rather than one continuous lecture
- **Progressive disclosure**: reveal text or diagram sections on demand, keeping unattended content out of view
- **Hierarchical outlines**: present a top-level map, then expand each branch ([Advance Organizers](../elements/advance-organizers.md))
- **Part-task sequencing**: teach sub-skills in isolation before integrating them into whole-task performance

### Target Learners
- Novices, whose limited domain schemas mean raw material arrives as many unrelated items [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]
- Learners in high-element-interactivity domains (statistics, programming, anatomy) where unchunked material overwhelms working memory [Sweller, 1988](https://doi.org/10.1207/s15516709cog1202_4) [+S]
- Less beneficial for experts, who already perceive large chunks and may be slowed by segmentation [~M]

### Target Learning Goals
- Procedural skill acquisition: sequencing sub-steps of a complex procedure
- Schema formation: building hierarchical knowledge structures from parts
- Retention of structured factual content (vocabulary, anatomy, historical sequences)

### Instructions
1. Analyze the material to find natural boundaries — steps, sub-concepts, or causal episodes — and decide the smallest meaningful unit.
2. Label each chunk with a heading or caption so learners encode it as a single retrievable unit ([Clear Structure & Presentation](../principles/clear-structure-presentation.md)).
3. Sequence chunks from simple to complex, ensuring each builds on consolidated prior chunks ([Cognitive Load Management](../principles/cognitive-load-management.md)).
4. Present one chunk at a time; hide or withhold upcoming material until the learner is ready (progressive disclosure or segmented media).
5. Give learners pacing control — pause, replay, or "continue" — so consolidation can complete before new load arrives.
6. Follow each chunk or chunk group with retrieval or application ([Practice](../elements/practice.md)) so chunks integrate into schemas rather than staying isolated.

## Related Strategies
- [Segmenting](segmenting.md) — the multimedia-learning variant: breaking continuous animation or narration into learner-paced segments
- [Spaced Repetition](../elements/spaced-repetition.md) — distributes chunk consolidation over time rather than within a session
- [Advance Organizers](../elements/advance-organizers.md) — supplies the top-level structure into which chunks are placed

## Examples
- **Khan Academy** (https://www.khanacademy.org) — math videos are segmented into short single-concept units, each followed by practice items keyed to that unit.
- **Duolingo** (https://www.duolingo.com) — language content is broken into small lesson chunks (a handful of vocabulary items and one grammar pattern per lesson), sequenced so each chunk reuses prior ones.
- **Anatomy textbooks using regional hierarchy** — presenting the brachial plexus as roots → trunks → divisions → cords → branches, one level per figure, rather than as a single diagram.

## Key Sources
- Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81–97. [doi:10.1037/h0043158](https://doi.org/10.1037/h0043158)
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285. [doi:10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4)
- Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences, 24*(1), 87–114. [doi:10.1017/S0140525X01003922](https://doi.org/10.1017/S0140525X01003922)
- Gobet, F., Lane, P. C. R., Croker, S., Cheng, P. C.-H., Jones, G., Oliver, I., & Pine, J. M. (2001). Chunking mechanisms in human learning. *Trends in Cognitive Sciences, 5*(6), 236–243. [doi:10.1007/978-1-4419-1428-6_1731)01662-4](https://doi.org/10.1007/978-1-4419-1428-6_1731)01662-4)
- Mayer, R. E. (2009). *Multimedia Learning* (2nd ed.). Cambridge University Press. [doi:10.1017/CBO9780511811678](https://doi.org/10.1017/CBO9780511811678)