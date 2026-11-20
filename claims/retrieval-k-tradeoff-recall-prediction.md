---
type: claim
title: Retrieving a moderate number of similar cards improves unseen-card predictions, but retrieving too many harms all metrics
description: Retrieving a moderate number of similar cards improves unseen-card predictions, but retrieving too many harms all metrics
id: retrieval-k-tradeoff-recall-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: matthew-shu-2024
    resource: "https://doi.org/10.48550/arXiv.2402.12291"
    title: "Matthew Shu, Nishant Balepur, Shi Feng, Jordan Boyd-Graber. (2024). KAR3L: Knowledge-Aware Retrieval and Representations aid Retention and Learning in Students. arXiv. [doi:10.48550/arXiv.2402.12291](https://doi.org/10.48550/arXiv.2402.12291)"
    author: Matthew Shu, Nishant Balepur, Shi Feng, Jordan Boyd-Graber
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Retrieving a moderate number of similar cards improves unseen-card predictions, but retrieving too many harms all metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Retrieval boosts unseen-card metrics from k=0 to k=5 and k=10, while k≥15 harms all metrics versus k=0 on seen and unseen cards. [→ Matthew Shu 2024](#matthew-shu-2024)

## Evidence

### Matthew Shu 2024

Matthew Shu, Nishant Balepur, Shi Feng, Jordan Boyd-Graber. (2024). KAR3L: Knowledge-Aware Retrieval and Representations aid Retention and Learning in Students. arXiv. [doi:10.48550/arXiv.2402.12291](https://doi.org/10.48550/arXiv.2402.12291)

`q2 · i?` · `causal · r1`

Numerical comparison across retrieval sizes (Table 3) shows unseen-card AUC rising from 0.776 (k=0) to 0.786 (k=5) then falling to 0.757 (k=15). The article reports retrieval "boosts metrics from k = 0 to k = 5 and k = 10" on unseen cards, and attributes the k≥15 degradation to excess irrelevant flashcards distracting the model.

> "However, retrieving too many flashcards (k ≥ 15) on seen and unseen cards harms all metrics versus k = 0, likely because the excess flashcards are irrelevant, distracting KAR3L."

## Discussion


## Related Claims
- [KAR3L outperforms existing student models at predicting flashcard recall on seen cards, with the best AUC and calibration](kar3l-best-seen-card-recall-prediction.md) — related
- [KAR3L predicts recall on unseen flashcards via semantic inference, beating the only other capable models in all metrics](kar3l-unseen-card-semantic-inference.md) — related
- [Both BERT content embeddings and flashcard-level study features contribute to KAR3L's prediction accuracy and calibration](kar3l-ablation-content-and-history-both-help.md) — related
- [In a single-group pre-post simulation with no comparison group, KAR3L's recall prediction for a semantically related, unstudied flashcard rose from before to after one flashcard was correctly recalled](semantic-transfer-forgetting-curve.md) — related
