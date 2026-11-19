---
type: claim
title: A LightGBM model with knowledge-driven rule-based features outperforms fine-tuned BERT and an Attention-CNN baseline for hedge detection in peer-tutoring conversation
description: A LightGBM model with knowledge-driven rule-based features outperforms fine-tuned BERT and an Attention-CNN baseline for hedge detection in peer-tutoring conversation
id: lightgbm-knowledge-driven-features-beat-bert-hedge-detection
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

# A LightGBM model with knowledge-driven rule-based features outperforms fine-tuned BERT and an Attention-CNN baseline for hedge detection in peer-tutoring conversation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Knowledge-driven features in LightGBM achieved F1 of 79.0 versus 70.6 for fine-tuned BERT and 64.5 for the Attention-CNN baseline on the three minority hedge classes. [→ Yann Raphalen 2022](#yann-raphalen-2022)

## Evidence

### Yann Raphalen 2022

Yann Raphalen, Chloé Clavel, Justine Cassell. (2022). "You might think about slightly revising the title": Identifying Hedges in Peer-tutoring Interactions. [doi:10.18653/v1/2022.acl-long.153](https://doi.org/10.18653/v1/2022.acl-long.153)

`q2 · i?` · `design · r2`

Model comparison experiment on the peer-tutoring corpus, evaluated by averaged weighted F1 over the three hedge classes across 5-fold cross-validation. The authors report "79.0 vs. 70.6" against BERT and "79.0 vs 64.5" against the Attention-CNN baseline.

> "the use of "Knowledge-Driven" features based on rules built from linguistic knowledge of hedges in the LightGBM model outperforms the use of pre-trained embeddings within a fine-tuned BERT model (79.0 vs. 70.6), and in the neural baseline from (Goel et al., 2019) (79.0 vs 64.5)."

## Discussion


## Related Claims
- [Best hedge-detection performance (F1 79.0) came from LightGBM using nearly all feature groups](lightgbm-all-features-best-f1-79.md) — possibly the same claim (merge candidate)
- [TF-IDF encoded text with a random forest classifier outperformed several strong baselines including LSTM, HAN, CNN and RCNN](tfidf-random-forest-beats-strong-baselines.md) — related
