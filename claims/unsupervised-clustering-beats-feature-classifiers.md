---
type: claim
title: Unsupervised time-series clustering identifies low performers more accurately than SVM or decision-tree classifiers trained on two temporal statistics
description: Unsupervised time-series clustering identifies low performers more accurately than SVM or decision-tree classifiers trained on two temporal statistics
id: unsupervised-clustering-beats-feature-classifiers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2019
sources:
  - id: peach-2019
    resource: "https://doi.org/10.1038/s41539-019-0054-0"
    title: "Peach, R. L., Yaliraki, S. N., Lefevre, D. and Barahona, M. (2019). Data-driven unsupervised clustering of online learner behaviour. npj Science of Learning 4:14. https://doi.org/10.1038/s41539-019-0054-0"
    author: Peach, R. L., Yaliraki, S. N., Lefevre, D. and Barahona, M.
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Unsupervised time-series clustering identifies low performers more accurately than SVM or decision-tree classifiers trained on two temporal statistics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` SVM (RBF kernel) and depth-4 decision-tree classifiers trained on mean binge session length and percentage task completion predicted only 3-4 of 7 low-performance learners, versus 6 of 7 located by the unsupervised clustering. [→ Peach 2019](#peach-2019)

## Evidence

### Peach 2019

Peach, R. L., Yaliraki, S. N., Lefevre, D. and Barahona, M. (2019). Data-driven unsupervised clustering of online learner behaviour. npj Science of Learning 4:14. https://doi.org/10.1038/s41539-019-0054-0

`q2 · i?` · `associational · r1`

Comparison of the unsupervised clustering against an SVM (RBF kernel) and a depth-4 decision tree trained on the two statistical features from Fig. 4. Both classifiers showed poor accuracy: "only 3– 4 out of 7 low-performance learners were accurately predicted".

> "For both methods, we ﬁnd that the accuracy of learner classi ﬁcation against performance is low: only 3– 4 out of 7 low-performance learners were accurately predicted."

## Discussion


## Related Claims
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — related
- [All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts](classifiers-beat-zero-rule-baseline-engagement.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [Cluster-based sampling of single answers from clusters (cluster centroid and random cluster instance) required the least manual grading and correcting work, outperforming full-cluster and random sampling strategies](cluster-instance-sampling-minimizes-grading-work.md) — related
