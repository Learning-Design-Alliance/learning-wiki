---
type: claim
title: OptimNN achieves lower test RMSE than EM, CGD, and SGD for fitting BKT and its variants across four tutoring datasets
description: OptimNN achieves lower test RMSE than EM, CGD, and SGD for fitting BKT and its variants across four tutoring datasets
id: optimnn-lower-rmse-than-em-cgd-sgd
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
evidence_strength: moderate
sources:
  - id: badrinath-2023
    resource: "https://github.com/abadrinath947/OptimNN"
    title: "Badrinath, A. and Pardos, Z. (2023). Optimizing Bayesian Knowledge Tracing with Neural Network Parameter Generation. https://github.com/abadrinath947/OptimNN"
    author: Badrinath, A. and Pardos, Z.
    q: 2
    i: 1
---

# OptimNN achieves lower test RMSE than EM, CGD, and SGD for fitting BKT and its variants across four tutoring datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i1` small

## Subclaims
`q2 i?` OptimNN shows decreased RMSE compared to EM, CGD, and SGD when fitting BKT, KT-IDEM, and ILE on held-out test sets, with the largest gains on the item-level variants. [→ Badrinath 2023](#badrinath-2023)

## Evidence

### Badrinath 2023

Badrinath, A. and Pardos, Z. (2023). Optimizing Bayesian Knowledge Tracing with Neural Network Parameter Generation. https://github.com/abadrinath947/OptimNN

`q2 · i1`

Comparison of test RMSE on AST09, ALG08, AST12, and BRI08 (Table 2) for BKT, KT-IDEM, and ILE fitted by OptimNN versus EM, CGD, and SGD, with corrected resampled t-test confidence intervals. The paper reports "an average improvement of 4.0% over EM, 24.2% over CGD and 1.8% over SGD".

> "To fit BKT parameters on these datasets, OptimNN shows decreased RMSE compared to all prior methods, with an average improvement of 4.0% over EM, 24.2% over CGD and 1.8% over SGD (where results are available for each method)."

## Discussion


## Related Claims
-
