---
type: claim
title: On the FCE corpus the feature set performs comparably to prior work (r = 0.64 on test), though below one coherence-feature study
description: On the FCE corpus the feature set performs comparably to prior work (r = 0.64 on test), though below one coherence-feature study
id: fce-regression-comparable-to-prior-aes-work
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: mixed
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
  - id: sowmya-vajjala-2016-2
    resource: "https://arxiv.org/abs/1612.00729"
    title: "Sowmya Vajjala. (2016). Automated assessment of non-native learner essays: Investigating the role of linguistic features. International Journal of Artificial Intelligence in Education. https://arxiv.org/abs/1612.00729"
    author: Sowmya Vajjala
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# On the FCE corpus the feature set performs comparably to prior work (r = 0.64 on test), though below one coherence-feature study

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The FCE regression model reached r = 0.64 and MAE 3.6 on FCE-TEST, statistically indistinguishable from Yannakoudakis et al. (2011) but significantly below Yannakoudakis and Briscoe (2012). [→ Sowmya Vajjala 2016](#sowmya-vajjala-2016)

## Evidence

### Sowmya Vajjala 2016

Sowmya Vajjala. (2016). Automated assessment of non-native learner essays: Investigating the role of linguistic features. International Journal of Artificial Intelligence in Education. https://arxiv.org/abs/1612.00729

`q2 · i?` · `associational · r2`

Regression on the FCE corpus using the same train-test split as prior research (1141 training texts from year 2000, 97 test texts from 2001). Test correlation was 0.64 with "a MAE of 3.6".

> "On testing with FCE-T EST (containing 97 texts), the model had a correlation of 0.64 and a MAE of 3.6."

### Sowmya Vajjala 2016 (2)

Sowmya Vajjala. (2016). Automated assessment of non-native learner essays: Investigating the role of linguistic features. International Journal of Artificial Intelligence in Education. https://arxiv.org/abs/1612.00729

`q2 · i?` · `associational · r2`

Cocor correlation comparison against prior FCE results: no significant difference versus Yannakoudakis et al. (2011), but the Yannakoudakis and Briscoe (2012) result was "signiﬁcantly better (p < 0.05)" than this model.

> "However, the result from the second study (Yannakoudakis and Briscoe, 2012) is signiﬁcantly better (p < 0.05) than the current model, which can perhaps be attribute d to the presence of additional coherence features in their model"

## Discussion


## Related Claims
- [Regression on TOEFL11SUBSET reaches a Pearson correlation of 0.8 with proficiency scores](toefl11-regression-correlation-0-8.md) — related
