---
type: claim
title: Extracting a decision tree from a random forest outperformed traditional DT, RFC, and RFR classifiers on this prediction task
description: Extracting a decision tree from a random forest outperformed traditional DT, RFC, and RFR classifiers on this prediction task
id: dt-from-rfc-outperforms-standard-classifiers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: mark-abdelshiheed-2024
    resource: "https://doi.org/10.1007/978-3-031-64299-9_11"
    title: "Mark Abdelshiheed, Jennifer K. Jacobs, and Sidney K. D'Mello. (2024). Aligning Tutor Discourse Supporting Rigorous Thinking with Tutee Content Mastery for Predicting Math Achievement. [doi:10.1007/978-3-031-64299-9_11](https://doi.org/10.1007/978-3-031-64299-9_11)"
    author: "Mark Abdelshiheed, Jennifer K. Jacobs, and Sidney K. D'Mello"
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Extracting a decision tree from a random forest outperformed traditional DT, RFC, and RFR classifiers on this prediction task

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The extracted-DT approach achieved higher AUCs than a traditional DT (0.59), RFC (0.64), and RFR (0.58, R2 = .018). [→ Mark Abdelshiheed 2024](#mark-abdelshiheed-2024)

## Evidence

### Mark Abdelshiheed 2024

Mark Abdelshiheed, Jennifer K. Jacobs, and Sidney K. D'Mello. (2024). Aligning Tutor Discourse Supporting Rigorous Thinking with Tutee Content Mastery for Predicting Math Achievement. [doi:10.1007/978-3-031-64299-9_11](https://doi.org/10.1007/978-3-031-64299-9_11)

`q2 · i?` · `associational · r2`

Comparison analysis (Section 3.3) of the extraction procedure against standard classifiers on the same data: "the best traditional DT had an AUC of0.59"; the best RFC reached 0.64 and the best RFR 0.58 (R2 = .018), versus 0.77 for the extracted DT.

> "None of these attempts came close to the results from the last column of Table 3. Specifically, the best traditional DT had an AUC of0.59 and likely overfitted the data by picking suboptimal features, such as Press for Accuracy, at the root node due to its low Gini index score."

## Discussion


## Related Claims
- [Combining tutor talk moves with student ITS metrics predicts math assessment scores better than either feature source alone (AUC 0.77 vs 0.63 and 0.66)](combined-talk-moves-its-predict-math-achievement.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — reports the opposite
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [The talk-move/ITS interaction pattern persists when predicting changes in assessment scores across rounds](talk-moves-its-robust-across-score-changes.md) — related
