---
type: element
id: concept-map
title: Concept Map
description: A concept map is a node-and-link diagram that externalizes relationships among ideas, making the structure of a knowledge domain visible.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Concept Map

> **Element** · [All elements](index.md)

## Description
A concept map is a diagram in which concepts appear as nodes and labeled links express the relationships between them, forming a propositional structure ("concept — linking word — concept"). It functions both as a learning activity (learners construct maps) and as an assessment or advance organizer (instructors provide or score maps). Concept maps make knowledge structure — not just knowledge items — visible and revisable.

## Design Implications

Concept mapping supports meaningful learning by forcing learners to identify relationships rather than memorize isolated facts [Concept maps improve learning.](../claims/concept-maps-improve-learning.md) [+M]. Construction is the active ingredient: learners who generate and justify links outperform those who merely study a completed map, though studying expert maps still beats no mapping [Concept mapping improves learning.](../claims/concept-mapping-improves-learning.md) [+M]. Because maps externalize structure, they also serve as diagnostic tools — missing or mislabeled links reveal misconceptions that prose responses can hide.

### Context
#### Requirements
- A focused question or domain ("What causes seasons?") — maps built without a focus question tend to become unstructured brainstorm webs
- Explicit teaching of the notation: nodes, labeled links, cross-links, and hierarchies are conventions learners must learn before mapping helps
- Iteration and feedback — maps should be revised as understanding deepens, not treated as one-off products
- Moderate prior knowledge; learners need something to relate before relational tasks pay off

#### Constraints
- The node-and-link format itself consumes working memory; novices juggling unfamiliar content *and* unfamiliar notation can experience overload [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [~M] — provide partial maps or a small starter set of concepts
- Poor fit for purely procedural or motor skills where knowledge is not propositional
- Scoring maps reliably is difficult; without a rubric (e.g., counting valid propositions and cross-links), grading becomes subjective
- Learners can produce well-formed maps with shallow links if the task rewards quantity over quality of propositions

### Target Learners
- Learners with moderate prior knowledge who can relate new ideas to existing schemas [Concept mapping improves learning.](../claims/concept-mapping-improves-learning.md) [+M]
- Students in conceptually dense domains (biology, chemistry, history) where causal and hierarchical relationships matter
- Less effective for complete novices, who lack the knowledge to propose meaningful links [Concept maps improve learning.](../claims/concept-maps-improve-learning.md) [~M]

### Target Learning Goals
- Relational and structural knowledge: seeing how concepts connect, not just what they are
- Misconception diagnosis: surfacing faulty links for revision
- Knowledge organization for transfer and retrieval [Concept maps improve learning.](../claims/concept-maps-improve-learning.md) [+M]

### Affordances
- [Cognitive Load Management](../principles/cognitive-load-management.md) — externalizing relationships onto the diagram offloads the working-memory burden of holding multiple concepts and their connections in mind simultaneously, letting learners manipulate structure visibly rather than mentally
- [Activation](../principles/activation.md) — building a map requires retrieving prior knowledge and explicitly connecting it to new material, enacting activation as a structural rather than purely discussion-based activity
- [Clear Structure](../principles/clear-structure.md) — a completed map gives learners an explicit overview of a domain's organization, functioning as a spatial [advance organizer](advance-organizers.md)
- [Analogical Reasoning](../principles/analogical-reasoning.md) — cross-links between distant branches of a map are where analogies surface; prompting learners to add cross-links directly exercises relational mapping across domains

## Related Elements
- [Advance Organizers](advance-organizers.md) — a completed concept map is a graphic form of organizer presented before instruction
- [Annotating](../principles/annotating.md) — the textual counterpart: marking relationships in prose rather than diagramming them
- [Analogies](analogies.md) — cross-links in a map often encode analogical relationships; both depend on relational reasoning
- [Application](application.md) — maps should be revised after application tasks, when structural understanding has been tested
- [Assessment](assessment.md) — concept maps serve as formative assessment of knowledge structure, not just content recall

## Patterns That Use This Element
- [5E Learning Cycle](../patterns/5e-learning-cycle.md) — mapping in the "Explain" and "Elaborate" phases to consolidate relationships
- [Concept Attainment](../patterns/concept-attainment.md) — maps record the attributes and exemplars that define attained concepts
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — expert maps model how a domain expert organizes knowledge

## Examples

- **[CmapTools](https://cmap.ihmc.us/cmaptools/)** — IHMC's free concept-mapping software, developed by Novak's group; supports collaboration and propositional link labels, and is the reference implementation of the Novak & Cañas method.
- **[Lucidchart](https://www.lucidchart.com)** / **[Miro](https://miro.com)** — general diagramming platforms commonly used for concept mapping in course design; lack CmapTools' proposition-focused scaffolding but integrate with LMS workflows.
- **Pre-lecture organizer maps** — instructor provides a partially completed map (concepts given, links blank) that students complete during and after instruction, then revise as a unit review.

## Key Sources
- Novak, J. D., & Cañas, A. J. (2008). The theory underlying concept maps and how to construct and use them. *Technical Report IHMC CmapTools 2006-01 Rev 01-2008*, Florida Institute for Human and Machine Cognition. [https://cmap.ihmc.us/docs/theory-of-concept-maps](https://cmap.ihmc.us/docs/theory-of-concept-maps)
- Nesbit, J. C., & Adesope, O. O. (2006). Learning with concept and knowledge maps: A meta-analysis. *Review of Educational Research, 76*(3), 413–448. [doi:10.3102/00346543076003413](https://doi.org/10.3102/00346543076003413)
- Novak, J. D. (1990). Concept mapping: A useful tool for science education. *Journal of Research in Science Teaching, 27*(10), 937–949. [doi:10.1002/tea.3660271003](https://doi.org/10.1002/tea.3660271003)
- Karpicke, J. D., & Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science, 331*(6018), 772–775. [doi:10.1126/science.1199327](https://doi.org/10.1126/science.1199327)