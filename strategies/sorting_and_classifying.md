---
type: strategy
id: sorting_and_classifying
title: Sorting and Classifying
description: Learners group items into categories based on shared features, either into given categories or ones they construct themselves.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Sorting and Classifying

> **Strategy** · [All strategies](index.md)

## Description
Sorting and classifying asks learners to organize a set of items — examples, cases, objects, statements, problems — into categories, either using categories supplied by the instructor or by generating their own categories and justifying them. The cognitive work lies in discriminating which features matter, comparing items against one another, and articulating the criteria that govern membership. It converts passive recognition of examples into active construction of category structure.

## Design Implications

Classification tasks force learners to encode the *features that define* a concept rather than its surface appearance, which supports discrimination and transfer better than studying examples one at a time [~M]. When learners sort into instructor-defined categories, the task functions as a check on conceptual understanding; when they generate their own categories, it functions as inductive concept construction. Sorting multiple cases into a shared framework is a core mechanism of [Concept Attainment](../patterns/concept-attainment.md), and contrasting non-examples against examples during sorting sharpens category boundaries [~S].

### Context
#### Requirements
- A carefully constructed item set: enough examples per category to establish the pattern, including borderline and non-examples to test boundaries
- Clear (or deliberately discoverable) criteria for category membership
- A mechanism for learners to justify placements — labels, written rationales, or discussion — since unarticulated sorting can rely on surface matching
- Feedback or reveal step so learners can compare their sort against an expert sort

#### Constraints
- If items differ on too many irrelevant features, learners may sort by surface similarity and never encode the deep criterion [-M]
- Open-ended sorting with no criteria, feedback, or consolidation can leave novices with idiosyncratic, incorrect categories [-M]
- Poorly chosen item sets (too few examples, no non-examples) underdetermine the concept and produce overgeneralization [-W]
- For novices with high item counts, sorting can add extraneous load; chunking the item set mitigates this [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [~M]

#### Implementation Variability
- **Closed sort**: categories given; learners place items (card sorts, drag-and-drop, Venn diagrams)
- **Open sort**: learners generate and name their own categories, then defend the criteria
- **Guess-my-rule**: one learner sorts silently; others infer the classification rule — makes criteria explicit through inference
- **Error analysis**: learners receive a mis-sorted set and must find and correct the errors
- **Progressive sorting**: begin with two obvious categories, add borderline items as discrimination improves

### Target Learners
- Novices building initial category structure for a domain, provided the item set controls irrelevant variation [~M]
- Intermediate learners who benefit from borderline cases that force refinement of over-simple categories [~W]
- Young learners: sorting is developmentally foundational and supports early math and literacy (e.g., attribute blocks, word sorts) [+W]

### Target Learning Goals
- Concept formation and discrimination: learning what defines a category and what does not
- Vocabulary and terminology: attaching precise labels to discriminated categories
- Transfer preparation: multiple varied cases sorted into one framework support flexible application [Exposure to multiple varied cases supports flexible transfer.](../claims/cognitive-flexibility-theory-multiple-cases.md) [~M]

### Instructions
1. Select the target concept and identify its defining features and common misconceptions.
2. Build an item set: 3–5 clear examples per category, 2–3 non-examples, and 1–2 borderline cases.
3. Decide closed vs. open sort; for open sorts, require learners to name and state criteria for each category.
4. Have learners sort, then justify placements aloud or in writing ([Articulation](../elements/articulation.md)).
5. Reveal or discuss an expert sort; focus debrief on the borderline items and disagreements.
6. Follow with application: learners classify *new* items or use the categories to solve a problem.

## Related Strategies
- [Concept Attainment](../patterns/concept-attainment.md) — the pattern this strategy enacts; sorting is its core activity cycle
- [Comparing Cases](../elements/comparing-cases.md) — sorting is comparison made cumulative across a whole item set
- [Card Sorting](card-sorting.md) — the physical/digital modality most often used to implement sorts

## Examples
- **Words Their Way** (Bear, Invernizzi, Templeton, & Johnston) — developmental word study in which students sort spelling/word-feature cards into categories (e.g., short vs. long vowel patterns), then hunt for exceptions. Widely used in elementary literacy instruction.
- **Card sorts in biology** — sorting organism cards into taxonomic groups before formal classification instruction, then revising the sort after instruction to reveal misconceptions.
- **UX card sorting** (e.g., in Optimal Workshop's tools, https://www.optimalworkshop.com) — the same mechanism applied to information architecture: users sort content items into navigation categories to reveal mental models.

## Key Sources
- Marton, F., & Booth, S. (1997). *Learning and awareness.* Lawrence Erlbaum Associates. (Variation theory: discernment of critical features through contrast and classification)
- Tennyson, R. D., & Park, O.-C. (1980). The teaching of concepts: A review of instructional design research literature. *Review of Educational Research, 50*(1), 55–70. [doi:10.3102/00346543050001055](https://doi.org/10.3102/00346543050001055)
- Bear, D. R., Invernizzi, M., Templeton, S., & Johnston, F. (2015). *Words Their Way: Word Study for Phonics, Vocabulary, and Spelling Instruction* (6th ed.). Pearson.
- Bruner, J. S., Goodnow, J. J., & Austin, G. A. (1956). *A study of thinking.* Wiley.