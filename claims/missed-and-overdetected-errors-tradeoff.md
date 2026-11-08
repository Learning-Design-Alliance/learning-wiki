---
type: claim
title: "The method missed three errors and overdetected 11 errors (3.6%), with a trade-off between overdetection and oversight"
description: "The method missed three errors and overdetected 11 errors (3.6%), with a trade-off between overdetection and oversight"
id: missed-and-overdetected-errors-tradeoff
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: yamaguchi-tomoko-2022
    resource: "https://doi.org/10.1038/s41598-022-10502-7"
    title: "Yamaguchi Tomoko, Nakamura Ryoichi, Kuboki Akihito, Otori Nobuyoshi. (2022). Clinical study of skill assessment based on time sequential measurement changes. Scientific Reports. https://doi.org/10.1038/s41598-022-10502-7"
    author: Yamaguchi Tomoko, Nakamura Ryoichi, Kuboki Akihito, Otori Nobuyoshi
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The method missed three errors and overdetected 11 errors (3.6%), with a trade-off between overdetection and oversight

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Otolaryngologists' video review found three missed errors and 11 overdetections, constituting 3.6% of all errors. [→ Yamaguchi Tomoko 2022](#yamaguchi-tomoko-2022)
`q1 i?` The authors state a trade-off exists between over-detection and oversight and judge overdetection tolerable because oversight can lead to serious accidents. [→ Yamaguchi Tomoko 2022](#yamaguchi-tomoko-2022)

## Evidence

### Yamaguchi Tomoko 2022

Yamaguchi Tomoko, Nakamura Ryoichi, Kuboki Akihito, Otori Nobuyoshi. (2022). Clinical study of skill assessment based on time sequential measurement changes. Scientific Reports. https://doi.org/10.1038/s41598-022-10502-7

`q2 · i?` · `design · r2`

Validity check by otolaryngologists reviewing surgery videos: "a total of 11 overdetections were confirmed", constituting "3.6% of all errors", alongside three missed errors of two types involving non-visible instrument tips.

> "In addition, some of the errors detected as “type 5: variation in position” and “type 3: proximity of the tips” may have been overdetected. Thus, a total of 11 overdetections were confirmed. This constituted 3.6% of all errors."

## Discussion


## Related Claims
- [LLM graders show model-specific precision/recall trade-offs, so a single metric is insufficient to judge grading quality](llm-grader-precision-recall-tradeoffs-single-metric-insufficient.md) — a broader claim this one bears on
- [Models exhibit a recall–precision trade-off: Logistic Regression and Naïve Bayes maximize recall (0.94) with more false positives, while XGBoost balances recall with stronger precision](recall-precision-tradeoff-early-warning-models.md) — related
