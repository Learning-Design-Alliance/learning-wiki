---
type: claim
title: Tested on coder-disagreement messages, multi-label classifiers labelled most messages into two adjacent phases with one predicted label matching the manual label, and partially correct predictions exceeded half of the set
description: Tested on coder-disagreement messages, multi-label classifiers labelled most messages into two adjacent phases with one predicted label matching the manual label, and partially correct predictions exceeded half of the...
id: disagreementset-partially-correct-adjacent-predictions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
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

# Tested on coder-disagreement messages, multi-label classifiers labelled most messages into two adjacent phases with one predicted label matching the manual label, and partially correct predictions exceeded half of the set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q3 i?` On the DisagreementSet, partially correct predictions accounted for beyond half of the messages, an outcome opposite to the AgreementSet test results. [→ Yuanyuan Hu 2023](#yuanyuan-hu-2023)
`q3 i?` The classifiers labelled most DisagreementSet messages into two adjacent phases, one of which matched the coders' manual labels. [→ Yuanyuan Hu 2023 (2)](#yuanyuan-hu-2023-2)

## Evidence

### Yuanyuan Hu 2023

Yuanyuan Hu. (2023). Can Multi-Label Classifiers Help Identify Subjectivity? A Deep Learning Approach to Classifying Cognitive Presence in MOOCs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00310-5

`q3 · i?` · `design · r2`

Validation of the best-performing multi-label classifiers, trained on the AgreementSet, on the DisagreementSet (Table 6, Fig. 6). "Partially correct" means one of two predicted labels equalled the manual label; here they exceeded half the set, unlike on the AgreementSet.

> "the messages that were labelled partially correct accounted for beyond half of the entire DisagreementSet. This outcome was opposite to the results in the testing AgreementSet (Table 4)."

### Yuanyuan Hu 2023 (2)

Yuanyuan Hu. (2023). Can Multi-Label Classifiers Help Identify Subjectivity? A Deep Learning Approach to Classifying Cognitive Presence in MOOCs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00310-5

`q3 · i?` · `design · r2`

Confusion-matrix analysis (Fig. 6) of predictions on the DisagreementSet. The article reports messages were labelled into either one unique phase or "two adjacent phases", with one predicted label matching the coders' manual label.

> "In contrast, they labelled most of the DisagreementSet messages into two adjacent phases, amongst which one of the predicted labels was the same with the manual labels."

## Discussion


## Related Claims
- [On the DisagreementSet, data augmentation improved the multi-label classifiers' exact match ratio and F1 score, while both ratios declined relative to the AgreementSet test](data-augmentation-improves-disagreementset-performance.md) — related
- [Partially correct predictions on the AgreementSet were mostly Exploration-labelled messages, with Integration more often the alternative predicted label than Triggering event](exploration-integration-partial-prediction-pattern.md) — related
- [Multi-label BERT classifiers slightly outperformed single-label Random Forest baselines on example-based F1 scores but under-performed with lower exact match ratios on MOOC cognitive presence classification](multi-label-bert-f1-beats-rf-exact-match-lower.md) — related
- [Multi-label classifiers predicted MOOC messages as one label or two adjacent cognitive presence phases only, while expert coders produced non-adjacent and three-phase labels on almost 4% of messages](multi-label-predictions-adjacent-phases-only.md) — related
- [Cognitive presence comprises four phases of critical thinking — triggering event, exploration, integration, and resolution — which are not always sequential](coi-cognitive-presence-four-phases.md) — related
