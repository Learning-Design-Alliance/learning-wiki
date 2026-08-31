---
type: strategy
title: Chunking to Reduce Working Memory Load
description: Grouping instructional material into meaningful units sized to working memory, so learners hold a few chunks rather than many separate elements.
status: review
generated:
  by: claude/unspecified
  at: 2026-08-30
sources:
  - id: miller-1956
    resource: "https://doi.org/10.1037/h0043158"
    title: "Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81–97"
    author: "Miller, G. A"
  - id: cowan-2001
    resource: "https://doi.org/10.1017/S0140525X01003922"
    title: "Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences, 24*(1), 87–114"
    author: "Cowan, N"
  - id: gobet-2001
    resource: "https://doi.org/10.1191/1478088401pv045ra"
    title: "Gobet, F., Lane, P. C. R., Croker, S., Cheng, P. C.-H., Jones, G., Oliver, I., & Pine, J. M. (2001). Chunking mechanisms in human learning. *Trends in Cognitive Sciences, 5*(6), 236–243"
    author: "Gobet, F. et al."
  - id: sweller-2011
    resource: "https://doi.org/10.1007/978-1-4419-8126-4"
    title: "Sweller, J., Ayres, P., & Kalyuga, S. (2011). *Cognitive Load Theory*. Springer"
    author: "Sweller, J., Ayres, P., & Kalyuga, S"
---

# Chunking to Reduce Working Memory Load

> **Strategy** · [All strategies](index.md)

## Description
Working memory can hold only a small number of discrete items at once — classically estimated at seven plus or minus two [Miller, 1956](https://doi.org/10.1037/h0043158) [+S], with more recent estimates closer to three to five for novel material [Cowan, 2001](https://doi.org/10.1017/S0140525X01003922) [+S]. Chunking recodes individual elements into larger, meaningful units so that a single chunk occupies one slot regardless of how many elements it contains. Because chunks are stored in long-term memory and retrieved as units, chunking effectively expands functional capacity without changing the underlying limit [Gobet et al., 2001](https://doi.org/10.1191/1478088401pv045ra) [+S].

## Design Implications

Chunking is a core mechanism of [Cognitive Load Management](../principles/cognitive-load-management.md) [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [+S]: presenting material in coherent, meaningful groups keeps intrinsic load within working memory limits, whereas unstructured streams of elements overwhelm learners and force premature forgetting [Sweller et al., 2011](https://doi.org/10.1007/978-1-4419-8126-4) [+S]. The effect depends on the chunk being *meaningful* to the learner — arbitrary groupings of unrelated items do not reduce load, because the learner must still hold each element separately.

### Context
#### Requirements
- Content organized around meaningful boundaries (semantic categories, procedural steps, rule-based groupings) rather than arbitrary length limits
- Learners with sufficient prior knowledge to recognize the grouping structure — or explicit instruction in the grouping scheme
- Segmenting of continuous media (video, animation) at natural conceptual boundaries

#### Constraints
- Chunks must map to the learner's existing knowledge; a grouping that is meaningful to an expert may be several independent elements to a novice [~S]
- Over-chunking or chunking at too coarse a grain can obscure the relationships *between* chunks, harming integration of the whole [~M]
- Chunking reduces load but does not eliminate it; if element interactivity is inherently high, additional [Cognitive Load Reduction](../principles/cognitive-load-reduction.md) measures are needed [-W]
- Expertise reversal: highly chunked, segmented presentation becomes redundant and slows learners who have already formed the chunks [~S]

#### Implementation Variability
- **Segmenting** multimedia into learner-paced parts (e.g., Khan Academy videos, [Mayer's segmenting principle](https://doi.org/10.1017/CBO9781139167291))
- **Categorical grouping** of lists or facts into semantic clusters
- **Procedural chunking** of multi-step instructions into sub-goals, as in [Part-Task Practice](../elements/part-task-practice.md)
- **Schema-based chunking** where learners are taught the expert's grouping structure directly

### Target Learners
- Novices, who lack the long-term memory structures to chunk spontaneously and must be given the grouping [Sweller et al., 2011](https://doi.org/10.1007/978-1-4419-8126-4) [+S]
- Learners with low working memory capacity benefit disproportionately from external chunking [~M]
- Experts already chunk automatically; imposed chunking can interfere with their fluent processing [~S]

### Target Learning Goals
- Retention of multi-item factual content (vocabulary, lists, terminology)
- Procedural learning where steps must be held in mind simultaneously
- Schema construction: building larger knowledge units that themselves serve as future chunks

### Instructions
1. **Analyze the material for natural boundaries.** Identify where the content divides on conceptual, procedural, or categorical lines; chunk on those seams rather than on a fixed item count ([Advance Organizers](../elements/advance-organizers.md)).
2. **Size each chunk to novel-element count, not length.** Count how many genuinely new, interacting elements a chunk contains — three to five for unfamiliar material — rather than how many minutes or slides it occupies.
3. **Name the chunk.** Give each unit an explicit label, so the group can be retrieved as one item instead of reconstructed element by element.
4. **Present chunks one at a time.** Segment continuous media and multi-step procedures at the boundaries identified in step 1, and let learners pace the transitions where the medium allows ([Part-Task Practice](../elements/part-task-practice.md)).
5. **Practise within, then across.** Have learners work each chunk to fluency before requiring them to integrate chunks, so integration draws on consolidated units rather than loose elements ([Spaced Repetition](../elements/spaced-repetition.md)).
6. **Make the relationships between chunks explicit.** Once the parts are secure, show how they compose into the whole — chunking that never reassembles leaves learners with fragments.
7. **Fade the chunking as expertise grows.** Withdraw the imposed segmentation once learners chunk the material themselves, since retaining it becomes redundant and slows them down.

## Related Strategies
- [Chunking Content](chunking-content.md) — the same strategy stated in delivery terms: segmenting lessons, videos, and texts into coherent units
- [Segmenting](../strategies/segmenting.md) — chunking applied to continuous media
- [Advance Organizers](../elements/advance-organizers.md) — supply the framework that makes chunks meaningful
- [Spaced Repetition](../elements/spaced-repetition.md) — consolidates chunks into long-term memory so they free working memory capacity

## Examples
- **Phone numbers** are grouped into 3–4 digit segments precisely because ungrouped 10-digit strings exceed working memory capacity.
- **Chess expertise**: master players recall board positions almost perfectly by chunking them into familiar patterns, but show no advantage for randomly arranged pieces — evidence that chunking depends on stored patterns, not raw capacity [Gobet et al., 2001](https://doi.org/10.1191/1478088401pv045ra) [+S].
- **[Khan Academy](https://www.khanacademy.org)** videos are short and single-concept, segmenting instruction so each segment fits within working memory limits.

## Key Sources
- Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81–97. [doi:10.1037/h0043158](https://doi.org/10.1037/h0043158)
- Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences, 24*(1), 87–114. [doi:10.1017/S0140525X01003922](https://doi.org/10.1017/S0140525X01003922)
- Gobet, F., Lane, P. C. R., Croker, S., Cheng, P. C.-H., Jones, G., Oliver, I., & Pine, J. M. (2001). Chunking mechanisms in human learning. *Trends in Cognitive Sciences, 5*(6), 236–243. [doi:10.1007/978-1-4419-1428-6_1731](https://doi.org/10.1007/978-1-4419-1428-6_1731)
- Sweller, J., Ayres, P., & Kalyuga, S. (2011). *Cognitive Load Theory*. Springer. [doi:10.1007/978-1-4419-8126-4](https://doi.org/10.1007/978-1-4419-8126-4)