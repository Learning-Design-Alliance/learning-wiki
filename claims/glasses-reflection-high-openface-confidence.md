---
type: claim
title: Glasses reflections can render eyes unrecognizable in webcam frames while OpenFace confidence stays above 0.97
description: Glasses reflections can render eyes unrecognizable in webcam frames while OpenFace confidence stays above 0.97
id: glasses-reflection-high-openface-confidence
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: bodonhelyi-2026
    resource: "https://doi.org/10.48550/arXiv.2602.09904"
    title: "Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E. (2026). Safeguarding Privacy: Privacy-Preserving Detection of Mind Wandering and Disengagement Using Federated Learning in Online Education. [doi:10.48550/arXiv.2602.09904](https://doi.org/10.48550/arXiv.2602.09904)"
    author: Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E.
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Glasses reflections can render eyes unrecognizable in webcam frames while OpenFace confidence stays above 0.97

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Screen reflection on glasses can make the eyes unrecognizable and untraceable in selected frames while the OpenFace framework still reports confidence above 0.97, so failed gaze extraction goes undetected. [→ Bodonhelyi 2026](#bodonhelyi-2026)

## Evidence

### Bodonhelyi 2026

Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E. (2026). Safeguarding Privacy: Privacy-Preserving Detection of Mind Wandering and Disengagement Using Federated Learning in Online Education. [doi:10.48550/arXiv.2602.09904](https://doi.org/10.48550/arXiv.2602.09904)

`q1 · i?` · `design · r2`

Demonstration with example webcam frames of users with and without glasses (Figure 2): reflection can make "eyes unrecognizable and untraceable in a selected frame sequence" while OpenFace confidence "still stays above 0.97".

> "the screen reflection on participants’ glasses might make their eyes unrecognizable and untraceable in a selected frame sequence, while the confidence provided by the OpenFace (Baltrusaitis et al, 2018) framework still stays above 0.97 (Figure 2)."

## Discussion


## Related Claims
- [LIME analysis shows the latent features mainly encode information from eye and mouth areas of the face](lime-eye-mouth-areas-in-latent-features.md) — related
