---
type: claim
title: Knowledge tracing predicts test performance well at intermediate learning levels but is insensitive to individual differences among students who have nominally reached mastery
description: Knowledge tracing predicts test performance well at intermediate learning levels but is insensitive to individual differences among students who have nominally reached mastery
id: kt-external-validity-test-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-25
evidence_strength: mixed
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
    rigour: 1
  - id: corbett-1995-2
    resource: "https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf"
    title: "Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf"
    author: Albert T. Corbett and John R. Anderson
    q: 2
    i: "?"
    kind: associational
    rigour: "?"
---

# Knowledge tracing predicts test performance well at intermediate learning levels but is insensitive to individual differences among students who have nominally reached mastery

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2` · `i3` large
> **Currency** · newest study 1995 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 1998**: tool and model accuracy changes quickly

## Subclaims
`q2 i3` On the third test, taken before full mastery, actual and predicted exercise-completion accuracy correlated r=0.69 across students. [→ Corbett 1995](#corbett-1995)
`q2 i?` On the first two post-mastery tests the model predicted no variability across students, yet raw tutor error rate reliably predicted test accuracy (TAR=-0.64 on test 2), which the authors call problematic. [→ Corbett 1995 (2)](#corbett-1995-2)

## Evidence

### Corbett 1995

Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf

`q2 · i3` · `associational · r1`

Experiment 2 external-validity study (Corbett, Anderson & O'Brien, in press) with twenty college students completing cumulative tests after sections 1, 4 and 6. On test 3, which included sub-mastery material, the correlation of actual and expected accuracy was "r = 0.69" (n=19; one student's data lost).

> "Under these conditions, the knowledge tracing model is quite sensitive to individual differences in test performance. The correlation of actual and expected valued, r = 0.69 is reliable"

### Corbett 1995 (2)

Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf

`q2 · i?` · `associational · r?`

Same Experiment 2 analysis: because all rules were estimated mastered before tests 1 and 2, the model's knowledge estimates had no variability, but correlation of tutor error rate with test accuracy was TAR=-0.64 on test 2, indicating persistent individual differences the standard model missed.

> "The correlation of tutor errors and test accuracy for the second test, TAR = -0.64 is problematic, however. While the model indicates there are no differences among students following remediation, tutor error rate is a strong and reliable predictor of test performance"

## Discussion


## Related Claims
- [After nominal mastery, variability in knowledge-tracing test predictions reflects persistent differences in the slip parameter rather than knowledge state](kt-slip-parameter-dominates-test-predictions.md) — related
- [Incorporating individualized learning and performance parameter weights makes knowledge tracing sensitive to residual individual differences after nominal mastery](kt-individualized-parameter-weights.md) — related
- [Students in the knowledge-tracing mastery condition were more likely to reach 90% test accuracy than students completing only the required exercises](kt-mastery-condition-test-success.md) — related
