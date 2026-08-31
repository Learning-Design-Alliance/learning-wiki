---
type: element
title: Recall prior knowledge
description: "Activates learners' existing mental models to connect new information."
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Recall prior knowledge

## Description
Recall prior knowledge is an instructional element that prompts learners to retrieve and surface what they already know before encountering new material. By activating existing schemas, it gives new information points of attachment, making it easier to encode, organize, and later retrieve. It typically appears early in a learning sequence — as opening questions, brainstorming, concept mapping, or analogy — and functions as the "activation" phase in several canonical instructional models.

## Design Implications

Activating prior knowledge improves comprehension and retention because new information is integrated into existing schemas rather than stored as isolated facts [Prior knowledge is one of the strongest predictors of learning outcomes.](../claims/prior-knowledge-not-related-to-performance.md) [~M]. The activation must be *relevant* — prompts should target knowledge actually needed for the new material, not general warm-up questions. Structured activation (e.g., a [Concept Mapping](concept-mapping.md) task or an [Advance Organizer](advance-organizers.md)) outperforms unstructured discussion because it makes the to-be-connected knowledge explicit and inspectable [Advance organizers improve retention of unfamiliar material.](../claims/self-explanation-improves-conceptual-understanding.md) [+M].

### Context
#### Requirements
- Accurate diagnosis of what learners actually know (misconceptions activated here will interfere with new learning)
- Prompts targeted at knowledge relevant to the upcoming content, not generic interest questions
- A visible product of the recall (map, list, prediction) that can be revisited and revised during instruction
- Follow-through: the activated knowledge must be explicitly connected to new content, not merely recalled and dropped

#### Constraints
- Activating incorrect or naive conceptions without later confronting them entrenches misconceptions and interferes with learning [-M]
- If learners lack relevant prior knowledge, activation prompts produce frustration or fabricated "knowledge" rather than useful schemas [-M]
- Overly long or open-ended recall activities consume time and working memory without aiding integration [~W]
- For learners with strong, well-organized knowledge, elaborate activation can be redundant and slow progress [~M]

### Target Learners
- Learners with some relevant background who need help connecting it to new material [+M]
- Novices in conceptual domains (STEM, humanities) where new ideas build hierarchically on prior ones
- Less useful for complete novices, who need foundational knowledge built first rather than activated

### Target Learning Goals
- Conceptual understanding: integrating new concepts into existing knowledge structures
- Transfer: preparing learners to apply knowledge across contexts by making underlying schemas explicit
- Misconception repair: surfacing faulty prior conceptions so they can be addressed ([Cognitive Conflict](cognitive-conflict.md))

### Affordances
- [Activation](../principles/activation.md) — this element *is* the enactment of the activation principle: it operationalizes the claim that learning is facilitated when existing knowledge is retrieved and made available before new instruction
- [Scaffolding](../principles/scaffolding.md) — recall prompts provide temporary structure that bridges what learners know to what they are about to learn, and can be faded as learners internalize the habit of self-activating
- [Analogical Reasoning](../principles/analogical-reasoning.md) — [Analogies](analogies.md) are a special case of prior-knowledge recall in which a familiar domain is deliberately mapped onto an unfamiliar one

## Related Elements
- [Concept Mapping](concept-mapping.md) — a structured format for externalizing and organizing recalled knowledge
- [Pre-Reading Questioning](pre-reading-questioning.md) — a lightweight activation technique used before text study
- [Analogies](analogies.md) — connect new content to well-known source domains
- [Advance Organizers](advance-organizers.md) — introductory frameworks that anchor incoming material to existing knowledge
- [Cognitive Conflict](cognitive-conflict.md) — the follow-on move when activated prior knowledge turns out to be misconceived

## Patterns That Use This Element
- [Gagné's 9 Events](../patterns/gagnés-9-events-of-instruction.md) — "stimulate recall of prior learning" (event 3)
- [Anchored Instruction](../patterns/anchored-instruction.md) — anchors activate relevant experience before problem exploration
- [4C Instructional Design](../patterns/4cid-four-component-instructional-design.md) — prior knowledge activation supports task classification and sequencing

Merrill's First Principles also place activation first ("activation of existing knowledge"), though no dedicated pattern page exists yet.

## Examples
- **[Activating Prior Knowledge](../strategies/activating_prior_knowledge.md)** — a general strategy of opening questions, brainstorming, or quick-writes before new instruction.
- **[Activate Background Knowledge](../strategies/activate_background_knowledge.md)** — a UDL-aligned variant that deliberately surfaces diverse learner experiences as assets.
- **K-W-L charts** — learners record what they *Know*, what they *Want* to know, and later what they *Learned*; the K and W columns are the activation component.
- **[Khan Academy](https://www.khanacademy.org)** — unit introductions and "review" prerequisites links prompt recall of earlier topics before new lessons.

## Key Sources
- Ausubel, D. P. (1960). The use of advance organizers in the learning and retention of meaningful verbal material. *Journal of Educational Psychology, 51*(5), 267–272. [doi:10.1037/h0046669](https://doi.org/10.1037/h0046669)
- Dochy, F., Segers, M., & Buehl, M. M. (1999). The relation between assessment practices and outcomes of studies: The case of research on prior knowledge. *Educational Psychology Review, 11*(2), 145–186. [doi:10.3102/00346543069002145](https://doi.org/10.3102/00346543069002145)
- Bransford, J. D., & Johnson, M. K. (1972). Contextual prerequisites for understanding: Some investigations of comprehension and recall. *Journal of Verbal Learning and Verbal Behavior, 11*(6), 717–726. [doi:10.1016/s0022-5371(72)80006-9](https://doi.org/10.1016/s0022-5371(72)80006-9)
- Karpicke, J. D., & Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science, 331*(6018), 772–775. [doi:10.1126/science.1199327](https://doi.org/10.1126/science.1199327)
