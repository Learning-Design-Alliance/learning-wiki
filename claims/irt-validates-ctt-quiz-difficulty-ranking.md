---
type: claim
title: CTT-based quiz difficulty rankings are validated by IRT analysis with near-perfect rank correlation
description: CTT-based quiz difficulty rankings are validated by IRT analysis with near-perfect rank correlation
id: irt-validates-ctt-quiz-difficulty-ranking
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: parker-2026
    resource: "https://doi.org/10.48550/arxiv.2605.00294"
    title: "Parker, M. J., & Zavala-Cerna, M. G. (2026). What Don't You Understand? Using Large Language Models to Identify and Characterize Student Misconceptions About Challenging Topics. https://arxiv.org/abs/2605.00294 Originally published 2025. [doi:10.48550/arxiv.2605.00294](https://doi.org/10.48550/arxiv.2605.00294)"
    author: "Parker, M. J., & Zavala-Cerna, M. G."
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# CTT-based quiz difficulty rankings are validated by IRT analysis with near-perfect rank correlation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` A 1-parameter logistic (Rasch) IRT model produces quiz difficulty rankings that correlate nearly perfectly with classical test theory rankings for Immunology. [→ Parker 2026](#parker-2026)

## Evidence

### Parker 2026

Parker, M. J., & Zavala-Cerna, M. G. (2026). What Don't You Understand? Using Large Language Models to Identify and Characterize Student Misconceptions About Challenging Topics. https://arxiv.org/abs/2605.00294 Originally published 2025. [doi:10.48550/arxiv.2605.00294](https://doi.org/10.48550/arxiv.2605.00294)

`q3 · i?` · `associational · r2`

IRT validation using the py-irt package on results from 765 Immunology students across three cohorts. "The Spearman correlation was .99, p < 10-5" between IRT-based and CTT-based quiz difficulty rankings, supporting the simpler CTT approach.

> "the Spearman correlation against the CTT ranking of those same quizzes was taken. The Spearman correlation was .99, p < 10-5"

## Discussion


## Related Claims
- [CTT and MFRM yield a positive, perfect correlation between item difficulty indices for open-ended items under a crossed design](ctt-mfrm-difficulty-indices-perfect-correlation-open-ended.md) — related
- [CTT and MFRM yield similar item difficulty results for open-ended questions regardless of crossed or nested design](ctt-mfrm-agreement-robust-to-design.md) — related
- [Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)](llm-difficulty-magnitude-error-varies-across-models.md) — related
- [Quiz-level first-attempt performance analysis across cohorts identifies persistently challenging topics in online biomedical science courses](quiz-level-cross-cohort-analysis-identifies-persistent-challenging-topics.md) — related
- [Items ranked from easiest to most difficult are identical under CTT and MFRM](identical-item-difficulty-ranking-ctt-mfrm.md) — related
- [In operational reading-test data, item parameter estimates from a standard 2PL/GPCM that ignores local dependence closely match those from the testlet model (average correlations 0.9893 and 0.9978)](local-dependence-small-impact-item-parameters-real-data.md) — related
- [Item response theory analysis identifies image optimization, structure diameter, and structure surface distance as the most difficult assessment items](irt-identifies-most-difficult-ultrasound-items.md) — related
- [Class-average Δθ correlates strongly with ⟨g⟩ (r = 0.99), and an IAS of 25% is necessary but not sufficient for average Δθ > 1](class-average-delta-theta-ias-25-percent.md) — related
- [Rasch-model difficulty estimates confirmed the three test sets were of augmented difficulty and that Post-Tests were less difficult than their corresponding Pre-Tests](rasch-difficulty-pre-post-tests.md) — related
