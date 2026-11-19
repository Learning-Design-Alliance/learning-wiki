---
type: claim
title: Adding n-gram features significantly improved the hedge classifier, but tutoring moves and nonverbal features did not
description: Adding n-gram features significantly improved the hedge classifier, but tutoring moves and nonverbal features did not
id: ngrams-help-tutoring-moves-nonverbal-do-not
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: yann-raphalen-2022
    resource: "https://doi.org/10.18653/v1/2022.acl-long.153"
    title: "Yann Raphalen, Chloé Clavel, Justine Cassell. (2022). \"You might think about slightly revising the title\": Identifying Hedges in Peer-tutoring Interactions. [doi:10.18653/v1/2022.acl-long.153](https://doi.org/10.18653/v1/2022.acl-long.153)"
    author: Yann Raphalen, Chloé Clavel, Justine Cassell
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Adding n-gram features significantly improved the hedge classifier, but tutoring moves and nonverbal features did not

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Introducing unigrams and bigrams significantly improved classifier performance over the rule-based label alone, while tutoring moves and nonverbal behaviors did not significantly improve it. [→ Yann Raphalen 2022](#yann-raphalen-2022)

## Evidence

### Yann Raphalen 2022

Yann Raphalen, Chloé Clavel, Justine Cassell. (2022). "You might think about slightly revising the title": Identifying Hedges in Peer-tutoring Interactions. [doi:10.18653/v1/2022.acl-long.153](https://doi.org/10.18653/v1/2022.acl-long.153)

`q2 · i?` · `design · r2`

Incremental feature ablation with LightGBM (Table 5), adding feature groups stepwise to the rule-based label. The article reports the n-gram addition as significant and states "neither the tutoring moves nor the nonverbal features significantly improved the performance of the model."

> "the introduction of n-grams significantly improved the performance of our classifier, suggesting that some lexical and syntactic information describing the hedge classes was not present in the rule-based model."

## Discussion


## Related Claims
- [Best hedge-detection performance (F1 79.0) came from LightGBM using nearly all feature groups](lightgbm-all-features-best-f1-79.md) — related
- [Rule-based classifier labels and expected lexical markers (I, sorry, just, would) rank among the most important SHAP features for hedge classes](rule-based-labels-top-shap-features.md) — related
- [Where labelled training data is limited, adding hand-crafted features improves the performance of neural text evaluation models](handcrafted-features-improve-neural-low-resource.md) — a broader claim this one bears on
