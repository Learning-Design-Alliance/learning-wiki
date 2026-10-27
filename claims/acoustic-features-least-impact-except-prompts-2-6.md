---
type: claim
title: Acoustic features have none to least impact on scoring QWK except for prompts 2 and 6
description: Acoustic features have none to least impact on scoring QWK except for prompts 2 and 6
id: acoustic-features-least-impact-except-prompts-2-6
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: pakhi-bamdev-2023
    resource: "https://doi.org/10.1007/s40593-022-00291-5"
    title: "Pakhi Bamdev, Manraj Singh Grover, Yaman Kumar Singla, Payman Vafaee, Mika Hama, Rajiv Ratn Shah. (2023). Automated Speech Scoring System Under The Lens Evaluating and interpreting the linguistic cues for language proficiency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00291-5"
    author: Pakhi Bamdev, Manraj Singh Grover, Yaman Kumar Singla, Payman Vafaee, Mika Hama, Rajiv Ratn Shah
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Acoustic features have none to least impact on scoring QWK except for prompts 2 and 6

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Removing audio features has none to least impact on QWK for every prompt except prompts 2 and 6, where audio and speech-delivery features gain importance. [→ Pakhi Bamdev 2023](#pakhi-bamdev-2023)

## Evidence

### Pakhi Bamdev 2023

Pakhi Bamdev, Manraj Singh Grover, Yaman Kumar Singla, Payman Vafaee, Mika Hama, Rajiv Ratn Shah. (2023). Automated Speech Scoring System Under The Lens Evaluating and interpreting the linguistic cues for language proficiency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00291-5

`q2 · i?` · `design · r2`

Leave-one-out ablation of the acoustic feature group across six prompts. The authors report audio features have "none to least impact on QWK for every prompt except for prompts 2 and 6", where rhythm and stress patterns receive more importance in scoring.

> "Audio features (AF) have none to least impact on QWK for every prompt except for prompts 2 and 6."

## Discussion


## Related Claims

- [Removing grammar and vocabulary features drops scoring QWK by 7-13% across prompts](gvf-removal-drops-qwk-7-13-percent.md) — related
- [Adding fluency features to content features sharply increases scoring QWK for every prompt](fluency-features-sharp-qwk-increase-ablation.md) — related
- [Lower model performance on Prompt 2 tracks poor inter-annotator agreement (QWK 0.560 vs 0.758)](prompt2-low-performance-tracks-annotator-agreement.md)
- [Multimodal XGBoost models achieved rubric-aligned scoring comparable to expert ratings, and no single modality approached multimodal performance](multimodal-xgboost-expert-comparable-scoring.md)
