---
type: claim
title: "As the number of factors increases, TAME's power decreases less than ANOVA's, with a significant method-by-factors interaction"
description: "As the number of factors increases, TAME's power decreases less than ANOVA's, with a significant method-by-factors interaction"
id: tame-power-degrades-less-with-more-factors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: moderate
newest_evidence: 2016
sources:
  - id: thanaporn-patikorn-2016
    resource: "https://sites.google.com/site/tamemethod/"
    title: "Thanaporn Patikorn, Douglas Selent, Neil T. Heffernan, Joseph E. Beck, Jian Zou. (2016). Using a Single Model Trained across Multiple Experiments to Improve the Detection of Treatment Effects. Proceedings of the 10th International Conference on Educational Data Mining. https://sites.google.com/site/tamemethod/"
    author: Thanaporn Patikorn, Douglas Selent, Neil T. Heffernan, Joseph E. Beck, Jian Zou
    q: 2
    i: 2
    kind: design
    rigour: 2
---

# As the number of factors increases, TAME's power decreases less than ANOVA's, with a significant method-by-factors interaction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i2` medium
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i2` The method-by-factors interaction on statistical power is statistically significant (partial eta squared of 0.042), with TAME losing less power than ANOVA as factors increase. [→ Thanaporn Patikorn 2016](#thanaporn-patikorn-2016)

## Evidence

### Thanaporn Patikorn 2016

Thanaporn Patikorn, Douglas Selent, Neil T. Heffernan, Joseph E. Beck, Jian Zou. (2016). Using a Single Model Trained across Multiple Experiments to Improve the Detection of Treatment Effects. Proceedings of the 10th International Conference on Educational Data Mining. https://sites.google.com/site/tamemethod/

`q2 · i2` · `design · r2`

Numerical simulation result shown in Figure 2 of the large-scale simulation study. The authors believe this is because TAME accounts for noises better than ANOVA by using more data that is available to TAME.

> "Figure 2 shows that as the number of factors increases, the power of TAME decreases less than the power of ANOVA. This decrease leads to a difference in power between the two methods based on the number of factors. The number of factors is statistically significant (F(4,70713) = 769.046, p<0.001) with a partial eta squared of 0.042."

## Discussion


## Related Claims
- [In resampled real data from the experiment with the strongest treatment effect, TAME detects the effect better than ANOVA especially when sample size is 40 or below](tame-resampling-experiment3-small-samples.md) — a narrower finding that bears on this claim
