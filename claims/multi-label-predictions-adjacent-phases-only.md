---
type: claim
title: "Multi-label classifiers predicted MOOC messages as one label or two adjacent cognitive presence phases only, while expert coders produced non-adjacent and three-phase labels on almost 4% of messages"
description: "Multi-label classifiers predicted MOOC messages as one label or two adjacent cognitive presence phases only, while expert coders produced non-adjacent and three-phase labels on almost 4% of messages"
id: multi-label-predictions-adjacent-phases-only
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: yuanyuan-hu-2023
    resource: "https://doi.org/10.1007/s40593-022-00310-5"
    title: "Yuanyuan Hu. (2023). Can Multi-Label Classifiers Help Identify Subjectivity? A Deep Learning Approach to Classifying Cognitive Presence in MOOCs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00310-5"
    author: Yuanyuan Hu
    q: 3
    i: "?"
    kind: design
    rigour: 2
  - id: yuanyuan-hu-2023-2
    resource: "https://doi.org/10.1007/s40593-022-00310-5"
    title: "Yuanyuan Hu. (2023). Can Multi-Label Classifiers Help Identify Subjectivity? A Deep Learning Approach to Classifying Cognitive Presence in MOOCs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00310-5"
    author: Yuanyuan Hu
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Multi-label classifiers predicted MOOC messages as one label or two adjacent cognitive presence phases only, while expert coders produced non-adjacent and three-phase labels on almost 4% of messages

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Across tests on both the AgreementSet and DisagreementSet, the multi-label classifiers never predicted more than two labels, and all two-label predictions were adjacent phases. [→ Yuanyuan Hu 2023](#yuanyuan-hu-2023)
`q3 i?` By contrast, expert coders labelled almost 4% of messages into two non-adjacent phases or even three phases, which the authors treat as possibly subjectively incorrect categorisation. [→ Yuanyuan Hu 2023 (2)](#yuanyuan-hu-2023-2)

## Evidence

### Yuanyuan Hu 2023

Yuanyuan Hu. (2023). Can Multi-Label Classifiers Help Identify Subjectivity? A Deep Learning Approach to Classifying Cognitive Presence in MOOCs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00310-5

`q3 · i?` · `design · r2`

Analysis of prediction outputs across the multi-label classification experiments on both test sets. The article found "the maximum number of predicted labels was not more than two" and that every two-label prediction paired adjacent cognitive presence phases.

> "the maximum number of predicted labels was not more than two in the multi-label classification experiments including the tests on the AgreementSet and DisagreementSet, and all the two-label predictions were adjacent phases of cognitive presence."

### Yuanyuan Hu 2023 (2)

Yuanyuan Hu. (2023). Can Multi-Label Classifiers Help Identify Subjectivity? A Deep Learning Approach to Classifying Cognitive Presence in MOOCs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00310-5

`q3 · i?` · `design · r2`

Analysis of the three expert coders' categorisation of the sample (Table 3). The article states "almost 4% of the messages" received non-adjacent or three-phase labels, framed as potentially subjectively incorrect, contrasting with the classifier's adjacent-only outputs.

> "In contrast, almost 4% of the messages in the categorisation results by the expert coders (Table 3) were labelled into two non-adjacent phases or even three phases, which could be subjectively incorrect categorisation."

## Discussion


## Related Claims
- [Partially correct predictions on the AgreementSet were mostly Exploration-labelled messages, with Integration more often the alternative predicted label than Triggering event](exploration-integration-partial-prediction-pattern.md) — related
- [Tested on coder-disagreement messages, multi-label classifiers labelled most messages into two adjacent phases with one predicted label matching the manual label, and partially correct predictions exceeded half of the set](disagreementset-partially-correct-adjacent-predictions.md) — related
- [Multi-label BERT classifiers slightly outperformed single-label Random Forest baselines on example-based F1 scores but under-performed with lower exact match ratios on MOOC cognitive presence classification](multi-label-bert-f1-beats-rf-exact-match-lower.md) — related
- [On the DisagreementSet, data augmentation improved the multi-label classifiers' exact match ratio and F1 score, while both ratios declined relative to the AgreementSet test](data-augmentation-improves-disagreementset-performance.md) — related
- [Previous automated single-label classifiers of cognitive presence risked inheriting the subjectivity of manual categorisation from their training data preparation](single-label-classifiers-inherit-coder-subjectivity.md) — related
