---
type: claim
title: On the Fraction dataset, InitialD outperforms random sampling, uncertainty sampling and a normal adaptive test in cold-start response-pattern reconstruction
description: On the Fraction dataset, InitialD outperforms random sampling, uncertainty sampling and a normal adaptive test in cold-start response-pattern reconstruction
id: initiald-outperforms-strategies-fraction-cold-start
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
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

# On the Fraction dataset, InitialD outperforms random sampling, uncertainty sampling and a normal adaptive test in cold-start response-pattern reconstruction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Using the Fraction dataset, the InitialD DPP-based strategy achieves lower log-loss and a narrower confidence interval than Random, Uncertainty and CAT strategies when the first questions are asked to a newcomer. [→ Jill-Jêenn Vie 2018](#jill-jeenn-vie-2018)

## Evidence

### Jill-Jêenn Vie 2018

Jill-Jêenn Vie, Fabrice Popineau, Éric Bruillard, Yolaine Bourda. (2018). Automated Test Assembly for Handling Learner Cold-Start in Large-Scale Assessments. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-017-0163-y

`q2 · i?` · `design · r2`

Numerical cross-validation results on the Fraction dataset (536 middle school students, 20 fraction-subtraction questions), reported in the Results section: "InitialD performs better than the other strategies", with 8 questions reconstructing "82% of answers"; log-loss tables give 0.376 ± 0.027 for InitialD after 8 questions versus 0.515 ± 0.06 for CAT.

> "In Fig. 3, InitialD performs better than the other strategies, and with a narrow confidence interval. 8 questions seem enough to reconstruct correctly 82% of answers, and converge to a minimal log-loss."

## Discussion


## Related Claims
- [InitialD converges faster toward the final diagnosis only for small question counts; a standard CAT converges faster beyond about 14 questions](initiald-early-cat-late-convergence.md) — related
- [On the TIMSS dataset, InitialD reaches the same estimation error with fewer questions than random sampling or a traditional adaptive test](initiald-question-efficiency-timss.md) — related
- [On the TIMSS dataset, random sampling performs well compared to a normal adaptive test, possibly because the test is already balanced](random-competitive-with-cat-on-balanced-timss.md) — related
- [Meta-behavioral pattern extraction outperforms knowledge-concept-based collaborative extraction, which fails to consistently boost performance due to data sparsity](meta-behavioral-extraction-beats-kc-based-variants.md) — related
