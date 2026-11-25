---
type: claim
title: Incorporating individualized learning and performance parameter weights makes knowledge tracing sensitive to residual individual differences after nominal mastery
description: Incorporating individualized learning and performance parameter weights makes knowledge tracing sensitive to residual individual differences after nominal mastery
id: kt-individualized-parameter-weights
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-25
evidence_strength: moderate
newest_evidence: 1995
recheck_by: 1998
sources:
  - id: corbett-1995
    resource: "https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf"
    title: "Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf"
    author: Albert T. Corbett and John R. Anderson
    q: 2
    i: 3
    kind: associational
    rigour: 2
  - id: corbett-1995-2
    resource: "https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf"
    title: "Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf"
    author: Albert T. Corbett and John R. Anderson
    q: 2
    i: 2
    kind: associational
    rigour: 1
---

# Incorporating individualized learning and performance parameter weights makes knowledge tracing sensitive to residual individual differences after nominal mastery

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1`–`r2` · `q2` · `i2`–`i3`
> **Currency** · newest study 1995 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 1998**: tool and model accuracy changes quickly

## Subclaims
`q2 i3` Best-fitting individual difference weights applied to Experiment 2 data raised the test-2 actual/expected accuracy correlation to r=0.51. [→ Corbett 1995](#corbett-1995)
`q2 i2` With weights estimated dynamically from early-section error rates in Experiment 3, the test-2 correlation was r=0.31 (p<0.10) and test-3 r=0.81. [→ Corbett 1995 (2)](#corbett-1995-2)

## Evidence

### Corbett 1995

Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf

`q2 · i3` · `associational · r2`

Reanalysis of the Experiment 2 tutor and test data: four per-student weights (one per parameter type) were fit post hoc, each rule's parameters converted to odds, weighted, and converted back. Test-2 correlation of actual and expected accuracy became "r = 0.51".

> "However, this individualized model is considerably more sensitive to individual differences in the second test. The correlation of actual and expected accuracy for that test is now reliable, r = 0.51"

### Corbett 1995 (2)

Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf

`q2 · i2` · `associational · r1`

Experiment 3 (Corbett, Anderson, Carver & Brancolini, 1994): twenty students; weights estimated by regression from error rates on required exercises at each section's start. Test-2 sensitivity was marginal ("r = 0.31, p \<0.10"); test-3 sensitivity was r=0.81; tutor-data fit r=0.79 across 345 goals.

> "Unlike the standard model, however, the individualized knowledge tracing model is moderately sensitive to these residual differences, r = 0.31, p \<0.10"

## Discussion


## Related Claims
- [Knowledge tracing predicts test performance well at intermediate learning levels but is insensitive to individual differences among students who have nominally reached mastery](kt-external-validity-test-prediction.md) — related
- [After nominal mastery, variability in knowledge-tracing test predictions reflects persistent differences in the slip parameter rather than knowledge state](kt-slip-parameter-dominates-test-predictions.md) — related
- [Individualized Knowledge Tracing parameters fit student data significantly better and change mastery-learning practice decisions for many students](individualized-kt-parameters-change-practice-decisions.md) — related
- [Standard knowledge tracing models in use do not allow individual learning rates or individualized initial knowledge](standard-knowledge-tracing-lacks-individualization.md) — related
