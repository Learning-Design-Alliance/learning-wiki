---
type: claim
title: "In a statewide VLE algebra dataset, item missingness is nonignorable: skipping is related to student ability and item difficulty as measured in 2PL-IRT"
description: "In a statewide VLE algebra dataset, item missingness is nonignorable: skipping is related to student ability and item difficulty as measured in 2PL-IRT"
id: vle-item-skipping-nonignorable-missingness
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: xue-2020
    resource: "https://educationaldatamining.org/EDM2020/"
    title: "Xue, K., Huggins-Manley, A. C., & Leite, W. (2020). Semi-supervised Learning Method for Adjusting Biased Item Difficulty Estimates Caused by Nonignorable Missingness under 2PL-IRT Model. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), pp. 715-719. https://educationaldatamining.org/EDM2020/"
    author: "Xue, K., Huggins-Manley, A. C., & Leite, W."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: xue-2020-2
    resource: "https://educationaldatamining.org/EDM2020/"
    title: "Xue, K., Huggins-Manley, A. C., & Leite, W. (2020). Semi-supervised Learning Method for Adjusting Biased Item Difficulty Estimates Caused by Nonignorable Missingness under 2PL-IRT Model. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), pp. 715-719. https://educationaldatamining.org/EDM2020/"
    author: "Xue, K., Huggins-Manley, A. C., & Leite, W."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: xue-2020-3
    resource: "https://educationaldatamining.org/EDM2020/"
    title: "Xue, K., Huggins-Manley, A. C., & Leite, W. (2020). Semi-supervised Learning Method for Adjusting Biased Item Difficulty Estimates Caused by Nonignorable Missingness under 2PL-IRT Model. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), pp. 715-719. https://educationaldatamining.org/EDM2020/"
    author: "Xue, K., Huggins-Manley, A. C., & Leite, W."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# In a statewide VLE algebra dataset, item missingness is nonignorable: skipping is related to student ability and item difficulty as measured in 2PL-IRT

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` Students with lower ability had a higher probability to skip an item shown to them, and students had a higher probability to skip more difficult items. [→ Xue 2020](#xue-2020)
`q2 i?` Students with high ability had a lower probability to skip a whole domain, while the relationship between ability and completing a domain was inconsistent. [→ Xue 2020 (2)](#xue-2020-2)
`q2 i?` The VLE response data contained large proportions of missingness (55% to 75% per item) across 63,625 students. [→ Xue 2020 (3)](#xue-2020-3)

## Evidence

### Xue 2020

Xue, K., Huggins-Manley, A. C., & Leite, W. (2020). Semi-supervised Learning Method for Adjusting Biased Item Difficulty Estimates Caused by Nonignorable Missingness under 2PL-IRT Model. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), pp. 715-719. https://educationaldatamining.org/EDM2020/

`q2 · i?` · `associational · r2`

Hierarchical logistic regression on operational VLE data (third level: item skipping regressed on pretest math ability S and observed incorrect response rate Dk), conducted per domain and district. The article reports "students with lower ability level had higher probability to skip an item shown to them" and a higher skip probability for harder items.

> "The logistic regression test showed that students with lower ability level had higher probability to skip an item shown to them; and student had a higher probability to skip item with higher diﬃculties."

### Xue 2020 (2)

Xue, K., Huggins-Manley, A. C., & Leite, W. (2020). Semi-supervised Learning Method for Adjusting Biased Item Difficulty Estimates Caused by Nonignorable Missingness under 2PL-IRT Model. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), pp. 715-719. https://educationaldatamining.org/EDM2020/

`q2 · i?` · `associational · r2`

First-level hierarchical logistic regression of skipping a domain on pretest state standardized test scores, fit per school district and domain. For "most school districts and most students, β1,ij were signiﬁcant negative". The completing-domain test produced no consistent conclusion.

> "After ﬁtting the models, we found that for most school districts and most students, β1,ij were signiﬁcant negative. We can conclude that students with high ability level had a lower probability to skip a domain"

### Xue 2020 (3)

Xue, K., Huggins-Manley, A. C., & Leite, W. (2020). Semi-supervised Learning Method for Adjusting Biased Item Difficulty Estimates Caused by Nonignorable Missingness under 2PL-IRT Model. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), pp. 715-719. https://educationaldatamining.org/EDM2020/

`q2 · i?` · `associational · r2`

Operational data exploration of students' responses to Algebra I items in a statewide-used VLE, with 10 algebra domains and 41 to 89 items per domain. Because students could skip randomly selected items, "The proportion of missingness for each item is between 55% to 75%".

> "The total number of students was 63,625. Since students were allowed to skip items in the learning environment when they responded to the items which were selected by the system randomly, the responses to each item contained large amount of missing values. The proportion of missingness for each item is between 55% to 75%."

## Discussion


## Related Claims
- [Existing item fit statistics are derived for linear tests under assumptions of no missing responses and normal ability distributions, leaving adaptive testing contexts understudied](item-fit-statistics-derived-for-linear-tests-only.md) — related
- [A semi-supervised deep learning architecture recovers the ability distribution of anchor students more accurately than direct 2PL-IRT fitting under simulated nonignorable missingness](semi-supervised-deep-learning-unbiased-ability-estimates.md) — related
- [Both proposed adjustment methods (IEA and BA) reduce RMSE of item difficulty estimates from direct 2PL-IRT fitting, with BA yielding more consistent (lower-variance) estimates in simulation](iea-ba-reduce-difficulty-estimate-bias.md) — related
