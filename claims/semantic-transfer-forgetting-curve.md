---
type: claim
title: "In a single-group pre-post simulation with no comparison group, KAR3L's recall prediction for a semantically related, unstudied flashcard rose from before to after one flashcard was correctly recalled"
description: "In a single-group pre-post simulation with no comparison group, KAR3L's recall prediction for a semantically related, unstudied flashcard rose from before to after one flashcard was correctly recalled."
id: semantic-transfer-forgetting-curve
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: matthew-shu-2024
    resource: "https://doi.org/10.48550/arXiv.2402.12291"
    title: "Matthew Shu, Nishant Balepur, Shi Feng, Jordan Boyd-Graber. (2024). KAR3L: Knowledge-Aware Retrieval and Representations aid Retention and Learning in Students. arXiv. [doi:10.48550/arXiv.2402.12291](https://doi.org/10.48550/arXiv.2402.12291)"
    author: Matthew Shu, Nishant Balepur, Shi Feng, Jordan Boyd-Graber
    q: 1
    i: "?"
    kind: causal
    rigour: 1
---

# In a single-group pre-post simulation with no comparison group, KAR3L's recall prediction for a semantically related, unstudied flashcard rose from before to after one flashcard was correctly recalled

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In a single-group pre-post simulation with no comparison group, the predicted recall of unstudied, related Card 2 (Abraham Lincoln) rose from before to after Card 1 (James Garfield) was correctly recalled on day 10. [→ Matthew Shu 2024](#matthew-shu-2024)

## Evidence

### Matthew Shu 2024

Matthew Shu, Nishant Balepur, Shi Feng, Jordan Boyd-Graber. (2024). KAR3L: Knowledge-Aware Retrieval and Representations aid Retention and Learning in Students. arXiv. [doi:10.48550/arXiv.2402.12291](https://doi.org/10.48550/arXiv.2402.12291)

`q1 · i?` · `causal · r1`

Simulation analysis (Figure 3) constructs simulated forgetting curves for two related US history cards by querying KAR3L at times from zero to twenty days. The result is a model-behavior demonstration, not a human experiment: the article says it "highlights the benefit of making semantic inferences across flashcards".

> "When Card 1 is recalled correctly on day 10, the recall prediction of Card 2 (Abraham Lincoln, 16th U.S. president) increases despite not being studied."

## Discussion


## Related Claims
- [KAR3L outperforms existing student models at predicting flashcard recall on seen cards, with the best AUC and calibration](kar3l-best-seen-card-recall-prediction.md) — related
- [In an online user study, KAR3L+Δ matches FSRS on post-test accuracy while reducing recall time, yielding higher testing throughput](kar3l-delta-policy-higher-testing-throughput.md) — related
- [KAR3L predicts recall on unseen flashcards via semantic inference, beating the only other capable models in all metrics](kar3l-unseen-card-semantic-inference.md) — related
- [Retrieving a moderate number of similar cards improves unseen-card predictions, but retrieving too many harms all metrics](retrieval-k-tradeoff-recall-prediction.md) — related
- [Both BERT content embeddings and flashcard-level study features contribute to KAR3L's prediction accuracy and calibration](kar3l-ablation-content-and-history-both-help.md) — related
