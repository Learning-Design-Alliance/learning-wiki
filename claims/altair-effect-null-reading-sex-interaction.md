---
type: claim
title: The Altair (engine) main effect is not significant for winter RIT scores in either content area, but an Altair-by-sex interaction is significant in Reading only
description: The Altair (engine) main effect is not significant for winter RIT scores in either content area, but an Altair-by-sex interaction is significant in Reading only
id: altair-effect-null-reading-sex-interaction
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: mixed
sources:
  - id: bo-2020
    resource: "https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-an-engine-evaluation-study-based-on-empirical-data/"
    title: "Bo, E., & Meyer, P. (2020). Comparability of MAP Growth tests administered through different technology and psychometric infrastructure: An engine evaluation study based on empirical data. Portland, OR: NWEA. https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-an-engine-evaluation-study-based-on-empirical-data/"
    author: "Bo, E., & Meyer, P."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: bo-2020-2
    resource: "https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-an-engine-evaluation-study-based-on-empirical-data/"
    title: "Bo, E., & Meyer, P. (2020). Comparability of MAP Growth tests administered through different technology and psychometric infrastructure: An engine evaluation study based on empirical data. Portland, OR: NWEA. https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-an-engine-evaluation-study-based-on-empirical-data/"
    author: "Bo, E., & Meyer, P."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The Altair (engine) main effect is not significant for winter RIT scores in either content area, but an Altair-by-sex interaction is significant in Reading only

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Adding the Altair treatment variable does not improve model fit for winter RIT scores in Reading or Mathematics. [→ Bo 2020](#bo-2020)
`q2 i?` An Altair-by-sex interaction significantly improves model fit in Reading (chi-squared = 6.75, p < 0.01) but not in Mathematics (chi-squared = 0.31, p = 0.57). [→ Bo 2020 (2)](#bo-2020-2)

## Evidence

### Bo 2020

Bo, E., & Meyer, P. (2020). Comparability of MAP Growth tests administered through different technology and psychometric infrastructure: An engine evaluation study based on empirical data. Portland, OR: NWEA. https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-an-engine-evaluation-study-based-on-empirical-data/

`q2 · i?` · `causal · r2`

Mixed-effect model comparison (students nested within schools; 165,906 Reading and 163,058 Mathematics students) testing the Altair fixed effect. The article reports nonsignificant chi-squares, and profile confidence intervals for Altair included 0 in both content areas.

> "The chi-square test for deviance of Model 2 and Model 3 yielded nonsignificant chi-squares for both content areas (chi-squared = 0.04, p= 0.83 in Reading; chi-squared = 1.06, p= 0.30 in Mathematics), indicating that the Altair variable is not needed to predict the winter RIT scores in both content areas."

### Bo 2020 (2)

Bo, E., & Meyer, P. (2020). Comparability of MAP Growth tests administered through different technology and psychometric infrastructure: An engine evaluation study based on empirical data. Portland, OR: NWEA. https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-an-engine-evaluation-study-based-on-empirical-data/

`q2 · i?` · `causal · r2`

Likelihood-ratio test comparing Models 3 and 4 in the same nested mixed-effect analysis. The Altair-by-sex coefficient was significant in Reading per profile confidence intervals (0.14 to 1.02); no effect size was printed, so impact is null.

> "The chi-square test for deviance of Model 3 and Model 4 yields a significant chi-square in Reading (chi-squared = 6.75, p < 0.01) and a non-significant chi-square in Mathematics (chi-squared=0.31, p=0.57), indicating that the sex and Altair interaction variable should be included to predict the winter Reading RIT scores."

## Discussion


## Related Claims
- [Growth-score differences between CBE and COLO are small, exceeding 0.2 only in Reading Grades K–1 (favoring CBE) and Mathematics Grade 8 (favoring COLO)](map-growth-cbe-colo-growth-effect-sizes-small.md) — related
- [Marginal reliabilities of MAP Growth winter scores are comparable across engines and all in the 0.90s, with CBE showing slightly higher precision (lower SEM)](cbe-colo-reliability-comparable-cbe-higher-precision.md) — related
