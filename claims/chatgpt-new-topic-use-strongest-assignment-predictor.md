---
type: claim
title: Frequency of using ChatGPT for learning new topics is the strongest predictor of assignment-related ChatGPT use
description: Frequency of using ChatGPT for learning new topics is the strongest predictor of assignment-related ChatGPT use
id: chatgpt-new-topic-use-strongest-assignment-predictor
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: surajit-das-and-aleksei-eliseev-2025
    resource: "https://doi.org/10.48550/arXiv.2508.12013"
    title: "Surajit Das and Aleksei Eliseev. (2025). Predicting ChatGPT Use in Assignments: Implications for AI-Aware Assessment Design. arXiv preprint. [doi:10.48550/arXiv.2508.12013](https://doi.org/10.48550/arXiv.2508.12013)"
    author: Surajit Das and Aleksei Eliseev
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: surajit-das-and-aleksei-eliseev-2025-2
    resource: "https://doi.org/10.48550/arXiv.2508.12013"
    title: "Surajit Das and Aleksei Eliseev. (2025). Predicting ChatGPT Use in Assignments: Implications for AI-Aware Assessment Design. arXiv preprint. [doi:10.48550/arXiv.2508.12013](https://doi.org/10.48550/arXiv.2508.12013)"
    author: Surajit Das and Aleksei Eliseev
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Frequency of using ChatGPT for learning new topics is the strongest predictor of assignment-related ChatGPT use

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` SHAP analysis of the binary model identified ChatGPT_Used_in_New_Learning as the most impactful variable, with mean absolute SHAP value of 0.500. [→ Surajit Das and Aleksei Eliseev 2025](#surajit-das-and-aleksei-eliseev-2025)
`q2 i?` Gain-based feature importance corroborated the SHAP findings, ranking ChatGPT_Used_in_New_Learning first with gain 20.30. [→ Surajit Das and Aleksei Eliseev 2025 (2)](#surajit-das-and-aleksei-eliseev-2025-2)

## Evidence

### Surajit Das and Aleksei Eliseev 2025

Surajit Das and Aleksei Eliseev. (2025). Predicting ChatGPT Use in Assignments: Implications for AI-Aware Assessment Design. arXiv preprint. [doi:10.48550/arXiv.2508.12013](https://doi.org/10.48550/arXiv.2508.12013)

`q2 · i?` · `associational · r1`

SHAP summary analysis of the binary XGBoost model's top 15 features. The article identifies 'The most impactful variable was ChatGPT_Used_in_New_Learning' at 'mean | SHAP value | = 0.500', linking frequent use for new topics to assignment use.

> "The most impactful variable was ChatGPT_Used_in_New_Learning (mean | SHAP value | = 0.500), indicating that students who frequently use generative AI tools for learning new topics are substantially more likely to use it for assignment preparation as well."

### Surajit Das and Aleksei Eliseev 2025 (2)

Surajit Das and Aleksei Eliseev. (2025). Predicting ChatGPT Use in Assignments: Implications for AI-Aware Assessment Design. arXiv preprint. [doi:10.48550/arXiv.2508.12013](https://doi.org/10.48550/arXiv.2508.12013)

`q2 · i?` · `associational · r1`

Gain-based importance analysis from the same binary XGBoost model, which the article says corroborated the SHAP findings: 'The top three features areChatGPT_Used_in_New_Learning (20.30),ChatGPT_Education_Integration(11.42)& ChatGPT_4_Non_Performer(10.40)'.

> "The top three features areChatGPT_Used_in_New_Learning (20.30),ChatGPT_Education_Integration(11.42)& ChatGPT_4_Non_Performer(10.40)."

## Discussion


## Related Claims
- [ChatGPT-related attitudinal and behavioral variables dominate early association and predictive-power screening of survey features](chatgpt-features-dominate-eda-screening.md) — possibly the same claim (merge candidate)
- [Demographic variables such as sex, institution and country had near-zero influence on predicted ChatGPT assignment use](demographics-near-zero-influence-chatgpt-use.md) — related
- [An XGBoost binary classifier predicts self-reported ChatGPT use in academic assignments with 80.1% test accuracy](xgboost-binary-predicts-chatgpt-assignment-use.md) — related
