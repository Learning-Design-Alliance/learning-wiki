---
type: claim
title: The Orientation Statistic Read From Learner Records Is a Difficulty Sort
status: review
generated:
  by: claude/unspecified
  at: 2026-10-15
id: observation-orients-edges-only-where-prerequisites-gate
evidence_strength:
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: porcaro-2026
    resource: "https://doi.org/10.5281/zenodo.23480842"
    title: "David S. Porcaro. (2026). What learner records can say about a prerequisite edge. Research release learning-graph-budget-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480842"
    author: David S. Porcaro
    q: 1
    i: "?"
    kind: theoretical
    rigour: "?"
---

# The Orientation Statistic Read From Learner Records Is a Difficulty Sort

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r?` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Evidence quality** · This claim rests on one research release that has not been peer-reviewed. Its research and writing were carried out by an AI system (Claude Code) under one human author, and its scope audit and reproduction were made by AI agents with no part in the work; no research team independent of the author has reviewed or replicated it. Treat it as a lead to check, not an established finding.

The statistic that orients a pair from asymmetric conditional failure points, whenever some learners fail
both skills, from the skill fewer learners fail to the skill more learners fail. It is therefore right
exactly as often as the true edges run from an easier skill to a harder one, the property known as
sortability.

## Subclaims

> **Restated 2026-10-14** to match the article. The earlier version read orientation accuracy as a
> property of the prerequisite mechanism; the identity shows it is a property of how difficulty runs
> along the edges, which the mechanism helps set.

- With *f*ₐ and *f*ᵦ the failure rates on *a* and *b* and *j* the rate of failing both, the statistic
  equals *j*(*f*ᵦ − *f*ₐ)/(*f*ₐ*f*ᵦ), so its sign is the sign of *f*ᵦ − *f*ₐ. In all 30 cells of the
  simulation sweep it oriented every scored edge exactly as a difficulty sort did.
- A prerequisite itself makes the dependent skill fail more often, so deeper skills look harder even where
  latent difficulty does not rise with depth: where it is independent of depth the statistic oriented
  0.883 [0.854, 0.910] of edges at hardness 1.0 and 0.773 [0.736, 0.809] at 0.0.
- Where any one of a skill's prerequisites suffices and later skills are easier, it was right on only 0.009
  to 0.020 of the edges into skills with two or more prerequisites.
- On ASSISTments, with grades assigned by a name-matching rule no person checked, the skill from the higher
  grade was harder in 0.576 of pairs: difficulty rises only weakly with grade there.

## Evidence

### Porcaro 2026

David S. Porcaro. (2026). What learner records can say about a prerequisite edge. Research release learning-graph-budget-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480842

`q1 · i?` · `theoretical · r?`

An algebraic identity for the orientation statistic and a simulation sweep with one generator (Section 5.1), with difficulty placed against grade order on two real corpora. Observation record: `lazuli-graph-simulation-2026`.

## Discussion

**What this narrows.** Sortability has to be measured in each corpus before any direction is read. An
estimator that uses variation in the order learners met two skills is not tied to difficulty, but it needs
learners who met the skills in both orders and an order that ability did not choose; in simulation such an
estimator was fooled when abler learners chose the order.

**Scope.** The identity covers one statistic. The sweep is simulated, with one generator.

## Related Claims

- [Learner records rarely establish that a prerequisite edge exists.](observation-cannot-establish-a-prerequisite-edge.md) — the existence limit
- [Prior difficulty collections mostly lack fine-grained classification of student difficulties](prior-difficulty-collections-lack-fine-grained-classification.md)
- [Learning-curve plateaus were caused by learners' failure to overcome specific difficulties at critical stages, not by the order in which habits developed](plateaus-caused-by-unovercome-difficulties.md) — related
