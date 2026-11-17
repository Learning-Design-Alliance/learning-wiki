---
type: claim
title: "MICA's universal visualization scripts encode about a dozen data dimensions, and OpenSim worlds allow visualization of ~100,000 data points"
description: "MICA's universal visualization scripts encode about a dozen data dimensions, and OpenSim worlds allow visualization of ~100,000 data points"
id: immersive-visualization-dimensions-and-opensim-scale
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: weak
newest_evidence: 2012
sources:
  - id: s-g-djorgovski-2012
    resource: "https://doi.org/10.48550/arXiv.1301.6808"
    title: "S. G. Djorgovski, Piet Hut, Rob Knop, Giuseppe Longo, Steve McMillan, Enrico Vesperini, Ciro Donalek, Matthew Graham, Asish Mahabal, Franz Sauer, Charles White, Crista Lopes. (2012). The MICA Experiment: Astrophysics in Virtual Worlds. ref. proc. SLACTIONS 2012 International Research Conference on Virtual Worlds. [doi:10.48550/arXiv.1301.6808](https://doi.org/10.48550/arXiv.1301.6808)"
    author: S. G. Djorgovski, Piet Hut, Rob Knop, Giuseppe Longo, Steve McMillan, Enrico Vesperini, Ciro Donalek, Matthew Graham, Asish Mahabal, Franz Sauer, Charles White, Crista Lopes
    q: 2
    i: "?"
    kind: design
    rigour: 1
  - id: s-g-djorgovski-2012-2
    resource: "https://doi.org/10.48550/arXiv.1301.6808"
    title: "S. G. Djorgovski, Piet Hut, Rob Knop, Giuseppe Longo, Steve McMillan, Enrico Vesperini, Ciro Donalek, Matthew Graham, Asish Mahabal, Franz Sauer, Charles White, Crista Lopes. (2012). The MICA Experiment: Astrophysics in Virtual Worlds. ref. proc. SLACTIONS 2012 International Research Conference on Virtual Worlds. [doi:10.48550/arXiv.1301.6808](https://doi.org/10.48550/arXiv.1301.6808)"
    author: S. G. Djorgovski, Piet Hut, Rob Knop, Giuseppe Longo, Steve McMillan, Enrico Vesperini, Ciro Donalek, Matthew Graham, Asish Mahabal, Franz Sauer, Charles White, Crista Lopes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# MICA's universal visualization scripts encode about a dozen data dimensions, and OpenSim worlds allow visualization of ~100,000 data points

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r1`–`r2` · `q2`
> **Currency** · newest study 2012 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Using shapes, textures, orientations, transparency, rotation and pulsation of data objects, MICA expects about a dozen parameter space dimensions can be encoded in immersive pseudo-3D displays. [→ S. G. Djorgovski 2012](#s-g-djorgovski-2012)
`q2 i?` In OpenSim worlds, MICA can easily visualize ~100,000 data points; beyond that, individual points are better replaced by isodensity surfaces, with outliers kept as individual points. [→ S. G. Djorgovski 2012 (2)](#s-g-djorgovski-2012-2)

## Evidence

### S. G. Djorgovski 2012

S. G. Djorgovski, Piet Hut, Rob Knop, Giuseppe Longo, Steve McMillan, Enrico Vesperini, Ciro Donalek, Matthew Graham, Asish Mahabal, Franz Sauer, Charles White, Crista Lopes. (2012). The MICA Experiment: Astrophysics in Virtual Worlds. ref. proc. SLACTIONS 2012 International Research Conference on Virtual Worlds. [doi:10.48550/arXiv.1301.6808](https://doi.org/10.48550/arXiv.1301.6808)

`q2 · i?` · `design · r1`

Development report on universal scripts for immersive visualization of highly dimensional data sets, built with Desdemona Enfield, including the alpha (transparency) layer as an added encoding dimension. The authors state "we expect that about a dozen parameter space dimensions can be encoded" in these displays.

> "We are using data object shapes, textures, orientations, transparency, rotation, pulsation, etc., to encode additional data dimensions beyond the obvious spatial XYZ coordinates, color, and size of data objects (Fig. 7)."

### S. G. Djorgovski 2012 (2)

S. G. Djorgovski, Piet Hut, Rob Knop, Giuseppe Longo, Steve McMillan, Enrico Vesperini, Ciro Donalek, Matthew Graham, Asish Mahabal, Franz Sauer, Charles White, Crista Lopes. (2012). The MICA Experiment: Astrophysics in Virtual Worlds. ref. proc. SLACTIONS 2012 International Research Conference on Virtual Worlds. [doi:10.48550/arXiv.1301.6808](https://doi.org/10.48550/arXiv.1301.6808)

`q2 · i?` · `design · r2`

Report on porting the visualization scripts into OpenSim worlds, initially Intel's ScienceSim and then Virtual Caltech, which overcame SL's limited prim quotas. The printed scale is "~ 100,000 data points", with the stated fallback to isodensity surfaces beyond that.

> "In our OpenSim experiments, we can easily visualize ~ 100,000 data points. Beyond that, individual data point representations are better replaced by isodensity surfaces, at least for the majority of the data; outliers are still best represented as individual data points."

## Discussion


## Related Claims
- [MICA's weekly popular science lectures in Second Life drew typical audiences of about 50-70 avatars](mica-popular-lectures-attendance-50-70-avatars.md) — related
- [Second Life scripts can represent physical quantities in real time and set initial position, velocity, and mass, satisfying key teaching-oriented simulator criteria](sl-real-time-representation-and-initial-parameters-feasible.md) — related
