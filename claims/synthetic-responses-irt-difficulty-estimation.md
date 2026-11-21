---
type: claim
title: IRT difficulty parameters can be estimated without student testing via simulated responses, reaching a Pearson correlation of 0.7791 with benchmark difficulty on unseen questions
description: IRT difficulty parameters can be estimated without student testing via simulated responses, reaching a Pearson correlation of 0.7791 with benchmark difficulty on unseen questions
id: synthetic-responses-irt-difficulty-estimation
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

# IRT difficulty parameters can be estimated without student testing via simulated responses, reaching a Pearson correlation of 0.7791 with benchmark difficulty on unseen questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A two-stage model that simulates student responses and applies 1PL IRT estimation yields difficulty parameters correlating 0.7791 (Pearson) and 0.7606 (Spearman) with benchmark parameters on 470 holdout questions. [→ Matías Hoyl 2026](#matias-hoyl-2026)

## Evidence

### Matías Hoyl 2026

Matías Hoyl. (2026). Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation. arXiv. [doi:10.48550/arXiv.2602.00034](https://doi.org/10.48550/arXiv.2602.00034)

`q2 · i?` · `design · r2`

Evaluation on the 470-question holdout test set of a dataset of 251,851 student responses to mathematics questions; the printed table reports "Pearson correlation 0.7791", Spearman 0.7606, and RMSE 1.1857 against benchmark 1PL parameters. No standardised effect size is printed for this finding, so impact is coded i? (no magnitude reported; not a null effect).

> "The final model achieved a Pearson correlation of approximately 0.78 (Spearman correlation ~0.76) between its predicted 1PL IRT difficulty parameters and benchmark 1PL parameters derived from actual student data, when evaluated on completely unseen questions."

## Discussion


## Related Claims
- [Adding LLM-extracted pedagogical features raises difficulty-prediction correlation from about 0.68 to about 0.78 over embeddings and traditional features](llm-pedagogical-features-drive-difficulty-gain.md) — related
- [Simulated-response difficulty estimates match the accuracy of a traditional 1PL analysis using approximately 5,818 real student answers (about 22.87% of available data)](rmse-efficiency-5818-real-answers.md) — related
- [The simulated-respondent approach recovers the guessing parameter c at correlation 0.48, far above regression baselines, suggesting it captures genuine response behavior](simulated-respondents-recover-guessing-parameter-048.md) — related
