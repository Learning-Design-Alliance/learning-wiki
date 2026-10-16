---
type: claim
title: The same mean difference yields different partial eta squared values depending on whether it is analyzed in a within- or between-subjects design
description: The same mean difference yields different partial eta squared values depending on whether it is analyzed in a within- or between-subjects design
id: eta-partial-differs-by-design
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
sources:
  - id: lakens-2013
    resource: "https://doi.org/10.3389/fpsyg.2013.00863"
    title: "Lakens, D. (2013). Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs. Frontiers in Psychology. https://doi.org/10.3389/fpsyg.2013.00863"
    author: Lakens, D.
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# The same mean difference yields different partial eta squared values depending on whether it is analyzed in a within- or between-subjects design

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` For identical means and standard deviations, η²p is 0.26 when the data come from a between-subjects design and 0.71 from a within-subjects design, because positive correlation between measures reduces error variance. [→ Lakens 2013](#lakens-2013)

## Evidence

### Lakens 2013

Lakens, D. (2013). Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and ANOVAs. Frontiers in Psychology. https://doi.org/10.3389/fpsyg.2013.00863

`q2 · i?` · `theoretical · r3`

Illustrative worked example (artificial movie evaluations, M1 = 7.7, SD1 = 0.95, M2 = 8.7, SD2 = 0.82, mean difference of 1). The article shows η²p = 0.26 (One-Way ANOVA, F(1,18) = 6.34) versus η²p = 0.71 (repeated-measures ANOVA, F(1,9) = 22.50), while generalized eta squared η²G = 0.26 in both.

> "Depending on whether the data were collected in a between or within-subjects design, the effect size partial eta squared ( η2 p) for the difference between these two observations (for details, see the illustrative example below) is either 0.26 or 0.71, respectively."

## Discussion


## Related Claims
- [Repeated-measures designs with strongly correlated observations yield dramatically higher statistical power than between-subjects designs for the same mean difference](within-subjects-correlation-increases-power.md) — related
- [For within-subjects designs, the author recommends reporting Cohen's d_rm or Cohen's d_av rather than Cohen's dz](recommend-drm-or-dav-for-within-designs.md) — related
