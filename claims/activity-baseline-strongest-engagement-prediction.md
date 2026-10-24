---
type: claim
title: For activity-defined engagement prediction in DTA logs, the activity-only Baseline remained strongest, and permutation importance was dominated by activity indicators
description: For activity-defined engagement prediction in DTA logs, the activity-only Baseline remained strongest, and permutation importance was dominated by activity indicators
id: activity-baseline-strongest-engagement-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: wang-s-and-zhao-j-2026
    title: Wang S and Zhao J 2026
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# For activity-defined engagement prediction in DTA logs, the activity-only Baseline remained strongest, and permutation importance was dominated by activity indicators

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For activity_deﬁned_engagement, the Baseline model was strongest across held-out metrics, and none of the augmented feature sets materially improved it, reflecting overlap between predictors and the outcome definition. [→ Wang S and Zhao J 2026](#wang-s-and-zhao-j-2026)

## Evidence

### Wang S and Zhao J 2026

Wang S and Zhao J (2026) Reflective AI use and student engagement in AI-supported programming: technology acceptance, programming self-efficacy, and behavioral trace evidence. Front. Psychol. 17:1929887. https://doi.org/10.3389/fpsyg.2026.1929887

`q2 · i?` · `associational · r2`

Held-out comparison on the DTA dataset for the activity-defined engagement target, constructed as the mean of standardized activity indicators with students at or above the 67th percentile labeled positive. The article reports "Foractivity_deﬁned_engagement, the Baseline model was strongest across the held-out metrics"; repeated cross-validation produced almost identical ROC-AUC values across configurations. The article notes the label is not an independent psychological criterion.

> "Foractivity_deﬁned_engagement, the Baseline model was strongest across the held-out metrics, as expected from the overlap between its predictors and the outcomedeﬁnition."

## Discussion


## Related Claims
- [Recovery-related behavioral features add only a small, unstable held-out Macro-F1 gain for final-success prediction in DTA logs (0.725 to 0.743), with negligible average window-sensitivity differences](dta-recovery-features-small-unstable-gain.md) — related
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — reports the opposite
