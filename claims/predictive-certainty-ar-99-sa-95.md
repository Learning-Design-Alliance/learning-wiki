---
type: claim
title: "The predictive certainty of the trained networks was high (99% for action recognition, 95% for skill assessment) despite differing accuracies"
description: "The predictive certainty of the trained networks was high (99% for action recognition, 95% for skill assessment) despite differing accuracies"
id: predictive-certainty-ar-99-sa-95
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

# The predictive certainty of the trained networks was high (99% for action recognition, 95% for skill assessment) despite differing accuracies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Predictive certainty, computed as the highest class probability per prediction, was 99% for action recognition (max 100%, min 62%) and 95% for skill assessment (max 99.9%, min 57%). [→ Atroshchenko Gennady V. 2025](#atroshchenko-gennady-v-2025)

## Evidence

### Atroshchenko Gennady V. 2025

Atroshchenko Gennady V., Korup Lærke Riis, Hashemi Nasseh, Østergaard Lasse Riis, Tolsgaard Martin G., Rasmussen Sten. (2025). Artificial intelligence-based action recognition and skill assessment in robotic cardiac surgery simulation: a feasibility study. Journal of Robotic Surgery. https://doi.org/10.1007/s11701-025-02563-3

`q2 · i?` · `design · r2`

Test-set certainty analysis comparing predicted class probabilities against ground truth labels for both networks. The high SA certainty (95%) contrasts with its low 56% test accuracy, which the authors do not explicitly reconcile in the reported results.

> "The predictive certainty for AR was 99%, with a maximum of 100% and a minimum of 62%. For SA, the predictive certainty was 95%, with a maximum of 99.9% and a minimum of 57%."

## Discussion


## Related Claims
- [Deep learning models trained on JIGSAWS kinematic and video data achieve high accuracy in predicting surgeon skill level and mOSATS scores](deep-learning-high-accuracy-skill-prediction-jigsaws.md) — related
- [Fivefold cross-validation of the action recognition network yields a mean accuracy of 98%, while skill assessment cross-validation varies widely (mean 79%)](cross-validation-ar-98-sa-79-mean-accuracy.md) — related
