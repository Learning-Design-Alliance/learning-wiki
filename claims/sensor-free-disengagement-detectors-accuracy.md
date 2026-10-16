---
type: claim
title: Automated detectors of disengaged behaviors inferred from interaction-log data alone reached AUC over 0.8 for gaming and correlated 0.55 with observed off-task behavior
description: Automated detectors of disengaged behaviors inferred from interaction-log data alone reached AUC over 0.8 for gaming and correlated 0.55 with observed off-task behavior
id: sensor-free-disengagement-detectors-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
sources:
  - id: kenneth-r-koedinger-2012
    resource: "http://learnlab.org/datashop"
    title: "Kenneth R. Koedinger, Emma Brunskill, Ryan S.J.d. Baker, Elizabeth A. McLaughlin, and John Stamper. (2012). New Potentials for Data-Driven Intelligent Tutoring System Development and Optimization. http://learnlab.org/datashop"
    author: Kenneth R. Koedinger, Emma Brunskill, Ryan S.J.d. Baker, Elizabeth A. McLaughlin, and John Stamper
    q: 2
    i: "?"
    kind: review
    rigour: 2
  - id: kenneth-r-koedinger-2012-2
    resource: "http://learnlab.org/datashop"
    title: "Kenneth R. Koedinger, Emma Brunskill, Ryan S.J.d. Baker, Elizabeth A. McLaughlin, and John Stamper. (2012). New Potentials for Data-Driven Intelligent Tutoring System Development and Optimization. http://learnlab.org/datashop"
    author: Kenneth R. Koedinger, Emma Brunskill, Ryan S.J.d. Baker, Elizabeth A. McLaughlin, and John Stamper
    q: 2
    i: 3
    kind: review
    rigour: 2
---

# Automated detectors of disengaged behaviors inferred from interaction-log data alone reached AUC over 0.8 for gaming and correlated 0.55 with observed off-task behavior

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · review `r2` · `q2` · `i3` large

## Subclaims
`q2 i?` Gaming-the-system detectors validated on new students and lessons achieved A' / AUC over 0.8 using interaction features such as repeated fast errors on poorly known skills. [→ Kenneth R. Koedinger 2012](#kenneth-r-koedinger-2012)
`q2 i3` The first off-task behavior detector achieved a correlation of 0.55 between predicted and observer-noted frequency of off-task behavior, with cross-validation at the student level. [→ Kenneth R. Koedinger 2012 (2)](#kenneth-r-koedinger-2012-2)

## Evidence

### Kenneth R. Koedinger 2012

Kenneth R. Koedinger, Emma Brunskill, Ryan S.J.d. Baker, Elizabeth A. McLaughlin, and John Stamper. (2012). New Potentials for Data-Driven Intelligent Tutoring System Development and Optimization. http://learnlab.org/datashop

`q2 · i?` · `review · r2`

Detectors of gaming the system (Baker et al. 2004, as reported here) were trained on field-observation or text-replay labels and J48 decision trees, using features like "repeated fast errors on poorly known skills". Validation on new students and lessons found A'/AUC over 0.8; the article prints no standardized effect size for this finding.

> "The automated detectors were validated for effectiveness for new students and tutor lessons on different topics (within the same year-long mathematics curriculum), and were found to be reasonably effective (A’/AUC over 0.8) under these conditions."

### Kenneth R. Koedinger 2012 (2)

Kenneth R. Koedinger, Emma Brunskill, Ryan S.J.d. Baker, Elizabeth A. McLaughlin, and John Stamper. (2012). New Potentials for Data-Driven Intelligent Tutoring System Development and Optimization. http://learnlab.org/datashop

`q2 · i3` · `review · r2`

Off-task behavior detection (Baker 2007, as reported here) relied solely on semantic interface actions and timing data, with cross-validation at the student level. The article prints a correlation of 0.55 (r = 0.55) between predicted and observer-noted off-task frequency, a large printed association.

> "The first detector of this behavior, by Baker (2007), achieved a correlation of 0.55 between each student’s predicted frequency of off-task behavior and the behavior’s frequency as noted by field observers, with cross-validation conducted at the student level."

## Discussion


## Related Claims
-
