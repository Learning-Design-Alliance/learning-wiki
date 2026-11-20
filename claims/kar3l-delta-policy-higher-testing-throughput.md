---
type: claim
title: In an online user study, KAR3L+Δ matches FSRS on post-test accuracy while reducing recall time, yielding higher testing throughput
description: In an online user study, KAR3L+Δ matches FSRS on post-test accuracy while reducing recall time, yielding higher testing throughput
id: kar3l-delta-policy-higher-testing-throughput
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
  - id: matthew-shu-2024-2
    resource: "https://doi.org/10.48550/arXiv.2402.12291"
    title: "Matthew Shu, Nishant Balepur, Shi Feng, Jordan Boyd-Graber. (2024). KAR3L: Knowledge-Aware Retrieval and Representations aid Retention and Learning in Students. arXiv. [doi:10.48550/arXiv.2402.12291](https://doi.org/10.48550/arXiv.2402.12291)"
    author: Matthew Shu, Nishant Balepur, Shi Feng, Jordan Boyd-Graber
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# In an online user study, KAR3L+Δ matches FSRS on post-test accuracy while reducing recall time, yielding higher testing throughput

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 32 six-day study sessions from 27 users, KAR3L+Δ users maintain post-test accuracy while reducing recall time on all cards, achieving TTP of 2.74 versus FSRS's 2.58. [→ Matthew Shu 2024](#matthew-shu-2024)
`q2 i?` KAR3L+Δ shows significantly lower post-test response time on all cards studied (6.27 sec vs 6.82 sec, p < 0.05), while response accuracy gains are similar between schedulers. [→ Matthew Shu 2024 (2)](#matthew-shu-2024-2)

## Evidence

### Matthew Shu 2024

Matthew Shu, Nishant Balepur, Shi Feng, Jordan Boyd-Graber. (2024). KAR3L: Knowledge-Aware Retrieval and Representations aid Retention and Learning in Students. arXiv. [doi:10.48550/arXiv.2402.12291](https://doi.org/10.48550/arXiv.2402.12291)

`q2 · i?` · `causal · r1`

Online within-subject user study (Table 4) with 32 six-day sessions from 27 students, each scheduler used on one of two fixed 20-card test sets. Pre/post-test accuracy more than doubles (0.42 to 0.86) under both schedulers; KAR3L+Δ reaches TTP 2.74 versus FSRS's 2.58.

> "As a result, KAR3L + ∆users obtain higher testing throughput (TTP) than FSRS users, as users studying with KAR3L answer a similar number of facts correctly in less time (2.74 vs 2.58 flashcards answered correctly per second)."

### Matthew Shu 2024 (2)

Matthew Shu, Nishant Balepur, Shi Feng, Jordan Boyd-Graber. (2024). KAR3L: Knowledge-Aware Retrieval and Representations aid Retention and Learning in Students. arXiv. [doi:10.48550/arXiv.2402.12291](https://doi.org/10.48550/arXiv.2402.12291)

`q2 · i?` · `causal · r1`

Test-mode results (Table 4 caption) report post-test response time on all cards of 6.27 sec for KAR3L+Δ versus 6.82 sec for FSRS, with the asterisk marking t-test significance (p < 0.05). Response accuracy is similar between the two schedulers, so the throughput gain comes from time, not accuracy.

> "KAR3L + ∆ users have similar pre-test and post-test accuracy versus FSRS users but much lower post-test response time, enhancing testing throughput (TTP)."

## Discussion


## Related Claims
- [KAR3L outperforms existing student models at predicting flashcard recall on seen cards, with the best AUC and calibration](kar3l-best-seen-card-recall-prediction.md) — related
- [In a single-group pre-post simulation with no comparison group, KAR3L's recall prediction for a semantically related, unstudied flashcard rose from before to after one flashcard was correctly recalled](semantic-transfer-forgetting-curve.md) — related
- [Medical students using spaced study followed by quizzing achieved significantly higher recall accuracy than quiz-only students in sessions s1 and s2](study-quiz-group-higher-recall-accuracy.md) — related
