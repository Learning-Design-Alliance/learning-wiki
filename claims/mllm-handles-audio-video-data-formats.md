---
type: claim
title: MLLMs can analyze alternative experimental data formats, including WAV audio files and video, enabling classroom-scale analyses
description: MLLMs can analyze alternative experimental data formats, including WAV audio files and video, enabling classroom-scale analyses
id: mllm-handles-audio-video-data-formats
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jochen-kuhn-2026
    resource: "https://doi.org/10.1088/1361-6404/ae303b"
    title: "Jochen Kuhn, David J. Rakestraw, Stefan Küchemann & Patrik Vogt. (2026). AI-Supported Mini-Labs: Combining Smartphone-Based Experiments and Multimodal AI. Originally published 2025. [doi:10.1088/1361-6404/ae303b](https://doi.org/10.1088/1361-6404/ae303b)"
    author: "Jochen Kuhn, David J. Rakestraw, Stefan Küchemann & Patrik Vogt"
    q: 1
    i: "?"
    kind: design
    rigour: 1
  - id: jochen-kuhn-2026-2
    resource: "https://doi.org/10.1088/1361-6404/ae303b"
    title: "Jochen Kuhn, David J. Rakestraw, Stefan Küchemann & Patrik Vogt. (2026). AI-Supported Mini-Labs: Combining Smartphone-Based Experiments and Multimodal AI. Originally published 2025. [doi:10.1088/1361-6404/ae303b](https://doi.org/10.1088/1361-6404/ae303b)"
    author: "Jochen Kuhn, David J. Rakestraw, Stefan Küchemann & Patrik Vogt"
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# MLLMs can analyze alternative experimental data formats, including WAV audio files and video, enabling classroom-scale analyses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r1` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` ChatGPT-4o can process audio files in WAV format to generate spectrograms and analyze lightning-generated VLF signals, and can analyze video files for time-resolved spectroscopy. [→ Jochen Kuhn 2026](#jochen-kuhn-2026)
`q1 i?` AI-supported video analysis is fast enough that students can design and study physiological experiments in class, which the authors say is difficult without AI assistance. [→ Jochen Kuhn 2026 (2)](#jochen-kuhn-2026-2)

## Evidence

### Jochen Kuhn 2026

Jochen Kuhn, David J. Rakestraw, Stefan Küchemann & Patrik Vogt. (2026). AI-Supported Mini-Labs: Combining Smartphone-Based Experiments and Multimodal AI. Originally published 2025. [doi:10.1088/1361-6404/ae303b](https://doi.org/10.1088/1361-6404/ae303b)

`q1 · i?` · `design · r1`

Authors' demonstration in Example 2: a lightning sferics recording made with a simple receiving device was saved as a WAV file and analyzed by ChatGPT-4o, which produced a spectrogram of tweeks; the article characterizes the acoustic analysis precision as remarkable but prints no accuracy value.

> "This example illustrates that an MLLM is also capable of handling alternative data formats—in this case, an audio ﬁle in WAV format. Moreover, it demonstrates the remarkable precision with which acoustic analyses can be conducted"

### Jochen Kuhn 2026 (2)

Jochen Kuhn, David J. Rakestraw, Stefan Küchemann & Patrik Vogt. (2026). AI-Supported Mini-Labs: Combining Smartphone-Based Experiments and Multimodal AI. Originally published 2025. [doi:10.1088/1361-6404/ae303b](https://doi.org/10.1088/1361-6404/ae303b)

`q1 · i?` · `design · r1`

Authors' report on Example 3, real-time spectroscopy of blood volume dynamics from a smartphone video of light transmitted through a finger; the article states the analysis was very fast and that even a single experiment is difficult to perform without AI assistance because students would need to learn video analysis software.

> "The analysis by ChatGPT-4o was very fast and dramatically enhances the opportunity for doing this type of analysis in the classroom."

## Discussion


## Related Claims
- [MLLM-supported analysis offers advantages over conventional methods: time savings, high-quality exportable visualizations, and access to analyses beyond school mathematics](mllm-analysis-advantages-over-conventional.md) — a broader claim this one bears on
- [MLLM-based analysis of smartphone accelerometer data aligns with conventional spreadsheet analysis of the same dataset](mllm-analysis-matches-spreadsheet-drag-coefficient.md) — related
