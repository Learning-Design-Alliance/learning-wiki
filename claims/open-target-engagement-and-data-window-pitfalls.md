---
type: claim
title: "Choosing one's own investigation target creates engagement, and common pitfalls are defining signal length N and sample spacing Ts and failing to crop the data window"
description: "Choosing one's own investigation target creates engagement, and common pitfalls are defining signal length N and sample spacing Ts and failing to crop the data window"
id: open-target-engagement-and-data-window-pitfalls
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
sources:
  - id: p-pirinen-2023
    resource: "https://doi.org/10.1088/1361-6404/ad0790"
    title: "P. Pirinen, P. Klein, S. Z. Lahme, A. Lehtinen, L. Rončević, and A. Susac. (2023). Learning digital signal processing using an interactive Jupyter notebook and smartphone accelerometer data. [doi:10.1088/1361-6404/ad0790](https://doi.org/10.1088/1361-6404/ad0790)"
    author: P. Pirinen, P. Klein, S. Z. Lahme, A. Lehtinen, L. Rončević, and A. Susac
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: p-pirinen-2023-2
    resource: "https://doi.org/10.1088/1361-6404/ad0790"
    title: "P. Pirinen, P. Klein, S. Z. Lahme, A. Lehtinen, L. Rončević, and A. Susac. (2023). Learning digital signal processing using an interactive Jupyter notebook and smartphone accelerometer data. [doi:10.1088/1361-6404/ad0790](https://doi.org/10.1088/1361-6404/ad0790)"
    author: P. Pirinen, P. Klein, S. Z. Lahme, A. Lehtinen, L. Rončević, and A. Susac
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Choosing one's own investigation target creates engagement, and common pitfalls are defining signal length N and sample spacing Ts and failing to crop the data window

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Enabling students to choose their own target for investigation creates engagement and excitement, since the outcome is not known beforehand and students choose targets they genuinely care about. [→ P. Pirinen 2023](#p-pirinen-2023)
`q2 i?` A common pitfall is defining the signal length N and sample spacing Ts when moving from artificial examples to real measurement, and students often need instructor help to crop the accelerometer data to a window containing only the examined signal. [→ P. Pirinen 2023 (2)](#p-pirinen-2023-2)

## Evidence

### P. Pirinen 2023

P. Pirinen, P. Klein, S. Z. Lahme, A. Lehtinen, L. Rončević, and A. Susac. (2023). Learning digital signal processing using an interactive Jupyter notebook and smartphone accelerometer data. [doi:10.1088/1361-6404/ad0790](https://doi.org/10.1088/1361-6404/ad0790)

`q2 · i?` · `design · r2`

Authors' observation from running the task, which they connect to prior findings that "freedom and choice afforded by open-ended lab work can be beneficial for student engagement and enjoyment". No quantitative measure is reported.

> "We have observed that enabling students to choose their own target for investigation creates engagement and excitement as the outcome of the experiment is not known to anyone beforehand"

### P. Pirinen 2023 (2)

P. Pirinen, P. Klein, S. Z. Lahme, A. Lehtinen, L. Rončević, and A. Susac. (2023). Learning digital signal processing using an interactive Jupyter notebook and smartphone accelerometer data. [doi:10.1088/1361-6404/ad0790](https://doi.org/10.1088/1361-6404/ad0790)

`q2 · i?` · `design · r2`

Observation from implementations: despite a direct prompt in the notebook instructions, identifying sample spacing and signal length "has most often required help from an instructor"; cropping the data window is a second point where an instructor is often needed.

> "A common pitfall for students involves the definition of the signal length N and sample spacing Ts when moving from artificial examples to real measurement."

## Discussion


## Related Claims
- [MBP-KT performance is optimal with sliding-window size N between 2 and 4 and is not sensitive to pattern-set length K (variation within 2%)](mbp-kt-hyperparameter-sensitivity-n-k.md) — related
- [Students involved in near-space balloon exploration showed excitement and a sense of ownership of the project](student-ownership-near-space-exploration.md) — related
