---
type: claim
title: CTT-based quiz difficulty rankings are validated by IRT analysis with near-perfect rank correlation
description: CTT-based quiz difficulty rankings are validated by IRT analysis with near-perfect rank correlation
id: irt-validates-ctt-quiz-difficulty-ranking
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: parker-2025
    resource: "https://arxiv.org/abs/2605.00294"
    title: "Parker, M. J., & Zavala-Cerna, M. G. (2025). What Don't You Understand? Using Large Language Models to Identify and Characterize Student Misconceptions About Challenging Topics. https://arxiv.org/abs/2605.00294"
    author: "Parker, M. J., & Zavala-Cerna, M. G."
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# CTT-based quiz difficulty rankings are validated by IRT analysis with near-perfect rank correlation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`

## Subclaims
`q3 i?` A 1-parameter logistic (Rasch) IRT model produces quiz difficulty rankings that correlate nearly perfectly with classical test theory rankings for Immunology. [→ Parker 2025](#parker-2025)

## Evidence

### Parker 2025

Parker, M. J., & Zavala-Cerna, M. G. (2025). What Don't You Understand? Using Large Language Models to Identify and Characterize Student Misconceptions About Challenging Topics. https://arxiv.org/abs/2605.00294

`q3 · i?` · `associational · r2`

IRT validation using the py-irt package on results from 765 Immunology students across three cohorts. "The Spearman correlation was .99, p < 10-5" between IRT-based and CTT-based quiz difficulty rankings, supporting the simpler CTT approach.

> "the Spearman correlation against the CTT ranking of those same quizzes was taken. The Spearman correlation was .99, p < 10-5"

## Discussion


## Related Claims
- [CTT and MFRM yield a positive, perfect correlation between item difficulty indices for open-ended items under a crossed design](ctt-mfrm-difficulty-indices-perfect-correlation-open-ended.md) — related
- [CTT and MFRM yield similar item difficulty results for open-ended questions regardless of crossed or nested design](ctt-mfrm-agreement-robust-to-design.md) — related
- [Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)](llm-difficulty-magnitude-error-varies-across-models.md) — related
- [Quiz-level first-attempt performance analysis across cohorts identifies persistently challenging topics in online biomedical science courses](quiz-level-cross-cohort-analysis-identifies-persistent-challenging-topics.md) — related
