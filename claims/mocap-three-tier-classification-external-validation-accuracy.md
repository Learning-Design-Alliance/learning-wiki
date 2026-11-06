---
type: claim
title: "A motion-capture ML three-tier classification model classifies laparoscopic experience with 67.3% accuracy on a dissection task and 56.9% on a suturing task in external validation"
description: "A motion-capture ML three-tier classification model classifies laparoscopic experience with 67.3% accuracy on a dissection task and 56.9% on a suturing task in external validation"
id: mocap-three-tier-classification-external-validation-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: ebina-koki-2025
    resource: "https://doi.org/10.1007/s00464-025-12018-3"
    title: "Ebina Koki, Abe Takashige, Hotta Kiyohiko, Lingbo Yan, Kamijo Chihiro, Higuchi Madoka, Kon Masafumi, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Murai Sachiyo, Senoo Taku, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Konno Atsushi, Shinohara Nobuo. (2025). External validation of a motion capture-based surgical skill assessment system in laparoscopic simulation training environments. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12018-3"
    author: Ebina Koki, Abe Takashige, Hotta Kiyohiko, Lingbo Yan, Kamijo Chihiro, Higuchi Madoka, Kon Masafumi, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Murai Sachiyo, Senoo Taku, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Konno Atsushi, Shinohara Nobuo
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# A motion-capture ML three-tier classification model classifies laparoscopic experience with 67.3% accuracy on a dissection task and 56.9% on a suturing task in external validation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` In external validation with new participants, the three-tier classification model achieved overall accuracy of 67.3% for Dissection Task and 56.9% for Suturing Task. [→ Ebina Koki 2025](#ebina-koki-2025)

## Evidence

### Ebina Koki 2025

Ebina Koki, Abe Takashige, Hotta Kiyohiko, Lingbo Yan, Kamijo Chihiro, Higuchi Madoka, Kon Masafumi, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Murai Sachiyo, Senoo Taku, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Konno Atsushi, Shinohara Nobuo. (2025). External validation of a motion capture-based surgical skill assessment system in laparoscopic simulation training environments. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12018-3

`q3 · i?` · `design · r2`

External validation study: 107 datasets from 52 participants (urologists, junior residents, medical students) performing porcine-organ wet-lab tasks, with models trained only on prior data (n = 104). The study reports "67.3% (95% CI: 61.3–73.3%)" for Dissection Task and 56.9% for Suturing Task.

> "The overall classification accuracy (micro average of accuracy) after excluding the subsequent data of repeaters was 67.3% (95% CI: 61.3–73.3%) for Dissection Task and 56.9% (95% CI: 50.1–63.7%) for Suturing Task."

## Discussion


## Related Claims
- [Three-tier classification frequently misclassifies intermediate surgeons, suggesting procedural caseload is a limited surrogate for skill in simulation training](intermediate-tier-misclassification-caseload-limitation.md) — related
- [The ML regression model's predicted GOALS scores correlate strongly with expert evaluations (r = 0.86 dissection, r = 0.91 suturing) with small mean absolute errors](mocap-goals-prediction-correlation-mae.md) — related
- [Kinematic assessment systems for laparoscopic cholecystectomy are weakly validated, restricted to small datasets, and capture only a narrow component of operative competence](kinematic-lc-tools-limited-validation-narrow-construct.md) — a broader claim this one bears on
