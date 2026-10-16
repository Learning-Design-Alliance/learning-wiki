---
type: element
id: concept-map
aliases: [concept-semantic-map-element]
title: Concept Map
description: A concept map is a node-and-link diagram that externalizes relationships among ideas, making the structure of a knowledge domain visible.
canonical: true
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
sources:
  - id: jonassen-1984
    resource: "https://eric.ed.gov/?id=ED258538"
    title: "Jonassen, D. H. (1984). Semantic relationships and structural knowledge acquisition in introductory psychology. https://eric.ed.gov/?id=ED258538"
    author: Jonassen, D. H
---

# Concept Map

> **Element** · [All elements](index.md)
> **Evidence** · 6 claims (2 for, 3 mixed, 1 against) · 9 studies (4 causal, 2 quant-synthesis, 2 review, 1 theoretical), `q1`–`q4` · 4 of 9 report an effect size · 2 claims rest on one study

## Description
A concept map is a diagram in which concepts appear as nodes and labeled links express the relationships between them, forming a propositional structure ("concept — linking word — concept"). It functions both as a learning activity (learners construct maps) and as an assessment or advance organizer (instructors provide or score maps). Concept maps make knowledge structure — not just knowledge items — visible and revisable.

## Design Implications

Concept mapping supports meaningful learning by forcing learners to identify relationships rather than memorize isolated facts [Concept maps improve learning.](../claims/concept-mapping-improves-learning.md) [+M]. Construction is the active ingredient: learners who generate and justify links outperform those who merely study a completed map, though studying expert maps still beats no mapping [Concept mapping improves learning.](../claims/concept-mapping-improves-learning.md) [+M]. Because maps externalize structure, they also serve as diagnostic tools — missing or mislabeled links reveal misconceptions that prose responses can hide.

### Context
#### Requirements
- A focused question or domain ("What causes seasons?") — maps built without a focus question tend to become unstructured brainstorm webs
- Explicit teaching of the notation: nodes, labeled links, cross-links, and hierarchies are conventions learners must learn before mapping helps
- Iteration and feedback — maps should be revised as understanding deepens, not treated as one-off products
- Moderate prior knowledge; learners need something to relate before relational tasks pay off
- A term list of domain concepts to be placed into the map structure

#### Constraints
- The node-and-link format itself consumes working memory; novices juggling unfamiliar content *and* unfamiliar notation can experience overload [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [~M] — provide partial maps or a small starter set of concepts
- Poor fit for purely procedural or motor skills where knowledge is not propositional
- Scoring maps reliably is difficult; without a rubric (e.g., counting valid propositions and cross-links), grading becomes subjective
- Learners can produce well-formed maps with shallow links if the task rewards quantity over quality of propositions

### Target Learners
- Learners with moderate prior knowledge who can relate new ideas to existing schemas [Concept mapping improves learning.](../claims/concept-mapping-improves-learning.md) [+M]
- Students in conceptually dense domains (biology, chemistry, history) where causal and hierarchical relationships matter
- Less effective for complete novices, who lack the knowledge to propose meaningful links [Concept maps improve learning.](../claims/concept-mapping-improves-learning.md) [~M]
- introductory psychology students

### Target Learning Goals
- Relational and structural knowledge: seeing how concepts connect, not just what they are
- Misconception diagnosis: surfacing faulty links for revision
- Knowledge organization for transfer and retrieval [Concept maps improve learning.](../claims/concept-mapping-improves-learning.md) [+M]
- representing and analyzing interrelationships among domain concepts

### Affordances
- [Cognitive Load Management](../principles/cognitive-load-management.md) — externalizing relationships onto the diagram offloads the working-memory burden of holding multiple concepts and their connections in mind simultaneously, letting learners manipulate structure visibly rather than mentally
- [Activation](../principles/activation.md) — building a map requires retrieving prior knowledge and explicitly connecting it to new material, enacting activation as a structural rather than purely discussion-based activity
- [Clear Structure](../principles/clear-structure.md) — a completed map gives learners an explicit overview of a domain's organization, functioning as a spatial [advance organizer](advance-organizers.md)
- [Analogical Reasoning](../principles/analogical-reasoning.md) — cross-links between distant branches of a map are where analogies surface; prompting learners to add cross-links directly exercises relational mapping across domains
- [Semantic Network Theory](../theories/semantic-network-theory.md)

### Claims
<!-- Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] -->
- [Graphic Organizers Support Novice Comprehension](../claims/graphic-organizers-support-novice-comprehension.md) [+M]
- [Placing heavier cognitive demands on learners can be counterproductive in mapping tasks](../claims/heavy-cognitive-demands-of-mapping-can-be-counterproductive.md) [-W]
- [Teacher-initiated and student-mediated semantic mapping did not differ significantly in their effects on EFL reading comprehension](../claims/teacher-initiated-and-student-mediated-mapping-no-difference.md) [~W]

## The evidence by question
- *Does having learners build an organization of the content as a concept map help, and against what comparison?* [Concept mapping improves learning over most comparison conditions by a moderate average amount, but not over time-matched retrieval practice](../claims/concept-mapping-improves-learning.md) [+S]
- *Should learners construct the map themselves, study a provided one, or build it with the teacher or a peer?* [Learner-constructed graphic organizers are not shown to outperform provided ones: the one direct test, with college readers, favoured provided organizers on transfer](../claims/learner-constructed-graphic-organizers-outperform-provided.md) [~S]

## Related Elements

- [Advance Organizers](advance-organizers.md) — a completed concept map is a graphic form of organizer presented before instruction
- [Annotating](../principles/annotating.md) — the textual counterpart: marking relationships in prose rather than diagramming them
- [Analogies](analogies.md) — cross-links in a map often encode analogical relationships; both depend on relational reasoning
- [Application](application.md) — maps should be revised after application tasks, when structural understanding has been tested
- [Assessment](assessment.md) — concept maps serve as formative assessment of knowledge structure, not just content recall
- [Semantic Mapping Principle](../principles/graphic-organizers.md)
- [Concept Mapping](concept-mapping.md)

## Patterns That Use This Element
- [5E Learning Cycle](../principles/inquiry-based-learning.md) — mapping in the "Explain" and "Elaborate" phases to consolidate relationships
- [Concept Attainment](../patterns/concept-attainment.md) — maps record the attributes and exemplars that define attained concepts
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — expert maps model how a domain expert organizes knowledge

## Examples

- **[CmapTools](https://cmap.ihmc.us/cmaptools/)** — IHMC's free concept-mapping software, developed by Novak's group; supports collaboration and propositional link labels, and is the reference implementation of the Novak & Cañas method.
- **[Lucidchart](https://www.lucidchart.com)** / **[Miro](https://miro.com)** — general diagramming platforms commonly used for concept mapping in course design; lack CmapTools' proposition-focused scaffolding but integrate with LMS workflows.
- **Pre-lecture organizer maps** — instructor provides a partially completed map (concepts given, links blank) that students complete during and after instruction, then revise as a unit review.
- [Student-generated mapping exercise](../strategies/student-generated-mapping-strategy.md)
- [Teacher-provided graphic map as review](../strategies/teacher-provided-advance-graphic-map.md)
- [Graphic Organizers for Assessment](../strategies/graphic_organizers_for_assessment.md)
- [Visualizations and Mind Maps](../strategies/visualizations_and_mind_maps.md)
- [Lecture Support with Graphic Organizers](../strategies/graphic_organizers_for_lecture_support.md)
- [Graphic Organizers as Thinking Tools](../strategies/graphic_organizers_as_thinking_tools.md)
- [Unit Planning with Graphic Organizers](../strategies/graphic_organizers_for_unit_planning.md)

## Key Sources
- Novak, J. D., & Cañas, A. J. (2008). The theory underlying concept maps and how to construct and use them. *Technical Report IHMC CmapTools 2006-01 Rev 01-2008*, Florida Institute for Human and Machine Cognition. [https://cmap.ihmc.us/docs/theory-of-concept-maps](https://cmap.ihmc.us/docs/theory-of-concept-maps)
- Nesbit, J. C., & Adesope, O. O. (2006). Learning with concept and knowledge maps: A meta-analysis. *Review of Educational Research, 76*(3), 413–448. [doi:10.3102/00346543076003413](https://doi.org/10.3102/00346543076003413)
- Novak, J. D. (1990). Concept mapping: A useful tool for science education. *Journal of Research in Science Teaching, 27*(10), 937–949. [doi:10.1002/tea.3660271003](https://doi.org/10.1002/tea.3660271003)
- Karpicke, J. D., & Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science, 331*(6018), 772–775. [doi:10.1126/science.1199327](https://doi.org/10.1126/science.1199327)
- Jonassen, D. H. (1984). Semantic relationships and structural knowledge acquisition in introductory psychology. https://eric.ed.gov/?id=ED258538

<!-- merged 2026-10-15 from elements/concept-semantic-map-element ("Concept/semantic map"), a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Concept/semantic map

> **Element** · [All elements](index.md)
> **Evidence** · 4 claims (2 for, 1 mixed, 1 against) · 5 studies (2 causal, 2 quant-synthesis, 1 theoretical), `q1`–`q4` · 3 of 5 report an effect size · 2 claims rest on one study

## Description
A graphic organizer in which concepts are represented as nodes and their relationships as labeled or positional links. In the article it appears as student frame maps and skeletal templates, and can be provided complete as an advance organizer or given partially completed for students to fill in during mapping exercises.

## Design Implications

### Context
#### Requirements
- A term list of domain concepts to be placed into the map structure
#### Constraints
- 

### Target Learners
- introductory psychology students

### Target Learning Goals
- representing and analyzing interrelationships among domain concepts

### Affordances
- [Semantic Network Theory](../theories/semantic-network-theory.md)

### Claims
<!- - Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] - ->
- [Graphic Organizers Support Novice Comprehension](../claims/graphic-organizers-support-novice-comprehension.md) [+M]
- [Concept mapping improves learning over most comparison conditions by a moderate average amount, but not over time-matched retrieval practice](../claims/concept-mapping-improves-learning.md) [+M]
- [Placing heavier cognitive demands on learners can be counterproductive in mapping tasks](../claims/heavy-cognitive-demands-of-mapping-can-be-counterproductive.md) [-W]
- [Teacher-initiated and student-mediated semantic mapping did not differ significantly in their effects on EFL reading comprehension](../claims/teacher-initiated-and-student-mediated-mapping-no-difference.md) [~W]

## Related Elements

- [Semantic Mapping Principle](../principles/graphic-organizers.md)
- [Concept Mapping](concept-mapping.md)
- [Concept Map](concept-map.md)

## Examples

- [Student-generated mapping exercise](../strategies/student-generated-mapping-strategy.md)
- [Teacher-provided graphic map as review](../strategies/teacher-provided-advance-graphic-map.md)
- [Graphic Organizers for Assessment](../strategies/graphic_organizers_for_assessment.md)
- [Visualizations and Mind Maps](../strategies/visualizations_and_mind_maps.md)
- [Lecture Support with Graphic Organizers](../strategies/graphic_organizers_for_lecture_support.md)
- [Graphic Organizers as Thinking Tools](../strategies/graphic_organizers_as_thinking_tools.md)
- [Unit Planning with Graphic Organizers](../strategies/graphic_organizers_for_unit_planning.md)

## Key Sources
- Jonassen, D. H. (1984). Semantic relationships and structural knowledge acquisition in introductory psychology. https://eric.ed.gov/?id=ED258538
-->
