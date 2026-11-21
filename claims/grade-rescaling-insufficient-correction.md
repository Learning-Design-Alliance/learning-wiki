---
type: claim
title: Linear rescaling of AI grades toward the y = x line does not yield reliable machine grading because it leaves dispersion uncorrected
description: Linear rescaling of AI grades toward the y = x line does not yield reliable machine grading because it leaves dispersion uncorrected
id: grade-rescaling-insufficient-correction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: mok-2025
    resource: "https://doi.org/10.1088/1361-6552/adb92b"
    title: "Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)"
    author: Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Linear rescaling of AI grades toward the y = x line does not yield reliable machine grading because it leaves dispersion uncorrected

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Rescaling AI grades by the best-fit intercept and reciprocal gradient forces a y = x fit but does not correct grading inconsistency, can push full-mark solutions above 100% or zero-mark ones below 0%, and can make feedback incompatible with corrected grades. [→ Mok 2025](#mok-2025)

## Evidence

### Mok 2025

Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)

`q2 · i?` · `design · r2`

Grade-rescaling analysis demonstrated on GPT-4 (Fig. 16): rescaled grades follow the y = x line but data points remain spread out, with some rescaled grades above 100 or below 0; the article concludes rescaling is "not a very good solution" in the current status of development.

> "We conclude that in the current status of development, rescaling is not a very good solution to have more reliable machine grading performance."

## Discussion


## Related Claims
- [Homework effort correlates with test achievement as a stable linear 'academic main sequence' in introductory physics, at least until about 2016](academic-main-sequence-homework-effort-predicts-test-achievement.md) — related
- [Best-fit slope and intercept of the academic main sequence are inversely correlated, so the sequence is effectively characterized by a single degree of freedom](slope-intercept-inverse-correlation-main-sequence.md) — related
