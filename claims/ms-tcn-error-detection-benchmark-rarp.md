---
type: claim
title: MS-TCN/MS-TCN++ achieve the best error-detection performance among five vision models, but models overlook errors of short duration
description: MS-TCN/MS-TCN++ achieve the best error-detection performance among five vision models, but models overlook errors of short duration
id: ms-tcn-error-detection-benchmark-rarp
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: sirajudeen-n-2024
    resource: "https://doi.org/10.1007/s00464-024-11341-5"
    title: "Sirajudeen N., Boal M., Anastasiou D., Xu J., Stoyanov D., Kelly J., Collins J. W., Sridhar A., Mazomenos E., Francis N. K. (2024). Deep learning prediction of error and skill in robotic prostatectomy suturing. Surgical Endoscopy 38(12). https://doi.org/10.1007/s00464-024-11341-5"
    author: Sirajudeen N., Boal M., Anastasiou D., Xu J., Stoyanov D., Kelly J., Collins J. W., Sridhar A., Mazomenos E., Francis N. K.
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: sirajudeen-n-2024-2
    resource: "https://doi.org/10.1007/s00464-024-11341-5"
    title: "Sirajudeen N., Boal M., Anastasiou D., Xu J., Stoyanov D., Kelly J., Collins J. W., Sridhar A., Mazomenos E., Francis N. K. (2024). Deep learning prediction of error and skill in robotic prostatectomy suturing. Surgical Endoscopy 38(12). https://doi.org/10.1007/s00464-024-11341-5"
    author: Sirajudeen N., Boal M., Anastasiou D., Xu J., Stoyanov D., Kelly J., Collins J. W., Sridhar A., Mazomenos E., Francis N. K.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# MS-TCN/MS-TCN++ achieve the best error-detection performance among five vision models, but models overlook errors of short duration

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` MS-TCN++ achieved the highest AUC (65.10%) and Macro-F1 (58.97%) while MS-TCN achieved the highest mAP (37.14%) among the five models tested. [→ Sirajudeen N. 2024](#sirajudeen-n-2024)
`q2 i?` Both top models detected long-duration errors well but tended to overlook short errors. [→ Sirajudeen N. 2024 (2)](#sirajudeen-n-2024-2)

## Evidence

### Sirajudeen N. 2024

Sirajudeen N., Boal M., Anastasiou D., Xu J., Stoyanov D., Kelly J., Collins J. W., Sridhar A., Mazomenos E., Francis N. K. (2024). Deep learning prediction of error and skill in robotic prostatectomy suturing. Surgical Endoscopy 38(12). https://doi.org/10.1007/s00464-024-11341-5

`q2 · i?` · `design · r2`

Benchmark comparison of ResNet-50, TeCNO, MS-TCN, MS-TCN++ and Asformer classifying video frames as normal or error on the SAR-RARP50 test set. The article reports "the highest AUC and Macro-F1 with scores of 65.10% and 58.97%" for MS-TCN++.

> "Error estimation (Table 3) illustrates that MS-TCN++ achieved the highest AUC and Macro-F1 with scores of 65.10% and 58.97%, respectively. Its variant, MS-TCN, demonstrated the highest mAP score of 37.14%."

### Sirajudeen N. 2024 (2)

Sirajudeen N., Boal M., Anastasiou D., Xu J., Stoyanov D., Kelly J., Collins J. W., Sridhar A., Mazomenos E., Francis N. K. (2024). Deep learning prediction of error and skill in robotic prostatectomy suturing. Surgical Endoscopy 38(12). https://doi.org/10.1007/s00464-024-11341-5

`q2 · i?` · `design · r2`

Qualitative inspection of the error-detection outputs of the top two models, MS-TCN++ and MS-TCN, presented in Figs. 1–3. The article reports the models "tended to overlook short errors" while detecting long-duration errors well.

> "Both models showcased superior performance in detecting errors with long durations, albeit they tended to overlook short errors"

## Discussion


## Related Claims
-
