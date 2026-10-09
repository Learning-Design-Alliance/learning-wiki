---
type: claim
title: Regression analysis shows the MTCS method significantly degrades dilation-parameter precision relative to the Ratio of Eigenvalues method, while simulation factors explain most RMSE variation
description: Regression analysis shows the MTCS method significantly degrades dilation-parameter precision relative to the Ratio of Eigenvalues method, while simulation factors explain most RMSE variation
id: regression-mtcs-significant-k-precision
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
evidence_strength: weak
sources:
  - id: li-1998
    resource: "https://eric.ed.gov/?id=ED418999"
    title: "Li, Yuan H.; Lissitz, Robert W. (1998). An Evaluation of Multidimensional IRT Equating Methods by Assessing the Accuracy of Transforming Parameters onto a Target Test Metric. Paper presented at the annual meeting of the National Council on Measurement in Education. https://eric.ed.gov/?id=ED418999"
    author: Li, Yuan H.; Lissitz, Robert W.
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: li-1998-2
    resource: "https://eric.ed.gov/?id=ED418999"
    title: "Li, Yuan H.; Lissitz, Robert W. (1998). An Evaluation of Multidimensional IRT Equating Methods by Assessing the Accuracy of Transforming Parameters onto a Target Test Metric. Paper presented at the annual meeting of the National Council on Measurement in Education. https://eric.ed.gov/?id=ED418999"
    author: Li, Yuan H.; Lissitz, Robert W.
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# Regression analysis shows the MTCS method significantly degrades dilation-parameter precision relative to the Ratio of Eigenvalues method, while simulation factors explain most RMSE variation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q1`

## Subclaims
`q1 i?` In the regression predicting Log[RMSE] of the k estimate, the standardized coefficient for MTCS versus Ratio of Eigenvalues was 0.652 (significant), while Ratio of Trace versus Ratio of Eigenvalues was 0.067 (not significant); adjusted R2 ranged from 0.86 to 0.90. [→ Li 1998](#li-1998)

## Evidence

### Li 1998

Li, Yuan H.; Lissitz, Robert W. (1998). An Evaluation of Multidimensional IRT Equating Methods by Assessing the Accuracy of Transforming Parameters onto a Target Test Metric. Paper presented at the annual meeting of the National Council on Measurement in Education. https://eric.ed.gov/?id=ED418999

`q1 · i?` · `design · r2`

Inferential regression analysis of the first simulation study predicting Log[RMSE] of transformation-parameter estimates from method, sample size, test length, linking, and study situation dummies. The authors report the MTCS dummy coefficient of 0.652 significant and the Ratio of Trace dummy of 0.067 not significant; no effect size is printed.

> "The DM2's standardized regression coefficient was 0.652 which was statistically significant from zero. In contrast, the DMZ's standardized regression coefficient (Ratio of Trace versus Ratio of Eigenvalue) was 0.067 which was not statistically significant from zero."

### Li 1998 (2)

Li, Yuan H.; Lissitz, Robert W. (1998). An Evaluation of Multidimensional IRT Equating Methods by Assessing the Accuracy of Transforming Parameters onto a Target Test Metric. Paper presented at the annual meeting of the National Council on Measurement in Education. https://eric.ed.gov/?id=ED418999

`q1 · i?` · `causal · r2`

Same regression models as the primary analysis; the authors interpret the adjusted R2 range of 0.86 to 0.90 as showing the simulation factors account heavily for variation in each transformation-parameter estimate's RMSE.

> "The results of adjusted Rs for each of the Log[RMSE] models, ranging from 0.86 to 0.90, reported on the right side of Table 2, suggest that this set of simulation factors was very sensitive to variations in each of the transformation-parameter estimates."

## Discussion


## Related Claims
- [Least Squares procedures consistently outperform the MTCS method for estimating MIRT translation parameters m1 and m2](least-squares-beats-mtcs-translation-estimates.md) — related
- [The developed MIRT equating methods behave as unbiased, effective, and consistent estimators of transformation parameters](mirt-equating-methods-unbiased-effective-consistent.md) — related
- [The Ratio of Trace method consistently yields the most precise estimates of the MIRT dilation parameter k across all simulated equating situations](ratio-of-trace-best-dilation-estimate-mirt-equating.md) — related
- [Linear regression outperformed equipercentile and mean-sigma equating for predicting ARM scores and was selected as the final linking model](linear-regression-selected-linking-model.md) — related
- [Both proposed adjustment methods (IEA and BA) reduce RMSE of item difficulty estimates from direct 2PL-IRT fitting, with BA yielding more consistent (lower-variance) estimates in simulation](iea-ba-reduce-difficulty-estimate-bias.md) — related
