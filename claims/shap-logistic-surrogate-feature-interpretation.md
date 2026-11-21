---
type: claim
title: "SHAP analysis on a logistic regression surrogate over One Encoder's size-1 embeddings makes the deep model interpretable at the feature level with similar predictive performance (0.880 accuracy, 0.878 ROCAUC)"
description: "SHAP analysis on a logistic regression surrogate over One Encoder's size-1 embeddings makes the deep model interpretable at the feature level with similar predictive performance (0.880 accuracy, 0.878 ROCAUC)"
id: shap-logistic-surrogate-feature-interpretation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: xinzhe-zheng-2025
    resource: "https://doi.org/10.48550/arXiv.2509.00863"
    title: "Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng. (2025). Predicting Multi-Type Talented Students in Secondary School Using Semi-Supervised Machine Learning. arXiv. [doi:10.48550/arXiv.2509.00863](https://doi.org/10.48550/arXiv.2509.00863)"
    author: Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SHAP analysis on a logistic regression surrogate over One Encoder's size-1 embeddings makes the deep model interpretable at the feature level with similar predictive performance (0.880 accuracy, 0.878 ROCAUC)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Replacing the final classifier with logistic regression preserves performance close to the best method, enabling SHAP-based per-feature interpretation. [→ Xinzhe Zheng 2025](#xinzhe-zheng-2025)

## Evidence

### Xinzhe Zheng 2025

Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng. (2025). Predicting Multi-Type Talented Students in Secondary School Using Semi-Supervised Machine Learning. arXiv. [doi:10.48550/arXiv.2509.00863](https://doi.org/10.48550/arXiv.2509.00863)

`q2 · i?` · `design · r2`

Interpretation analysis in the Results section: SHAP values are computed with logistic regression consuming the size-1 One Encoder embeddings before final concatenation, so each embedding represents one feature. The article reports test accuracy of 0.880 and ROCAUC of 0.878.

> "the prediction performance of using logistic regression as the final classifier is 0.880 and 0.878 for test accuracy and ROCAUC respectively. We can see performance is similar to our best method"

## Discussion


## Related Claims
- [The compact One Encoder gives a more balanced, stable and less overfitted predictor than the Raw Encoder, with higher average test ROCAUC (0.882 vs 0.860)](one-encoder-outperforms-raw-encoder-balance.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — a broader claim this one bears on
- [Which knowledge-tracing model predicts learner performance best depends on the data, with logistic regression leading on smaller datasets and very long learner histories and deep knowledge tracing on large or sequential ones](knowledge-tracing-model-choice-depends-on-dataset.md) — related
- [TalentPredictor predicts seven talent types in secondary school students with a best test micro ROCAUC of 0.908 on a real-world dataset of 1,041 students](talentpredictor-0908-micro-rocauc-seven-talent-types.md) — a broader claim this one bears on
