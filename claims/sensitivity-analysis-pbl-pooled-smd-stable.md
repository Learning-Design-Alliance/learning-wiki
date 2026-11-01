---
type: claim
title: Removing 5 heterogeneous studies leaves the PBL advantage intact (SMD 0.79) with reduced heterogeneity, and the Liu et al study most affects stability
description: Removing 5 heterogeneous studies leaves the PBL advantage intact (SMD 0.79) with reduced heterogeneity, and the Liu et al study most affects stability
id: sensitivity-analysis-pbl-pooled-smd-stable
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-31
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: xu-wei-2021
    resource: "https://doi.org/10.1097/MD.0000000000027402"
    title: "Xu Wei, Ye Tingjie, Wang Xiaoling, Hayashi. Shogo. (2021). The effectiveness of the problem-based learning in medical cell biology education: A systematic meta-analysis. Medicine. https://doi.org/10.1097/MD.0000000000027402"
    author: Xu Wei, Ye Tingjie, Wang Xiaoling, Hayashi. Shogo
    q: 3
    i: 3
    kind: quant-synthesis
    rigour: 1
  - id: xu-wei-2021-2
    resource: "https://doi.org/10.1097/MD.0000000000027402"
    title: "Xu Wei, Ye Tingjie, Wang Xiaoling, Hayashi. Shogo. (2021). The effectiveness of the problem-based learning in medical cell biology education: A systematic meta-analysis. Medicine. https://doi.org/10.1097/MD.0000000000027402"
    author: Xu Wei, Ye Tingjie, Wang Xiaoling, Hayashi. Shogo
    q: 3
    i: "?"
    kind: quant-synthesis
    rigour: 2
---

# Removing 5 heterogeneous studies leaves the PBL advantage intact (SMD 0.79) with reduced heterogeneity, and the Liu et al study most affects stability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · quant-synthesis `r1`–`r2` · `q3` · `i3` large
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i3` After removing the 5 studies identified as heterogeneity sources, the pooled SMD was 0.79 (0.46, 1.11) with reduced heterogeneity (I2 = 61.5%, P = .05), confirming the conclusion was unaffected. [→ Xu Wei 2021](#xu-wei-2021)
`q3 i?` Leave-one-out sensitivity analysis showed pooled SMDs were unstable after the Liu et al study was removed, while other studies did not significantly affect stability. [→ Xu Wei 2021 (2)](#xu-wei-2021-2)

## Evidence

### Xu Wei 2021

Xu Wei, Ye Tingjie, Wang Xiaoling, Hayashi. Shogo. (2021). The effectiveness of the problem-based learning in medical cell biology education: A systematic meta-analysis. Medicine. https://doi.org/10.1097/MD.0000000000027402

`q3 · i3` · `quant-synthesis · r1`

Re-pooling after excluding the 5 studies named as heterogeneity sources (Liu, Yu, Lan, Tang, Wang et al) yielded the printed effect size SMD = 0.79 (95% CI 0.46, 1.11) with I2 = 61.5%, P = .05; the authors conclude removal "did not affect the conclusion".

> "When these 5 studies were removed and the remaining studies were combined to pool the SMD, the pooled SMD was calculated to be 0.79 (0.46, 1.11) (Fig. 5). The result proved that these 5 studies removing did not affect the conclusion. However, there was no heterogeneity (I2 = 61.5%, P = .05) among the remaining 4 studies after removing."

### Xu Wei 2021 (2)

Xu Wei, Ye Tingjie, Wang Xiaoling, Hayashi. Shogo. (2021). The effectiveness of the problem-based learning in medical cell biology education: A systematic meta-analysis. Medicine. https://doi.org/10.1097/MD.0000000000027402

`q3 · i?` · `quant-synthesis · r2`

Leave-one-out sensitivity analysis sequentially removing each study; only the Liu et al study significantly affected the stability of the pooled results, per the article's own reading of Figure 6.

> "As shown in Figure 6, pooled SMDs was unstable after Liu et al study was removed, which suggested that the Liu et al study affects the stability of pooled results significantly. However, the other studies did not affect the stability of pooled result significantly."

## Discussion


## Related Claims
- [After removing four studies identified as heterogeneity sources via Galbraith plot, the pooled CBL effect remains significant (g = 0.65)](cbl-effect-robust-after-galbraith-removal.md) — related
- [After removing five outlying studies identified by Galbraith plot, the PBL advantage persisted with low heterogeneity (Hedges' g = 0.592, I2 = 26.807%)](pbl-advantage-persists-after-galbraith-removal.md) — related
- [No single study affected the statistically significant PBL advantage in sensitivity analysis](pbl-advantage-robust-to-single-study-removal.md) — related
- [Pooled PBL-CBL versus LBL estimates show high heterogeneity and publication bias but remain robust in sensitivity and trim-and-fill analyses](pbl-cbl-meta-heterogeneity-publication-bias.md) — related
- [PBL's examination-score advantage holds across student majors, publication years, and class sizes, but heterogeneity remains high in all subgroups](pbl-exam-subgroup-analyses-heterogeneity.md) — related
