---
type: claim
title: "K* detectors identify no-PFL-shallow learners with cross-validated A′ of 0.790 and kappa 0.55"
description: "K* detectors identify no-PFL-shallow learners with cross-validated A′ of 0.790 and kappa 0.55"
id: kstar-detects-no-pfl-shallow-learning
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2013
recheck_by: 2016
sources:
  - id: gowda-2013
    resource: "https://doi.org/10.1007/s40593-013-0006-4"
    title: "Gowda, S. M., Baker, R. S., Corbett, A. T., & Rossi, L. M. (2013). Towards Automatically Detecting Whether Student Learning is Shallow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0006-4"
    author: "Gowda, S. M., Baker, R. S., Corbett, A. T., & Rossi, L. M."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# K* detectors identify no-PFL-shallow learners with cross-validated A′ of 0.790 and kappa 0.55

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2013 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2016**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A K* multiplicative-interactions model detects students whose problem-solving performance exceeds their preparation-for-future-learning performance, achieving A′ 0.790 and Kappa 0.55 under student-level cross-validation. [→ Gowda 2013](#gowda-2013)

## Evidence

### Gowda 2013

Gowda, S. M., Baker, R. S., Corbett, A. T., & Rossi, L. M. (2013). Towards Automatically Detecting Whether Student Learning is Shallow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0006-4

`q2 · i?` · `design · r2`

Same detector-development procedure applied to no-PFL-shallowness labels (20 of 71 students labeled shallow). No step regression model could be built because no individual feature had cross-validated Kappa over 0 for this construct; K* models succeeded.

> "The multiplicative-interactions model achieved a better A ′ and Kappa than the no-interactions model, achieving an A ′ of 0.790, and a Kappa of 0.55. Excellent precision and recall (for shallowness) were also achieved."

## Discussion


## Related Claims
- [K* models outperform step regression for detecting transfer-shallowness, with no-interactions and interaction models each best on different metrics](kstar-beats-step-regression-transfer-shallow.md) — related
- [K* detectors identify no-transfer-shallow learners at student-level cross-validated A′ of 0.766–0.791](kstar-detects-no-transfer-shallow-learning.md) — related
- [Shallowness detectors transfer between the transfer-shallow and PFL-shallow constructs with minimal A′ degradation](shallow-detectors-portable-across-constructs.md) — related
