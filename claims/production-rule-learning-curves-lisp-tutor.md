---
type: claim
title: Aggregating Lisp learning data by production rule yields systematic learning curves, while aggregation by more superficial units does not
description: Aggregating Lisp learning data by production rule yields systematic learning curves, while aggregation by more superficial units does not
id: production-rule-learning-curves-lisp-tutor
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
    kind: associational
    rigour: 1
---

# Aggregating Lisp learning data by production rule yields systematic learning curves, while aggregation by more superficial units does not

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 1995 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 1998**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Error rate on rules introduced in the first Lisp Tutor lesson averages about 0.42 at the first application opportunity and drops monotonically across successive opportunities. [→ Corbett 1995](#corbett-1995)
`q2 i?` Aggregating the data over exercises, goals, or surface Lisp constructs does not yield systematic learning curves. [→ Corbett 1995](#corbett-1995)

## Evidence

### Corbett 1995

Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf

`q2 · i?` · `associational · r1`

Analysis of tutor log data plotted in Figure 3, the mean learning curve for coding rules introduced in the first lesson of the Lisp Tutor curriculum. The article reports error rate "averages about 0.42" at first opportunity and declines monotonically; no effect size is printed.

> "The error rate averages about 0.42 across the first opportunity to apply each rule, then drops monotonically across the successive opportunities to apply the rules. Aggregating the data by other, more superficial units, e.g., over exercises, over problem solving goals within exercises, or over opportunities to employ each surface Lisp construct independent of problem solving context, does not yield systematic learning curves"

## Discussion


## Related Claims
- [Simulated learners can match human error rates overall while learning faster and making different kinds of errors than the students they model](simulated-learners-differ-from-humans-in-error-types.md) — related
- [Simulations show power functions fit aggregated means and standard deviations almost perfectly even when all underlying individual learning curves are discontinuous](aggregated-power-fits-mask-discontinuities.md) — related
- [Some ideal student-model rules are too general for some students and fail to transfer to more complex contexts, prompting a finer-grained 55-rule revision](kt-overgeneral-rule-partitioning.md) — related
- [Explicitly learned L2 rules can be automatized through systematic practice after a metalinguistic criterion is reached](explicit-rules-automatizable-through-practice.md) — related
