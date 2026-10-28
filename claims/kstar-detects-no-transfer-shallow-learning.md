---
type: claim
title: "K* detectors identify no-transfer-shallow learners at student-level cross-validated A′ of 0.766–0.791"
description: "K* detectors identify no-transfer-shallow learners at student-level cross-validated A′ of 0.766–0.791"
id: kstar-detects-no-transfer-shallow-learning
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
    kind: design
    rigour: 2
---

# K* detectors identify no-transfer-shallow learners at student-level cross-validated A′ of 0.766–0.791

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2013 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A K* multiplicative-interactions model cross-validated at the student level distinguishes students who perform better on the problem-solving test than the transfer test 76.6% of the time, with kappa 0.550. [→ Gowda 2013](#gowda-2013)

## Evidence

### Gowda 2013

Gowda, S. M., Baker, R. S., Corbett, A. T., & Rossi, L. M. (2013). Towards Automatically Detecting Whether Student Learning is Shallow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0006-4

`q2 · i?` · `design · r2`

Cross-validated detector development on tutor log data from 71 undergraduates using the Genetics Cognitive Tutor three-factor cross module. The K* multiplicative-interactions model achieved "an acceptable cross-validated kappa of 0.550 (55 % better than chance)", precision 0.873 and recall 0.815.

> "The A ′ value for the K* multiplicative-interactions model is 0.766, which indicates that the model can differentiate a student who performs better on the problem-solving test than the transfer test from a student who does not perform better on the problem-solving test than the transfer test, 76.6 % of the time."

## Discussion


## Related Claims
- [K* models outperform step regression for detecting transfer-shallowness, with no-interactions and interaction models each best on different metrics](kstar-beats-step-regression-transfer-shallow.md) — related
- [K* detectors identify no-PFL-shallow learners with cross-validated A′ of 0.790 and kappa 0.55](kstar-detects-no-pfl-shallow-learning.md) — related
- [Shallowness detectors transfer between the transfer-shallow and PFL-shallow constructs with minimal A′ degradation](shallow-detectors-portable-across-constructs.md) — related
