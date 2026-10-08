---
type: claim
title: "SET adapts its predicted ranking to individual students' errors for the typo and reverse causes but not for all causes"
description: "SET adapts its predicted ranking to individual students' errors for the typo and reverse causes but not for all causes"
id: set-cause-level-ranking-typo-reverse
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: weak
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

# SET adapts its predicted ranking to individual students' errors for the typo and reverse causes but not for all causes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The typo and reverse causes show substantially lower average predicted ranks under SET than under the baseline. [→ Savi 2021](#savi-2021)
`q2 i?` For operator relevant, different unit, and miss 10, SET's confidence intervals overlap the baseline, and miss 10 is poorly ranked by both models. [→ Savi 2021](#savi-2021)

## Evidence

### Savi 2021

Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J. (2021). Tracing Systematic Errors to Personalize Recommendations in Single Digit Multiplication and Beyond. Journal of Educational Data Mining, Volume 13, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382

`q2 · i?` · `design · r2`

Holdout-data cause-profile analysis (Figure 12) comparing average predicted ranks per cause for SET versus the majority-vote baseline. The article reports SET performs "substantially better than the baseline" for typo and reverse, while operator relevant, different unit, and miss 10 confidence intervals overlap the baseline.

> "The two remaining causes, the typo and reverse, do seem to perform substantially better than the baseline. The SET model thus seems to succeed in adapting its predicted ranking to students’ error responses for thetypo and reverse causes but fails to do so for others."

## Discussion


## Related Claims
- [In single-digit multiplication, most items are susceptible to nearly all considered error causes, which precludes the use of cognitive diagnostic models for this data](item-cause-density-precludes-cdms.md) — related
- [Larger error windows improve SET ranking performance, with a window of 30 errors yielding the highest MAP regardless of edge-weight transformation](larger-error-windows-improve-set-ranking.md) — related
