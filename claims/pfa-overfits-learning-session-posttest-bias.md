---
type: claim
title: PFA models overfit blocked-sequence learning-session accuracy and predict the posttest poorly, motivating AFM-based attentional modeling
description: PFA models overfit blocked-sequence learning-session accuracy and predict the posttest poorly, motivating AFM-based attentional modeling
id: pfa-overfits-learning-session-posttest-bias
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
  - id: meng-cao-2024-2
    resource: "https://doi.org/10.48550/arXiv.2407.15020"
    title: "Meng Cao, Wei Chu, Philip I. Pavlik Jr., Liang Zhang. (2024). Integrating Attentional Factors and Spacing in Logistic Knowledge Tracing Models to Explore the Impact of Training Sequences on Category Learning. [doi:10.48550/arXiv.2407.15020](https://doi.org/10.48550/arXiv.2407.15020)"
    author: Meng Cao, Wei Chu, Philip I. Pavlik Jr., Liang Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# PFA models overfit blocked-sequence learning-session accuracy and predict the posttest poorly, motivating AFM-based attentional modeling

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For the bird data, PFA tracked the learning session well (r1 up to 0.99) but showed no correlation with posttest data before spacing features, and adding spacing features declined posttest predictions. [→ Meng Cao 2024](#meng-cao-2024)

## Evidence

### Meng Cao 2024

Meng Cao, Wei Chu, Philip I. Pavlik Jr., Liang Zhang. (2024). Integrating Attentional Factors and Spacing in Logistic Knowledge Tracing Models to Explore the Impact of Training Sequences on Category Learning. [doi:10.48550/arXiv.2407.15020](https://doi.org/10.48550/arXiv.2407.15020)

`q2 · i?` · `design · r2`

Cross-validation results for the bird dataset (Table 3) show PFA r2 = -0.05 while r1 = 0.90; the article reports "on the posttest, both AFM and PFA models demonstrated poor predictive performance, with the PFA model showing no correlation with the human data".

> "on the posttest, both AFM and PFA models demonstrated poor predictive performance, with the PFA model showing no correlation with the human data"

### Meng Cao 2024 (2)

Meng Cao, Wei Chu, Philip I. Pavlik Jr., Liang Zhang. (2024). Integrating Attentional Factors and Spacing in Logistic Knowledge Tracing Models to Explore the Impact of Training Sequences on Category Learning. [doi:10.48550/arXiv.2407.15020](https://doi.org/10.48550/arXiv.2407.15020)

`q2 · i?` · `design · r2`

In the bird experiment's learning session, larger blocks yielded higher categorization accuracy, while the posttest showed the reverse; the article argues PFA's success-count assumption "does not hold true in the context of interleaving or blocking", so it overfits session data and biases against posttest results.

> "the larger the block size, the higher the accuracy of participants’ bird categorization. However, the posttest showed a reverse pattern that the smaller block size led to higher accuracy"

## Discussion


## Related Claims
- [Integrating both attentional factors and spacing features into the AFM substantially improves posttest prediction of category learning (bird data: a-AFM+ppe r2 = 0.79 vs. AFM r2 = 0.24)](afm-attention-plus-spacing-improves-posttest-prediction.md) — related
- [Attentional factors alone did not significantly boost overall model fit but improved learning-session and posttest predictions](attentional-factors-predictions-not-overall-fit.md) — related
- [Of the spacing features tested, recency and ppe improved model fit for the bird data while base4 did not contribute significantly](recency-ppe-improve-fit-base4-does-not.md) — related
- [Spacing-feature improvements in fit were pronounced for the bird data but weaker for the blob data, likely due to design differences in spacing variability](spacing-fit-gain-varies-by-dataset-design.md) — related
- [Despite BIC suggesting overfitting, PFA's 7-fold crossvalidated mean absolute deviation shows it generalizes well](pfa-crossvalidation-generalizes.md) — reports the opposite
