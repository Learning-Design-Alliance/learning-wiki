---
type: claim
title: "For peer interactions, a reduced-feature BILSTM using face size and speech activity achieves higher accuracy (86.1%) than the full-feature classifier"
description: "For peer interactions, a reduced-feature BILSTM using face size and speech activity achieves higher accuracy (86.1%) than the full-feature classifier"
id: reduced-features-bilstm-peer-interactions
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
---

# For peer interactions, a reduced-feature BILSTM using face size and speech activity achieves higher accuracy (86.1%) than the full-feature classifier

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For detecting children's interactions with peers, the reduced-feature detector obtained higher accuracy and F1 (86.1 and 92.3) than the full-feature detector (85.1 and 91.7). [→ Gonzalez Villasanti 2020](#gonzalez-villasanti-2020)

## Evidence

### Gonzalez Villasanti 2020

Gonzalez Villasanti, H., Justice, L. M., Chaparro-Moreno, L. J., Lin, T.-J., & Purtell, K. (2020). Automatized analysis of children's exposure to child-directed speech in preschool settings: Validation and application. PLoS ONE, 15(11), e0242511. https://doi.org/10.1371/journal.pone.0242511

`q2 · i?` · `design · r2`

LOSO cross-validation results (Table 1) for the peer interaction detector on the same 13-child Fall AM corpus; the reduced-feature model, mimicking indoor positioning sensors, outperformed the full-feature model. Accuracy metrics only; no effect size printed.

> "For the peer interaction detectors, the reduced features detector obtains higher accuracy and F1 score (86.1 and 92.3, respectively) than the detector trained with full features (85.1 and 91.7, respectively)."

## Discussion


## Related Claims
- [A BILSTM classifier using facial features and speech activity detects preschool children's interactions with adults with 81.1% accuracy under leave-one-subject-out validation](bilstm-facial-features-detect-adult-interactions.md) — related
