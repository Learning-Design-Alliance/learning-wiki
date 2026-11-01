---
type: claim
title: In resampled real data from the experiment with the strongest treatment effect, TAME detects the effect better than ANOVA especially when sample size is 40 or below
description: In resampled real data from the experiment with the strongest treatment effect, TAME detects the effect better than ANOVA especially when sample size is 40 or below
id: tame-resampling-experiment3-small-samples
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
    i: "?"
    kind: design
    rigour: 2
---

# In resampled real data from the experiment with the strongest treatment effect, TAME detects the effect better than ANOVA especially when sample size is 40 or below

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For experiment 3, TAME detects the treatment effect better than ANOVA, especially when the sample size <= 40. [→ Thanaporn Patikorn 2016](#thanaporn-patikorn-2016)

## Evidence

### Thanaporn Patikorn 2016

Thanaporn Patikorn, Douglas Selent, Neil T. Heffernan, Joseph E. Beck, Jian Zou. (2016). Using a Single Model Trained across Multiple Experiments to Improve the Detection of Treatment Effects. Proceedings of the 10th International Conference on Educational Data Mining. https://sites.google.com/site/tamemethod/

`q2 · i?` · `design · r2`

Reliability analysis on real data: for each experiment a model was trained on the other twenty-one experiments, with sample sizes from 10 to 100 resampled 1,000 times each. At sample size 10, TAME's detection probability was 0.2280 versus ANOVA's 0.0650.

> "Table 5 shows that for the experiment with the strongest treatment effect (experiment 3), TAME is able to detect the treatment effect better than ANOVA, especially when the sample size <= 40. This result agrees with the result of our simulation study."

## Discussion


## Related Claims
- [On real ASSISTments data, TAME and ANOVA agree on which experiments show significant treatment effects](tame-anova-agreement-real-assistments-data.md) — related
- [As the number of factors increases, TAME's power decreases less than ANOVA's, with a significant method-by-factors interaction](tame-power-degrades-less-with-more-factors.md) — a broader claim this one bears on
