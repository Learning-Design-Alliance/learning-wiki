---
type: claim
title: Spacing-feature improvements in fit were pronounced for the bird data but weaker for the blob data, likely due to design differences in spacing variability
description: Spacing-feature improvements in fit were pronounced for the bird data but weaker for the blob data, likely due to design differences in spacing variability
id: spacing-fit-gain-varies-by-dataset-design
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
sources:
  - id: meng-cao-2024
    resource: "https://doi.org/10.48550/arXiv.2407.15020"
    title: "Meng Cao, Wei Chu, Philip I. Pavlik Jr., Liang Zhang. (2024). Integrating Attentional Factors and Spacing in Logistic Knowledge Tracing Models to Explore the Impact of Training Sequences on Category Learning. [doi:10.48550/arXiv.2407.15020](https://doi.org/10.48550/arXiv.2407.15020)"
    author: Meng Cao, Wei Chu, Philip I. Pavlik Jr., Liang Zhang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Spacing-feature improvements in fit were pronounced for the bird data but weaker for the blob data, likely due to design differences in spacing variability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Recency and ppe improved R2, AUC, and RMSE for the bird data more than for the blob figures data. [→ Meng Cao 2024](#meng-cao-2024)

## Evidence

### Meng Cao 2024

Meng Cao, Wei Chu, Philip I. Pavlik Jr., Liang Zhang. (2024). Integrating Attentional Factors and Spacing in Logistic Knowledge Tracing Models to Explore the Impact of Training Sequences on Category Learning. [doi:10.48550/arXiv.2407.15020](https://doi.org/10.48550/arXiv.2407.15020)

`q2 · i?` · `causal · r2`

Comparison of cross-validated fit gains across the two datasets; the article attributes the difference to design, noting the bird experiment's 10 categories with wide vs. narrow spacing "provided more variability in the data", while the blob experiment's 3 categories produced narrower spacing intervals and less significant fit improvement.

> "After incorporating spacing features (recency and ppe) into both the AFM and PFA models, there was an improvement in model fit for bird category learning data, while the improvement was not as pro- nounced in the blob figures learning data"

## Discussion


## Related Claims
- [Integrating both attentional factors and spacing features into the AFM substantially improves posttest prediction of category learning (bird data: a-AFM+ppe r2 = 0.79 vs. AFM r2 = 0.24)](afm-attention-plus-spacing-improves-posttest-prediction.md) — related
- [Attentional factors alone did not significantly boost overall model fit but improved learning-session and posttest predictions](attentional-factors-predictions-not-overall-fit.md) — related
- [In blob-figure learning, category similarity moderates sequencing effects, and the a-AFM+ppe model best captured the reversed posttest pattern (r2 = 0.73)](blob-similarity-moderates-sequencing-model-fit.md) — related
- [PFA models overfit blocked-sequence learning-session accuracy and predict the posttest poorly, motivating AFM-based attentional modeling](pfa-overfits-learning-session-posttest-bias.md) — related
- [Of the spacing features tested, recency and ppe improved model fit for the bird data while base4 did not contribute significantly](recency-ppe-improve-fit-base4-does-not.md) — related
