---
type: claim
title: Astus diagnoses many learner errors without erroneous knowledge units by interpolating incorrect executions of procedures in the episodic tree
description: Astus diagnoses many learner errors without erroneous knowledge units by interpolating incorrect executions of procedures in the episodic tree
id: astus-error-diagnosis-interpolation
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
---

# Astus diagnoses many learner errors without erroneous knowledge units by interpolating incorrect executions of procedures in the episodic tree

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2015 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` When a learner executes an off-path step, Astus attempts to diagnose the error by manipulating the episodic tree to instantiate a step matching the off-path step. [→ Luc Paquette 2015](#luc-paquette-2015)

## Evidence

### Luc Paquette 2015

Luc Paquette, Jean-François Lebeau, Gabriel Beaulieu & André Mayers. (2015). Designing a Knowledge Representation Approach for the Generation of Pedagogical Interventions by MTTs. International Journal of Artificial Intelligence in Education 25:118–156. https://doi.org/10.1007/s40593-014-0030-z

`q1 · i?` · `design · r2`

Design description of Astus's error diagnosis mechanism in the Error Diagnosis section. Inspired by Sierra's impasse-and-repair theory, the framework searches the episodic tree for complex procedures that might be the source of the impasse and interpolates incorrect executions, so that "Astus attempts to diagnose the learner 's error by manipulating the content of the episodic tree."

> "When an off-path step is executed, Astus attempts to diagnose the learner ’s error by manipulating the content of the episodic tree to try to instantiate a step that matches the learner 's off-path step."

## Discussion


## Related Claims
- [Astus's pedagogical module automatically generates next-step hint content from the task model, whereas frameworks such as TDK and CTAT require hint messages to be included in the model of the task](astus-auto-generates-next-step-hints.md) — related
- [Astus prunes the episodic-tree interpolation search using two pre-computed methods to keep error diagnosis tractable despite exponential growth of interpolated branches in the worst case](episodic-tree-search-pruning-optimizations.md) — related
