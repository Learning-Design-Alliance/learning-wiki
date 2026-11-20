---
type: claim
title: "HyperOpt tuning also improves predictions of target students' performance on unseen later problems (temporal cross-validation)"
description: "HyperOpt tuning also improves predictions of target students' performance on unseen later problems (temporal cross-validation)"
id: tuned-agents-better-unseen-data
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: christopher-james-maclellan-2024
    resource: "https://doi.org/10.48550/arXiv.2408.13684"
    title: "Christopher James MacLellan, Kimberly Stowers, Lisa Brady. (2024). Evaluating Alternative Training Interventions Using Personalized Computational Models of Learning. Advances in Cognitive Systems, 10. Originally published 2022. [doi:10.48550/arXiv.2408.13684](https://doi.org/10.48550/arXiv.2408.13684)"
    author: Christopher James MacLellan, Kimberly Stowers, Lisa Brady
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# HyperOpt tuning also improves predictions of target students' performance on unseen later problems (temporal cross-validation)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Tuned agents predict target students' behavior better than the baseline on problems 6 through 20, which were not used in tuning. [→ Christopher James MacLellan 2024](#christopher-james-maclellan-2024)

## Evidence

### Christopher James MacLellan 2024

Christopher James MacLellan, Kimberly Stowers, Lisa Brady. (2024). Evaluating Alternative Training Interventions Using Personalized Computational Models of Learning. Advances in Cognitive Systems, 10. Originally published 2022. [doi:10.48550/arXiv.2408.13684](https://doi.org/10.48550/arXiv.2408.13684)

`q2 · i?` · `design · r2`

Temporal cross-validation: models tuned for 15 students on their first five problems, then compared to the baseline on the next 15 unseen problems; Figure 4(b) reports the comparison. No effect size printed.

> "We find that tuning also yields better predictions on unseen data that were not used for that purpose."

## Discussion


## Related Claims
- [Tuning Apprentice Learner agents to individual students with HyperOpt reduces prediction error relative to a generic baseline on the tutor problems used for tuning](hyperopt-tuned-agents-lower-error-same-data.md) — a broader claim this one bears on
- [Under causally valid, tuned settings, code-level embeddings do not consistently improve performance: rectified Code-DKT underperforms tuned DKT on several assignments, while ECKT remains competitive](code-embeddings-inconsistent-under-rectified-settings.md) — related
