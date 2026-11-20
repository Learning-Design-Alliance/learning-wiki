---
type: claim
title: Attentional factors alone did not significantly boost overall model fit but improved learning-session and posttest predictions
description: Attentional factors alone did not significantly boost overall model fit but improved learning-session and posttest predictions
id: attentional-factors-predictions-not-overall-fit
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: meng-cao-2024
    resource: "https://doi.org/10.48550/arXiv.2407.15020"
    title: "Meng Cao, Wei Chu, Philip I. Pavlik Jr., Liang Zhang. (2024). Integrating Attentional Factors and Spacing in Logistic Knowledge Tracing Models to Explore the Impact of Training Sequences on Category Learning. [doi:10.48550/arXiv.2407.15020](https://doi.org/10.48550/arXiv.2407.15020)"
    author: Meng Cao, Wei Chu, Philip I. Pavlik Jr., Liang Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Attentional factors alone did not significantly boost overall model fit but improved learning-session and posttest predictions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using attentional factors (counts of within- and between-category comparisons) in the AFM did not significantly enhance overall fit but improved both r1 and r2. [→ Meng Cao 2024](#meng-cao-2024)

## Evidence

### Meng Cao 2024

Meng Cao, Wei Chu, Philip I. Pavlik Jr., Liang Zhang. (2024). Integrating Attentional Factors and Spacing in Logistic Knowledge Tracing Models to Explore the Impact of Training Sequences on Category Learning. [doi:10.48550/arXiv.2407.15020](https://doi.org/10.48550/arXiv.2407.15020)

`q2 · i?` · `design · r2`

Bird dataset cross-validation (Table 4): a-AFM showed R2 0.21 and AUC 0.40-level RMSE similar to AFM, but r1 rose to 0.98 and r2 to 0.56; the article states "Utilizing attentional factors in isolation did not enhance overall model fit significantly but did result in improved predictions".

> "Utilizing attentional factors in isolation did not enhance overall model fit significantly but did result in improved predictions for both the learning session and posttest"

## Discussion


## Related Claims
- [Integrating both attentional factors and spacing features into the AFM substantially improves posttest prediction of category learning (bird data: a-AFM+ppe r2 = 0.79 vs. AFM r2 = 0.24)](afm-attention-plus-spacing-improves-posttest-prediction.md) — related
- [In blob-figure learning, category similarity moderates sequencing effects, and the a-AFM+ppe model best captured the reversed posttest pattern (r2 = 0.73)](blob-similarity-moderates-sequencing-model-fit.md) — related
- [Spacing-feature improvements in fit were pronounced for the bird data but weaker for the blob data, likely due to design differences in spacing variability](spacing-fit-gain-varies-by-dataset-design.md) — related
- [PFA models overfit blocked-sequence learning-session accuracy and predict the posttest poorly, motivating AFM-based attentional modeling](pfa-overfits-learning-session-posttest-bias.md) — related
