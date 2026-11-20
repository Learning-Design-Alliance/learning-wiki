---
type: claim
title: KAR3L outperforms existing student models at predicting flashcard recall on seen cards, with the best AUC and calibration
description: KAR3L outperforms existing student models at predicting flashcard recall on seen cards, with the best AUC and calibration
id: kar3l-best-seen-card-recall-prediction
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

# KAR3L outperforms existing student models at predicting flashcard recall on seen cards, with the best AUC and calibration

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On seen flashcards, KAR3L surpasses baseline student models (HLR, Leitner, SM-2, FSRS, LM-KT, GPT-3.5) in AUC and calibration error, winning 7 of 8 metrics. [→ Matthew Shu 2024](#matthew-shu-2024)

## Evidence

### Matthew Shu 2024

Matthew Shu, Nishant Balepur, Shi Feng, Jordan Boyd-Graber. (2024). KAR3L: Knowledge-Aware Retrieval and Representations aid Retention and Learning in Students. arXiv. [doi:10.48550/arXiv.2402.12291](https://doi.org/10.48550/arXiv.2402.12291)

`q2 · i?` · `design · r2`

Offline evaluation on the authors' collected dataset (Table 1) compares KAR3L against HLR, Leitner, SM-2, FSRS, LM-KT and GPT-3.5 on AUC, ECE, and accuracy when correct/incorrect. KAR3L reaches AUC 0.864 and ECE 0.091 on seen cards, and the caption states it "outperforms baselines in 7/8 metrics". The one exception is accuracy on incorrect seen cards, where FSRS scores 0.524 versus KAR3L's 0.250.

> "KAR3L outperforms baselines in 7/8 metrics, showcasing the offline strength of content-aware scheduling."

## Discussion


## Related Claims
- [KAR3L predicts recall on unseen flashcards via semantic inference, beating the only other capable models in all metrics](kar3l-unseen-card-semantic-inference.md) — related
- [Both BERT content embeddings and flashcard-level study features contribute to KAR3L's prediction accuracy and calibration](kar3l-ablation-content-and-history-both-help.md) — related
- [Retrieving a moderate number of similar cards improves unseen-card predictions, but retrieving too many harms all metrics](retrieval-k-tradeoff-recall-prediction.md) — related
- [In a single-group pre-post simulation with no comparison group, KAR3L's recall prediction for a semantically related, unstudied flashcard rose from before to after one flashcard was correctly recalled](semantic-transfer-forgetting-curve.md) — related
- [In an online user study, KAR3L+Δ matches FSRS on post-test accuracy while reducing recall time, yielding higher testing throughput](kar3l-delta-policy-higher-testing-throughput.md) — related
