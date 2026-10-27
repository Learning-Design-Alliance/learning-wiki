---
type: claim
title: Constraint information function analysis (AUC of CIF) detects faulty, redundant, and overly general constraints
description: Constraint information function analysis (AUC of CIF) detects faulty, redundant, and overly general constraints
id: cif-auc-detects-faulty-constraints
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
sources:
  - id: gálvez-2013
    resource: "https://doi.org/10.1007/s40593-013-0008-2"
    title: "Gálvez, J., Conejo, R., & Guzmán, E. (2013). Statistical Techniques to Explore the Quality of Constraints in Constraint-Based Modeling Environments. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0008-2"
    author: "Gálvez, J., Conejo, R., & Guzmán, E."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: gálvez-2013-2
    resource: "https://doi.org/10.1007/s40593-013-0008-2"
    title: "Gálvez, J., Conejo, R., & Guzmán, E. (2013). Statistical Techniques to Explore the Quality of Constraints in Constraint-Based Modeling Environments. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0008-2"
    author: "Gálvez, J., Conejo, R., & Guzmán, E."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Constraint information function analysis (AUC of CIF) detects faulty, redundant, and overly general constraints

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` In experiment 1, C2 had the lowest AUC (11.159) followed by C6, matching the PBC and alpha diagnoses; C8 showed the highest difficulty and CIF, suggesting it should be split. [→ Gálvez 2013](#galvez-2013)
`q2 i?` In experiment 2, the AUC analysis matched the PBC and alpha candidates (C12 and C9), with C12 oddly flattened and C9 redundant with C17. [→ Gálvez 2013 (2)](#galvez-2013-2)

## Evidence

### Gálvez 2013

Gálvez, J., Conejo, R., & Guzmán, E. (2013). Statistical Techniques to Explore the Quality of Constraints in Constraint-Based Modeling Environments. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0008-2

`q2 · i?` · `design · r2`

Calibration of CCCs from experiment 1 data followed by information function analysis (average AUC 14.808, SD 2.186). C2 (AUC 11.159) and C6 were lowest, with lower discrimination and higher guessing parameters. C8 had the highest difficulty and CIF, suggesting a split.

> "Constraint C 2, which was detected by PBC and Cronbach ’s alpha techniques as a questionable constraint, was also the one with a lower value of AUC, followed by constraint C 6. Those constraints were also those that have a lower value of the discriminant factor (a) and a slightly higher value of the guessing factor (c)."

### Gálvez 2013 (2)

Gálvez, J., Conejo, R., & Guzmán, E. (2013). Statistical Techniques to Explore the Quality of Constraints in Constraint-Based Modeling Environments. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0008-2

`q2 · i?` · `design · r2`

CIF analysis of experiment 2 data confirmed the candidates identified by the other two methods: C12 appeared flattened with a strange shape, and C9 overlapped the knowledge range covered by C17.

> "Using this information we can see that the set of candidate constraints to be removed, according to PBC and Cronbach ’s alpha (C 12 and maybe C 9), matches with the set suggested by the AUC analysis."

## Discussion


## Related Claims
- [The three statistical techniques produce consistent diagnoses of constraint quality across two experiments](three-methods-consistent-diagnosis.md) — a broader claim this one bears on
- [Point-biserial correlation analysis detects anomalous constraints in CBM problem solving data](pbc-detects-anomalous-constraints.md) — related
- [Cronbach's alpha if-item-deleted analysis identifies constraints that reduce problem consistency](cronbach-alpha-if-deleted-constraint-analysis.md) — related
