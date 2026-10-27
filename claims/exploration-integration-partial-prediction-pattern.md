---
type: claim
title: Partially correct predictions on the AgreementSet were mostly Exploration-labelled messages, with Integration more often the alternative predicted label than Triggering event
description: Partially correct predictions on the AgreementSet were mostly Exploration-labelled messages, with Integration more often the alternative predicted label than Triggering event
id: exploration-integration-partial-prediction-pattern
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
---

# Partially correct predictions on the AgreementSet were mostly Exploration-labelled messages, with Integration more often the alternative predicted label than Triggering event

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Among the partially correct predictions of the best-performing multi-label classifier, most messages had the manual label of Exploration, and Integration appeared more often than Triggering event as the alternative label. [→ Yuanyuan Hu 2023](#yuanyuan-hu-2023)

## Evidence

### Yuanyuan Hu 2023

Yuanyuan Hu. (2023). Can Multi-Label Classifiers Help Identify Subjectivity? A Deep Learning Approach to Classifying Cognitive Presence in MOOCs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00310-5

`q3 · i?` · `design · r2`

Qualitative and scatter-plot analysis (Figs. 7-11, Table 8) of the partially correct predictions from the best multi-label classifier with DA. "Most of the partially correct predictions had the manual label of Exploration", and the alternative label was more often Integration than Triggering event.

> "Most of the partially correct predictions had the manual label of Exploration (Fig. 9). They had more of the alternatively predicted label of Integration than Triggering event."

## Discussion


## Related Claims
- [Tested on coder-disagreement messages, multi-label classifiers labelled most messages into two adjacent phases with one predicted label matching the manual label, and partially correct predictions exceeded half of the set](disagreementset-partially-correct-adjacent-predictions.md) — related
- [Multi-label classifiers predicted MOOC messages as one label or two adjacent cognitive presence phases only, while expert coders produced non-adjacent and three-phase labels on almost 4% of messages](multi-label-predictions-adjacent-phases-only.md) — related
- [Cognitive presence comprises four phases of critical thinking — triggering event, exploration, integration, and resolution — which are not always sequential](coi-cognitive-presence-four-phases.md) — related
