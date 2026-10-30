---
type: claim
title: "Coordination actions discriminate well-functioning groups better than inactivity: a CART decision tree splits clusters on coordination counts (value 3.5), revising the assumption that gaps are the key failure indicator"
description: "Coordination actions discriminate well-functioning groups better than inactivity: a CART decision tree splits clusters on coordination counts (value 3.5), revising the assumption that gaps are the key failure indicator"
id: coordination-actions-better-indicator-than-inactivity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: h-ulrich-hoppe-2021
    resource: "https://doi.org/10.1007/s40593-020-00229-9"
    title: "H. Ulrich Hoppe, et al. (2021). Using Sequence Analysis to Determine the Well-Functioning of Small Groups in Large Online Courses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00229-9"
    author: H. Ulrich Hoppe, et al
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Coordination actions discriminate well-functioning groups better than inactivity: a CART decision tree splits clusters on coordination counts (value 3.5), revising the assumption that gaps are the key failure indicator

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In Study 1, the number of coordination actions was the best discriminator between sequence-analysis clusters, separating out more than 90% of cluster 1 at a split value of 3.5. [→ H. Ulrich Hoppe 2021](#h-ulrich-hoppe-2021)
`q2 i?` The authors conclude that coordination actions, typically occurring in the first half of the working period, can to some extent counter-balance the likely negative effects of inactivity. [→ H. Ulrich Hoppe 2021](#h-ulrich-hoppe-2021)

## Evidence

### H. Ulrich Hoppe 2021

H. Ulrich Hoppe, et al. (2021). Using Sequence Analysis to Determine the Well-Functioning of Small Groups in Large Online Courses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00229-9

`q2 · i?` · `associational · r1`

Regression-based CART analysis (in R) on Study 1 action counts (gaps and coordination) predicting cluster membership for the 65 groups. The article reports the split value 3.5 and that the tree "separates out more than 90% of cluster 1"; no effect size is printed.

> "Based on the principle of maximizing information gain in every split, we can conclude that the number of coordination actions with the separating value of 3.5 is the best discriminator and already separates out more than 90% of cluster 1 with relatively small mix-ins from the other clusters."

## Discussion


## Related Claims
- [Sequence-alignment clusters of small-group action logs differ in productivity and balance of contribution, with the largest cluster showing the lowest word count and highest imbalance](sequence-alignment-clusters-differ-in-quality.md) — related
- [Unsupervised time-series clustering identifies low performers more accurately than SVM or decision-tree classifiers trained on two temporal statistics](unsupervised-clustering-beats-feature-classifiers.md) — related
