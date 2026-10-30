---
type: claim
title: "Holistic scoring of German university students' essays posed significant challenges to both a neural model and an SVM with n-gram features"
description: "Holistic scoring of German university students' essays posed significant challenges to both a neural model and an SVM with n-gram features"
id: german-essay-scoring-challenges-both-models
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: xiaoyu-bai-manfred-stede-2023
    resource: "https://doi.org/10.1007/s40593-022-00323-0"
    title: "Xiaoyu Bai · Manfred Stede. (2023). A Survey of Current Machine Learning Approaches to Student Free-Text Evaluation for Intelligent Tutoring. International Journal of Artificial Intelligence in Education (2023) 33:994–1032. https://doi.org/10.1007/s40593-022-00323-0"
    author: Xiaoyu Bai · Manfred Stede
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# Holistic scoring of German university students' essays posed significant challenges to both a neural model and an SVM with n-gram features

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Horbach et al. (2017) found that scoring German essays posed significant challenges to both the Taghipour and Ng (2016) neural model and an SVM using n-gram features. [→ Xiaoyu Bai · Manfred Stede 2023](#xiaoyu-bai-manfred-stede-2023)

## Evidence

### Xiaoyu Bai · Manfred Stede 2023

Xiaoyu Bai · Manfred Stede. (2023). A Survey of Current Machine Learning Approaches to Student Free-Text Evaluation for Intelligent Tutoring. International Journal of Artificial Intelligence in Education (2023) 33:994–1032. https://doi.org/10.1007/s40593-022-00323-0

`q2 · i?` · `review · r2`

The survey describes Horbach et al. (2017)'s work on essays written in German by native-speaker university students, predicting holistic and rubric scores. The survey attributes the difficulty to the German language and the high writing proficiency of the essays. No effect size is printed.

> "They experimented with both the neural model by Taghipour and Ng (2016) and an SVM using n-gram features and found that their task posed significant challenges to either model."

## Discussion


## Related Claims
- [Cross-prompt scoring drops performance by between 0.01 and 0.30 QWK, with feature-based models holding an advantage in cross-prompt settings](cross-prompt-scoring-performance-drop.md) — related
- [For trait-specific automated essay scoring trained on a single resource, feature-based DNNs slightly outperform embedding-based DNNs, winning 11 of 16 trait-prompt comparisons](feature-models-edge-embeddings-trait-scoring.md) — related
- [Concatenating hand-crafted linguistic features with neural essay representations significantly increases essay scoring performance](hybrid-features-boost-essay-scoring.md) — related
- [Where labelled training data is limited, adding hand-crafted features improves the performance of neural text evaluation models](handcrafted-features-improve-neural-low-resource.md) — related
- [Ablation tests identify unique trait-relevant information in specific feature groups: readability and syntactic complexity for content, cohesion and readability for organization, and occurrence, length, or error features for language](ablation-tests-unique-feature-contributions.md) — related
- [Character-level embeddings increase robustness to student misspellings, but spelling correction as pre-processing was found more effective](character-embeddings-misspelling-robustness-mixed.md) — related
