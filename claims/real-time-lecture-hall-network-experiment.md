---
type: claim
title: The phyphox network interface enables real-time collaborative lecture-hall experiments in which students jointly determine a spring constant from a live frequency-over-mass plot
description: The phyphox network interface enables real-time collaborative lecture-hall experiments in which students jointly determine a spring constant from a live frequency-over-mass plot
id: real-time-lecture-hall-network-experiment
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
---

# The phyphox network interface enables real-time collaborative lecture-hall experiments in which students jointly determine a spring constant from a live frequency-over-mass plot

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In a live lecture-hall experiment, pairs of students built spring oscillators with phones and chocolate bars, and periodically submitted oscillation frequencies so a server could generate and project a frequency-over-mass plot to determine the spring constant in real time. [→ S Staacks 2022](#s-staacks-2022)

## Evidence

### S Staacks 2022

S Staacks, D Dorsel, S Hütz, F Stallmach, T Splith, H Heinke, C Stampfer. (2022). Collaborative smartphone experiments for large audiences with phyphox. https://doi.org/10.1088/1361-6404/ac7830

`q2 · i?` · `design · r2`

Real-time collaborative experiment in the same physics course: students received a bag, spring and chocolate bars, scanned a QR code with an event-specific phyphox configuration, and the app periodically submitted the current frequency every ten seconds. A Python script generated the frequency-over-mass plot, updated every few seconds on the main projector, with a model fit to extract the spring constant.

> "The goal of the collaborative experiment was to generate a frequency over mass plot to determine the spring constant for the identical springs used by the students."

## Discussion


## Related Claims
- [Filtering incoming data is essential for large-audience network experiments, and autocorrelation-quality thresholds plus mid-series mass selection remove most erroneous points](filtering-large-audience-experiment-data.md) — related
- [Collaborative smartphone pendulum data collected via a web form let students conduct an experiment before the lecture explains the theory, reproducing the expected pendulum behavior](web-form-flipped-lecture-experiment.md) — related
