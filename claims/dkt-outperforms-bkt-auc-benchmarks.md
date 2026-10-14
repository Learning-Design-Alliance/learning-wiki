---
type: claim
title: Deep Knowledge Tracing substantially outperforms Bayesian Knowledge Tracing on knowledge tracing benchmarks
description: Deep Knowledge Tracing substantially outperforms Bayesian Knowledge Tracing on knowledge tracing benchmarks
id: dkt-outperforms-bkt-auc-benchmarks
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-14
evidence_strength: moderate
sources:
  - id: chris-piech-2015
    resource: "https://github.com/chrispiech/DeepKnowledgeTracing"
    title: "Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein. (2015). Deep Knowledge Tracing. https://github.com/chrispiech/DeepKnowledgeTracing"
    author: Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein
    q: 2
    i: "?"
    kind: associational
    rigour: "?"
  - id: chris-piech-2015-2
    resource: "https://github.com/chrispiech/DeepKnowledgeTracing"
    title: "Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein. (2015). Deep Knowledge Tracing. https://github.com/chrispiech/DeepKnowledgeTracing"
    author: Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein
    q: 2
    i: "?"
    kind: design
    rigour: "?"
---

# Deep Knowledge Tracing substantially outperforms Bayesian Knowledge Tracing on knowledge tracing benchmarks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r?` · `q2`

## Subclaims
`q2 i?` On the Khan Academy dataset, LSTM-based DKT achieved an AUC of 0.85 versus 0.68 for standard BKT and 0.63 for the marginal baseline. [→ Chris Piech 2015](#chris-piech-2015)
`q2 i?` On the Assistments benchmark, DKT achieved an AUC of 0.86, a 25% gain over the best previously reported result of 0.69. [→ Chris Piech 2015 (2)](#chris-piech-2015-2)

## Evidence

### Chris Piech 2015

Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein. (2015). Deep Knowledge Tracing. https://github.com/chrispiech/DeepKnowledgeTracing

`q2 · i?` · `associational · r?`

Evaluation on anonymized Khan Academy eighth-grade usage data (1.4 million exercises by 47,495 students across 69 exercise types) with 5-fold cross validation. The article reports the LSTM model "led to an AUC of 0.85" against BKT at 0.68 and a marginal baseline of 0.63.

> "On the Khan dataset using an LSTM neural network model led to an AUC of 0.85 which was a notable improvement over the performance of a standard BKT (AUC = 0.68)"

### Chris Piech 2015 (2)

Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein. (2015). Deep Knowledge Tracing. https://github.com/chrispiech/DeepKnowledgeTracing

`q2 · i?` · `design · r?`

Evaluation on the Assistments 2009-2010 skill builder benchmark (15,931 students, 526K answers), described as the largest publicly available knowledge tracing dataset. DKT's AUC of 0.86 is a 25% gain over the prior best reported result of 0.69.

> "On the Assistments dataset DKT produced a 25% gain over the previous best reported result (AUC = 0.86 and 0.69 respectively)"

## Discussion


## Related Claims
- [BKTransformer rivals or surpasses deep KT baselines (DKT, SAKT) and BKT-EM in AUC, but DKT outperforms it on one dataset](bktransformer-rivals-deep-kt-auc.md) — related
- [SAKT underperforms DKT on all nine datasets, contradicting previously reported results](sakt-underperforms-dkt-all-datasets.md) — related
- [BKT and BKT+SK are the best models for predicting students' post-test scores in tutoring systems with elicit and tell interventions](bkt-best-post-test-prediction-intervention-tutors.md) — related
- [LSTM and LSTM+SK outperform the Bayesian models on predicting quantized learning gains](lstm-best-learning-gain-prediction.md) — related
- [LLMKT outperforms existing knowledge tracing methods at predicting student turn correctness in the CoMTA and MathDial tutoring dialogue datasets, and generally outperforms DKT-Sem.](llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md) — related
