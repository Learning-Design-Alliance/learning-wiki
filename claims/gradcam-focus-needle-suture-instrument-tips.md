---
type: claim
title: Grad-CAM visualization shows the action recognition network focuses on the needle, suture, and instrument tips during suturing and on the tissue during dissection
description: Grad-CAM visualization shows the action recognition network focuses on the needle, suture, and instrument tips during suturing and on the tissue during dissection
id: gradcam-focus-needle-suture-instrument-tips
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: atroshchenko-gennady-v-2025
    resource: "https://doi.org/10.1007/s11701-025-02563-3"
    title: "Atroshchenko Gennady V., Korup Lærke Riis, Hashemi Nasseh, Østergaard Lasse Riis, Tolsgaard Martin G., Rasmussen Sten. (2025). Artificial intelligence-based action recognition and skill assessment in robotic cardiac surgery simulation: a feasibility study. Journal of Robotic Surgery. https://doi.org/10.1007/s11701-025-02563-3"
    author: Atroshchenko Gennady V., Korup Lærke Riis, Hashemi Nasseh, Østergaard Lasse Riis, Tolsgaard Martin G., Rasmussen Sten
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Grad-CAM visualization shows the action recognition network focuses on the needle, suture, and instrument tips during suturing and on the tissue during dissection

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Gradient-weighted Class Activation Mapping revealed the algorithm attended to the needle, suture, and instrument tips during suturing and to the tissue during dissection. [→ Atroshchenko Gennady V. 2025](#atroshchenko-gennady-v-2025)

## Evidence

### Atroshchenko Gennady V. 2025

Atroshchenko Gennady V., Korup Lærke Riis, Hashemi Nasseh, Østergaard Lasse Riis, Tolsgaard Martin G., Rasmussen Sten. (2025). Artificial intelligence-based action recognition and skill assessment in robotic cardiac surgery simulation: a feasibility study. Journal of Robotic Surgery. https://doi.org/10.1007/s11701-025-02563-3

`q2 · i?` · `design · r2`

Interpretability analysis (Grad-CAM) of the trained action recognition network, shown in Fig. 4. The authors state Grad-CAM "aims to enhance the interpretability of deep learning algorithms", supporting surgeon-facing explanations of model attention.

> "Gradient-weighted Class Activation Mapping for the action recognition deep learning network (Fig. 4) revealed that the algorithm focused on the needle, suture, and instrument tips during suturing, and on the tissue during dissection."

## Discussion


## Related Claims
- [A CNN-LSTM deep learning network classifies suturing versus dissection actions from robotic cardiac surgery simulation video with 93% test accuracy](dl-action-recognition-93-percent-robotic-cardiac-wetlab.md) — related
