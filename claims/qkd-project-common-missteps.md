---
type: claim
title: Common student missteps cluster around protocol obfuscation, check-bit sampling, and parameter tuning
description: Common student missteps cluster around protocol obfuscation, check-bit sampling, and parameter tuning
id: qkd-project-common-missteps
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: brian-r-la-cour-2025
    resource: "https://doi.org/10.1109/qce65121.2025.20533"
    title: "Brian R. La Cour, Noah A. Davis. (2025). An Adversarial Quantum Key Distribution Project. arXiv. [doi:10.1109/qce65121.2025.20533](https://doi.org/10.1109/qce65121.2025.20533)"
    author: Brian R. La Cour, Noah A. Davis
    q: 2
    i: "?"
    kind: design
    rigour: 1
  - id: brian-r-la-cour-2025-2
    resource: "https://doi.org/10.1109/qce65121.2025.20533"
    title: "Brian R. La Cour, Noah A. Davis. (2025). An Adversarial Quantum Key Distribution Project. arXiv. [doi:10.1109/qce65121.2025.20533](https://doi.org/10.1109/qce65121.2025.20533)"
    author: Brian R. La Cour, Noah A. Davis
    q: 2
    i: "?"
    kind: design
    rigour: 1
---

# Common student missteps cluster around protocol obfuscation, check-bit sampling, and parameter tuning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Student Alice-and-Bob implementations most often fail through obfuscation attempts, static or absent check-bit sampling, and poorly chosen bit count, average photon number, or dark count probability. [→ Brian R. La Cour 2025](#brian-r-la-cour-2025)
`q2 i?` Eve-side mistakes most often stem from treating denial of service as a goal by measuring too often or adding too much noise. [→ Brian R. La Cour 2025 (2)](#brian-r-la-cour-2025-2)

## Evidence

### Brian R. La Cour 2025

Brian R. La Cour, Noah A. Davis. (2025). An Adversarial Quantum Key Distribution Project. arXiv. [doi:10.1109/qce65121.2025.20533](https://doi.org/10.1109/qce65121.2025.20533)

`q2 · i?` · `design · r1`

Authors' survey of common pitfalls (Sec. VII) from experience: obfuscation attempts "almost universally fail to deceive the eavesdropper" because Eve has read access, and sampling the same fixed portion each time lets Eve steal undetected. Descriptive, no statistics.

> "Once the Eve group notices this vulnerability in the protocol, they have free reign to steal all remaining key bits without detection."

### Brian R. La Cour 2025 (2)

Brian R. La Cour, Noah A. Davis. (2025). An Adversarial Quantum Key Distribution Project. arXiv. [doi:10.1109/qce65121.2025.20533](https://doi.org/10.1109/qce65121.2025.20533)

`q2 · i?` · `design · r1`

Authors' experiential observation about Eve-side mistakes in the adversarial project; denial of service is not a desired outcome since it flags the channel as insecure. No quantitative data reported.

> "Eavesdroppers tend to either measure too often or add too much noise and accept that the channel will be flagged as insecure."

## Discussion


## Related Claims
- [Before the QuILT, students incorrectly believed Bob always knows the polarization of Alice's photon in the B92 protocol, whether or not his detector clicks](bob-knows-photon-polarization-difficulty.md) — related
- [Revised simulation and activity significantly improved introductory students' answers on actions Alice and Bob can take to detect Eve (78.0% vs 58.9% correct)](revised-sim-improved-detect-eve-answers.md) — related
- [Students incorrectly claiming Bob knows the photon polarization when his detector does not click dropped from 41% on the pretest to 6% on the posttest](qkd-quilt-q1-no-click-error-reduction.md) — related
- [Post-test question 2 (Eve's orientation for a mismatched bit) was answered significantly better in 2016 than 2014 at the introductory level](posttest-q2-significantly-better-2016.md) — related
