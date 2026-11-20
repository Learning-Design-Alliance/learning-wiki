---
type: claim
title: "Integrating both attentional factors and spacing features into the AFM substantially improves posttest prediction of category learning (bird data: a-AFM+ppe r2 = 0.79 vs. AFM r2 = 0.24)"
description: "Integrating both attentional factors and spacing features into the AFM substantially improves posttest prediction of category learning (bird data: a-AFM+ppe r2 = 0.79 vs."
id: afm-attention-plus-spacing-improves-posttest-prediction
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

# Integrating both attentional factors and spacing features into the AFM substantially improves posttest prediction of category learning (bird data: a-AFM+ppe r2 = 0.79 vs. AFM r2 = 0.24)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Adding ppe spacing to the attention-based AFM raised the posttest correlation with human data from 0.24 (AFM) to 0.79 (a-AFM+ppe) in the bird category learning dataset. [→ Meng Cao 2024](#meng-cao-2024)

## Evidence

### Meng Cao 2024

Meng Cao, Wei Chu, Philip I. Pavlik Jr., Liang Zhang. (2024). Integrating Attentional Factors and Spacing in Logistic Knowledge Tracing Models to Explore the Impact of Training Sequences on Category Learning. [doi:10.48550/arXiv.2407.15020](https://doi.org/10.48550/arXiv.2407.15020)

`q2 · i?` · `design · r2`

Student-stratified five-fold cross-validation (ten iterations) on the bird category learning dataset (43,326 observations from 181 participants) compared LKT model variants; Table 4 reports r2 rising to 0.79 for a-AFM+ppe versus 0.24 for AFM, and the article states "incorporating ppe resulted in an improvement in posttest predictions".

> "incorporating ppe resulted in an improvement in posttest predictions"

## Discussion


## Related Claims
- [PFA models overfit blocked-sequence learning-session accuracy and predict the posttest poorly, motivating AFM-based attentional modeling](pfa-overfits-learning-session-posttest-bias.md) — related
- [Of the spacing features tested, recency and ppe improved model fit for the bird data while base4 did not contribute significantly](recency-ppe-improve-fit-base4-does-not.md) — related
- [Spacing-feature improvements in fit were pronounced for the bird data but weaker for the blob data, likely due to design differences in spacing variability](spacing-fit-gain-varies-by-dataset-design.md) — related
- [Attentional factors alone did not significantly boost overall model fit but improved learning-session and posttest predictions](attentional-factors-predictions-not-overall-fit.md) — related
- [In blob-figure learning, category similarity moderates sequencing effects, and the a-AFM+ppe model best captured the reversed posttest pattern (r2 = 0.73)](blob-similarity-moderates-sequencing-model-fit.md) — related
