---
type: claim
title: Combining tutor talk moves with student ITS metrics predicts math assessment scores better than either feature source alone (AUC 0.77 vs 0.63 and 0.66)
description: Combining tutor talk moves with student ITS metrics predicts math assessment scores better than either feature source alone (AUC 0.77 vs 0.63 and 0.66)
id: combined-talk-moves-its-predict-math-achievement
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

# Combining tutor talk moves with student ITS metrics predicts math assessment scores better than either feature source alone (AUC 0.77 vs 0.63 and 0.66)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A decision tree extracted from a random forest on combined talk-move and ITS features achieved higher AUC than trees from either feature source alone. [→ Mark Abdelshiheed 2024](#mark-abdelshiheed-2024)

## Evidence

### Mark Abdelshiheed 2024

Mark Abdelshiheed, Jennifer K. Jacobs, and Sidney K. D'Mello. (2024). Aligning Tutor Discourse Supporting Rigorous Thinking with Tutee Content Mastery for Predicting Math Achievement. [doi:10.1007/978-3-031-64299-9_11](https://doi.org/10.1007/978-3-031-64299-9_11)

`q2 · i?` · `associational · r2`

Analysis of 4124 evaluation periods from 1080 9th-graders in small-group tutoring plus MATHia ITS use; the combined-feature tree reached "AU C= 0.79" on the whole dataset (average 5-fold test AUC 0.77), versus 0.63 for talk moves and 0.66 for ITS alone in Table 3.

> "Thebest decision tree(AU C= 0.79) emerges from combining all features as shown in Figure 2c. The left half of the tree shows that Revoicing significantly distinguishes scores for low-mastery students."

## Discussion


## Related Claims
- [The talk-move/ITS interaction pattern persists when predicting changes in assessment scores across rounds](talk-moves-its-robust-across-score-changes.md) — related
- [Extracting a decision tree from a random forest outperformed traditional DT, RFC, and RFR classifiers on this prediction task](dt-from-rfc-outperforms-standard-classifiers.md) — related
- [ITS metrics alone predict assessment scores moderately, with higher APLS associated with better scores for low-mastery students](its-metrics-alone-predict-assessment.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [High tutor use of Revoicing is associated with much higher assessment scores for students with low ITS mastery](revoicing-predictive-low-mastery-students.md) — a narrower finding that bears on this claim
