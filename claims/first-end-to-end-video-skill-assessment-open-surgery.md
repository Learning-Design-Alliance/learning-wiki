---
type: claim
title: This is the first end-to-end trained approach classifying open surgery skill directly from video without hand-crafted feature extraction
description: This is the first end-to-end trained approach classifying open surgery skill directly from video without hand-crafted feature extraction
id: first-end-to-end-video-skill-assessment-open-surgery
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: hoffmann-hanna-2024
    resource: "https://doi.org/10.1007/s11548-024-03093-3"
    title: "Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus. (2024). AIxSuture: vision-based assessment of open suturing skills. International Journal of Computer Assisted Radiology and Surgery. https://doi.org/10.1007/s11548-024-03093-3"
    author: Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# This is the first end-to-end trained approach classifying open surgery skill directly from video without hand-crafted feature extraction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q1 i?` The authors state that no prior published model classified open surgical skill directly from video without hand-crafted feature extraction, and their approach omits intermediate feature extraction, easing translation into practice. [→ Hoffmann Hanna 2024](#hoffmann-hanna-2024)

## Evidence

### Hoffmann Hanna 2024

Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus. (2024). AIxSuture: vision-based assessment of open suturing skills. International Journal of Computer Assisted Radiology and Surgery. https://doi.org/10.1007/s11548-024-03093-3

`q1 · i?` · `design · r2`

Authors' novelty claim from the Introduction, supported by their survey of prior open-surgery approaches that relied on hand-crafted features (duration, path length, movement counts) or simulator-collected force, motion and touch data. The Conclusion repeats that they are "the first to predict surgical skill for open surgery based only upon video data".

> "Therefore to the best of our knowledge, a model classifying the surgical skill directly from a video using an open surgery dataset without the requirement of hand-crafted feature extraction has not yet been published."

## Discussion


## Related Claims
- [A CNN-LSTM deep learning network classifies suturing versus dissection actions from robotic cardiac surgery simulation video with 93% test accuracy](dl-action-recognition-93-percent-robotic-cardiac-wetlab.md) — related
- [In the narrative synthesis, deep learning models classify surgeon skill levels from kinematic data with accuracy up to 95.4%](deep-learning-skill-classification-up-to-95-percent.md) — related
