---
type: claim
title: The pipeline generates print-ready binary STL files for all five chart types in under 60 ms on a 150×150 mm plate
description: The pipeline generates print-ready binary STL files for all five chart types in under 60 ms on a 150×150 mm plate
id: tactile-pipeline-stl-under-60ms
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: lawrence-obiuwevwi-2026
    resource: "https://arxiv.org/abs/2607.01214"
    title: "Lawrence Obiuwevwi, Krzysztof J. Rechowicz, Jessica M. Johnson, Erika Frydenlund, Vikas Ashok, Sachin Shetty, & Sampath Jayarathna. (2026). Touching and Feeling the Data: A Reusable Software Pipeline for Tactile Statistical Graphs in Accessible Education. arXiv. https://arxiv.org/abs/2607.01214"
    author: "Lawrence Obiuwevwi, Krzysztof J. Rechowicz, Jessica M. Johnson, Erika Frydenlund, Vikas Ashok, Sachin Shetty, & Sampath Jayarathna"
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The pipeline generates print-ready binary STL files for all five chart types in under 60 ms on a 150×150 mm plate

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` All five chart types (scatter, bar, histogram, line, box plot) complete STL generation in under 60 ms, within the 250 ms threshold perceived as instantaneous. [→ Lawrence Obiuwevwi 2026](#lawrence-obiuwevwi-2026)

## Evidence

### Lawrence Obiuwevwi 2026

Lawrence Obiuwevwi, Krzysztof J. Rechowicz, Jessica M. Johnson, Erika Frydenlund, Vikas Ashok, Sachin Shetty, & Sampath Jayarathna. (2026). Touching and Feeling the Data: A Reusable Software Pipeline for Tactile Statistical Graphs in Accessible Education. arXiv. https://arxiv.org/abs/2607.01214

`q2 · i?` · `design · r2`

Performance test via test-pipeline.js on a 150×150 mm plate (Table I): scatter 51 ms, bar 35 ms, histogram 26 ms, line 25 ms, box plot 24 ms. The article reports "All five chart types complete in under 60 ms" and notes scatter and box plots have higher primitive counts.

> "All five chart types complete in under 60 ms, well within the 250 ms threshold perceived as instantaneous [27]. Scatter and box plots have higher primitive counts due to cylinder tessellation; cuboid-heavy types are faster and smaller."

## Discussion


## Related Claims
- [The pipeline reduces per-chart software labor from about two hours of manual Fusion 360 modeling to under 60 ms](tactile-pipeline-labor-reduction-four-orders.md) — related
