---
type: claim
title: Regression on TOEFL11SUBSET reaches a Pearson correlation of 0.8 with proficiency scores
description: Regression on TOEFL11SUBSET reaches a Pearson correlation of 0.8 with proficiency scores
id: toefl11-regression-correlation-0-8
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2016
recheck_by: 2019
sources:
  - id: sowmya-vajjala-2016
    resource: "https://arxiv.org/abs/1612.00729"
    title: "Sowmya Vajjala. (2016). Automated assessment of non-native learner essays: Investigating the role of linguistic features. International Journal of Artificial Intelligence in Education. https://arxiv.org/abs/1612.00729"
    author: Sowmya Vajjala
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Regression on TOEFL11SUBSET reaches a Pearson correlation of 0.8 with proficiency scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Modeling TOEFL11SUBSET proficiency as regression with all features achieved a Pearson correlation of 0.8 and MAE of 0.4 in 10-fold cross validation. [→ Sowmya Vajjala 2016](#sowmya-vajjala-2016)

## Evidence

### Sowmya Vajjala 2016

Sowmya Vajjala. (2016). Automated assessment of non-native learner essays: Investigating the role of linguistic features. International Journal of Artificial Intelligence in Education. https://arxiv.org/abs/1612.00729

`q2 · i?` · `associational · r2`

Regression experiment (SMOReg, 10-fold CV) treating the three TOEFL11 proficiency categories as an ordinal numeric scale. The all-features model obtained "a Pearson correlation of 0.8" with actual proficiency values.

> "The model achieved a Pearson correlation of 0.8 and a Mean Abs olute Error (MAE) of 0.4 with actual proﬁciency values."

## Discussion


## Related Claims
- [A broad linguistic feature set yields 73.2% classification accuracy for three-level proficiency scoring of TOEFL11 essays](broad-linguistic-features-73-percent-toefl11-classification.md) — related
- [On the FCE corpus the feature set performs comparably to prior work (r = 0.64 on test), though below one coherence-feature study](fce-regression-comparable-to-prior-aes-work.md) — related
