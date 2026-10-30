---
type: claim
title: Cross-prompt scoring drops performance by between 0.01 and 0.30 QWK, with feature-based models holding an advantage in cross-prompt settings
description: Cross-prompt scoring drops performance by between 0.01 and 0.30 QWK, with feature-based models holding an advantage in cross-prompt settings
id: cross-prompt-scoring-performance-drop
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
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
    kind: causal
    rigour: 2
---

# Cross-prompt scoring drops performance by between 0.01 and 0.30 QWK, with feature-based models holding an advantage in cross-prompt settings

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across models and traits, cross-prompt performance was lower than within-prompt performance, with QWK drops between 0.01 and 0.30. [→ Lohmann 2025](#lohmann-2025)
`q2 i?` For models trained on the MEWS prompts and ASAP 1, feature-based models outperformed embedding-based models in cross-prompt performance across traits. [→ Lohmann 2025 (2)](#lohmann-2025-2)

## Evidence

### Lohmann 2025

Lohmann, J. F., Junge, F., Möller, J., Fleckenstein, J., Trüb, R., Keller, S., Jansen, T., & Horbach, A. (2025). Neural Networks or Linguistic Features? - Comparing Different Machine-Learning Approaches for Automated Assessment of Text Quality Traits Among L1- and L2-Learners' Argumentative Essays. International Journal of Artificial Intelligence in Education, 35, 1178–1217. https://doi.org/10.1007/s40593-024-00426-w

`q2 · i?` · `design · r2`

Cross-prompt experiments trained on one prompt and tested on the other prompt within each corpus, using the best hyperparameter settings; Tables 5 and 6 report QWK and per-trait drops.

> "The analyses show that across models and traits, the performance drop ( /u1D6E5QWK ) when comparing the within-prompt performance to the cross-prompt performance was between − 0.01 and − 0.30"

### Lohmann 2025 (2)

Lohmann, J. F., Junge, F., Möller, J., Fleckenstein, J., Trüb, R., Keller, S., Jansen, T., & Horbach, A. (2025). Neural Networks or Linguistic Features? - Comparing Different Machine-Learning Approaches for Automated Assessment of Text Quality Traits Among L1- and L2-Learners' Argumentative Essays. International Journal of Artificial Intelligence in Education, 35, 1178–1217. https://doi.org/10.1007/s40593-024-00426-w

`q2 · i?` · `causal · r2`

Same cross-prompt analyses; however, embedding-based models trained on ASAP 2 consistently outperformed the feature-based model in cross-prompt performance, and T-tests revealed no significant cross-prompt advantage for the feature-based DNN.

> "Regarding the models trained on the MEWS prompts and ASAP 1, the feature-based models outperformed the embedding-based models in cross-prompt performance across traits."

## Discussion


## Related Claims
- [For trait-specific automated essay scoring trained on a single resource, feature-based DNNs slightly outperform embedding-based DNNs, winning 11 of 16 trait-prompt comparisons](feature-models-edge-embeddings-trait-scoring.md) — related
- [Holistic scoring of German university students' essays posed significant challenges to both a neural model and an SVM with n-gram features](german-essay-scoring-challenges-both-models.md) — related
