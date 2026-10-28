---
type: claim
title: "Ablation tests identify unique trait-relevant information in specific feature groups: readability and syntactic complexity for content, cohesion and readability for organization, and occurrence, length, or error features for language"
description: "Ablation tests identify unique trait-relevant information in specific feature groups: readability and syntactic complexity for content, cohesion and readability for organization, and occurrence, length, or error featu..."
id: ablation-tests-unique-feature-contributions
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
  - id: lohmann-2025-2
    resource: "https://doi.org/10.1007/s40593-024-00426-w"
    title: "Lohmann, J. F., Junge, F., Möller, J., Fleckenstein, J., Trüb, R., Keller, S., Jansen, T., & Horbach, A. (2025). Neural Networks or Linguistic Features? - Comparing Different Machine-Learning Approaches for Automated Assessment of Text Quality Traits Among L1- and L2-Learners' Argumentative Essays. International Journal of Artificial Intelligence in Education, 35, 1178–1217. https://doi.org/10.1007/s40593-024-00426-w"
    author: "Lohmann, J. F., Junge, F., Möller, J., Fleckenstein, J., Trüb, R., Keller, S., Jansen, T., & Horbach, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Ablation tests identify unique trait-relevant information in specific feature groups: readability and syntactic complexity for content, cohesion and readability for organization, and occurrence, length, or error features for language

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Removing readability and syntactic complexity features dropped content-trait performance across all four prompts, indicating information the embeddings and other features could not capture. [→ Lohmann 2025](#lohmann-2025)
`q2 i?` Length features emerged as an essential feature type across traits, capturing unique text characteristics. [→ Lohmann 2025 (2)](#lohmann-2025-2)

## Evidence

### Lohmann 2025

Lohmann, J. F., Junge, F., Möller, J., Fleckenstein, J., Trüb, R., Keller, S., Jansen, T., & Horbach, A. (2025). Neural Networks or Linguistic Features? - Comparing Different Machine-Learning Approaches for Automated Assessment of Text Quality Traits Among L1- and L2-Learners' Argumentative Essays. International Journal of Artificial Intelligence in Education, 35, 1178–1217. https://doi.org/10.1007/s40593-024-00426-w

`q2 · i?` · `design · r2`

Ablation tests iteratively removed one of nine feature groups from the full hybrid model, rerunning each trait- and prompt-specific model; Figure 5 shows the performance drops.

> "the performance of models for the content traits dropped across all four prompts when readability and syntactic complexity features were removed."

### Lohmann 2025 (2)

Lohmann, J. F., Junge, F., Möller, J., Fleckenstein, J., Trüb, R., Keller, S., Jansen, T., & Horbach, A. (2025). Neural Networks or Linguistic Features? - Comparing Different Machine-Learning Approaches for Automated Assessment of Text Quality Traits Among L1- and L2-Learners' Argumentative Essays. International Journal of Artificial Intelligence in Education, 35, 1178–1217. https://doi.org/10.1007/s40593-024-00426-w

`q2 · i?` · `design · r2`

Same ablation series on the hybrid models; consistent drops across prompts indicated a feature type contains trait-relevant information not captured by embeddings or other features.

> "Throughout traits, length features, in particular, emerged as an essential feature type capturing important and unique text characteristics for judging the student essays."

## Discussion


## Related Claims
- [Addition tests show trait-specific feature groups that most consistently enhance embedding-based models: morphological complexity for content, length for organization, and lexical sophistication, error, and occurrence features for language](addition-tests-trait-specific-feature-groups.md) — related
- [A response-length-only baseline scores poorly, showing scores depend on broader linguistic features](length-only-baseline-performs-poorly.md) — related
- [For trait-specific automated essay scoring trained on a single resource, feature-based DNNs slightly outperform embedding-based DNNs, winning 11 of 16 trait-prompt comparisons](feature-models-edge-embeddings-trait-scoring.md) — related
- [Adding fluency features to content features sharply increases scoring QWK for every prompt](fluency-features-sharp-qwk-increase-ablation.md) — related
- [Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs](ablation-all-features-maximize-auc.md) — related
- [Removing grammar and vocabulary features drops scoring QWK by 7-13% across prompts](gvf-removal-drops-qwk-7-13-percent.md) — related
- [Complex DNN architectures offer little advantage over simple linear ridge-regression baselines for trait scoring, implying nonlinearities and interactions were of minor importance](dnn-advantage-over-linear-baseline-minor.md) — reports the opposite
