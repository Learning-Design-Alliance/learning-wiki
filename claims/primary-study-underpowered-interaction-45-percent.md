---
type: claim
title: "The primary study (Lehmann et al., 2016) had only about 45% power to detect its observed interaction effect; roughly 150 participants would be needed for 80% power"
description: "The primary study (Lehmann et al., 2016) had only about 45% power to detect its observed interaction effect; roughly 150 participants would be needed for 80% power"
id: primary-study-underpowered-interaction-45-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-19
evidence_strength: moderate
sources:
  - id: sophia-c-weissgerber-2024
    resource: "https://doi.org/10.1007/s11409-023-09366-7"
    title: "Sophia C. Weissgerber, Denia Indah Permatasari Terhorst, Ralf Rummer. (2024). Is the perceptual disfluency effect moderated by working memory capacity? Direct replication of Lehmann et al. (2016). Metacognition and Learning. https://doi.org/10.1007/s11409-023-09366-7"
    author: Sophia C. Weissgerber, Denia Indah Permatasari Terhorst, Ralf Rummer
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The primary study (Lehmann et al., 2016) had only about 45% power to detect its observed interaction effect; roughly 150 participants would be needed for 80% power

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Simulation-based power analysis showed the primary study had around 45% power to detect an interaction effect of the size it obtained (X1X2-Y r = 0.386), and 150 participants would be needed for 80% power. [→ Sophia C. Weissgerber 2024](#sophia-c-weissgerber-2024)

## Evidence

### Sophia C. Weissgerber 2024

Sophia C. Weissgerber, Denia Indah Permatasari Terhorst, Ralf Rummer. (2024). Is the perceptual disfluency effect moderated by working memory capacity? Direct replication of Lehmann et al. (2016). Metacognition and Learning. https://doi.org/10.1007/s11409-023-09366-7

`q2 · i?` · `causal · r2`

Simulation-based power analysis using the InteractionPoweR R package and shiny app (Baranger et al., 2022; Finsaas et al., 2021), with inputs computed from the primary study's dataset (retention model, reliability of the retention test Cronbach's Alpha = 0.492). "Given that the X1X2-Y from the primary data was r = 0.386, the simulation shows that the primary study had around 45% power to detect an interaction effect of this size." A further simulation varying sample size from 40 to 200 showed 150 participants would be necessary for conventional 0.80 power.

> "Given that the X1X2-Y from the primary data was r = 0.386, the simulation shows that the primary study had around 45% power to detect an interaction effect of this size."

## Discussion


## Related Claims

- [Analytical degrees of freedom in the primary study (prior-knowledge filtering and control-variable selection) affected its results: removing prior knowledge as a control rendered the comprehension interaction nonsignificant](analytical-flexibility-primary-study-results.md)
- [The null effect of the disfluency × WMC interaction on transfer replicated the primary study's null finding, with both studies showing negative coefficients](transfer-null-interaction-replicated.md)
