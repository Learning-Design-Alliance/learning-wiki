---
type: claim
title: Almost all neural network models benefit from adding handcrafted wLDA and online dialogue features
description: Almost all neural network models benefit from adding handcrafted wLDA and online dialogue features
id: handcrafted-features-improve-neural-argument-classifiers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: luca-lugini-and-diane-litman-2018
    resource: "https://doi.org/10.18653/v1/w18-5208"
    title: "Luca Lugini and Diane Litman. (2018). Argument Component Classification for Classroom Discussions. [doi:10.18653/v1/w18-5208](https://doi.org/10.18653/v1/w18-5208)"
    author: Luca Lugini and Diane Litman
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Almost all neural network models benefit from adding handcrafted wLDA and online dialogue features

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Almost all neural network models benefit from additional handcrafted features, attributed to the limited amount of training data; LSTM models benefit more than CNNs, and feature ablation shows most online dialogue feature subsets contribute to performance. [→ Luca Lugini and Diane Litman 2018](#luca-lugini-and-diane-litman-2018)

## Evidence

### Luca Lugini and Diane Litman 2018

Luca Lugini and Diane Litman. (2018). Argument Component Classification for Classroom Discussions. [doi:10.18653/v1/w18-5208](https://doi.org/10.18653/v1/w18-5208)

`q2 · i?` · `design · r2`

Cross-validation comparison of neural network models with and without wLDA and online dialogue features (Table 3). The authors attribute the benefit to limited training data despite oversampling, and note LSTMs benefit more because they start from lower performance.

> "It is clear from Table 3 that almost all neural net- work models beneﬁt from additional handcrafted features (with the exception of precision and re- call for rows 13 and 14)."

## Discussion


## Related Claims
- [CNN models almost always outperform LSTM models for argument component classification in classroom discussions, with character-level LSTMs near random chance](cnn-outperforms-lstm-argument-component-classification.md) — related
- [Where labelled training data is limited, adding hand-crafted features improves the performance of neural text evaluation models](handcrafted-features-improve-neural-low-resource.md) — a broader claim this one bears on
- [Retraining a logistic regression classifier on classroom discussions with wLDA features plus online dialogue features achieves the best kappa overall](wlda-plus-online-dialogue-features-best-kappa.md) — related
- [A pre-trained essay argument mining system (wLDA) performs poorly when applied off-the-shelf to classroom discussions, performing comparably to a majority baseline](pretrained-essay-argument-miner-poor-on-classroom-discussions.md) — related
- [Attention-based neural classifiers outperformed vanilla neural models on Bloom's taxonomy question classification](attention-models-beat-vanilla-neural-baselines.md) — related
- [Attention-based encoders outperform LSTM-based encoders for multimodal discourse assessment in overall and component-level performance except Nature of Discourse](attention-encoders-outperform-lstm-discourse-assessment.md) — related
