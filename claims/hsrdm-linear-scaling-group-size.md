---
type: claim
title: Under the conditional-independence assumption, per-entity computation in the adapted HSRDM scales linearly in the number of students
description: Under the conditional-independence assumption, per-entity computation in the adapted HSRDM scales linearly in the number of students
id: hsrdm-linear-scaling-group-size
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: gili-2026
    resource: "https://doi.org/10.48550/arXiv.2604.21870"
    title: "Gili, Kaitlin, Nistala, Mainak, Wendell, Kristen, and Hughes, Michael C. (2026). Locating acts of mechanistic reasoning in student team conversations with mechanistic machine learning. [doi:10.48550/arXiv.2604.21870](https://doi.org/10.48550/arXiv.2604.21870)"
    author: Gili, Kaitlin, Nistala, Mainak, Wendell, Kristen, and Hughes, Michael C.
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Under the conditional-independence assumption, per-entity computation in the adapted HSRDM scales linearly in the number of students

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Because entity observations and latent states interact only through the shared system state, the cost of generating or evaluating data under the model grows linearly with the number of entities. [→ Gili 2026](#gili-2026)

## Evidence

### Gili 2026

Gili, Kaitlin, Nistala, Mainak, Wendell, Kristen, and Hughes, Michael C. (2026). Locating acts of mechanistic reasoning in student team conversations with mechanistic machine learning. [doi:10.48550/arXiv.2604.21870](https://doi.org/10.48550/arXiv.2604.21870)

`q1 · i?` · `design · r2`

Analytical statement about the model's structure under assumption (2), conditional independence of entity states given system states. The authors note the present analysis looks at small teams of 2-4 students but the model could scale to classroom-wide discussions of 50 or more students; no empirical timing results are printed.

> "Because entity observations and latent states only influence one another through the system latent variable, the cost of generating data from the model or evaluating the probability of data under the model remains linear in J as the number of entities grows."

## Discussion


## Related Claims
- [Computational complexity of the graph-based MML procedure scales with the number of latent variables within a conditionally independent subset, and brute-force integration scales exponentially with dimensionality](mml-complexity-scales-with-clique-state-spaces.md) — related
