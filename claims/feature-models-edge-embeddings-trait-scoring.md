---
type: claim
title: For trait-specific automated essay scoring trained on a single resource, feature-based DNNs slightly outperform embedding-based DNNs, winning 11 of 16 trait-prompt comparisons
description: For trait-specific automated essay scoring trained on a single resource, feature-based DNNs slightly outperform embedding-based DNNs, winning 11 of 16 trait-prompt comparisons
id: feature-models-edge-embeddings-trait-scoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: lohmann-2025
    resource: "https://doi.org/10.1007/s40593-024-00426-w"
    title: "Lohmann, J. F., Junge, F., Möller, J., Fleckenstein, J., Trüb, R., Keller, S., Jansen, T., & Horbach, A. (2025). Neural Networks or Linguistic Features? - Comparing Different Machine-Learning Approaches for Automated Assessment of Text Quality Traits Among L1- and L2-Learners' Argumentative Essays. International Journal of Artificial Intelligence in Education, 35, 1178–1217. https://doi.org/10.1007/s40593-024-00426-w"
    author: "Lohmann, J. F., Junge, F., Möller, J., Fleckenstein, J., Trüb, R., Keller, S., Jansen, T., & Horbach, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# For trait-specific automated essay scoring trained on a single resource, feature-based DNNs slightly outperform embedding-based DNNs, winning 11 of 16 trait-prompt comparisons

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across traits and prompts, feature-based models outperformed embedding-based models in 11 out of 16 cases, with overall average QWK of 0.614 versus 0.563, and the difference was not statistically significant. [→ Lohmann 2025](#lohmann-2025)

## Evidence

### Lohmann 2025

Lohmann, J. F., Junge, F., Möller, J., Fleckenstein, J., Trüb, R., Keller, S., Jansen, T., & Horbach, A. (2025). Neural Networks or Linguistic Features? - Comparing Different Machine-Learning Approaches for Automated Assessment of Text Quality Traits Among L1- and L2-Learners' Argumentative Essays. International Journal of Artificial Intelligence in Education, 35, 1178–1217. https://doi.org/10.1007/s40593-024-00426-w

`q2 · i?` · `design · r2`

Main cross-validated experiments on four prompts (ASAP L1, MEWS L2) scoring analytic traits; feature DNN averaged QWK 0.614 vs embedding DNN 0.563, with T-tests showing "no significant differences between the two approaches (p = .345)".

> "Across traits and prompts, the feature-based model outperformed the embedding-based model in 11 out of 16 cases. However, the performance of both models was similar."

## Discussion


## Related Claims
- [Addition tests show trait-specific feature groups that most consistently enhance embedding-based models: morphological complexity for content, length for organization, and lexical sophistication, error, and occurrence features for language](addition-tests-trait-specific-feature-groups.md) — related
- [Cross-prompt scoring drops performance by between 0.01 and 0.30 QWK, with feature-based models holding an advantage in cross-prompt settings](cross-prompt-scoring-performance-drop.md) — related
- [Complex DNN architectures offer little advantage over simple linear ridge-regression baselines for trait scoring, implying nonlinearities and interactions were of minor importance](dnn-advantage-over-linear-baseline-minor.md) — related
- [Ablation tests identify unique trait-relevant information in specific feature groups: readability and syntactic complexity for content, cohesion and readability for organization, and occurrence, length, or error features for language](ablation-tests-unique-feature-contributions.md) — related
- [Holistic scoring of German university students' essays posed significant challenges to both a neural model and an SVM with n-gram features](german-essay-scoring-challenges-both-models.md) — related
