---
type: strategy
id: tts-exemplar-coaching-pipeline
title: "TTS-based coaching pipeline: anchor and target exemplars, chunked recording, alignment, and focused drills"
description: "Generalizing from prior systems and grounded in shadowing pedagogy, the survey describes a four-step pipeline: \"render ananchorexemplar at a conservative tempo (120–140 WPM) and an optionaltargetat a faster tempo (150..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: wen-liang-2026
    resource: "https://arxiv.org/abs/2606.27380"
    title: "Wen Liang, Li Siyan, Zackary Rackauckas, and Julia Hirschberg. (2026). A Survey of Automated Presentation Coaching: Systems, Methods, and Open Challenges. https://arxiv.org/abs/2606.27380"
    author: Wen Liang, Li Siyan, Zackary Rackauckas, and Julia Hirschberg
---

# TTS-based coaching pipeline: anchor and target exemplars, chunked recording, alignment, and focused drills

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Generalizing from prior systems and grounded in shadowing pedagogy, the survey describes a four-step pipeline: "render ananchorexemplar at a conservative tempo (120–140 WPM) and an optionaltargetat a faster tempo (150–170 WPM)"; record the learner in short chunks of 5–12 s per section; align learner audio with the reference using CTC or DTW and compute deviations; and surface focused drills based on the highest-error dimensions. Effective exemplars tend to be short (under 12 s) to prevent cognitive overload.

## Design Implications

### Context
#### Requirements
- Neural TTS with controllability over rate, pauses, and emphasis; alignment via CTC or DTW; exemplars offered in multiple speed bands and vocabulary difficulty gradations.
#### Constraints
- Known limitations include over-constraining style when exemplars are treated as a single correct read, and synthetic emphasis that may not match domain conventions.

### Target Learners
- L2 English speakers rehearsing slide-based presentations

### Target Learning Goals
- Improved pronunciation, lexical stress, prosody, and pacing through exemplar-guided shadowing practice

## Related Strategies

- [Create small controlled presentation mini-sets as a near-term community benchmark](presentation-mini-sets-community-benchmark.md)

## Examples
-

## Key Sources
- Wen Liang, Li Siyan, Zackary Rackauckas, and Julia Hirschberg. (2026). A Survey of Automated Presentation Coaching: Systems, Methods, and Open Challenges. https://arxiv.org/abs/2606.27380
