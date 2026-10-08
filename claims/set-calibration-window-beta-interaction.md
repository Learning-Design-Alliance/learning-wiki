---
type: claim
title: SET calibration shows a window-size by beta interaction, with the lowest Brier score for window size 30, cause weights, and beta = .6
description: SET calibration shows a window-size by beta interaction, with the lowest Brier score for window size 30, cause weights, and beta = .6
id: set-calibration-window-beta-interaction
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

# SET calibration shows a window-size by beta interaction, with the lowest Brier score for window size 30, cause weights, and beta = .6

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Smaller window sizes require larger beta values for calibration (a window-size by beta interaction). [→ Savi 2021](#savi-2021)
`q2 i?` The overall lowest Brier score is obtained with window size 30, cause weights, and beta = .6. [→ Savi 2021](#savi-2021)

## Evidence

### Savi 2021

Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J. (2021). Tracing Systematic Errors to Personalize Recommendations in Single Digit Multiplication and Beyond. Journal of Educational Data Mining, Volume 13, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382

`q2 · i?` · `design · r2`

Training-data calibration evaluation via Brier scores across beta values (0 to 1.5 by .1), window sizes, and edge-weight configurations, shown in Figure 10 with 278 students. The article reports the interaction that "smaller window sizes require larger β values" and the best configuration at window 30, cause weights, beta = .6.

> "From the figure, a clear interaction between window size andβ emerges: smaller window sizes require larger β values. Again, a window size of 30 errors provides the lowest Brier score, regardless of the edge weight transformation. The overall lowest Brier score is obtained in the model with window size 30, cause weights, andβ =.6."

## Discussion


## Related Claims
- [In single-digit multiplication, most items are susceptible to nearly all considered error causes, which precludes the use of cognitive diagnostic models for this data](item-cause-density-precludes-cdms.md) — related
- [Larger error windows improve SET ranking performance, with a window of 30 errors yielding the highest MAP regardless of edge-weight transformation](larger-error-windows-improve-set-ranking.md) — related
