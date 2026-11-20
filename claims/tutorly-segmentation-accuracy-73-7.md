---
type: claim
title: "Tutorly's video segmentation by learning goal achieved 73.7% overall accuracy within a five-second margin, with accuracy decreasing for longer videos"
description: "Tutorly's video segmentation by learning goal achieved 73.7% overall accuracy within a five-second margin, with accuracy decreasing for longer videos"
id: tutorly-segmentation-accuracy-73-7
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: wengxi-li-2024
    resource: "https://doi.org/10.48550/arXiv.2405.12946"
    title: "Wengxi Li, Roy Pea, Nick Haber, and Hari Subramonyam. (2024). Tutorly: Turning Programming Videos Into Apprenticeship Learning Environments with LLMs. [doi:10.48550/arXiv.2405.12946](https://doi.org/10.48550/arXiv.2405.12946)"
    author: Wengxi Li, Roy Pea, Nick Haber, and Hari Subramonyam
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Tutorly's video segmentation by learning goal achieved 73.7% overall accuracy within a five-second margin, with accuracy decreasing for longer videos

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The VSLG segmentation algorithm reached 73.7% overall accuracy within a five-second error margin across three topics, and its effectiveness in identifying precise segmentation points diminishes over longer video durations. [→ Wengxi Li 2024](#wengxi-li-2024)

## Evidence

### Wengxi Li 2024

Wengxi Li, Roy Pea, Nick Haber, and Hari Subramonyam. (2024). Tutorly: Turning Programming Videos Into Apprenticeship Learning Environments with LLMs. [doi:10.48550/arXiv.2405.12946](https://doi.org/10.48550/arXiv.2405.12946)

`q2 · i?` · `design · r2`

Technical evaluation in which the lead author manually segmented three 20-minute videos and timestamps were compared against GPT-generated segments, counting matches "within five seconds error". The article reports 73.7% overall accuracy and calls it acceptable for educational content.

> "Video transcript segmentation by learning goals algorithm achieved an overall accuracy of 73.7% within a five-second margin, which is an acceptable performance for educational content."

## Discussion


## Related Claims
- [MOOC video engagement declines with video length, with median engagement under half the duration for videos longer than nine minutes](mooc-engagement-declines-with-video-length.md) — related
- [In a within-subject study, Tutorly improved post-test performance from 61.9% to 76.6% for learners studying exploratory data analysis from a streamcast](tutorly-within-subject-post-test-gain.md) — related
