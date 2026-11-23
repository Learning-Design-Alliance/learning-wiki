---
type: claim
title: The GPU re-write of the solver was not complicated, especially with guidance, and served as a useful exercise for understanding GPU computation
description: The GPU re-write of the solver was not complicated, especially with guidance, and served as a useful exercise for understanding GPU computation
id: gpu-rewrite-not-complicated-useful-exercise
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2013
sources:
  - id: knut-s-gjerden-2013
    resource: "https://doi.org/10.48550/arXiv.1305.3625"
    title: "Knut S. Gjerden. (2013). Making the case of GPUs in courses on computational physics. [doi:10.48550/arXiv.1305.3625](https://doi.org/10.48550/arXiv.1305.3625)"
    author: Knut S. Gjerden
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The GPU re-write of the solver was not complicated, especially with guidance, and served as a useful exercise for understanding GPU computation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2013 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` The author reports that only a handful of user-supplied functions were needed beyond available numerical libraries and that the re-write was not complicated when guidance is provided. [→ Knut S. Gjerden 2013](#knut-s-gjerden-2013)

## Evidence

### Knut S. Gjerden 2013

Knut S. Gjerden. (2013). Making the case of GPUs in courses on computational physics. [doi:10.48550/arXiv.1305.3625](https://doi.org/10.48550/arXiv.1305.3625)

`q1 · i?` · `design · r2`

Author's assessment in the Results section of the porting effort, based on his own first experience moving a solver from BLAS/FFTW library calls to CUBLAS/CUFFT. The article reports "The re-write to use the GPU was not complica ted, especially if guidance is provided."

> "The re-write to use the GPU was not complica ted, especially if guidance is provided, and is a useful exercise to understanding GP U computation."

## Discussion


## Related Claims
- [Qiskit-based exercises agree with theoretical predictions and support introducing quantum computing to undergraduates](qiskit-agrees-with-theory-classroom-effectiveness.md) — related
- [Students found the visualisation of numerical PDE solutions the most well-received aspect of the course](pde-visualisation-most-valued-by-students.md) — related
