---
type: claim
title: At the facet level, visualizing data is the most prevalent facet and co-occurs with applying statistics and synthesizing results
description: At the facet level, visualizing data is the most prevalent facet and co-occurs with applying statistics and synthesizing results
id: visualizing-data-most-prevalent-facet-associations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-18
evidence_strength: moderate
sources:
  - id: jina-kang-2026
    resource: "https://doi.org/10.1007/s11251-026-09803-5"
    title: "Jina Kang, Chungsoo Na, Morgan Diederich, Hillary Swanson, Lili Yan. (2026). Cultivating science data literacy in K-16 science education through data practices: A systematic review. Instructional Science. https://doi.org/10.1007/s11251-026-09803-5"
    author: Jina Kang, Chungsoo Na, Morgan Diederich, Hillary Swanson, Lili Yan
    q: 3
    i: "?"
    kind: review
    rigour: 2
  - id: jina-kang-2026-2
    resource: "https://doi.org/10.1007/s11251-026-09803-5"
    title: "Jina Kang, Chungsoo Na, Morgan Diederich, Hillary Swanson, Lili Yan. (2026). Cultivating science data literacy in K-16 science education through data practices: A systematic review. Instructional Science. https://doi.org/10.1007/s11251-026-09803-5"
    author: Jina Kang, Chungsoo Na, Morgan Diederich, Hillary Swanson, Lili Yan
    q: 3
    i: "?"
    kind: review
    rigour: 2
---

# At the facet level, visualizing data is the most prevalent facet and co-occurs with applying statistics and synthesizing results

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · review `r2` · `q3`

## Subclaims
`q3 i?` Visualizing data was the most prevalent facet (n = 33), frequently co-occurring with applying statistics (lift = 1.05, support = 0.57) and synthesizing results (lift = 1.07, support = 0.62). [→ Jina Kang 2026](#jina-kang-2026)
`q3 i?` Stronger associations included designing conditions → considering parameters (lift = 2.42, support = 0.14) and designing conditions → designing protocols (lift = 2.30, support = 0.17), with the reverse rule not meeting criteria. [→ Jina Kang 2026 (2)](#jina-kang-2026-2)

## Evidence

### Jina Kang 2026

Jina Kang, Chungsoo Na, Morgan Diederich, Hillary Swanson, Lili Yan. (2026). Cultivating science data literacy in K-16 science education through data practices: A systematic review. Instructional Science. https://doi.org/10.1007/s11251-026-09803-5

`q3 · i?` · `review · r2`

Association analysis using the Arules package in R on the 42 studies, with rules retained when lift > 1, support > 0.10, and confidence > 0.50. The review reports "visualizing data emerged as the most prevalent (n = 33)" and its co-occurrence metrics with applying statistics and synthesizing results.

> "Among the facets, visualizing data emerged as the most prevalent (n = 33). As shown in Fig. 2, it frequently co-occurred with applying statistics (#13; lift = 1.05, support = 0.57) and synthesizing results (#17; lift = 1.07, support = 0.62), suggesting that visualization was often paired with analytic and interpretive practices in the reviewed studies."

### Jina Kang 2026 (2)

Jina Kang, Chungsoo Na, Morgan Diederich, Hillary Swanson, Lili Yan. (2026). Cultivating science data literacy in K-16 science education through data practices: A systematic review. Instructional Science. https://doi.org/10.1007/s11251-026-09803-5

`q3 · i?` · `review · r2`

Association-rule analysis of facet co-occurrences across the 42 studies. The review reports the strongest directional rules within Designing Experiments and notes the reverse rule (considering parameters → designing conditions) did not meet the specified criteria.

> "Within the Designing Experiments (DE) dimension, the strongest directional associations observed across the reviewed studies appeared between designing conditions → considering parameters (lift = 2.42, support = 0.14) and designing conditions → designing protocols (lift = 2.30, support = 0.17)."

## Discussion


## Related Claims
- Collecting and analyzing data are the most prevalent data practices in K-16 science education research, while cleaning and disseminating data are least reported — related
- [K-12 and higher education show distinct, non-overlapping sets of co-occurring data practices](k12-versus-higher-education-distinct-data-practice-patterns.md) — related
- [Data type shapes practice emphasis: first-hand data aligns with problem understanding and experiment design, second-hand data with statistical analysis and synthesis](data-type-first-hand-second-hand-practice-alignment.md) — related
