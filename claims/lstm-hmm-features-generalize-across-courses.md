---
type: claim
title: LSTM with HMM session-state features transfers to a different course, significantly outperforming SVM for a majority of configurations
description: LSTM with HMM session-state features transfers to a different course, significantly outperforming SVM for a majority of configurations
id: lstm-hmm-features-generalize-across-courses
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

# LSTM with HMM session-state features transfers to a different course, significantly outperforming SVM for a majority of configurations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the precalculus course, LSTM with HMM state features significantly outperformed SVM for a majority of configurations, showing sequence-aware approaches generalize better to other courses. [→ Yohan Jo 2018](#yohan-jo-2018)

## Evidence

### Yohan Jo 2018

Yohan Jo, Keith Maki, Gaurav Tomar. (2018). Time Series Analysis of Clickstream Logs from Online Courses. [doi:10.48550/arXiv.1809.04177](https://doi.org/10.48550/arXiv.1809.04177)

`q2 · i?` · `associational · r1`

Transfer experiments (Table 6) testing classifiers trained on the algebra course on precalculus data, using MMM and HMM state features inferred via maximum likelihood estimation and the Viterbi algorithm. The article reports LSTM "signiﬁcantly outperforming SVM for a ma- jority of conﬁgurations".

> "LSTM with HMM features performs surprisingly well, signiﬁcantly outperforming SVM for a ma- jority of conﬁgurations."

## Discussion


## Related Claims
- [An LSTM using raw click features significantly outperforms SVM baselines at predicting final grades within the algebra course](lstm-outperforms-svm-grade-prediction-raw-clicks.md) — related
