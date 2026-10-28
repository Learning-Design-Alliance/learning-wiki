---
type: claim
title: "K* models outperform step regression for detecting transfer-shallowness, with no-interactions and interaction models each best on different metrics"
description: "K* models outperform step regression for detecting transfer-shallowness, with no-interactions and interaction models each best on different metrics"
id: kstar-beats-step-regression-transfer-shallow
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2013
sources:
  - id: gowda-2013
    resource: "https://doi.org/10.1007/s40593-013-0006-4"
    title: "Gowda, S. M., Baker, R. S., Corbett, A. T., & Rossi, L. M. (2013). Towards Automatically Detecting Whether Student Learning is Shallow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0006-4"
    author: "Gowda, S. M., Baker, R. S., Corbett, A. T., & Rossi, L. M."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# K* models outperform step regression for detecting transfer-shallowness, with no-interactions and interaction models each best on different metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2013 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The K* no-interactions model achieved better cross-validated Kappa and precision than all other models, while the K* multiplicative-interactions model achieved better A′ and recall than all other models for no-transfer-shallowness. [→ Gowda 2013](#gowda-2013)

## Evidence

### Gowda 2013

Gowda, S. M., Baker, R. S., Corbett, A. T., & Rossi, L. M. (2013). Towards Automatically Detecting Whether Student Learning is Shallow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0006-4

`q2 · i?` · `associational · r1`

Comparison of four models (K* and step regression, each with and without multiplicative interactions) in Table 2, evaluated with 10-fold student-level cross-validation on A′, Kappa, precision and recall. The authors conclude the overall success of the K* models suggests the relationships are non-linear.

> "the K* no-interactions model achieves a better cross-validated Kappa and better precision than all other models, and the K* multiplicative interactions model achieves better A ′ and better recall than all other models."

## Discussion


## Related Claims
- [K* detectors identify no-PFL-shallow learners with cross-validated A′ of 0.790 and kappa 0.55](kstar-detects-no-pfl-shallow-learning.md) — related
- [K* detectors identify no-transfer-shallow learners at student-level cross-validated A′ of 0.766–0.791](kstar-detects-no-transfer-shallow-learning.md) — related
- [Shallowness detectors transfer between the transfer-shallow and PFL-shallow constructs with minimal A′ degradation](shallow-detectors-portable-across-constructs.md) — related
