---
type: claim
title: "The skill assessment network distinguishing novice from expert surgeons reached only 56% test accuracy, failing to achieve useful performance"
description: "The skill assessment network distinguishing novice from expert surgeons reached only 56% test accuracy, failing to achieve useful performance"
id: skill-assessment-network-56-percent-accuracy-failed
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

# The skill assessment network distinguishing novice from expert surgeons reached only 56% test accuracy, failing to achieve useful performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The skill assessment deep learning network did not achieve desired characteristics, with 56% test accuracy; expert recall was 0.10 while novice recall was 1.00 in the test set. [→ Atroshchenko Gennady V. 2025](#atroshchenko-gennady-v-2025)

## Evidence

### Atroshchenko Gennady V. 2025

Atroshchenko Gennady V., Korup Lærke Riis, Hashemi Nasseh, Østergaard Lasse Riis, Tolsgaard Martin G., Rasmussen Sten. (2025). Artificial intelligence-based action recognition and skill assessment in robotic cardiac surgery simulation: a feasibility study. Journal of Robotic Surgery. https://doi.org/10.1007/s11701-025-02563-3

`q2 · i?` · `design · r2`

Test-set evaluation of the skill assessment network on first-attempt mitral stitches and atrial closure recordings labeled novice or expert. Table 2 shows Expert recall 0.1, precision 1.00, F1 0.19; Novice recall 1.00, precision 0.53, F1 0.69. The discussion states it "did not achieve the desired characteristics".

> "The action recognition model achieved an accuracy of 93%, while the skill assessment deep learning network had an accuracy of 56%."

## Discussion


## Related Claims
- [A CNN-LSTM deep learning network classifies suturing versus dissection actions from robotic cardiac surgery simulation video with 93% test accuracy](dl-action-recognition-93-percent-robotic-cardiac-wetlab.md) — related
- [Deep learning models trained on JIGSAWS kinematic and video data achieve high accuracy in predicting surgeon skill level and mOSATS scores](deep-learning-high-accuracy-skill-prediction-jigsaws.md) — reports the opposite
- [In the narrative synthesis, deep learning models classify surgeon skill levels from kinematic data with accuracy up to 95.4%](deep-learning-skill-classification-up-to-95-percent.md) — reports the opposite
- [A Leap Motion Controller-based system discriminated expert from novice surgical knot-tying performance with 100% accuracy, supporting construct validity for objective dexterity assessment](lmc-construct-validity-dexterity-assessment.md) — related
