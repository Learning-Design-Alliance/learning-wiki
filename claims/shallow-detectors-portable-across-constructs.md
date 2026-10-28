---
type: claim
title: Shallowness detectors transfer between the transfer-shallow and PFL-shallow constructs with minimal A′ degradation
description: Shallowness detectors transfer between the transfer-shallow and PFL-shallow constructs with minimal A′ degradation
id: shallow-detectors-portable-across-constructs
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

# Shallowness detectors transfer between the transfer-shallow and PFL-shallow constructs with minimal A′ degradation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2013 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Models built to predict transfer-shallow predict PFL-shallow with A′ 0.75, and models built to predict PFL-shallow predict transfer-shallow with A′ 0.73, suggesting the two constructs are substantially related. [→ Gowda 2013](#gowda-2013)

## Evidence

### Gowda 2013

Gowda, S. M., Baker, R. S., Corbett, A. T., & Rossi, L. M. (2013). Towards Automatically Detecting Whether Student Learning is Shallow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0006-4

`q2 · i?` · `associational · r1`

Cross-application analysis applying each shallowness detector to the other construct's labels. Kappa degraded more, dropping to 0.27 for transfer-shallow models predicting PFL-shallow and to 0.41 in the reverse direction, still substantially better than chance.

> "When the models built to predict transfer-shallow are applied to predict PFL-shallow, they have very minimal degradation in terms of A ′, achieving an A ′ of 0.75, almost as good as a model trained to predict PFL-shallow."

## Discussion


## Related Claims
- [K* models outperform step regression for detecting transfer-shallowness, with no-interactions and interaction models each best on different metrics](kstar-beats-step-regression-transfer-shallow.md) — related
- [K* detectors identify no-PFL-shallow learners with cross-validated A′ of 0.790 and kappa 0.55](kstar-detects-no-pfl-shallow-learning.md) — related
- [K* detectors identify no-transfer-shallow learners at student-level cross-validated A′ of 0.766–0.791](kstar-detects-no-transfer-shallow-learning.md) — related
