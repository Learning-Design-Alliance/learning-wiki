---
type: element
id: activation
title: Activation
description: Learners are encouraged to recall and activate prior knowledge to prepare for new learning.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Activation

> **Element** · [All elements](index.md)

## Description
Activation prompts learners to retrieve and make explicit what they already know before encountering new material. It functions as a bridge: existing knowledge structures provide the slots into which new information must be organized, so learning that begins with activation is faster and more coherent than learning that begins cold.

## Design Implications

Activation works because new knowledge is encoded in terms of what is already known — learners given a relevant schema before a passage comprehend and recall far more than those given the identical passage without it [Bransford & Johnson's context studies.](https://doi.org/10.1016/S0022-5371(72)80011-8) [+S]. Effective activation is specific and generative: asking learners to retrieve, predict, or map prior knowledge outperforms generic "think about what you know" prompts. Activation also serves a diagnostic function — it surfaces misconceptions and gaps the instructor can address before they interfere with new learning.

### Context
#### Requirements
- A prompt that targets knowledge genuinely relevant to the new material, not just any prior knowledge
- A generative task — retrieval, prediction, [Concept Mapping](concept-mapping.md), or discussion — rather than passive recall instructions
- Instructor follow-through: misconceptions surfaced by activation must be addressed, or they persist

#### Constraints
- Activating irrelevant or tangential prior knowledge can impair comprehension by priming the wrong schema [Context must be relevant to the material to aid comprehension.](https://doi.org/10.1016/S0022-5371(72)80011-8) [-S] — Bransford and Johnson found that context helped only when it matched the passage
- Activation of fluent but inaccurate intuitions (e.g., naive physics theories) can strengthen misconceptions unless followed by [Cognitive Conflict](cognitive-conflict.md) [~M]
- Prior knowledge alone does not guarantee better performance; what matters is whether it is structurally relevant and correctly organized [Prior knowledge is not automatically related to performance.](../claims/prior-knowledge-not-related-to-performance.md) [~M]
- For learners with very little relevant knowledge, activation prompts have nothing to retrieve and waste time — use [Advance Organizers](advance-organizers.md) or direct teaching instead

### Target Learners
- Learners with moderate prior knowledge who have relevant schemas but need a retrieval cue
- Interdisciplinary learners who must connect knowledge from one domain to another
- Novices benefit less from retrieval-based activation and more from organizer-provided structure

### Target Learning Goals
- Conceptual understanding: anchoring new concepts in existing knowledge structures
- Transfer: building cross-domain connections that support analogical reasoning
- Metacognitive awareness: helping learners recognize what they do and do not yet know

### Affordances
- [Activation](../principles/activation.md) — this element is the direct enactment of Merrill's first principle: learning is promoted when existing knowledge is activated as a foundation for new knowledge
- [Retrieval Practice](../principles/retrieval-practice.md) — activation is a low-stakes retrieval event; retrieving prior knowledge strengthens it and prepares related schemas for integration with new material
- [Metacognition](../principles/metacognition.md) — activation prompts learners to monitor their own knowledge state, making gaps visible before instruction rather than after assessment
- [Analogies and Prior Knowledge Activation](analogies-and-prior-knowledge-activation.md) — analogies are a structured form of activation that maps a familiar domain onto an unfamiliar one

## Related Elements
- [Advance Organizers](advance-organizers.md) — provides relevant subsuming concepts when learners cannot retrieve them independently
- [Analogies](analogies.md) — activates a source domain deliberately to structure a target domain
- [Cognitive Conflict](cognitive-conflict.md) — the necessary follow-on when activation surfaces misconceptions
- [Contextualization](contextualization.md) — situates new learning in a context that evokes relevant prior experience
- [Concept Mapping](concept-mapping.md) — a generative activation format that externalizes knowledge structure

## Patterns That Use This Element
- [Gagné's 9 Events](../patterns/gagnés-9-events-of-instruction.md) — "stimulate recall of prior learning" event
- [Anchored Instruction](../patterns/anchored-instruction.md) — the anchor context activates experiential knowledge before problem solving
- [Case-Based Learning](../patterns/case-based-learning.md) — cases activate learners' existing frameworks before analysis

## Examples

**[Activating Prior Knowledge](../strategies/activating_prior_knowledge.md)** — Structured pre-instruction prompts (KWL charts, prediction tasks, brainstorming) that require learners to retrieve relevant knowledge before new content is presented.

**[Activate Background Knowledge](../strategies/activate_background_knowledge.md)** — UDL-aligned practice of explicitly connecting lesson content to learners' lived experience and prior lessons at the start of instruction.

**[KWL charts](https://www.adlit.org/in-the-classroom/strategies/kwl-charts)** — Learners record what they Know, what they Want to know, and later what they Learned; the K and W steps are activation, the L step closes the loop.

**[Merrill's First Principles of Instruction](https://www.mdpi.com/2076-3417/12/3/1107)** — Activation is the first principle: effective instruction "activates existing knowledge as a foundation for new knowledge" and, where none exists, provides experience that will.

## Key Sources
- Bransford, J. D., & Johnson, M. K. (1972). Contextual prerequisites for understanding: Some investigations of comprehension and recall. *Journal of Verbal Learning and Verbal Behavior, 11*(6), 717–726. [doi:10.1016/s0022-5371(72)80006-9](https://doi.org/10.1016/s0022-5371(72)80006-9)
- Ausubel, D. P. (1968). *Educational psychology: A cognitive view*. Holt, Rinehart & Winston.
- Merrill, M. D. (2002). First principles of instruction. *Educational Technology Research and Development, 50*(3), 43–59. [doi:10.1007/BF02505024](https://doi.org/10.1007/BF02505024)
- Karpicke, J. D., & Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science, 331*(6018), 772–775. [doi:10.1126/science.1199327](https://doi.org/10.1126/science.1199327)
- Chi, M. T. H. (2005). Common sense conceptions of emergent processes: Why some misconceptions are robust. *Journal of the Learning Sciences, 14*(2), 161–199. [doi:10.1207/s15327809jls1402_1](https://doi.org/10.1207/s15327809jls1402_1)

---