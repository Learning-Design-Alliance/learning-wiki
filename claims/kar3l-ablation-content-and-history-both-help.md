---
type: claim
title: "Both BERT content embeddings and flashcard-level study features contribute to KAR3L's prediction accuracy and calibration"
description: "Both BERT content embeddings and flashcard-level study features contribute to KAR3L's prediction accuracy and calibration"
id: kar3l-ablation-content-and-history-both-help
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
    kind: design
    rigour: 2
---

# Both BERT content embeddings and flashcard-level study features contribute to KAR3L's prediction accuracy and calibration

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Ablating BERT embeddings or flashcard-level study data each degrades AUC and ECE, with No BERT worst on unseen cards. [→ Matthew Shu 2024](#matthew-shu-2024)

## Evidence

### Matthew Shu 2024

Matthew Shu, Nishant Balepur, Shi Feng, Jordan Boyd-Graber. (2024). KAR3L: Knowledge-Aware Retrieval and Representations aid Retention and Learning in Students. arXiv. [doi:10.48550/arXiv.2402.12291](https://doi.org/10.48550/arXiv.2402.12291)

`q2 · i?` · `design · r2`

Ablation study (Table 2) compares full KAR3L (AUC 0.780 seen) against versions discarding BERT embeddings (0.692) or discarding study features X(z) (0.680). On unseen cards, the article reports "No BERT has the worst AUC and ECE", indicating semantic inference is most valuable where study data is absent.

> "Adding BERT embeddings and flashcard-level study data both improve ECE and AUC (Table 2), showing that content and historical study data both enhance student modeling."

## Discussion


## Related Claims
- [Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs](ablation-all-features-maximize-auc.md) — a broader claim this one bears on
- [Ablation study shows metadata-enriched embeddings produce the largest accuracy drop, while attention masking, KV caching and dynamic batching primarily support inference efficiency](ablation-metadata-embeddings-largest-accuracy-drop.md) — related
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](cognitive-load-module-largest-ablation-drop.md) — related
- [KAR3L outperforms existing student models at predicting flashcard recall on seen cards, with the best AUC and calibration](kar3l-best-seen-card-recall-prediction.md) — related
- [Retrieving a moderate number of similar cards improves unseen-card predictions, but retrieving too many harms all metrics](retrieval-k-tradeoff-recall-prediction.md) — related
- [In a single-group pre-post simulation with no comparison group, KAR3L's recall prediction for a semantically related, unstudied flashcard rose from before to after one flashcard was correctly recalled](semantic-transfer-forgetting-curve.md) — related
