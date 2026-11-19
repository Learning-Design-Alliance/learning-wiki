---
type: claim
title: Filtering incoming data is essential for large-audience network experiments, and autocorrelation-quality thresholds plus mid-series mass selection remove most erroneous points
description: Filtering incoming data is essential for large-audience network experiments, and autocorrelation-quality thresholds plus mid-series mass selection remove most erroneous points
id: filtering-large-audience-experiment-data
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: s-staacks-2022
    resource: "https://doi.org/10.1088/1361-6404/ac7830"
    title: "S Staacks, D Dorsel, S Hütz, F Stallmach, T Splith, H Heinke, C Stampfer. (2022). Collaborative smartphone experiments for large audiences with phyphox. https://doi.org/10.1088/1361-6404/ac7830"
    author: S Staacks, D Dorsel, S Hütz, F Stallmach, T Splith, H Heinke, C Stampfer
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: s-staacks-2022-2
    resource: "https://doi.org/10.1088/1361-6404/ac7830"
    title: "S Staacks, D Dorsel, S Hütz, F Stallmach, T Splith, H Heinke, C Stampfer. (2022). Collaborative smartphone experiments for large audiences with phyphox. https://doi.org/10.1088/1361-6404/ac7830"
    author: S Staacks, D Dorsel, S Hütz, F Stallmach, T Splith, H Heinke, C Stampfer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Filtering incoming data is essential for large-audience network experiments, and autocorrelation-quality thresholds plus mid-series mass selection remove most erroneous points

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` With automated submission, erroneous data from handling the phone can be reliably detected via the ratio of autocorrelation maxima, rejecting any ratio below 0.75. [→ S Staacks 2022](#s-staacks-2022)
`q2 i?` A common unanticipated mistake—students forgetting to update the entered mass after changing it—was mitigated by keeping only a single submission from the middle of a series of identical mass values, which eliminated most outlying data points. [→ S Staacks 2022 (2)](#s-staacks-2022-2)

## Evidence

### S Staacks 2022

S Staacks, D Dorsel, S Hütz, F Stallmach, T Splith, H Heinke, C Stampfer. (2022). Collaborative smartphone experiments for large audiences with phyphox. https://doi.org/10.1088/1361-6404/ac7830

`q2 · i?` · `design · r2`

Design analysis of the lecture-hall live experiment's filtering: the ratio of the autocorrelation peak to the maximum of the autocorrelated data served as a data-quality measure, allowing the server to reject unusable data; the accepted frequency range was 0.1 Hz to 4 Hz and mass was limited to 50 g to 1 kg.

> "For proper harmonic oscillations, this ratio will be close to 1.0 and any ratio below 0.75 is rejected."

### S Staacks 2022 (2)

S Staacks, D Dorsel, S Hütz, F Stallmach, T Splith, H Heinke, C Stampfer. (2022). Collaborative smartphone experiments for large audiences with phyphox. https://doi.org/10.1088/1361-6404/ac7830

`q2 · i?` · `design · r2`

After repeating the oscillation-balance experiment with 50 first-year physics teacher students in Leipzig in January 2019 and observing the same forgotten-mass mistake, the authors grouped submissions by identical mass and kept only the middle submission; discarded points were still plotted as open circles in figure 4.

> "The eﬀectiveness of this strategy is supported by the observation that most outlying data points get eliminated this way."

## Discussion


## Related Claims
- [The phyphox network interface enables real-time collaborative lecture-hall experiments in which students jointly determine a spring constant from a live frequency-over-mass plot](real-time-lecture-hall-network-experiment.md) — related
