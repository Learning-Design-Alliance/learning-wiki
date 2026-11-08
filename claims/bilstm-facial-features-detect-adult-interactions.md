---
type: claim
title: "A BILSTM classifier using facial features and speech activity detects preschool children's interactions with adults with 81.1% accuracy under leave-one-subject-out validation"
description: "A BILSTM classifier using facial features and speech activity detects preschool children's interactions with adults with 81.1% accuracy under leave-one-subject-out validation"
id: bilstm-facial-features-detect-adult-interactions
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

# A BILSTM classifier using facial features and speech activity detects preschool children's interactions with adults with 81.1% accuracy under leave-one-subject-out validation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The full-feature BILSTM classifier trained with facial features and speech activity predicted children's interactions with adults more accurately (81.1% accuracy, F1 88.1) than a reduced-feature detector (80.8% accuracy, F1 87.6). [→ Gonzalez Villasanti 2020](#gonzalez-villasanti-2020)

## Evidence

### Gonzalez Villasanti 2020

Gonzalez Villasanti, H., Justice, L. M., Chaparro-Moreno, L. J., Lin, T.-J., & Purtell, K. (2020). Automatized analysis of children's exposure to child-directed speech in preschool settings: Validation and application. PLoS ONE, 15(11), e0242511. https://doi.org/10.1371/journal.pone.0242511

`q2 · i?` · `design · r2`

LOSO cross-validation of interaction detectors on Fall AM first-person video from 13 children, with manually coded interactions as reference. The full-feature model "achieves higher accuracy and F1 score (81.1 and 88.1, respectively)" than the reduced-feature model. No effect size is printed.

> "For the adult interaction detector, results show that the supervised full BILSTM classifier, trained with full facial features, achieves higher accuracy and F1 score (81.1 and 88.1, respectively) compared to the reduced feature detector (80.8 and 87.6, respectively)."

## Discussion


## Related Claims
- [For peer interactions, a reduced-feature BILSTM using face size and speech activity achieves higher accuracy (86.1%) than the full-feature classifier](reduced-features-bilstm-peer-interactions.md) — related
