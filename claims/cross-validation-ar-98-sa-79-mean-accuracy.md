---
type: claim
title: "Fivefold cross-validation of the action recognition network yields a mean accuracy of 98%, while skill assessment cross-validation varies widely (mean 79%)"
description: "Fivefold cross-validation of the action recognition network yields a mean accuracy of 98%, while skill assessment cross-validation varies widely (mean 79%)"
id: cross-validation-ar-98-sa-79-mean-accuracy
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

# Fivefold cross-validation of the action recognition network yields a mean accuracy of 98%, while skill assessment cross-validation varies widely (mean 79%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` K-fold cross-validation on the combined training and validation sets yielded a mean accuracy of 98.5 (± 1.5) for action recognition and 78.9 (± 16.8) for skill assessment. [→ Atroshchenko Gennady V. 2025](#atroshchenko-gennady-v-2025)

## Evidence

### Atroshchenko Gennady V. 2025

Atroshchenko Gennady V., Korup Lærke Riis, Hashemi Nasseh, Østergaard Lasse Riis, Tolsgaard Martin G., Rasmussen Sten. (2025). Artificial intelligence-based action recognition and skill assessment in robotic cardiac surgery simulation: a feasibility study. Journal of Robotic Surgery. https://doi.org/10.1007/s11701-025-02563-3

`q2 · i?` · `design · r2`

Fivefold cross-validation results reported in the Results section; Table 1 prints fold accuracies with mean accuracy (± SD) of 98.5 (± 1.5) for action recognition and 78.9 (± 16.8) for skill assessment. This cross-validation "provides a more generalized estimate of how the model would perform on unseen data".

> "Results from K-fold cross-validation are presented in Table 1, yielding a mean accuracy of 98% for action recognition and 79% for SA."

## Discussion


## Related Claims
- [A CNN-LSTM deep learning network classifies suturing versus dissection actions from robotic cardiac surgery simulation video with 93% test accuracy](dl-action-recognition-93-percent-robotic-cardiac-wetlab.md) — related
- [High‐skill recognition is better for knot tying, whereas low‐skill recognition is better for the more demanding tasks (CS and IS)](task-dependent-skill-recognition-asymmetry.md) — related
- [The predictive certainty of the trained networks was high (99% for action recognition, 95% for skill assessment) despite differing accuracies](predictive-certainty-ar-99-sa-95.md) — related
