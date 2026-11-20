---
type: claim
title: Adding demographics slightly worsens assessment-based simulation, and demographics-only simulation drops heavily
description: Adding demographics slightly worsens assessment-based simulation, and demographics-only simulation drops heavily
id: demographics-limited-value-with-assessment-history
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: songlin-xu-and-xinyu-zhang-2023
    resource: "https://doi.org/10.48550/arXiv.2310.19206"
    title: "Songlin Xu and Xinyu Zhang. (2023). Leveraging generative artificial intelligence to simulate student learning behavior. [doi:10.48550/arXiv.2310.19206](https://doi.org/10.48550/arXiv.2310.19206)"
    author: Songlin Xu and Xinyu Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Adding demographics slightly worsens assessment-based simulation, and demographics-only simulation drops heavily

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Simulation performance with demographics plus all past assessments (Type iii, r = 0.68) is slightly worse than assessments alone (Type ii, r = 0.69), and demographics-only simulation drops heavily. [→ Songlin Xu and Xinyu Zhang 2023](#songlin-xu-and-xinyu-zhang-2023)

## Evidence

### Songlin Xu and Xinyu Zhang 2023

Songlin Xu and Xinyu Zhang. (2023). Leveraging generative artificial intelligence to simulate student learning behavior. [doi:10.48550/arXiv.2310.19206](https://doi.org/10.48550/arXiv.2310.19206)

`q2 · i?` · `design · r2`

In the N = 4524 Open University dataset simulation, the authors report performance "gets a little worse when we add demographics (Type iii:r = 0.68) compared with only using assessments (Type ii: r = 0.69)", attributing this to limited demographics in the dataset.

> "Surprisingly, we find that the simulation performance gets a little worse when we add demographics (Type iii:r = 0.68) compared with only using assessments (Type ii: r = 0.69)."

## Discussion


## Related Claims
- [Heterogeneity within demographic categories means group variables as predictors can disadvantage atypical group members and underrepresented groups](demographic-category-heterogeneity-harms-atypical-members.md) — related
- [Simulated final exam scores become more realistic as more past assessment history is used to instantiate virtual students](more-assessment-history-improves-simulation.md) — related
