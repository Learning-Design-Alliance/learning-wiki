---
type: claim
title: Learned difficulty parameters show a moderate positive correlation with empirical KC difficulty on QATD2k
description: Learned difficulty parameters show a moderate positive correlation with empirical KC difficulty on QATD2k
id: learned-difficulty-correlates-empirical-difficulty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: shuyan-huang-2026
    resource: "https://doi.org/10.48550/arxiv.2605.01097"
    title: "Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Andrew Lan. (2026). Interpretable Difficulty-Aware Knowledge Tracing in Tutor-Student Dialogues. arXiv preprint. https://arxiv.org/abs/2605.01097 [doi:10.48550/arxiv.2605.01097](https://doi.org/10.48550/arxiv.2605.01097)"
    author: Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Andrew Lan
    q: 2
    i: 2
    kind: design
    rigour: 2
---

# Learned difficulty parameters show a moderate positive correlation with empirical KC difficulty on QATD2k

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i2` medium
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i2` Predicted KC difficulty correlates moderately positively with ground-truth difficulty computed from empirical correctness statistics (r = 0.368, p < 0.001). [→ Shuyan Huang 2026](#shuyan-huang-2026)

## Evidence

### Shuyan Huang 2026

Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Andrew Lan. (2026). Interpretable Difficulty-Aware Knowledge Tracing in Tutor-Student Dialogues. arXiv preprint. https://arxiv.org/abs/2605.01097 [doi:10.48550/arxiv.2605.01097](https://doi.org/10.48550/arxiv.2605.01097)

`q2 · i2` · `design · r2`

Analysis on QATD2k test set, chosen because it is "collected from real-world educational environments"; ground-truth KC difficulty follows classical test theory as 1 − Ncorrect/Ntotal, predicted values min–max normalized, Pearson correlation computed across KCs (r = 0.368, p < 0.001).

> "Results show a moderate positive correlation (r= 0.368 ,p<0.001 ), suggesting that the learned difficulty parameters align with empirical difficulty patterns across KCs to a certain extent"

## Discussion


## Related Claims
- [Test difficulty value defined as ratio of observed to maximum score vector length times cosine of their angle equals test mean divided by number of items](test-difficulty-value-cosine-definition.md) — related
- [Point measure correlations were unchanged by the difficulty adjustment because the new person ability estimates are linear transformations of the old ones](map-k2-point-measure-correlations-unchanged.md) — related
- [Intersection point k0 of item difficulty and discriminating curves provides a data-driven item-deletion criterion](k0-intersection-item-deletion-criterion.md) — related
- [Scores on the debugging-oriented Python proficiency assessment moderately predict successful code repair](proficiency-assessment-predicts-fix-success.md) — related
- [Point-biserial item-total correlation is negatively related to test discriminating value and can be expressed via item and test difficulty and discrimination parameters](point-biserial-negative-test-discrimination-relation.md) — related
- Ground-truth difficulty labels in reviewed studies come roughly equally from expert/annotator labelling (34%), Classical Test Theory (34%), and Item Response Theory (26%) — related
