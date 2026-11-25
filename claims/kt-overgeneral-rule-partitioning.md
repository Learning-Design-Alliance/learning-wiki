---
type: claim
title: Some ideal student-model rules are too general for some students and fail to transfer to more complex contexts, prompting a finer-grained 55-rule revision
description: Some ideal student-model rules are too general for some students and fail to transfer to more complex contexts, prompting a finer-grained 55-rule revision
id: kt-overgeneral-rule-partitioning
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
    i: "?"
    kind: design
    rigour: 3
  - id: corbett-1995-2
    resource: "https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf"
    title: "Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf"
    author: Albert T. Corbett and John R. Anderson
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Some ideal student-model rules are too general for some students and fail to transfer to more complex contexts, prompting a finer-grained 55-rule revision

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 1995 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 1998**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Error rate on the variable-declaration rule jumped to about 55% at the first exercise requiring two parameters, suggesting roughly half the students had encoded a non-ideal rule that did not generalize. [→ Corbett 1995](#corbett-1995)
`q2 i?` The cognitive model was revised, ultimately growing to 55 rules including separate rules for declaring the first versus each additional parameter variable. [→ Corbett 1995 (2)](#corbett-1995-2)

## Evidence

### Corbett 1995

Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf

`q2 · i?` · `design · r3`

Learning-curve analysis (Figure 5) of the declare-parameter rule in the Experiment 1 tutor data: error decreased over four single-parameter exercises, then jumped at the first two-parameter function definition. The article interprets this as non-ideal rule encoding; no effect size is printed.

> "The 55% error rate at goal six in this figure suggests that just under half the students had encoded the ideal rule initially and were able to apply it in the new situation. The other students initially encoded a non-ideal rule that was sufficient to complete the first four exercises but failed to generalize"

### Corbett 1995 (2)

Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf

`q2 · i?` · `associational · r2`

Model-revision statement following the generalization failures: the curriculum's cognitive model was expanded to 55 rules, with variable declaration split into first-argument and additional-argument rules (Figure 6 re-plots the data as two curves).

> "We revised the cognitive model in response to this problem. Ultimately the cognitive model for this curriculum has grown to 55 rules"

## Discussion


## Related Claims
- [Applying skill theory to grammar conflates constructs: pedagogical rules are not what exists in learners' mental representation](grammar-as-skill-is-a-conflation.md) — related
- [Declarative memory predicts learning of complex grammatical rules during initial grammar learning](declarative-memory-predicts-complex-grammar-learning.md) — related
- [Aggregating Lisp learning data by production rule yields systematic learning curves, while aggregation by more superficial units does not](production-rule-learning-curves-lisp-tutor.md) — related
