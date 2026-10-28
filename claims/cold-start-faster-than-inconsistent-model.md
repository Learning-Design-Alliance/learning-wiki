---
type: claim
title: Cold-start initialization converges faster than starting from an inconsistent student model
description: Cold-start initialization converges faster than starting from an inconsistent student model
id: cold-start-faster-than-inconsistent-model
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2015
sources:
  - id: fabiano-dorça-2015
    resource: "https://doi.org/10.1007/s40593-015-0037-0"
    title: "Fabiano Dorça. (2015). Implementation and use of Simulated Students for Test and Validation of new Adaptive Educational Systems: a Practical Insight. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-015-0037-0"
    author: Fabiano Dorça
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Cold-start initialization converges faster than starting from an inconsistent student model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2015 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` When LSp was initialized with cold start (0.50 in all dimensions), all 10 executions produced consistent results with fewer iterations (average 194.6) than experiments starting from an inconsistent model. [→ Fabiano Dorça 2015](#fabiano-dorca-2015)

## Evidence

### Fabiano Dorça 2015

Fabiano Dorça. (2015). Implementation and use of Simulated Students for Test and Validation of new Adaptive Educational Systems: a Practical Insight. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-015-0037-0

`q2 · i?` · `design · r2`

Simulation experiment using strategy 3 with cold-start initialization (LSp set to 0.50). All 10 executions produced consistent results, averaging 194.6 iterations and 14.6 learning problems. The article notes "inconsistencies in the student model seem to be worse than the lack of initial information about student's LS."

> "Table 9 shows the number of iterations, the amount of learning problems (LP), and the resulting LSp values at the end of the simulated learning process for 10 consecutive executions of this experiment. As it can be seen, all executions produced consistent results."

## Discussion


## Related Claims
- [Consistent student models reduce learning problems and raise average performance, supporting reuse of student models across courses](consistent-model-improves-performance.md) — a broader claim this one bears on
- [Reinforcing learning styles absent from the selected combination on poor performance (strategy 3) yields the most consistent probabilistic learning-style model](strategy3-best-lsp-consistency.md) — related
- [On the Fraction dataset, InitialD outperforms random sampling, uncertainty sampling and a normal adaptive test in cold-start response-pattern reconstruction](initiald-outperforms-strategies-fraction-cold-start.md) — related
- [On the TIMSS dataset, InitialD reaches the same estimation error with fewer questions than random sampling or a traditional adaptive test](initiald-question-efficiency-timss.md) — related
- [InitialD converges faster toward the final diagnosis only for small question counts; a standard CAT converges faster beyond about 14 questions](initiald-early-cat-late-convergence.md) — related
- [On the TIMSS dataset, random sampling performs well compared to a normal adaptive test, possibly because the test is already balanced](random-competitive-with-cat-on-balanced-timss.md) — related
