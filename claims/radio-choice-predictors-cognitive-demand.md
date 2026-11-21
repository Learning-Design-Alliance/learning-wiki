---
type: claim
title: For radio-button problems, cognitive-demand metrics (Bloom level, difficulty, distinct misconceptions) are the strongest random-forest predictors of student choice
description: For radio-button problems, cognitive-demand metrics (Bloom level, difficulty, distinct misconceptions) are the strongest random-forest predictors of student choice
id: radio-choice-predictors-cognitive-demand
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

# For radio-button problems, cognitive-demand metrics (Bloom level, difficulty, distinct misconceptions) are the strongest random-forest predictors of student choice

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the random-forest model for 1-out-of-N multiple-choice problems, the three most influential predictors of student choice are bloom-level-of-exercise (0.138), exercise-difficulty-level (0.137), and distinct-misconceptions (0.108). [→ Tobias Geisler and Gerd Kortemeyer 2026](#tobias-geisler-and-gerd-kortemeyer-2026)

## Evidence

### Tobias Geisler and Gerd Kortemeyer 2026

Tobias Geisler and Gerd Kortemeyer. (2026). When AI Evaluates Its Own Work: Validating Learner-Initiated, AI-Generated Physics Practice Problems. arXiv. [doi:10.1103/9hh9-vt4d](https://doi.org/10.1103/9hh9-vt4d)

`q2 · i?` · `associational · r1`

Random-forest model trained on 224 radio-button training samples with 56 test samples; the article reports a test accuracy of 58.9% (OOB 57.6%). Feature importances as printed; no standardized effect size.

> "Its three most influential predictors are bloom-level-of-exercise (importance: 0.138), exercise-difficulty-level (0.137), and the domain-specific metric distinct-misconceptions (0.108)."

## Discussion


## Related Claims
- [Student choice correlates positively with solution-strategy hints and cognitive-depth metrics, and radio problem type is a negative hub against Cluster A](choice-correlates-with-strategy-and-depth.md) — related
- [For numerical problems, explicit units and included solution strategy dominate prediction of student choice, with substantially better model accuracy](numerical-choice-predictors-units-strategy.md) — related
- [Core problem-statement metrics show only moderate judge agreement, and multi-class metrics (Bloom level, difficulty) perform poorly](problem-statement-metrics-moderate-categorical-poor.md) — related
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — a broader claim this one bears on
