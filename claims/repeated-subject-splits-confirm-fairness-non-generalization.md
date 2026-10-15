---
type: claim
title: Repeated subject-level split experiments confirm that validation-level fairness improvements from MAE-gap regularization do not correspond to consistent generalization to unseen subjects
description: Repeated subject-level split experiments confirm that validation-level fairness improvements from MAE-gap regularization do not correspond to consistent generalization to unseen subjects
id: repeated-subject-splits-confirm-fairness-non-generalization
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: christoforos-fragkiadakis-2026
    resource: "https://doi.org/10.48550/arxiv.2609.02232"
    title: "Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag. (2026). Fairness-Aware Multimodal Transformer Modeling for Real-Time Student Attention Estimation. https://arxiv.org/abs/2609.02232 [doi:10.48550/arxiv.2609.02232](https://doi.org/10.48550/arxiv.2609.02232)"
    author: Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Repeated subject-level split experiments confirm that validation-level fairness improvements from MAE-gap regularization do not correspond to consistent generalization to unseen subjects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across multiple re-drawn subject-level train-validation-test splits with paired baseline and fairness-model comparisons, validation improvements achieved by fairness regularization did not correspond to consistent generalization to unseen subjects. [→ Christoforos Fragkiadakis 2026](#christoforos-fragkiadakis-2026)

## Evidence

### Christoforos Fragkiadakis 2026

Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag. (2026). Fairness-Aware Multimodal Transformer Modeling for Real-Time Student Attention Estimation. https://arxiv.org/abs/2609.02232 [doi:10.48550/arxiv.2609.02232](https://doi.org/10.48550/arxiv.2609.02232)

`q2 · i?` · `design · r2`

Robustness experiment in which the dataset was partitioned multiple times at the subject level with stratified demographic sampling; the same subject partitions were shared across baseline and fairness models for paired comparisons within each split.

> "The results were consistent with the main experiments and further supported that the validation improvements achieved by fairness regularization did not correspond to consistent generalization to unseen subjects (Appendix B)."

## Discussion


## Related Claims
- [Demographic MAE-gap regularization reduces targeted subgroup gaps on validation data, but these fairness gains do not consistently transfer to held-out test subjects](mae-gap-regularization-validation-gains-do-not-generalize.md) — possibly the same claim (merge candidate)
