---
type: claim
title: When item difficulty and simulee ability ranges align (minimum -10, maximum 8), Pychometrik recovery is accurate, with correlations above 0.99 across all three sample sizes; recovery degrades above the simulee ability maximum of 7.94
description: When item difficulty and simulee ability ranges align (minimum -10, maximum 8), Pychometrik recovery is accurate, with correlations above 0.99 across all three sample sizes; recovery degrades above the simulee ability...
id: pychometrik-accurate-recovery-when-ranges-align
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: he-2021
    resource: "https://www.nwea.org/research/publication/a-comparison-of-item-parameter-estimates-in-pychometrik-and-the-existing-item-calibration-tool/"
    title: "He, W., Bo, E., Meyer, P., & Grandgeorge, R. (2021). A comparison of item parameter estimates in Pychometrik and the existing item calibration tool. NWEA. https://www.nwea.org/research/publication/a-comparison-of-item-parameter-estimates-in-pychometrik-and-the-existing-item-calibration-tool/"
    author: "He, W., Bo, E., Meyer, P., & Grandgeorge, R."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: he-2021-2
    resource: "https://www.nwea.org/research/publication/a-comparison-of-item-parameter-estimates-in-pychometrik-and-the-existing-item-calibration-tool/"
    title: "He, W., Bo, E., Meyer, P., & Grandgeorge, R. (2021). A comparison of item parameter estimates in Pychometrik and the existing item calibration tool. NWEA. https://www.nwea.org/research/publication/a-comparison-of-item-parameter-estimates-in-pychometrik-and-the-existing-item-calibration-tool/"
    author: "He, W., Bo, E., Meyer, P., & Grandgeorge, R."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# When item difficulty and simulee ability ranges align (minimum -10, maximum 8), Pychometrik recovery is accurate, with correlations above 0.99 across all three sample sizes; recovery degrades above the simulee ability maximum of 7.94

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` With aligned ranges, MAD and RMSE were small (e.g., MAD 0.27 and RMSE 0.47 at n = 2,000) and correlations were 0.99 or 1.00. [→ He 2021](#he-2021)
`q2 i?` Because no simulees had ability above 7.94, RMSE and MAD were high and correlations low for item difficulty bins above that point. [→ He 2021 (2)](#he-2021-2)

## Evidence

### He 2021

He, W., Bo, E., Meyer, P., & Grandgeorge, R. (2021). A comparison of item parameter estimates in Pychometrik and the existing item calibration tool. NWEA. https://www.nwea.org/research/publication/a-comparison-of-item-parameter-estimates-in-pychometrik-and-the-existing-item-calibration-tool/

`q2 · i?` · `design · r2`

Summary (Table 3.10) of the recovery simulation restricted to item difficulties between -10 and 8: MAD 0.45/0.34/0.27, RMSE 0.75/0.59/0.47, and correlations 0.99/0.99/1.00 for sample sizes 500/1,000/2,000.

> "Both MAD and RMSE are small across all three sample sizes, and the correlations are all above 0.99. These results indicate that Pychometrik is working properly."

### He 2021 (2)

He, W., Bo, E., Meyer, P., & Grandgeorge, R. (2021). A comparison of item parameter estimates in Pychometrik and the existing item calibration tool. NWEA. https://www.nwea.org/research/publication/a-comparison-of-item-parameter-estimates-in-pychometrik-and-the-existing-item-calibration-tool/

`q2 · i?` · `design · r2`

Bin-level results (Figures 3.5-3.7, sample size 2,000) show recovery degrades for item difficulties beyond the simulee ability maximum; Grade 8 simulees gave the best results because their distribution resembles the item distribution.

> "As recalled in the Wright map above, there are no simulees with an ability above 7.94. Thus, the results show high RMSE, MAD and low correlations above that point on the right end of the x-axis in all three figures."

## Discussion


## Related Claims
- [In the Pychometrik item parameter recovery simulation across 27 conditions (Grades K-8, sample sizes 500, 1,000, and 2,000), recovery accuracy increased with sample size and was best for Grade 8 simulees](pychometrik-recovery-sample-size-and-grade-effects.md) — related
- [In a fixed-person calibration simulation with 60 Rasch items and 1,200 simulees, estimates from both tools were comparable to true parameters, with the existing tool underestimating difficulty by 0.03 RIT on average](simulation-comparability-60-items-1200-simulees.md) — related
- [Item calibration results from Pychometrik and the existing tool are mostly comparable across 1,180 AGC-calibrated MAP Growth items, with average RIT differences ranging from 0.33 (mathematics) to 0.91 (science)](pychometrik-existing-tool-comparable-calibration-real-data.md) — related
