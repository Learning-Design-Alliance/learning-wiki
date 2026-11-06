---
type: claim
title: "A CNN-LSTM deep learning network classifies suturing versus dissection actions from robotic cardiac surgery simulation video with 93% test accuracy"
description: "A CNN-LSTM deep learning network classifies suturing versus dissection actions from robotic cardiac surgery simulation video with 93% test accuracy"
id: dl-action-recognition-93-percent-robotic-cardiac-wetlab
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
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

# A CNN-LSTM deep learning network classifies suturing versus dissection actions from robotic cardiac surgery simulation video with 93% test accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A deep learning network combining CNN spatial feature extraction with LSTM temporal information recognized the surgical actions suturing and dissection from video with 93% accuracy on an unseen test set, with average recall, precision, and F1-score all at 93%. [→ Atroshchenko Gennady V. 2025](#atroshchenko-gennady-v-2025)

## Evidence

### Atroshchenko Gennady V. 2025

Atroshchenko Gennady V., Korup Lærke Riis, Hashemi Nasseh, Østergaard Lasse Riis, Tolsgaard Martin G., Rasmussen Sten. (2025). Artificial intelligence-based action recognition and skill assessment in robotic cardiac surgery simulation: a feasibility study. Journal of Robotic Surgery. https://doi.org/10.1007/s11701-025-02563-3

`q2 · i?` · `design · r2`

Test-set evaluation of the action recognition network trained on 435 annotated recordings of wet lab tasks. The results section reports the model "achieved an accuracy of 93%", with Table 2 weighted-average recall, precision and F1-score each 0.93 for suturing and dissection classification.

> "The action recognition model achieved an accuracy of 93%, while the skill assessment deep learning network had an accuracy of 56%."

## Discussion


## Related Claims
- [Fivefold cross-validation of the action recognition network yields a mean accuracy of 98%, while skill assessment cross-validation varies widely (mean 79%)](cross-validation-ar-98-sa-79-mean-accuracy.md) — related
- [Grad-CAM visualization shows the action recognition network focuses on the needle, suture, and instrument tips during suturing and on the tissue during dissection](gradcam-focus-needle-suture-instrument-tips.md) — related
- [The skill assessment network distinguishing novice from expert surgeons reached only 56% test accuracy, failing to achieve useful performance](skill-assessment-network-56-percent-accuracy-failed.md) — related
