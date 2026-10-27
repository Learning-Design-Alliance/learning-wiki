---
type: claim
title: On the TIMSS dataset, random sampling performs well compared to a normal adaptive test, possibly because the test is already balanced
description: On the TIMSS dataset, random sampling performs well compared to a normal adaptive test, possibly because the test is already balanced
id: random-competitive-with-cat-on-balanced-timss
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
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

# On the TIMSS dataset, random sampling performs well compared to a normal adaptive test, possibly because the test is already balanced

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On TIMSS, Random performed well relative to a normal adaptive test, which the authors attribute to the item bank already being balanced so random questions tend to be diverse. [→ Jill-Jêenn Vie 2018](#jill-jeenn-vie-2018)

## Evidence

### Jill-Jêenn Vie 2018

Jill-Jêenn Vie, Fabrice Popineau, Éric Bruillard, Yolaine Bourda. (2018). Automated Test Assembly for Handling Learner Cold-Start in Large-Scale Assessments. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-017-0163-y

`q2 · i?` · `design · r2`

Secondary comparative observation from the Discussion section of the cross-validation simulations: on a well-balanced item bank, naive random selection already approaches adaptive-test accuracy, an explanation the article presents tentatively ("It may be because").

> "On the TIMSS dataset, the Random strategy performs well compared to a normal adaptive test. It may be because the test is already well balanced, so random questions have high probability to be diverse."

## Discussion


## Related Claims
- [On the Fraction dataset, InitialD outperforms random sampling, uncertainty sampling and a normal adaptive test in cold-start response-pattern reconstruction](initiald-outperforms-strategies-fraction-cold-start.md) — related
- [On the TIMSS dataset, InitialD reaches the same estimation error with fewer questions than random sampling or a traditional adaptive test](initiald-question-efficiency-timss.md) — related
- [CAT adjusts test questions as the testing goes along](cat-adjusts-questions-during-testing.md) — a broader claim this one bears on
- [InitialD converges faster toward the final diagnosis only for small question counts; a standard CAT converges faster beyond about 14 questions](initiald-early-cat-late-convergence.md) — related
