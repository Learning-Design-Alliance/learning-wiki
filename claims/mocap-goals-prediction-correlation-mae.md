---
type: claim
title: "The ML regression model's predicted GOALS scores correlate strongly with expert evaluations (r = 0.86 dissection, r = 0.91 suturing) with small mean absolute errors"
description: "The ML regression model's predicted GOALS scores correlate strongly with expert evaluations (r = 0.86 dissection, r = 0.91 suturing) with small mean absolute errors"
id: mocap-goals-prediction-correlation-mae
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

# The ML regression model's predicted GOALS scores correlate strongly with expert evaluations (r = 0.86 dissection, r = 0.91 suturing) with small mean absolute errors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Predicted GOALS scores from the motion-based regression model correlated with expert-evaluated mean GOALS scores at r = 0.86 (Dissection) and r = 0.91 (Suturing), with MAEs of 2.51 ± 1.82 and 1.56 ± 1.20. [→ Ebina Koki 2025](#ebina-koki-2025)

## Evidence

### Ebina Koki 2025

Ebina Koki, Abe Takashige, Hotta Kiyohiko, Lingbo Yan, Kamijo Chihiro, Higuchi Madoka, Kon Masafumi, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Murai Sachiyo, Senoo Taku, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Konno Atsushi, Shinohara Nobuo. (2025). External validation of a motion capture-based surgical skill assessment system in laparoscopic simulation training environments. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12018-3

`q3 · i?` · `design · r2`

External validation against two experts' blinded video-based GOALS ratings (inter-rater ICC 0.83 dissection, 0.81 suturing); all 107 datasets were used since repeat sessions do not affect regression verification. The study reports "0.86 and 2.51 ± 1.82" and "0.91 and 1.56 ± 1.20".

> "The correlation coefficient and MAE were 0.86 and 2.51 ± 1.82 (95% CI: 2.16–2.86) for Dissection Task and 0.91 and 1.56 ± 1.20 (95% CI: 1.40–1.92) for Suturing Task."

## Discussion


## Related Claims
- [A motion-capture ML three-tier classification model classifies laparoscopic experience with 67.3% accuracy on a dissection task and 56.9% on a suturing task in external validation](mocap-three-tier-classification-external-validation-accuracy.md) — related
- [Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)](llm-difficulty-magnitude-error-varies-across-models.md) — related
- [Self-assessment and expert evaluation scores correlate strongly on a suture exercise](sa-ee-strong-correlation-suture.md) — related
- [Kinematic indices computed from the developed system correlate strongly with those from the six-camera system, indicating comparable skill-evaluation capability](kinematic-indices-high-spearman-correlation.md) — related
