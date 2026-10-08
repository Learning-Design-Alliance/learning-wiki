---
type: claim
title: In single-digit multiplication, most items are susceptible to nearly all considered error causes, which precludes the use of cognitive diagnostic models for this data
description: In single-digit multiplication, most items are susceptible to nearly all considered error causes, which precludes the use of cognitive diagnostic models for this data
id: item-cause-density-precludes-cdms
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
  - id: savi-2021-2
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382"
    title: "Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J. (2021). Tracing Systematic Errors to Personalize Recommendations in Single Digit Multiplication and Beyond. Journal of Educational Data Mining, Volume 13, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382"
    author: "Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# In single-digit multiplication, most items are susceptible to nearly all considered error causes, which precludes the use of cognitive diagnostic models for this data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`–`q2`

## Subclaims
`q2 i?` 50 items are susceptible to all 14 considered causes, 21 items to 13 causes, and 10 items to 12 causes. [→ Savi 2021](#savi-2021)
`q2 i?` When causes are tagged to all items, CDM identifiability conditions are not met, so parameter estimation would be suspect. [→ Savi 2021 (2)](#savi-2021-2)

## Evidence

### Savi 2021

Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J. (2021). Tracing Systematic Errors to Personalize Recommendations in Single Digit Multiplication and Beyond. Journal of Educational Data Mining, Volume 13, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382

`q2 · i?` · `design · r2`

Histogram analysis of the number of applicable error categories per single-digit multiplication item (Figure 3). The article reports that "50 items are susceptible to all 14 considered causes," 21 to 13, and 10 to 12, illustrating the dense item-cause association.

> "It shows that all considered error categories can apply to the largest fraction of items: 50 items are susceptible to all 14 considered causes, 21 items are susceptible to 13 of the considered causes, and 10 items are susceptible to 12 of the considered causes."

### Savi 2021 (2)

Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J. (2021). Tracing Systematic Errors to Personalize Recommendations in Single Digit Multiplication and Beyond. Journal of Educational Data Mining, Volume 13, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382

`q1 · i?` · `design · r2`

Analytical argument in the related-work section, citing Gu and Xu (2018) on CDM identifiability. The article concludes that CDM parameter estimation "would be suspect and lead to spurious results" in this setting, motivating errors rather than items as the unit of analysis.

> "The necessary and suﬃcient conditions for identiﬁability of parameters in CDMs have recently been derived (Gu and Xu, 2018), and when there exist causes that are tagged to all items these identiﬁability conditions are not met."

## Discussion


## Related Claims
- [SET adapts its predicted ranking to individual students' errors for the typo and reverse causes but not for all causes](set-cause-level-ranking-typo-reverse.md) — related
- [SET calibration shows a window-size by beta interaction, with the lowest Brier score for window size 30, cause weights, and beta = .6](set-calibration-window-beta-interaction.md) — related
