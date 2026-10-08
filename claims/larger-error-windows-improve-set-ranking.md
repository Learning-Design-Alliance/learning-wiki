---
type: claim
title: Larger error windows improve SET ranking performance, with a window of 30 errors yielding the highest MAP regardless of edge-weight transformation
description: Larger error windows improve SET ranking performance, with a window of 30 errors yielding the highest MAP regardless of edge-weight transformation
id: larger-error-windows-improve-set-ranking
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: savi-2021
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382"
    title: "Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J. (2021). Tracing Systematic Errors to Personalize Recommendations in Single Digit Multiplication and Beyond. Journal of Educational Data Mining, Volume 13, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382"
    author: "Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Larger error windows improve SET ranking performance, with a window of 30 errors yielding the highest MAP regardless of edge-weight transformation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` MAP is higher for larger window sizes, and a window size of 30 errors provides the highest MAP across all k and edge-weight transformations. [→ Savi 2021](#savi-2021)

## Evidence

### Savi 2021

Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J. (2021). Tracing Systematic Errors to Personalize Recommendations in Single Digit Multiplication and Beyond. Journal of Educational Data Mining, Volume 13, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382

`q2 · i?` · `design · r2`

Training-data evaluation of SET model configurations (278 students, average 51.6 to 80.6 predictions per student) across window sizes 1, 3, 7, 15, and 30 and four edge-weight schemes, shown as MAP@k heatmaps in Figure 9. The article reports the pattern that "the MAP is higher for larger window sizes" with window 30 best.

> "From the figure, a clear pattern emerges where the MAP is higher for larger window sizes. A window size of 30 errors provides the highest MAP, regardless of the edge weight transformation and across all k."

## Discussion


## Related Claims
- [SET calibration shows a window-size by beta interaction, with the lowest Brier score for window size 30, cause weights, and beta = .6](set-calibration-window-beta-interaction.md) — related
- [SET adapts its predicted ranking to individual students' errors for the typo and reverse causes but not for all causes](set-cause-level-ranking-typo-reverse.md) — related
