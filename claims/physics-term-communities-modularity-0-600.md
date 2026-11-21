---
type: claim
title: Community detection yields 15 communities (modularity ≈ 0.600), but some conceptually related physics terms are not clustered together
description: Community detection yields 15 communities (modularity ≈ 0.600), but some conceptually related physics terms are not clustered together
id: physics-term-communities-modularity-0-600
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: jibeom-seo-2024
    resource: "https://doi.org/10.3938/npsm.74.944"
    title: "Jibeom Seo, Jun Cho, Sukyung Han, Meesoon Ha. (2024). Semantic Network Analysis of Achievement Standards in Physics of 2022 Revised Curriculum. arXiv. [doi:10.3938/npsm.74.944](https://doi.org/10.3938/npsm.74.944)"
    author: Jibeom Seo, Jun Cho, Sukyung Han, Meesoon Ha
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: jibeom-seo-2024-2
    resource: "https://doi.org/10.3938/npsm.74.944"
    title: "Jibeom Seo, Jun Cho, Sukyung Han, Meesoon Ha. (2024). Semantic Network Analysis of Achievement Standards in Physics of 2022 Revised Curriculum. arXiv. [doi:10.3938/npsm.74.944](https://doi.org/10.3938/npsm.74.944)"
    author: Jibeom Seo, Jun Cho, Sukyung Han, Meesoon Ha
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Community detection yields 15 communities (modularity ≈ 0.600), but some conceptually related physics terms are not clustered together

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Optimized greedy modularity detection on the physics-term network found 15 communities with modularity about 0.600, with related terms mostly clustering together but some misgroupings. [→ Jibeom Seo 2024](#jibeom-seo-2024)
`q2 i?` Inter-community shortest-path analysis shows Communities 6, 1, and 5 closely connected while Communities 7, 3, and 4 are relatively distant, suggesting weak interconnections between geometrical optics and acoustics. [→ Jibeom Seo 2024 (2)](#jibeom-seo-2024-2)

## Evidence

### Jibeom Seo 2024

Jibeom Seo, Jun Cho, Sukyung Han, Meesoon Ha. (2024). Semantic Network Analysis of Achievement Standards in Physics of 2022 Revised Curriculum. arXiv. [doi:10.3938/npsm.74.944](https://doi.org/10.3938/npsm.74.944)

`q2 · i?` · `associational · r2`

Community detection on the physics-term network using the optimized greedy algorithm in NetworkX; the article also reports that "related concepts such as 'mechanical energy' and 'escape speed' are not clustered with 'kinetic energy' and 'potential energy,' even though they are closely related."

> "A total of 15 communities were identified, resulting in a modularity value of approximately 0.600."

### Jibeom Seo 2024 (2)

Jibeom Seo, Jun Cho, Sukyung Han, Meesoon Ha. (2024). Semantic Network Analysis of Achievement Standards in Physics of 2022 Revised Curriculum. arXiv. [doi:10.3938/npsm.74.944](https://doi.org/10.3938/npsm.74.944)

`q2 · i?` · `design · r2`

Average shortest path length analysis between communities (Fig. 6); the article notes that although geometrical optics and acoustics share a content domain, "the considerable distance between these communities suggests a potential lack of interconnections between them."

> "Communities 6, 1, and 5 are closely connected, whereas Communities 7, 3, and 4 are relatively distant from each other."

## Discussion


## Related Claims
- [Fuzzy Infomap community detection on a similarity network of 231 problem session networks finds ten overlapping clusters](ten-overlapping-clusters-problem-sessions.md) — related
- [Infomap community structure matches the curriculum's block organization exactly for Mathematics and partially for Physics and the integrated network](infomap-communities-match-curriculum-blocks.md) — related
- [Module analysis of FCI responses identified 13 student subgroups, with three normative groups differing in accuracy (77%, 73%, 53%) and in conceptual coherence](module-analysis-13-student-groups-fci.md) — related
- [In small interactive-engagement sections, network density and community counts stayed effectively constant over the semester](small-sections-constant-density-communities.md) — related
- [Curriculum-similarity network analysis of 31 Nanjing University departments identifies four disciplinary communities with sequentially decreasing degree centrality](four-disciplinary-communities-curriculum-similarity.md) — related
