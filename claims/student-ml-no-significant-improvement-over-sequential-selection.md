---
type: claim
title: Student-built decision-tree classifiers typically do not significantly improve event classification over the sequential selection in this laboratory
description: Student-built decision-tree classifiers typically do not significantly improve event classification over the sequential selection in this laboratory
id: student-ml-no-significant-improvement-over-sequential-selection
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: waiton-2026
    resource: "https://doi.org/10.1088/1361-6404/ae8086"
    title: "Waiton, J., Bateman, J., Evans, J. J., Finnerud, O. G., Gramellini, E., Guenette, R., Guzowski, P., Kedziora, A., Söldner-Rembold, S. (2026). A sterile-neutrino search using data from the MicroBooNE liquid-argon time projection chamber performed in an undergraduate teaching laboratory. Originally published 2025. [doi:10.1088/1361-6404/ae8086](https://doi.org/10.1088/1361-6404/ae8086)"
    author: Waiton, J., Bateman, J., Evans, J. J., Finnerud, O. G., Gramellini, E., Guenette, R., Guzowski, P., Kedziora, A., Söldner-Rembold, S.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Student-built decision-tree classifiers typically do not significantly improve event classification over the sequential selection in this laboratory

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` When students implement random decision forests and compare purity and efficiency with their sequential selection, the ML model typically does not achieve a significant improvement, because some sequential-selection variables are already machine-learning derived. [→ Waiton 2026](#waiton-2026)

## Evidence

### Waiton 2026

Waiton, J., Bateman, J., Evans, J. J., Finnerud, O. G., Gramellini, E., Guenette, R., Guzowski, P., Kedziora, A., Söldner-Rembold, S. (2026). A sterile-neutrino search using data from the MicroBooNE liquid-argon time projection chamber performed in an undergraduate teaching laboratory. Originally published 2025. [doi:10.1088/1361-6404/ae8086](https://doi.org/10.1088/1361-6404/ae8086)

`q2 · i?` · `design · r2`

Observation from the machine-learning stage of the teaching laboratory, where students train random decision forests in scikit-learn and compare metrics with their hand-built selection; the article reports "does not achieve a significant improvement". No effect size or test statistic is printed.

> "Once students have implemented their ML model, they should compare the purity and efficiency with that achieved by their sequential selection and discuss the comparison. Typically their ML model does not achieve a significant improvement, since some of the variables used in the sequential selection, as described in table 2, are already determined by ML."

## Discussion


## Related Claims
- [Students using sequential topological selections on the MicroBooNE teaching sample typically reach approximately 80% efficiency and 85% purity](students-achieve-80-efficiency-85-purity-sequential-selection.md) — related
- [Random forest and support vector machine models also failed to beat chance when predicting laboratory performance, supporting the null result](rf-svm-also-fail-beat-chance-lab-performance.md) — related
