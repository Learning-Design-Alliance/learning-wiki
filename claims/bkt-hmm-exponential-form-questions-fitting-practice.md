---
type: claim
title: The exponential functional form of the BKT Markov chain calls into question the popular practice of fitting that model form to student data
description: The exponential functional form of the BKT Markov chain calls into question the popular practice of fitting that model form to student data
id: bkt-hmm-exponential-form-questions-fitting-practice
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: weak
newest_evidence: 2013
recheck_by: 2016
sources:
  - id: brett-van-de-sande-2013
    resource: "https://doi.org/10.5281/zenodo.3554629"
    title: "Van de Sande, B. (2013). Properties of the Bayesian Knowledge Tracing Model. *Journal of Educational Data Mining, 5*(2). [doi:10.5281/zenodo.3554629](https://doi.org/10.5281/zenodo.3554629)"
    author: Van de Sande, B.
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
---

# The exponential functional form of the BKT Markov chain calls into question the popular practice of fitting that model form to student data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q1`
> **Currency** · newest study 2013 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2016**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Because the Markov-chain form of BKT (which predicts the student-averaged probability of a correct application) has the functional form of an exponential, while some studies report individual learning better described by a power law, the article argues these results call into question fitting the Markov model form of BKT to student data. [→ Brett Van de Sande 2013](#brett-van-de-sande-2013)

## Evidence

### Brett Van de Sande 2013

Van de Sande, B. (2013). Properties of the Bayesian Knowledge Tracing Model. *Journal of Educational Data Mining, 5*(2). [doi:10.5281/zenodo.3554629](https://doi.org/10.5281/zenodo.3554629)

`q1 · i?` · `theoretical · r3`

Authors' interpretation in the conclusion (type e), weighing the analytical exponential solution for the BKT Markov chain (the hidden Markov model form is analysed separately, by fixed-point analysis) against Heathcote et al.'s exponential account and Chi et al.'s finding that student learning of physics skills was better explained by a power law even for individual students. No new data are analyzed here.

> "Together, these results call into question the popular practice of ﬁtting the Markov model form of BKT to student data. Perhaps a model that has power law behavior would work better?"

## Discussion

## Related Claims

- [The survey states that deep learning knowledge tracing models exhibit superior performance to Bayesian and logistic models but have significant room for improvement in interpretability.](deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability.md) — the general claim this finding bears on, with the studies behind it
- [The HMM form of BKT, solved analytically, is a three-parameter exponential in opportunity number](bkt-hmm-form-is-three-parameter-exponential.md) — related
- [The identifiability problem of the BKT HMM arises because combinations of P(G) and P(L0) with the same product A give identical functional forms](bkt-identifiability-explained-by-parameter-a.md) — related
- Semi-Markov models fit the writing-process data better than continuous-time Markov chain models — related
- [A Hidden Markov Model over knowledge states identifies Analytical Thinking (A5) as the learning bottleneck with the lowest forward transition probability](hmm-identifies-a5-bottleneck.md) — related
- [Individualized Knowledge Tracing parameters fit student data significantly better and change mastery-learning practice decisions for many students](individualized-kt-parameters-change-practice-decisions.md) — related
- [The Knowledge Tracing Algorithm does not suffer the identifiability problem: all four parameters affect its behavior separately](kt-algorithm-no-identifiability-problem.md) — related
