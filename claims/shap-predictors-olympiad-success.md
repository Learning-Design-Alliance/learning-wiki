---
type: claim
title: Mathematics skills are the dominant positive predictor of first-round success, while conventional vocational interests negatively predict success
description: Mathematics skills are the dominant positive predictor of first-round success, while conventional vocational interests negatively predict success
id: shap-predictors-olympiad-success
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: tschisgale-2026
    resource: "https://doi.org/10.48550/arXiv.2609.35151"
    title: "Tschisgale, P., & Neumann, K. (2026). “What If I Had Participated?”—A Machine Learning-Based Counterfactual Analysis of Non-Participants’ Success Potential in STEM Competitions: The Case of the German Physics Olympiad. Leibniz Institute for Science and Mathematics Education (IPN), Kiel, Germany. [doi:10.48550/arXiv.2609.35151](https://doi.org/10.48550/arXiv.2609.35151)"
    author: "Tschisgale, P., & Neumann, K."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Mathematics skills are the dominant positive predictor of first-round success, while conventional vocational interests negatively predict success

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` SHAP analysis of the final elastic net model identified mathematics skills as the dominant predictor, with high scores shifting predicted success upward and low scores downward; RIASEC-Conventional showed a negative direction. [→ Tschisgale 2026](#tschisgale-2026)

## Evidence

### Tschisgale 2026

Tschisgale, P., & Neumann, K. (2026). “What If I Had Participated?”—A Machine Learning-Based Counterfactual Analysis of Non-Participants’ Success Potential in STEM Competitions: The Case of the German Physics Olympiad. Leibniz Institute for Science and Mathematics Education (IPN), Kiel, Germany. [doi:10.48550/arXiv.2609.35151](https://doi.org/10.48550/arXiv.2609.35151)

`q2 · i?` · `associational · r2`

A SHAP analysis on the participant sample decomposed predictions of the final elastic net model. Mathematics skills showed the largest spread (approximately −0.18 to +0.28 in predicted-probability units) with a "clean monotonic pattern"; RIASEC-Conventional was negative, and physics/engineering-related skills ranged approximately −0.11 to +0.10. Subject interest in physics had essentially no practical effect.

> "The SHAP analysis revealed mathematics skills as the dominant predictor, accounting for by far the largest spread of SHAP values, ranging from approximately −0.18 to +0.28 in predicted-probability units, with a clean monotonic pattern"

## Discussion


## Related Claims
- [Elastic net logistic regression performs comparably to random forest and gradient boosting in predicting first-round Physics Olympiad success and is selected as the final model](elastic-net-comparable-performance-olympiad-success.md) — related
- [SHAP analysis identifies undergraduate GPA rank as the most influential predictor, followed by gender, confidence, undergraduate score average, and CET-4 performance](shap-undergrad-gpa-rank-strongest-predictor.md) — related
- [Physics Olympiad participants differ most strongly from non-participants (|d| ≥ 1.0) in STEM-related skills, physics-specific motivational-affective variables, and physics and mathematics self-concept](descriptive-group-differences-olympiad-participants.md) — related
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — related
