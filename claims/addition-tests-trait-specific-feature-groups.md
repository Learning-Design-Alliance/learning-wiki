---
type: claim
title: "Addition tests show trait-specific feature groups that most consistently enhance embedding-based models: morphological complexity for content, length for organization, and lexical sophistication, error, and occurrence features for language"
description: "Addition tests show trait-specific feature groups that most consistently enhance embedding-based models: morphological complexity for content, length for organization, and lexical sophistication, error, and occurrence..."
id: addition-tests-trait-specific-feature-groups
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

# Addition tests show trait-specific feature groups that most consistently enhance embedding-based models: morphological complexity for content, length for organization, and lexical sophistication, error, and occurrence features for language

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Supplementing embedding-based DNNs with one feature group at a time showed content traits gained most from morphological complexity features and organization traits from length features. [→ Lohmann 2025](#lohmann-2025)
`q2 i?` Lexical sophistication, error, and occurrence features were most likely to produce performance gains across the language traits. [→ Lohmann 2025](#lohmann-2025)

## Evidence

### Lohmann 2025

Lohmann, J. F., Junge, F., Möller, J., Fleckenstein, J., Trüb, R., Keller, S., Jansen, T., & Horbach, A. (2025). Neural Networks or Linguistic Features? - Comparing Different Machine-Learning Approaches for Automated Assessment of Text Quality Traits Among L1- and L2-Learners' Argumentative Essays. International Journal of Artificial Intelligence in Education, 35, 1178–1217. https://doi.org/10.1007/s40593-024-00426-w

`q2 · i?` · `design · r2`

Addition tests reran each trait- and prompt-specific embedding model nine times, adding one of nine feature groups; Figure 4 reports the QWK gains per trait and prompt.

> "Across prompts, performance gains on the content traits appeared most often when the morphological complexity features supplemented the contextual embeddings. Supplementing the contextual embedding input, length features turned out to be most important for the organization traits."

## Discussion


## Related Claims
- [Ablation tests identify unique trait-relevant information in specific feature groups: readability and syntactic complexity for content, cohesion and readability for organization, and occurrence, length, or error features for language](ablation-tests-unique-feature-contributions.md) — related
- [The most predictive linguistic features differ across datasets, overlapping only in lexical diversity measures](aes-predictive-features-not-generalizable-across-corpora.md) — related
- [For trait-specific automated essay scoring trained on a single resource, feature-based DNNs slightly outperform embedding-based DNNs, winning 11 of 16 trait-prompt comparisons](feature-models-edge-embeddings-trait-scoring.md) — related
- [A response-length-only baseline scores poorly, showing scores depend on broader linguistic features](length-only-baseline-performs-poorly.md) — related
- [Complex DNN architectures offer little advantage over simple linear ridge-regression baselines for trait scoring, implying nonlinearities and interactions were of minor importance](dnn-advantage-over-linear-baseline-minor.md) — reports the opposite
