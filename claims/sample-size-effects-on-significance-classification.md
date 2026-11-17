---
type: claim
title: Reducing the number of plotted data points significantly decreases sensitivity and increases specificity, while 200-point plots significantly drop specificity with no significant sensitivity change
description: Reducing the number of plotted data points significantly decreases sensitivity and increases specificity, while 200-point plots significantly drop specificity with no significant sensitivity change
id: sample-size-effects-on-significance-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: moderate
newest_evidence: 2014
sources:
  - id: aaron-fisher-2014
    resource: "https://doi.org/10.7717/peerj.589"
    title: "Aaron Fisher, G. Brooke Anderson, Roger Peng, Jeff Leek. (2014). A randomized trial in a massive online open course shows people don't know what a statistically significant relationship looks like, but they can learn. arXiv. [doi:10.7717/peerj.589](https://doi.org/10.7717/peerj.589)"
    author: Aaron Fisher, G. Brooke Anderson, Roger Peng, Jeff Leek
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: aaron-fisher-2014-2
    resource: "https://doi.org/10.7717/peerj.589"
    title: "Aaron Fisher, G. Brooke Anderson, Roger Peng, Jeff Leek. (2014). A randomized trial in a massive online open course shows people don't know what a statistically significant relationship looks like, but they can learn. arXiv. [doi:10.7717/peerj.589](https://doi.org/10.7717/peerj.589)"
    author: Aaron Fisher, G. Brooke Anderson, Roger Peng, Jeff Leek
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Reducing the number of plotted data points significantly decreases sensitivity and increases specificity, while 200-point plots significantly drop specificity with no significant sensitivity change

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` The Lower n category (35 points) significantly decreased sensitivity (OR=.454) and increased specificity (OR=1.67); the Larger n category (200 points) significantly dropped specificity (OR=.320) with no significant sensitivity change (OR=.891). [→ Aaron Fisher 2014](#aaron-fisher-2014)

## Evidence

### Aaron Fisher 2014

Aaron Fisher, G. Brooke Anderson, Roger Peng, Jeff Leek. (2014). A randomized trial in a massive online open course shows people don't know what a statistically significant relationship looks like, but they can learn. arXiv. [doi:10.7717/peerj.589](https://doi.org/10.7717/peerj.589)

`q3 · i?` · `causal · r2`

Logistic regression comparison of plot categories against the 100-point reference in the MOOC randomized trial. The "Lower n" plot category of 35 data points showed sensitivity OR=.454 and specificity OR=1.67 relative to reference.

> "reducing the number of datapoints shown (“Lower n” plot category) signiﬁcantly decreased sensitivity (Odds Ratio (OR) = .454, 95%CI: .385-.535) and increased speciﬁcity (OR=1.67, 95%CI: 1.39-2.04)."

### Aaron Fisher 2014 (2)

Aaron Fisher, G. Brooke Anderson, Roger Peng, Jeff Leek. (2014). A randomized trial in a massive online open course shows people don't know what a statistically significant relationship looks like, but they can learn. arXiv. [doi:10.7717/peerj.589](https://doi.org/10.7717/peerj.589)

`q3 · i?` · `causal · r2`

In the same regression analysis, the "Larger n" plots of 200 datapoints showed a significant specificity drop (OR=.320) with no significant sensitivity change (OR=.891); classification probability became fairly similar across truly significant and non-significant plots.

> "The exception to this counter-balancing trend came in “Larger n” plots of 200 datapoints, where students showed a signiﬁcant drop in speciﬁcity (OR=.320, 95%CI: .271-.377), and no signiﬁcant change in sensitivity (OR=.891, 95%CI: .763-1.04)."

## Discussion


## Related Claims
- [MOOC students visually classify statistically significant scatterplot relationships correctly only 47.4% of the time, while classifying non-significant ones correctly 74.6% of the time](low-sensitivity-visual-significance-classification-scatterplots.md) — related
- [Practice on repeat survey attempts significantly improves sensitivity for Reference, Best Fit, and Lower n plots, with overall accuracy gains for Reference and Best Fit but not Lower n](practice-improves-significance-detection-sensitivity.md) — related
- [Adding visual aids such as a best-fit line or lowess smooth increases the probability a relationship is called significant regardless of its actual significance](visual-aids-shift-significance-perception.md) — related
