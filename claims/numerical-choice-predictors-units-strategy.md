---
type: claim
title: For numerical problems, explicit units and included solution strategy dominate prediction of student choice, with substantially better model accuracy
description: For numerical problems, explicit units and included solution strategy dominate prediction of student choice, with substantially better model accuracy
id: numerical-choice-predictors-units-strategy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: tobias-geisler-and-gerd-kortemeyer-2026
    resource: "https://doi.org/10.1103/9hh9-vt4d"
    title: "Tobias Geisler and Gerd Kortemeyer. (2026). When AI Evaluates Its Own Work: Validating Learner-Initiated, AI-Generated Physics Practice Problems. arXiv. [doi:10.1103/9hh9-vt4d](https://doi.org/10.1103/9hh9-vt4d)"
    author: Tobias Geisler and Gerd Kortemeyer
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# For numerical problems, explicit units and included solution strategy dominate prediction of student choice, with substantially better model accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the random-forest model for numerical problems, the most influential features are measurement-unit-is-clearly-stated (importance 0.364) and includes-solution-strategy (0.261), and the model achieves a test accuracy of 83.8%. [→ Tobias Geisler and Gerd Kortemeyer 2026](#tobias-geisler-and-gerd-kortemeyer-2026)

## Evidence

### Tobias Geisler and Gerd Kortemeyer 2026

Tobias Geisler and Gerd Kortemeyer. (2026). When AI Evaluates Its Own Work: Validating Learner-Initiated, AI-Generated Physics Practice Problems. arXiv. [doi:10.1103/9hh9-vt4d](https://doi.org/10.1103/9hh9-vt4d)

`q2 · i?` · `associational · r1`

Random-forest model trained on 148 numerical training samples with 37 test samples. The article reports test accuracy 83.8% and the two leading feature importances as printed; no standardized effect size.

> "It exhibits substantially better performance, achieving a test accuracy of 83.8% (5-fold CV accuracy: 0 .827 ± 0.044; OOB accuracy: 84.5%). Here, the most influential features are measurement-unit-is-clearly-stated (importance: 0.364) and includes-solution-strategy (0.261)."

## Discussion


## Related Claims
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — reports the opposite
- [For radio-button problems, cognitive-demand metrics (Bloom level, difficulty, distinct misconceptions) are the strongest random-forest predictors of student choice](radio-choice-predictors-cognitive-demand.md) — related
- [Adding in-game strategy features to pre-test features substantially improves LSTM-based stealth assessment accuracy](in-game-strategy-features-improve-prediction-over-pretest-only.md) — related
