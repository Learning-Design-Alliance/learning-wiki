---
type: claim
title: Applicants who submitted AI-written essays were admitted at lower rates than comparable non-users, with an estimated penalty of about 1.5 percentage points per AI-written essay
description: Applicants who submitted AI-written essays were admitted at lower rates than comparable non-users, with an estimated penalty of about 1.5 percentage points per AI-written essay
id: ai-essay-use-penalized-in-admissions
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: calvin-isley-2026
    resource: "https://arxiv.org/abs/2609.22549"
    title: "Calvin Isley, Johann D. Gaebler, and Sharad Goel. (2026). AI-written admissions essays are widespread but penalized. arXiv preprint. https://arxiv.org/abs/2609.22549"
    author: Calvin Isley, Johann D. Gaebler, and Sharad Goel
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: calvin-isley-2026-2
    resource: "https://arxiv.org/abs/2609.22549"
    title: "Calvin Isley, Johann D. Gaebler, and Sharad Goel. (2026). AI-written admissions essays are widespread but penalized. arXiv preprint. https://arxiv.org/abs/2609.22549"
    author: Calvin Isley, Johann D. Gaebler, and Sharad Goel
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Applicants who submitted AI-written essays were admitted at lower rates than comparable non-users, with an estimated penalty of about 1.5 percentage points per AI-written essay

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` Double machine learning estimates controlling for roughly 400 covariates show a 1.5 p.p. decrease in admission probability per AI-written essay (significant at p < 0.01). [→ Calvin Isley 2026](#calvin-isley-2026)
`q2 i?` Adjusting additionally for essay quality measures increases the estimated penalty to 2.6 p.p. per AI-written essay, though this model may be subject to post-treatment bias. [→ Calvin Isley 2026 (2)](#calvin-isley-2026-2)

## Evidence

### Calvin Isley 2026

Calvin Isley, Johann D. Gaebler, and Sharad Goel. (2026). AI-written admissions essays are widespread but penalized. arXiv preprint. https://arxiv.org/abs/2609.22549

`q2 · i?` · `associational · r2`

DML analysis (random forest nuisance functions, 5-fold cross-fitting) of admission decisions in the 2023 and 2024 cycles, adjusting for around 400 covariates. The main estimate is "a 1.5 p.p. decrease in admission probability for each submitted essay that was AI-written"; the year-specific 2023 estimate was not statistically significant.

> "In the first row of the second column, we estimate a 1.5 p.p. decrease in admission probability for each submitted essay that was AI-written, after controlling for our rich set of covariates, but excluding measures of essay quality because of potential post-treatment bias."

### Calvin Isley 2026 (2)

Calvin Isley, Johann D. Gaebler, and Sharad Goel. (2026). AI-written admissions essays are widespread but penalized. arXiv preprint. https://arxiv.org/abs/2609.22549

`q2 · i?` · `associational · r2`

A specification additionally adjusting for the constructed essay-quality dimensions estimates "a penalty of 2.6 p.p. for each AI-written essay"; the authors note this model may be subject to post-treatment bias since AI-written essays are on average stronger.

> "In this case, the estimated effect increases to a penalty of 2.6 p.p. for each AI-written essay, or about 6.0 p.p. for the typical applicant who used AI."

## Discussion


## Related Claims
- [By the 2025 admissions cycle, a majority of applicants to the studied public policy master's program submitted at least one primarily AI-generated essay despite an explicit prohibition](majority-applicants-submitted-ai-generated-essays-2025.md) — related
- [Admissions staff rate essays they perceive as AI-generated lower than essays they believe are human-written, even after adjusting for measured essay quality and actual AI authorship](perceived-ai-use-lowers-staff-quality-ratings.md) — related
- [The availability of AI assistants improved the quality of submitted admissions essays, particularly mechanical aspects and especially for international applicants](ai-availability-improved-essay-quality.md) — related
- [AI-text detectors misclassify authentic TOEFL essays by non-native English speakers at a mean false-positive rate of 61.3% across seven detectors, far more often than native-speaker essays](detector-61-3-percent-false-positives-non-native-toefl.md) — related
