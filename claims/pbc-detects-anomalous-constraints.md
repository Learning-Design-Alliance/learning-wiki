---
type: claim
title: Point-biserial correlation analysis detects anomalous constraints in CBM problem solving data
description: Point-biserial correlation analysis detects anomalous constraints in CBM problem solving data
id: pbc-detects-anomalous-constraints
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2013
recheck_by: 2016
sources:
  - id: gálvez-2013
    resource: "https://doi.org/10.1007/s40593-013-0008-2"
    title: "Gálvez, J., Conejo, R., & Guzmán, E. (2013). Statistical Techniques to Explore the Quality of Constraints in Constraint-Based Modeling Environments. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0008-2"
    author: "Gálvez, J., Conejo, R., & Guzmán, E."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: gálvez-2013-2
    resource: "https://doi.org/10.1007/s40593-013-0008-2"
    title: "Gálvez, J., Conejo, R., & Guzmán, E. (2013). Statistical Techniques to Explore the Quality of Constraints in Constraint-Based Modeling Environments. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0008-2"
    author: "Gálvez, J., Conejo, R., & Guzmán, E."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Point-biserial correlation analysis detects anomalous constraints in CBM problem solving data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2013 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2016**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In experiment 1, constraint C2 showed a notably low PBC (0.210) and C6 was flagged as a candidate for removal. [→ Gálvez 2013](#galvez-2013)
`q2 i?` In experiment 2, constraint C12 showed a negative PBC (-0.054), identifying it as a bad constraint. [→ Gálvez 2013 (2)](#galvez-2013-2)

## Evidence

### Gálvez 2013

Gálvez, J., Conejo, R., & Guzmán, E. (2013). Statistical Techniques to Explore the Quality of Constraints in Constraint-Based Modeling Environments. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0008-2

`q2 · i?` · `associational · r1`

Analysis of exam data from 24 undergraduates at the University of Malaga using PIPSE and CBM-Engine. The PBC analysis flagged C2 (PBC 0.210) as significantly lower than other constraints and C6 as a discard candidate. The article notes 'A negative value would suggest that students with higher scores violate the constraint.'

> "In this experiment, the PBC technique produced the result in Table 1, where we can see that C 2 has a significant lower value than the others. C 6 also has a low value and would be a candidate to be discarded from the dataset."

### Gálvez 2013 (2)

Gálvez, J., Conejo, R., & Guzmán, E. (2013). Statistical Techniques to Explore the Quality of Constraints in Constraint-Based Modeling Environments. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0008-2

`q2 · i?` · `design · r2`

Replication with a different sample of 23 students in January 2013. PBC analysis identified C12 (PBC -0.054) as problematic and C9 as under suspicion, consistent with the first experiment's method.

> "Using the same analysis as the previous experiment, the PBC obtained is shown in Table 5. The results do indicate a problem with C 12, since its PBC is negative. Other constraint under suspicion is C 9due to its low value in comparison to the others."

## Discussion


## Related Claims
- [Constraint information function analysis (AUC of CIF) detects faulty, redundant, and overly general constraints](cif-auc-detects-faulty-constraints.md) — related
- [Cronbach's alpha if-item-deleted analysis identifies constraints that reduce problem consistency](cronbach-alpha-if-deleted-constraint-analysis.md) — possibly the same claim (merge candidate)
- The three statistical techniques produce consistent diagnoses of constraint quality across two experiments — a broader claim this one bears on
- [Point-biserial item-total correlation is negatively related to test discriminating value and can be expressed via item and test difficulty and discrimination parameters](point-biserial-negative-test-discrimination-relation.md) — related
