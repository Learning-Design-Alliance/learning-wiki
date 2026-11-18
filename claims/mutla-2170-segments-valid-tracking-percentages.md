---
type: claim
title: "After filtering, the MUTLA video data contain 2170 question segments, with 61.54% having valid face tracking for at least 50% of frames and 18.30% fully tracked"
description: "After filtering, the MUTLA video data contain 2170 question segments, with 61.54% having valid face tracking for at least 50% of frames and 18.30% fully tracked"
id: mutla-2170-segments-valid-tracking-percentages
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: fangli-xu-2019
    resource: "https://doi.org/10.48550/arXiv.1910.06078"
    title: "Fangli Xu, Lingfei Wu, KP Thai, Carol Hsu, Wei Wang, Richard Tong. (2019). MUTLA: A Large-Scale Dataset for Multimodal Teaching and Learning Analytics. [doi:10.48550/arXiv.1910.06078](https://doi.org/10.48550/arXiv.1910.06078)"
    author: Fangli Xu, Lingfei Wu, KP Thai, Carol Hsu, Wei Wang, Richard Tong
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# After filtering, the MUTLA video data contain 2170 question segments, with 61.54% having valid face tracking for at least 50% of frames and 18.30% fully tracked

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The filtered video corpus contains 2170 segments, of which 61.54% have at least 50% valid tracking, 49.88% at least 70%, and 18.30% 100% valid tracking, where valid tracking means a fully visible student face. [→ Fangli Xu 2019](#fangli-xu-2019)

## Evidence

### Fangli Xu 2019

Fangli Xu, Lingfei Wu, KP Thai, Carol Hsu, Wei Wang, Richard Tong. (2019). MUTLA: A Large-Scale Dataset for Multimodal Teaching and Learning Analytics. [doi:10.48550/arXiv.1910.06078](https://doi.org/10.48550/arXiv.1910.06078)

`q2 · i?` · `design · r2`

Descriptive dataset statistics from the video processing section: after filtering the corpus contains "2170 segments", and Table 2 reports valid-tracking percentages (61.54% at least 50%, 49.88% at least 70%, 18.30% at 100%), with valid tracking defined as a fully visible student face. These are descriptive counts, not test statistics.

> "After filtering, it contains 2170 segments. Table 2 showed the percentage of valid tracking of the segments for different percentile. We define that fully visible student face as valid tracking."

## Discussion


## Related Claims
- [The MUTLA dataset covers 156 students from two SAIL after-school centers in China working across 6 subjects](mutla-156-students-two-centers-six-subjects.md) — related
- [LittleLearner's capabilities tightly track its controlled exposure: strong on in-scope tasks, degrading beyond the K-5 boundary](littlelearner-capabilities-track-controlled-exposure.md) — related
- [Across scaling, post-training, and in-context learning, the pretraining filter rather than the intervention sets LittleLearner's capability ceiling](pretraining-filter-sets-capability-ceiling.md) — related
