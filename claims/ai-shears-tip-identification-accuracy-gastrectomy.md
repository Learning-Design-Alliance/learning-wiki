---
type: claim
title: An AI semantic segmentation algorithm identifies the HARMONIC shears active blade and tip from laparoscopic video with high accuracy (blade TPR 0.873, Dice 0.837; tip TPR 0.813, Dice 0.846)
description: An AI semantic segmentation algorithm identifies the HARMONIC shears active blade and tip from laparoscopic video with high accuracy (blade TPR 0.873, Dice 0.837; tip TPR 0.813, Dice 0.846)
id: ai-shears-tip-identification-accuracy-gastrectomy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: matsumoto-shiro-2024
    resource: "https://doi.org/10.1038/s41598-024-63388-y"
    title: "Matsumoto Shiro, Kawahira Hiroshi, Fukata Kyohei, Doi Yasunori, Kobayashi Nao, Hosoya Yoshinori, Sata Naohiro. (2024). Laparoscopic distal gastrectomy skill evaluation from video: a new artificial intelligence-based instrument identification system. Scientific Reports. https://doi.org/10.1038/s41598-024-63388-y"
    author: Matsumoto Shiro, Kawahira Hiroshi, Fukata Kyohei, Doi Yasunori, Kobayashi Nao, Hosoya Yoshinori, Sata Naohiro
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# An AI semantic segmentation algorithm identifies the HARMONIC shears active blade and tip from laparoscopic video with high accuracy (blade TPR 0.873, Dice 0.837; tip TPR 0.813, Dice 0.846)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A DeepLab v2-based AI algorithm achieved TPR 0.873, FPR 0.0041, and Dice 0.837 for the active blade, and TPR 0.813, FPR 0.111, Dice 0.846 for the blade tip on an 180-image evaluation set. [→ Matsumoto Shiro 2024](#matsumoto-shiro-2024)

## Evidence

### Matsumoto Shiro 2024

Matsumoto Shiro, Kawahira Hiroshi, Fukata Kyohei, Doi Yasunori, Kobayashi Nao, Hosoya Yoshinori, Sata Naohiro. (2024). Laparoscopic distal gastrectomy skill evaluation from video: a new artificial intelligence-based instrument identification system. Scientific Reports. https://doi.org/10.1038/s41598-024-63388-y

`q2 · i?` · `design · r2`

Accuracy evaluation on a test dataset of 180 still images extracted from the 18 videos, of which 114 showed the active blade and 90 showed the tip clearly. The authors note that "the accuracy of our study in identifying the approximately 1 mm-long HARMONIC tip was highly satisfactory."

> "In the active blade evaluation from 114 images, the TPR was 0.873, the FPR was 0.0041, and the Dice was 0.837. The Active blade tip was evaluated using 90 images, and when inferred within the ground truth tip area, was judged as True. The TPR was 0.813, the FPR was 0.111 and the Dice was 0.846."

## Discussion


## Related Claims
- [The algorithm's U-net segmentation achieves 98% precision for locating grasper clamps in video frames](unet-segmentation-98-percent-clamp-precision.md) — related
- [Expert surgeons' instrument tip total travel distance was significantly shorter than novices' (343,794 vs 575,721 pixels)](experts-shorter-total-travel-distance.md) — related
- [Expert and novice surgeons showed no significant differences in tip velocity, acceleration, or jerk in clinical laparoscopic surgery](no-velocity-acceleration-jerk-difference-clinical.md) — related
- [An AI algorithm shows almost perfect agreement with expert evaluators in pass/fail assessment of peg transfer laparoscopic simulation videos](ai-almost-perfect-agreement-peg-transfer-assessment.md) — related
