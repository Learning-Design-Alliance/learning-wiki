---
type: claim
title: KAR3L predicts recall on unseen flashcards via semantic inference, beating the only other capable models in all metrics
description: KAR3L predicts recall on unseen flashcards via semantic inference, beating the only other capable models in all metrics
id: kar3l-unseen-card-semantic-inference
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

# KAR3L predicts recall on unseen flashcards via semantic inference, beating the only other capable models in all metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On cards with no study data, KAR3L bests LM-KT and GPT-3.5 in all metrics, though an AUC gap between unseen and seen cards remains. [→ Matthew Shu 2024](#matthew-shu-2024)

## Evidence

### Matthew Shu 2024

Matthew Shu, Nishant Balepur, Shi Feng, Jordan Boyd-Graber. (2024). KAR3L: Knowledge-Aware Retrieval and Representations aid Retention and Learning in Students. arXiv. [doi:10.48550/arXiv.2402.12291](https://doi.org/10.48550/arXiv.2402.12291)

`q2 · i?` · `causal · r1`

Offline evaluation (Table 1, unseen-card columns) tests content-aware models on flashcards the student has never studied. KAR3L achieves AUC 0.786 and ECE 0.085 on unseen cards versus LM-KT's 0.684/0.234 and GPT-3.5's 0.519/0.481. The article reports that "there is an AUC gap between unseen and seen cards" for KAR3L.

> "On unseen cards, KAR3L bests LM-KT and GPT-3.5, the only other models able to predict recall on unseen cards, in all metrics."

## Discussion


## Related Claims
- [KAR3L outperforms existing student models at predicting flashcard recall on seen cards, with the best AUC and calibration](kar3l-best-seen-card-recall-prediction.md) — related
- [In a single-group pre-post simulation with no comparison group, KAR3L's recall prediction for a semantically related, unstudied flashcard rose from before to after one flashcard was correctly recalled](semantic-transfer-forgetting-curve.md) — related
- [Retrieving a moderate number of similar cards improves unseen-card predictions, but retrieving too many harms all metrics](retrieval-k-tradeoff-recall-prediction.md) — related
