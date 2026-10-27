---
type: strategy
id: negative-feedback-without-knowledge-engineering
title: Provide negative feedback on errors without knowledge engineering efforts by diagnosing errors via impasse-and-repair interpolation of the task model
description: The article argues that MTT frameworks should be able to deliver negative feedback on errors without authoring erroneous knowledge units or buggy rules.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: luc-paquette-2015
    resource: "https://doi.org/10.1007/s40593-014-0030-z"
    title: "Luc Paquette, Jean-François Lebeau, Gabriel Beaulieu & André Mayers. (2015). Designing a Knowledge Representation Approach for the Generation of Pedagogical Interventions by MTTs. International Journal of Artificial Intelligence in Education 25:118–156. https://doi.org/10.1007/s40593-014-0030-z"
    author: "Luc Paquette, Jean-François Lebeau, Gabriel Beaulieu & André Mayers"
---

# Provide negative feedback on errors without knowledge engineering efforts by diagnosing errors via impasse-and-repair interpolation of the task model

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article argues that MTT frameworks should be able to deliver negative feedback on errors without authoring erroneous knowledge units or buggy rules. It states that "the capability for an MTT framework to be able to provide negative feedback without requiring any knowledge engineering efforts would thus be valuable as the benefits of this intervention would now outweigh its cost." Astus implements this by diagnosing off-path steps through interpolation inspired by Sierra's impasse-and-repair processes, then generating feedback from the diagnosed branch of the episodic tree.

## Design Implications

### Context
#### Requirements
- Requires a task model whose procedures, queries and declarative knowledge units have semantics the MTT can interpret, so incorrect executions can be interpolated
#### Constraints
- The article notes negative feedback's high modeling efforts have usually outweighed its benefits in ITSs, and the diagnosis process can misattribute mental steps when multiple interpolations match

### Target Learners
- computer science undergraduate students working with MTTs

### Target Learning Goals
- correcting errors in well-defined procedural tasks through negative feedback

### Affordances
- [Sierra Impasse Repair Theory](../theories/cognitivism.md)

## Claims

- [Astus diagnoses many learner errors without erroneous knowledge units by interpolating incorrect executions of procedures in the episodic tree](../claims/astus-error-diagnosis-interpolation.md) [+W]
- [Astus prunes the episodic-tree interpolation search using two pre-computed methods to keep error diagnosis tractable despite exponential growth of interpolated branches in the worst case](../claims/episodic-tree-search-pruning-optimizations.md) [+W]

## Related Strategies

- [Provide Feedback](provide_feedback.md)

## Examples
-

## Key Sources
- Luc Paquette, Jean-François Lebeau, Gabriel Beaulieu & André Mayers. (2015). Designing a Knowledge Representation Approach for the Generation of Pedagogical Interventions by MTTs. International Journal of Artificial Intelligence in Education 25:118–156. https://doi.org/10.1007/s40593-014-0030-z
