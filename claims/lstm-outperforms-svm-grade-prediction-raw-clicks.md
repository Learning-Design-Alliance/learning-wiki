---
type: claim
title: An LSTM using raw click features significantly outperforms SVM baselines at predicting final grades within the algebra course
description: An LSTM using raw click features significantly outperforms SVM baselines at predicting final grades within the algebra course
id: lstm-outperforms-svm-grade-prediction-raw-clicks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: yohan-jo-2018
    resource: "https://doi.org/10.48550/arXiv.1809.04177"
    title: "Yohan Jo, Keith Maki, Gaurav Tomar. (2018). Time Series Analysis of Clickstream Logs from Online Courses. [doi:10.48550/arXiv.1809.04177](https://doi.org/10.48550/arXiv.1809.04177)"
    author: Yohan Jo, Keith Maki, Gaurav Tomar
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# An LSTM using raw click features significantly outperforms SVM baselines at predicting final grades within the algebra course

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Within the algebra course, LSTM with raw click features significantly outperformed all other baselines for most configurations, reaching 94.79% test accuracy with all data. [→ Yohan Jo 2018](#yohan-jo-2018)

## Evidence

### Yohan Jo 2018

Yohan Jo, Keith Maki, Gaurav Tomar. (2018). Time Series Analysis of Clickstream Logs from Online Courses. [doi:10.48550/arXiv.1809.04177](https://doi.org/10.48550/arXiv.1809.04177)

`q2 · i?` · `associational · r1`

Classification experiments on the algebra Coursera course (Table 5) comparing LSTM against SVM baselines using raw clicks, click categories, and MMM/HMM state features. The article reports "signiﬁcantly outperforming all other baselines for most conﬁgurations" (significance by 2-tailed Student T-Test, p≤0.05).

> "LSTM using raw click features is the clear winner within the Algebra course, signiﬁcantly outperforming all other baselines for most conﬁgurations."

## Discussion


## Related Claims
- [LSTM with HMM session-state features transfers to a different course, significantly outperforming SVM for a majority of configurations](lstm-hmm-features-generalize-across-courses.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — related
