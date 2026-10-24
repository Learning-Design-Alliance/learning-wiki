---
type: claim
title: Learner Records Rarely Establish That a Prerequisite Edge Exists
status: review
generated:
  by: claude/unspecified
  at: 2026-10-15
id: observation-cannot-establish-a-prerequisite-edge
evidence_strength:
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: porcaro-2026
    resource: "https://doi.org/10.5281/zenodo.23480842"
    title: "David S. Porcaro. (2026). What learner records can say about a prerequisite edge. Research release learning-graph-budget-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480842"
    author: David S. Porcaro
    q: 2
    i: "?"
    kind: associational
    rigour: "?"
---

# Learner Records Rarely Establish That a Prerequisite Edge Exists

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r?` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Evidence quality** · This claim rests on one research release that has not been peer-reviewed. Its research and writing were carried out by an AI system (Claude Code) under one human author, and its scope audit and reproduction were made by AI agents with no part in the work; no research team independent of the author has reviewed or replicated it. Treat it as a lead to check, not an established finding.

An edge from skill *a* to skill *b* is tested by comparing first attempts at *b* by learners who had
passed *a* with those of learners who had attempted *a* without passing it. On most platforms that
comparison is too small to test, and most of the supported edges that can be tested do not survive an
adjustment for general ability.

## Subclaims

> **Restated 2026-10-14** to match the article. The earlier account, that a fixed curriculum order is
> what empties the comparison, was replaced after the empty-cell study measured where pairs are lost.

- Most pairs of skills are attempted by few of the same learners: on EDM Cup the median pair has no
  learner in common, and on ASSISTments only 4.
- Where a pair is covered, its identifying cell holds tens of learners on most corpora, while a test of a
  drop of 0.10 needs between 277 and 379 learners in each group. Only Eedi, with 118,971 learners, could
  test more than a quarter of its pairs.
- A uniform order of skills hides only the reverse direction of a pair; the curriculum's own direction
  can still be tested, because platforms often move learners on before they pass the earlier skill (a mastery-gated
  tutor can prevent this). How a
  platform documents its order did not predict which corpora could decide pairs.
- Learners who fail one skill tend to fail others, so almost any pair shows a drop: +0.125 for an
  arbitrary pair on Eedi, more than the 0.10 sought. At most 27.6% of supported edges survived an
  adjustment for each learner's accuracy on other skills in the four corpora that could be checked. The
  adjustment can also remove real dependence, so an edge that fails it is unknown, not absent.
- A null counts against an edge only where a later skill that needs both is reached by enough learners
  (the reachability gate); without it, the absence of a drop is a fact about the corpus.

## Evidence

### Porcaro 2026

David S. Porcaro. (2026). What learner records can say about a prerequisite edge. Research release learning-graph-budget-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480842

`q2 · i?` · `associational · r?`

Positivity, power and an ability adjustment computed over pairs of skills in eight corpora of real learner records (Section 5.1), with synthetic detection floors and deranged controls. Observation record: `lazuli-graph-external-corpora-2026`.

## Discussion

**What would establish an edge.** Randomized edge release: a platform that would hold *b* until *a* is
mastered releases *b* to a random part of its learners. That creates the identifying cell on purpose and
removes general ability from the comparison, but it still needs hundreds of learners per arm for each
edge it tests (the article's Table 16).

**Scope.** Archival records from practice platforms, tutors and online courses; one outcome (the first
attempt at *b*) and one claimed effect (a drop of 0.10). A pair that cannot be tested is unknown, not
shown to be unrelated.

## Related Claims

- [The orientation statistic read from learner records is a difficulty sort.](observation-orients-edges-only-where-prerequisites-gate.md) — why a direction read from records is not evidence for an edge
- [The greedy cycle-break algorithm functions as a safety mechanism: none of the five evaluation topics required prerequisite-edge removal](cycle-break-safety-mechanism-concept-graphs.md) — related
