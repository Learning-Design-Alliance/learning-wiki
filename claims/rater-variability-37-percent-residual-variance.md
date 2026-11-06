---
type: claim
title: "Rater variability accounted for 37% of residual variance in faculty total scores and 52% in communication scores"
description: "Rater variability accounted for 37% of residual variance in faculty total scores and 52% in communication scores"
id: rater-variability-37-percent-residual-variance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: gao-xiaoxing-2026
    resource: "https://doi.org/10.2196/95578"
    title: "Gao Xiaoxing, Huang Xiaoming, Hu Rongrong, Zhang Li, Liu Huiting, Zhang Bingqing, Wei Chong, Qiu Wei, Zhang Mengyu, Sun Xuefeng. (2026). Evaluating Large Language Model–Based Automated Scoring in a Voice-Based Virtual Standardized Patient Platform for Medical Students: Cross-Sectional Agreement Study. JMIR Medical Education. https://doi.org/10.2196/95578"
    author: Gao Xiaoxing, Huang Xiaoming, Hu Rongrong, Zhang Li, Liu Huiting, Zhang Bingqing, Wei Chong, Qiu Wei, Zhang Mengyu, Sun Xuefeng
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# Rater variability accounted for 37% of residual variance in faculty total scores and 52% in communication scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` A random intercept for rater yielded a variance partition coefficient of 0.37 for total scores, indicating substantial between-rater severity differences. [→ Gao Xiaoxing 2026](#gao-xiaoxing-2026)

## Evidence

### Gao Xiaoxing 2026

Gao Xiaoxing, Huang Xiaoming, Hu Rongrong, Zhang Li, Liu Huiting, Zhang Bingqing, Wei Chong, Qiu Wei, Zhang Mengyu, Sun Xuefeng. (2026). Evaluating Large Language Model–Based Automated Scoring in a Voice-Based Virtual Standardized Patient Platform for Medical Students: Cross-Sectional Agreement Study. JMIR Medical Education. https://doi.org/10.2196/95578

`q3 · i?` · `associational · r2`

Rater-clustering analysis in the 92-student VSP study fit a linear mixed-effects model with a rater random intercept. The article states this "indicates that 37% of the unexplained variance in human total scores was attributable to between-rater differences in average scoring severity or leniency," and accounting for clustering improved fit (ΔAIC=19.10).

> "A linear mixed-effects model with fixed effects for the AI total score and case and a random intercept for rater showed notable rater dependence (Var[rater]=3.05; Var[residual]=5.29), yielding a VPC of 0.37."

## Discussion


## Related Claims
- [AI-faculty agreement was stronger for information gathering than for communication skills](llm-agreement-stronger-information-gathering-than-communication.md) — related
- [Grading variability: 40.7% of grade variance lies between teachers and essay quality is the largest random effect](variance-decomposition-teacher-grading.md) — related
- [Inter-assessor agreement on OSCE scores is substantial, with a pooled intraclass correlation coefficient of 0.77](pt-osce-icc-assessors-substantial.md) — related
- [Raters using the tool discriminate between facilitation videos depicting positive, mixed and negative influence on learning, with all pairwise mean differences significant at p < 0.001](fbat-discriminates-video-levels.md) — related
