---
type: claim
title: "Simulated-response difficulty estimates match the accuracy of a traditional 1PL analysis using approximately 5,818 real student answers (about 22.87% of available data)"
description: "Simulated-response difficulty estimates match the accuracy of a traditional 1PL analysis using approximately 5,818 real student answers (about 22.87% of available data)"
id: rmse-efficiency-5818-real-answers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: matías-hoyl-2026
    resource: "https://doi.org/10.48550/arXiv.2602.00034"
    title: "Matías Hoyl. (2026). Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation. arXiv. [doi:10.48550/arXiv.2602.00034](https://doi.org/10.48550/arXiv.2602.00034)"
    author: Matías Hoyl
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Simulated-response difficulty estimates match the accuracy of a traditional 1PL analysis using approximately 5,818 real student answers (about 22.87% of available data)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The model's RMSE of 1.1857 against ground-truth difficulty equals what traditional 1PL IRT estimation achieves with approximately 5,818 real student answers for the 470 holdout questions, roughly 22.87% of available responses. [→ Matías Hoyl 2026](#matias-hoyl-2026)

## Evidence

### Matías Hoyl 2026

Matías Hoyl. (2026). Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation. arXiv. [doi:10.48550/arXiv.2602.00034](https://doi.org/10.48550/arXiv.2602.00034)

`q2 · i?` · `design · r2`

RMSE-based efficiency evaluation: traditional 1PL IRT was simulated on subsamples of real student responses from 1% to 100%, repeated 10 times per percentage, and RMSE was averaged; the model's RMSE was 1.1857. The equivalence figure of about 5,818 answers (22.87%) is the article's own comparison, not a tested causal effect.

> "This comparison reveals that our model’s difficulty estimates achieve an accuracy comparable to what a traditional 1PL IRT analysis would achieve if it used approximately 5,818 real student answers for these 470 holdout questions."

## Discussion


## Related Claims
- [IRT difficulty parameters can be estimated without student testing via simulated responses, reaching a Pearson correlation of 0.7791 with benchmark difficulty on unseen questions](synthetic-responses-irt-difficulty-estimation.md) — related
- [Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)](llm-difficulty-magnitude-error-varies-across-models.md) — related
