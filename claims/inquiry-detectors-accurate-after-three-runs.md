---
type: claim
title: Machine-learned detectors of science inquiry skill made accurate inferences after a student ran a simulation three times
description: Machine-learned detectors of science inquiry skill made accurate inferences after a student ran a simulation three times
id: inquiry-detectors-accurate-after-three-runs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
newest_evidence: 2012
recheck_by: 2015
sources:
  - id: kenneth-r-koedinger-2012
    resource: "http://learnlab.org/datashop"
    title: "Kenneth R. Koedinger, Emma Brunskill, Ryan S.J.d. Baker, Elizabeth A. McLaughlin, and John Stamper. (2012). New Potentials for Data-Driven Intelligent Tutoring System Development and Optimization. http://learnlab.org/datashop"
    author: Kenneth R. Koedinger, Emma Brunskill, Ryan S.J.d. Baker, Elizabeth A. McLaughlin, and John Stamper
    q: 2
    i: "?"
    kind: review
    rigour: 1
---

# Machine-learned detectors of science inquiry skill made accurate inferences after a student ran a simulation three times

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r1` · `q2`
> **Currency** · newest study 2012 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2015**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Classifiers trained on hand-labeled science microworld logs inferred a student's inquiry skill accurately after three simulation runs (each under a minute), enabling rapid intervention. [→ Kenneth R. Koedinger 2012](#kenneth-r-koedinger-2012)

## Evidence

### Kenneth R. Koedinger 2012

Kenneth R. Koedinger, Emma Brunskill, Ryan S.J.d. Baker, Elizabeth A. McLaughlin, and John Stamper. (2012). New Potentials for Data-Driven Intelligent Tutoring System Development and Optimization. http://learnlab.org/datashop

`q2 · i?` · `review · r1`

Detector approach for ill-defined domains: humans hand-labeled replayed student interaction logs from science microworlds, and standard classification algorithms were trained and validated on new students and microworlds. The article reports detectors were "reasonably effective under these conditions" and accurate after three simulation runs.

> "Sao Pedro and colleagues found the detectors could make accurate inferences about a specific student’s inquiry skill after that student had run the simulation three times (each run takes under a minute), enabling reasonably rapid intervention."

## Discussion


## Related Claims
- [Automated detectors of disengaged behaviors inferred from interaction-log data alone reached AUC over 0.8 for gaming and correlated 0.55 with observed off-task behavior](sensor-free-disengagement-detectors-accuracy.md) — related
- [Automated gaming-the-system detectors built with XGBoost reliably recognize gaming in both problem-solving and self-explanation steps](xgboost-gaming-detectors-decimal-point.md) — related
