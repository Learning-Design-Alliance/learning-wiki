---
type: claim
title: A MATLAB inverse-kinematics pipeline automated generation of 38 of 52 LIS signs on Pepper and cut authoring time from 45–60 to under 10 minutes per sign
description: A MATLAB inverse-kinematics pipeline automated generation of 38 of 52 LIS signs on Pepper and cut authoring time from 45–60 to under 10 minutes per sign
id: ik-pipeline-automates-pepper-lis-sign-generation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: giulia-boaa-2025
    resource: "https://doi.org/10.1007/978-981-95-2382-5_8"
    title: "Giulia Boaa, Marco Boaa, Cristina Gena, Alessandro Mazzei, Massimo Donini, and Alberto Lillo. (2025). Using the Pepper Robot to Support Sign Language Communication. https://github.com/CodeCruncher63/ISCR2025 [doi:10.1007/978-981-95-2382-5_8](https://doi.org/10.1007/978-981-95-2382-5_8)"
    author: Giulia Boaa, Marco Boaa, Cristina Gena, Alessandro Mazzei, Massimo Donini, and Alberto Lillo
    q: 2
    i: "?"
    kind: design
    rigour: 3
  - id: giulia-boaa-2025-2
    resource: "https://github.com/CodeCruncher63/ISCR2025"
    title: "Giulia Boaa, Marco Boaa, Cristina Gena, Alessandro Mazzei, Massimo Donini, and Alberto Lillo. (2025). Using the Pepper Robot to Support Sign Language Communication. https://github.com/CodeCruncher63/ISCR2025"
    author: Giulia Boaa, Marco Boaa, Cristina Gena, Alessandro Mazzei, Massimo Donini, and Alberto Lillo
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# A MATLAB inverse-kinematics pipeline automated generation of 38 of 52 LIS signs on Pepper and cut authoring time from 45–60 to under 10 minutes per sign

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r3` · `q2`

## Subclaims
`q2 i?` The semi-automated pipeline successfully generated 38 of the 52 manually implemented signs (73%); ten failed due to asymmetric or body-involving movements and four due to kinematic infeasibility or solver instability. [→ Giulia Boaa 2025](#giulia-boaa-2025)
`q2 i?` Automated sign creation took under 10 minutes per sign versus approximately 45–60 minutes for manual creation. [→ Giulia Boaa 2025 (2)](#giulia-boaa-2025-2)

## Evidence

### Giulia Boaa 2025

Giulia Boaa, Marco Boaa, Cristina Gena, Alessandro Mazzei, Massimo Donini, and Alberto Lillo. (2025). Using the Pepper Robot to Support Sign Language Communication. https://github.com/CodeCruncher63/ISCR2025 [doi:10.1007/978-981-95-2382-5_8](https://doi.org/10.1007/978-981-95-2382-5_8)

`q2 · i?` · `design · r3`

Technical implementation result from the methodology section: a MATLAB inverse-kinematics solver plus Python exporter reproduced "38	out of the 52" signs; failures stemmed from asymmetric movements and solver instability.

> "This approach successfully automated the genera0on of 38	out of the 52	manually implemented signs (73%). Ten signs could not be reproduced due to asymmetric or body-involving movements, and four others failed due to kinema0c infeasibility or solver instability."

### Giulia Boaa 2025 (2)

Giulia Boaa, Marco Boaa, Cristina Gena, Alessandro Mazzei, Massimo Donini, and Alberto Lillo. (2025). Using the Pepper Robot to Support Sign Language Communication. https://github.com/CodeCruncher63/ISCR2025

`q2 · i?` · `design · r3`

Authoring-time comparison reported in the methodology section: manual sign creation took "approximately 45–60 minutes" versus "under 10 minutes per sign" with the automated pipeline.

> "On average, the manual crea0on of a sign required approximately 45–60 minutes, while the automated method reduced this to under 10 minutes per sign, including coordinate setup and execu0on."

## Discussion


## Related Claims
- [Recognition of individual Pepper-produced LIS signs varies widely, with several signs significantly above chance and others not significant](pepper-lis-sign-recognition-binomial-tests.md) — related
- [LIS users recognize Pepper's isolated signs far better than its full signed sentences in an exploratory evaluation](pepper-isolated-signs-recognized-better-than-sentences.md) — related
