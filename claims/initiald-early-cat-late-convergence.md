---
type: claim
title: InitialD converges faster toward the final diagnosis only for small question counts; a standard CAT converges faster beyond about 14 questions
description: InitialD converges faster toward the final diagnosis only for small question counts; a standard CAT converges faster beyond about 14 questions
id: initiald-early-cat-late-convergence
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: mixed
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: jill-jêenn-vie-2018
    resource: "https://doi.org/10.1007/s40593-017-0163-y"
    title: "Jill-Jêenn Vie, Fabrice Popineau, Éric Bruillard, Yolaine Bourda. (2018). Automated Test Assembly for Handling Learner Cold-Start in Large-Scale Assessments. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-017-0163-y"
    author: Jill-Jêenn Vie, Fabrice Popineau, Éric Bruillard, Yolaine Bourda
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# InitialD converges faster toward the final diagnosis only for small question counts; a standard CAT converges faster beyond about 14 questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For k ≤ 9 questions InitialD converges faster towards the final diagnosis, while for k ≥ 14 the CAT baseline converges faster, indicating adaptation benefits emerge only in later stages. [→ Jill-Jêenn Vie 2018](#jill-jeenn-vie-2018)

## Evidence

### Jill-Jêenn Vie 2018

Jill-Jêenn Vie, Fabrice Popineau, Éric Bruillard, Yolaine Bourda. (2018). Automated Test Assembly for Handling Learner Cold-Start in Large-Scale Assessments. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-017-0163-y

`q2 · i?` · `design · r2`

Numerical cross-validation result on the Fraction dataset (Results section): the diagnostic advantage of the non-adaptive DPP sampling is limited to the early cold-start stage; adaptive selection takes over once several ability estimates exist.

> "For k ≤ 9, InitialD converges faster towards the final diagnosis, while for k ≥ 14, CAT converges faster, showing a benefit in adaptation in later periods of the process."

## Discussion


## Related Claims
- [On the TIMSS dataset, InitialD reaches the same estimation error with fewer questions than random sampling or a traditional adaptive test](initiald-question-efficiency-timss.md) — related
- [On the Fraction dataset, InitialD outperforms random sampling, uncertainty sampling and a normal adaptive test in cold-start response-pattern reconstruction](initiald-outperforms-strategies-fraction-cold-start.md) — related
- [On the TIMSS dataset, random sampling performs well compared to a normal adaptive test, possibly because the test is already balanced](random-competitive-with-cat-on-balanced-timss.md) — related
- [Cold-start initialization converges faster than starting from an inconsistent student model](cold-start-faster-than-inconsistent-model.md) — related
