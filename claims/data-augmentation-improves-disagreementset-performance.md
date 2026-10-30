---
type: claim
title: "On the DisagreementSet, data augmentation improved the multi-label classifiers' exact match ratio and F1 score, while both ratios declined relative to the AgreementSet test"
description: "On the DisagreementSet, data augmentation improved the multi-label classifiers' exact match ratio and F1 score, while both ratios declined relative to the AgreementSet test"
id: data-augmentation-improves-disagreementset-performance
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
---

# On the DisagreementSet, data augmentation improved the multi-label classifiers' exact match ratio and F1 score, while both ratios declined relative to the AgreementSet test

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Testing the best-performing classifiers on the DisagreementSet, using the data augmentation method improved the exact match ratio and the F1 score compared with the classifiers without DA. [→ Yuanyuan Hu 2023](#yuanyuan-hu-2023)

## Evidence

### Yuanyuan Hu 2023

Yuanyuan Hu. (2023). Can Multi-Label Classifiers Help Identify Subjectivity? A Deep Learning Approach to Classifying Cognitive Presence in MOOCs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00310-5

`q3 · i?` · `design · r2`

Validation test of the multi-label classifiers on the coder-disagreement messages (Table 6). "The exact match ratio and the F1 score were improved by using the DA method", while relative to the AgreementSet test the exact match and fully incorrect ratios largely declined.

> "The exact match ratio and the F1 score were improved by using the DA method. Compared to the results of the AgreementSet in Table 4, we found the F1 score reached the similar value in the test with the DA method, but the exact match ratio and the fully incorrect ratio largely declined."

## Discussion


## Related Claims
- [Multi-label BERT classifiers slightly outperformed single-label Random Forest baselines on example-based F1 scores but under-performed with lower exact match ratios on MOOC cognitive presence classification](multi-label-bert-f1-beats-rf-exact-match-lower.md) — related
- [Tested on coder-disagreement messages, multi-label classifiers labelled most messages into two adjacent phases with one predicted label matching the manual label, and partially correct predictions exceeded half of the set](disagreementset-partially-correct-adjacent-predictions.md) — related
- [Multi-label classifiers predicted MOOC messages as one label or two adjacent cognitive presence phases only, while expert coders produced non-adjacent and three-phase labels on almost 4% of messages](multi-label-predictions-adjacent-phases-only.md) — related
