---
type: claim
title: Ordinary least products calibration of ASR output lowers error in CDS measures, with adult word counts comparable to LENA-level performance
description: Ordinary least products calibration of ASR output lowers error in CDS measures, with adult word counts comparable to LENA-level performance
id: olp-calibration-cds-measures
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-08
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: gonzalez-villasanti-2020
    resource: "https://doi.org/10.1371/journal.pone.0242511"
    title: "Gonzalez Villasanti, H., Justice, L. M., Chaparro-Moreno, L. J., Lin, T.-J., & Purtell, K. (2020). Automatized analysis of children's exposure to child-directed speech in preschool settings: Validation and application. PLoS ONE, 15(11), e0242511. https://doi.org/10.1371/journal.pone.0242511"
    author: "Gonzalez Villasanti, H., Justice, L. M., Chaparro-Moreno, L. J., Lin, T.-J., & Purtell, K."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: gonzalez-villasanti-2020-2
    resource: "https://doi.org/10.1371/journal.pone.0242511"
    title: "Gonzalez Villasanti, H., Justice, L. M., Chaparro-Moreno, L. J., Lin, T.-J., & Purtell, K. (2020). Automatized analysis of children's exposure to child-directed speech in preschool settings: Validation and application. PLoS ONE, 15(11), e0242511. https://doi.org/10.1371/journal.pone.0242511"
    author: "Gonzalez Villasanti, H., Justice, L. M., Chaparro-Moreno, L. J., Lin, T.-J., & Purtell, K."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Ordinary least products calibration of ASR output lowers error in CDS measures, with adult word counts comparable to LENA-level performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Adapting raw ASR measures with OLP regression as part of the LOSO loop reduced median absolute relative error across CDS measures for adult, peer, and focal-child speech. [→ Gonzalez Villasanti 2020](#gonzalez-villasanti-2020)
`q2 i?` For adapted adult TNW the system obtained MRE of -1.8%, within the error range reported for other automatic word-count tools in early childhood settings. [→ Gonzalez Villasanti 2020 (2)](#gonzalez-villasanti-2020-2)

## Evidence

### Gonzalez Villasanti 2020

Gonzalez Villasanti, H., Justice, L. M., Chaparro-Moreno, L. J., Lin, T.-J., & Purtell, K. (2020). Automatized analysis of children's exposure to child-directed speech in preschool settings: Validation and application. PLoS ONE, 15(11), e0242511. https://doi.org/10.1371/journal.pone.0242511

`q2 · i?` · `design · r2`

LOSO cross-validation of the CDS measurement system on the 13-child corpus, comparing raw versus OLP-adapted ASR measures in Table 2; the adapted results show "lower mARE compared to raw measures". Error metrics only; no effect size printed.

> "The LOSO performance using the OLP adaptation is also shown in Table 2, showing lower mARE compared to raw measures."

### Gonzalez Villasanti 2020 (2)

Gonzalez Villasanti, H., Justice, L. M., Chaparro-Moreno, L. J., Lin, T.-J., & Purtell, K. (2020). Automatized analysis of children's exposure to child-directed speech in preschool settings: Validation and application. PLoS ONE, 15(11), e0242511. https://doi.org/10.1371/journal.pone.0242511

`q2 · i?` · `design · r2`

Comparison of adapted CIDR mean relative errors against LENA benchmarks reported in prior reviews; adult TNW MRE was -1.8% and focal child TNW MRE was -16.1%. The article states the adult result is adequate; focal-child correlation remained lower than LENA averages.

> "For our adapted results, we obtained MRE for adult TNW of -1.8%, and -16.1% for focal child TNW."

## Discussion


## Related Claims
- [ASR accuracy for children's speech improves with child age (r = -0.44 between age and word-count error)](asr-child-speech-improves-with-age.md) — related
- [Adult talk to children is higher during structured morning center time, while peer and child talk are higher during unstructured afternoon free play](classroom-task-shapes-cds-source.md) — related
- [LENA automated adult word counts are reliable for Spanish-language home environments](lena-adult-word-estimates-reliable-spanish.md) — related
