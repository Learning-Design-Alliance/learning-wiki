---
type: claim
title: Of the spacing features tested, recency and ppe improved model fit for the bird data while base4 did not contribute significantly
description: Of the spacing features tested, recency and ppe improved model fit for the bird data while base4 did not contribute significantly
id: recency-ppe-improve-fit-base4-does-not
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

# Of the spacing features tested, recency and ppe improved model fit for the bird data while base4 did not contribute significantly

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In bird category learning, adding recency or ppe enhanced fit, whereas base4 did not significantly improve it. [→ Meng Cao 2024](#meng-cao-2024)

## Evidence

### Meng Cao 2024

Meng Cao, Wei Chu, Philip I. Pavlik Jr., Liang Zhang. (2024). Integrating Attentional Factors and Spacing in Logistic Knowledge Tracing Models to Explore the Impact of Training Sequences on Category Learning. [doi:10.48550/arXiv.2407.15020](https://doi.org/10.48550/arXiv.2407.15020)

`q2 · i?` · `design · r2`

Cross-validated model fitting on the bird dataset (Table 3) compared AFM and PFA with ppe, base4, and recency; the article reports that "both recency and ppe ex- hibited an enhancement in model fit, while base4 did not contribute significantly to the improvement", so later analyses used only recency and ppe.

> "Upon the inclusion of spacing features, both recency and ppe ex- hibited an enhancement in model fit, while base4 did not contribute significantly to the improvement."

## Discussion


## Related Claims
- [Integrating both attentional factors and spacing features into the AFM substantially improves posttest prediction of category learning (bird data: a-AFM+ppe r2 = 0.79 vs. AFM r2 = 0.24)](afm-attention-plus-spacing-improves-posttest-prediction.md) — related
- [PFA models overfit blocked-sequence learning-session accuracy and predict the posttest poorly, motivating AFM-based attentional modeling](pfa-overfits-learning-session-posttest-bias.md) — related
- [Spacing-feature improvements in fit were pronounced for the bird data but weaker for the blob data, likely due to design differences in spacing variability](spacing-fit-gain-varies-by-dataset-design.md) — related
