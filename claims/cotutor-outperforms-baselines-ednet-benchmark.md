---
type: claim
title: COTUTOR outperforms BKT, DKT, and Code-DKT across all evaluation metrics on the EdNet KT1 benchmark
description: COTUTOR outperforms BKT, DKT, and Code-DKT across all evaluation metrics on the EdNet KT1 benchmark
id: cotutor-outperforms-baselines-ednet-benchmark
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: yuchen-wang-2025
    resource: "https://doi.org/10.48550/arXiv.2509.23996"
    title: "Yuchen Wang, Pei-Duo Yu, Chee Wei Tan. (2025). Future-Proofing Programmers: Optimal Knowledge Tracing for AI-Assisted Personalized Education. [doi:10.48550/arXiv.2509.23996](https://doi.org/10.48550/arXiv.2509.23996)"
    author: Yuchen Wang, Pei-Duo Yu, Chee Wei Tan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# COTUTOR outperforms BKT, DKT, and Code-DKT across all evaluation metrics on the EdNet KT1 benchmark

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the EdNet KT1 subset, COTUTOR achieved higher accuracy (84.3%) than BKT (72.5%), DKT (78.9%), and Code-DKT (78.2%), and better AUC-ROC, PR-AUC, RMSE, and NLL. [→ Yuchen Wang 2025](#yuchen-wang-2025)

## Evidence

### Yuchen Wang 2025

Yuchen Wang, Pei-Duo Yu, Chee Wei Tan. (2025). Future-Proofing Programmers: Optimal Knowledge Tracing for AI-Assisted Personalized Education. [doi:10.48550/arXiv.2509.23996](https://doi.org/10.48550/arXiv.2509.23996)

`q2 · i?` · `design · r2`

Benchmark evaluation on EdNet KT1, a subset of a large-scale dataset from the Santa TOEIC tutoring system, comparing COTUTOR against BKT, DKT, and Code-DKT on accuracy, AUC-ROC, PR-AUC, RMSE, and NLL. The article reports COTUTOR "outperforms the baseline models across all evaluation metrics" with 84.3% accuracy versus 78.9% for DKT.

> "Table II summarizes the results of the benchmark evaluation, where COTUTORoutperforms the baseline models across all evaluation metrics, demonstrating its superior ability to track student progress and predict future learning events, thus supportingH1."

## Discussion


## Related Claims
- [COTUTOR achieved the highest prediction accuracy of student performance in the classroom study, outperforming BKT, DKT, and Code-DKT](cotutor-highest-classroom-prediction-accuracy.md) — related
- [In a university AI course, students assisted by COTUTOR achieved the highest average assignment score, exceeding the control group with a medium effect size](cotutor-highest-assignment-scores-controlled-study.md) — related
- [The survey states that deep learning knowledge tracing models exhibit superior performance to Bayesian and logistic models but have significant room for improvement in interpretability.](deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability.md) — a broader claim this one bears on
