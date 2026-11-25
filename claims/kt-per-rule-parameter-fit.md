---
type: claim
title: Allowing knowledge-tracing learning and performance parameters to vary across rules substantially improves fit to tutor performance data
description: Allowing knowledge-tracing learning and performance parameters to vary across rules substantially improves fit to tutor performance data
id: kt-per-rule-parameter-fit
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
    rigour: 1
  - id: corbett-1995-2
    resource: "https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf"
    title: "Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf"
    author: Albert T. Corbett and John R. Anderson
    q: 2
    i: 3
    kind: associational
    rigour: 1
---

# Allowing knowledge-tracing learning and performance parameters to vary across rules substantially improves fit to tutor performance data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2` · `i3` large
> **Currency** · newest study 1995 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 1998**: tool and model accuracy changes quickly

## Subclaims
`q2 i3` With parameters held constant across 21 rules, predicted and actual goal-level accuracy correlated r=0.47 with mean absolute error 0.16. [→ Corbett 1995](#corbett-1995)
`q2 i3` With per-rule parameter estimates, the correlation rose to r=0.85 and mean absolute error fell to 0.07. [→ Corbett 1995 (2)](#corbett-1995-2)

## Evidence

### Corbett 1995

Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf

`q2 · i3` · `associational · r1`

Experiment 1 internal-validity study (Corbett & Anderson, 1993): students completed 158 required programming goals across 25 exercises; actual and predicted correct-action probabilities were compared across goals. The correlation was "moderately correlated (r=0.47, p \< 0.05)".

> "The expected and actual probabilities were moderately correlated (r=0.47, p \< 0.05), the mean error rate was 0.06 and the mean absolute error rate was 0.16"

### Corbett 1995 (2)

Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf

`q2 · i3` · `associational · r1`

Reanalysis within Experiment 1 fitting learning and performance parameters separately for each of the 21 ideal coding rules. Best-fitting per-rule estimates gave a "substantially better fit, r=0.85" with mean error -0.01 and absolute error 0.07.

> "If we allow the learning and performance parameter estimates to vary across rules, best fitting estimates provide a substantially better fit, r=0.85. The mean error in prediction, -0.01, and the absolute error in prediction, 0.07, are both reduced in the revised fit"

## Discussion


## Related Claims
- [Standard knowledge tracing models in use do not allow individual learning rates or individualized initial knowledge](standard-knowledge-tracing-lacks-individualization.md) — related
- [Individualized Knowledge Tracing parameters fit student data significantly better and change mastery-learning practice decisions for many students](individualized-kt-parameters-change-practice-decisions.md) — related
- [Learner models with population-level parameters systematically misestimate the trial of mastery for most students whose learning rates vary](population-parameters-systematic-mastery-error.md) — related
