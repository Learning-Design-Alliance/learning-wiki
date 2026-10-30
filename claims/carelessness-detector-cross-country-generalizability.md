---
type: claim
title: Carelessness detectors trained on Philippine students generalize to USA students without re-fitting
description: Carelessness detectors trained on Philippine students generalize to USA students without re-fitting
id: carelessness-detector-cross-country-generalizability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2014
recheck_by: 2017
sources:
  - id: maria-ofelia-z-san-pedro-2014
    resource: "https://doi.org/10.1007/s40593-014-0015-y"
    title: "Maria Ofelia Z. San Pedro, Ryan S. J. d. Baker, & Ma. Mercedes T. Rodrigo. (2014). Carelessness and Affect in an Intelligent Tutoring System for Mathematics. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-014-0015-y"
    author: "Maria Ofelia Z. San Pedro, Ryan S. J. d. Baker, & Ma. Mercedes T. Rodrigo"
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Carelessness detectors trained on Philippine students generalize to USA students without re-fitting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2017**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Detectors trained on Philippine data achieved correlations of 0.708 and 0.609 (NoScooter detector) and 0.834 and 0.788 (Scooter detector) on USA data. [→ Maria Ofelia Z. San Pedro 2014](#maria-ofelia-z-san-pedro-2014)

## Evidence

### Maria Ofelia Z. San Pedro 2014

Maria Ofelia Z. San Pedro, Ryan S. J. d. Baker, & Ma. Mercedes T. Rodrigo. (2014). Carelessness and Affect in an Intelligent Tutoring System for Mathematics. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-014-0015-y

`q2 · i?` · `associational · r2`

Generalizability test applying Philippine-trained detectors, without modification, to logs from 117 USA 6th–8th grade students (52 Scooter, 65 NoScooter). The article reports the detectors "performed quite well for all combinations of training and test conditions".

> "The detector developed on the NoScooter sample from the Philippines achieved a correlation of 0.708 to the USA NoScooter data, and a correlation of 0.609 to the USA Scooter data."

## Discussion


## Related Claims
- [Automated detectors of disengaged behaviors inferred from interaction-log data alone reached AUC over 0.8 for gaming and correlated 0.55 with observed off-task behavior](sensor-free-disengagement-detectors-accuracy.md) — related
- [Lab-trained mind wandering detectors generalize to in-the-wild lecture viewing across task, setting, and cultural group, with BiLSTM on latent features reaching F1 = 0.352](cross-dataset-generalization-mind-wandering-detection.md) — related
- [Pre-test knowledge differed significantly across the three countries, producing a country by test time interaction](pretest-differences-country-time-interaction.md) — related
