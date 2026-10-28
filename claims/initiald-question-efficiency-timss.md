---
type: claim
title: On the TIMSS dataset, InitialD reaches the same estimation error with fewer questions than random sampling or a traditional adaptive test
description: On the TIMSS dataset, InitialD reaches the same estimation error with fewer questions than random sampling or a traditional adaptive test
id: initiald-question-efficiency-timss
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2018
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

# On the TIMSS dataset, InitialD reaches the same estimation error with fewer questions than random sampling or a traditional adaptive test

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Asking 7 questions via InitialD yields on average the same estimation error as 12 random questions or 19 questions from a traditional adaptive test, and 12 questions suffice for a diagnostic predicting 70% of outcomes. [→ Jill-Jêenn Vie 2018](#jill-jeenn-vie-2018)

## Evidence

### Jill-Jêenn Vie 2018

Jill-Jêenn Vie, Fabrice Popineau, Éric Bruillard, Yolaine Bourda. (2018). Automated Test Assembly for Handling Learner Cold-Start in Large-Scale Assessments. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-017-0163-y

`q2 · i?` · `design · r2`

Cross-validation simulation on the TIMSS dataset (757 8th-grade learners, 23 mathematics questions, 13 knowledge components), Results section: InitialD shows "a lower log-loss in response pattern reconstruction" from the first question onward, and "12 questions seem enough to get a diagnostic that predicts correctly 70% of the outcomes."

> "Asking 7 questions over 23 using the strategy InitialD leads in average to the same estimation error than asking 12 questions at random, or asking 19 questions using a traditional adaptive test. InitialD converges towards the final diagnosis faster than the other strategies."

## Discussion


## Related Claims
- [InitialD converges faster toward the final diagnosis only for small question counts; a standard CAT converges faster beyond about 14 questions](initiald-early-cat-late-convergence.md) — related
- [On the Fraction dataset, InitialD outperforms random sampling, uncertainty sampling and a normal adaptive test in cold-start response-pattern reconstruction](initiald-outperforms-strategies-fraction-cold-start.md) — related
- [On the TIMSS dataset, random sampling performs well compared to a normal adaptive test, possibly because the test is already balanced](random-competitive-with-cat-on-balanced-timss.md) — related
- [CAT adjusts test questions as the testing goes along](cat-adjusts-questions-during-testing.md) — related
- [Cold-start initialization converges faster than starting from an inconsistent student model](cold-start-faster-than-inconsistent-model.md) — related
