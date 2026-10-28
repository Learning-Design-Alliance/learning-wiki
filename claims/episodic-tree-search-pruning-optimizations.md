---
type: claim
title: Astus prunes the episodic-tree interpolation search using two pre-computed methods to keep error diagnosis tractable despite exponential growth of interpolated branches in the worst case
description: Astus prunes the episodic-tree interpolation search using two pre-computed methods to keep error diagnosis tractable despite exponential growth of interpolated branches in the worst case
id: episodic-tree-search-pruning-optimizations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2015
sources:
  - id: luc-paquette-2015
    resource: "https://doi.org/10.1007/s40593-014-0030-z"
    title: "Luc Paquette, Jean-François Lebeau, Gabriel Beaulieu & André Mayers. (2015). Designing a Knowledge Representation Approach for the Generation of Pedagogical Interventions by MTTs. International Journal of Artificial Intelligence in Education 25:118–156. https://doi.org/10.1007/s40593-014-0030-z"
    author: "Luc Paquette, Jean-François Lebeau, Gabriel Beaulieu & André Mayers"
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: luc-paquette-2015-2
    resource: "https://doi.org/10.1007/s40593-014-0030-z"
    title: "Luc Paquette, Jean-François Lebeau, Gabriel Beaulieu & André Mayers. (2015). Designing a Knowledge Representation Approach for the Generation of Pedagogical Interventions by MTTs. International Journal of Artificial Intelligence in Education 25:118–156. https://doi.org/10.1007/s40593-014-0030-z"
    author: "Luc Paquette, Jean-François Lebeau, Gabriel Beaulieu & André Mayers"
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Astus prunes the episodic-tree interpolation search using two pre-computed methods to keep error diagnosis tractable despite exponential growth of interpolated branches in the worst case

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`
> **Currency** · newest study 2015 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` In the worst case, the number of interpolated branches can increase exponentially for every interpolated procedure, motivating pruning of the interpolation tree. [→ Luc Paquette 2015](#luc-paquette-2015)
`q1 i?` Two pruning methods relying on information pre-computed from the procedural graph are implemented: accessible-primitive-procedure sets and data-flow analysis of queries. [→ Luc Paquette 2015 (2)](#luc-paquette-2015-2)

## Evidence

### Luc Paquette 2015

Luc Paquette, Jean-François Lebeau, Gabriel Beaulieu & André Mayers. (2015). Designing a Knowledge Representation Approach for the Generation of Pedagogical Interventions by MTTs. International Journal of Artificial Intelligence in Education 25:118–156. https://doi.org/10.1007/s40593-014-0030-z

`q1 · i?` · `design · r2`

Analytical complexity statement in the Episodic Tree Search Optimization section. Because interpolations are applied recursively to every procedure and to every combination of possible query disruptions, the article notes that "the number of interpolated branch can increase exponentially for every interpolated procedure," motivating pruning of branches that cannot lead to the learner's off-path step.

> "In the worst case scenario, the number of interpolated branch can increase exponentially for every interpolated procedure."

### Luc Paquette 2015 (2)

Luc Paquette, Jean-François Lebeau, Gabriel Beaulieu & André Mayers. (2015). Designing a Knowledge Representation Approach for the Generation of Pedagogical Interventions by MTTs. International Journal of Artificial Intelligence in Education 25:118–156. https://doi.org/10.1007/s40593-014-0030-z

`q1 · i?` · `design · r2`

Description of the two implemented pruning methods in the Episodic Tree Search Optimization section. The first pre-computes, for each goal and procedure, "a set of primitive procedures that are accessible from that knowledge unit"; the second uses data-flow analysis to avoid disrupting queries unrelated to the off-path step's arguments.

> "for every goal and procedure contained in the procedural graph, we compute a set of primitive procedures that are accessible from that knowledge unit."

## Discussion


## Related Claims
- [Astus diagnoses many learner errors without erroneous knowledge units by interpolating incorrect executions of procedures in the episodic tree](astus-error-diagnosis-interpolation.md) — related
- [Allowing procedural constructs (branches, rules, loops, recursion) in an authoring tool dramatically raises authoring complexity and demands debugging support](procedural-authoring-constructs-raise-complexity.md) — related
