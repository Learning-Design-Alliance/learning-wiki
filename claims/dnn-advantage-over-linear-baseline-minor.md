---
type: claim
title: Complex DNN architectures offer little advantage over simple linear ridge-regression baselines for trait scoring, implying nonlinearities and interactions were of minor importance
description: Complex DNN architectures offer little advantage over simple linear ridge-regression baselines for trait scoring, implying nonlinearities and interactions were of minor importance
id: dnn-advantage-over-linear-baseline-minor
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
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

# Complex DNN architectures offer little advantage over simple linear ridge-regression baselines for trait scoring, implying nonlinearities and interactions were of minor importance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Comparisons to a feature-based linear regression baseline only partly revealed advantages for the DNN target models, and the T-tests were not significant. [→ Lohmann 2025](#lohmann-2025)

## Evidence

### Lohmann 2025

Lohmann, J. F., Junge, F., Möller, J., Fleckenstein, J., Trüb, R., Keller, S., Jansen, T., & Horbach, A. (2025). Neural Networks or Linguistic Features? - Comparing Different Machine-Learning Approaches for Automated Assessment of Text Quality Traits Among L1- and L2-Learners' Argumentative Essays. International Journal of Artificial Intelligence in Education, 35, 1178–1217. https://doi.org/10.1007/s40593-024-00426-w

`q2 · i?` · `design · r2`

Baseline comparisons in the main experiments used ridge regression with the 220-feature set; the feature DNN even fell short in four of six MEWS traits (average ΔQWK −0.02), while ASAP advantages were small (0.02 and 0.01).

> "comparisons to the feature-based linear regression baseline only partly revealed advantages for the target models, and T-tests were not significant ( pfeatures = 0.818 , pembeddings = 0.465 )."

## Discussion


## Related Claims
- [ANN analysis identifies AI learning self-efficacy and perceived usefulness as the strongest and most stable predictors of AI learning anxiety, with only modest advantage over linear benchmarks](ann-appraisals-strongest-anxiety-predictors.md) — related
- [Quadratic and cubic trends significantly improved the linear model of teacher and student behavior, showing the importance of studying nonlinearity](quadratic-cubic-trends-improve-linear-model-teacher-behavior.md) — related
- [For trait-specific automated essay scoring trained on a single resource, feature-based DNNs slightly outperform embedding-based DNNs, winning 11 of 16 trait-prompt comparisons](feature-models-edge-embeddings-trait-scoring.md) — related
- [Ablation tests identify unique trait-relevant information in specific feature groups: readability and syntactic complexity for content, cohesion and readability for organization, and occurrence, length, or error features for language](ablation-tests-unique-feature-contributions.md) — reports the opposite
- [Addition tests show trait-specific feature groups that most consistently enhance embedding-based models: morphological complexity for content, length for organization, and lexical sophistication, error, and occurrence features for language](addition-tests-trait-specific-feature-groups.md) — reports the opposite
