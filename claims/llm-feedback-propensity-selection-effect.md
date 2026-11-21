---
type: claim
title: "Learners' propensity to request LLM feedback is positively associated with posttest scores, indicating a self-selection effect"
description: "Learners' propensity to request LLM feedback is positively associated with posttest scores, indicating a self-selection effect"
id: llm-feedback-propensity-selection-effect
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: thomas-2025
    resource: "https://doi.org/10.1007/978-3-032-03870-8_33"
    title: "Thomas, D. R., Borchers, C., Bhushan, S., Gatz, E., Gupta, S., & Koedinger, K. R. (2025). LLM-Generated Feedback Supports Learning If Learners Choose to Use It. arXiv. [doi:10.1007/978-3-032-03870-8_33](https://doi.org/10.1007/978-3-032-03870-8_33)"
    author: "Thomas, D. R., Borchers, C., Bhushan, S., Gatz, E., Gupta, S., & Koedinger, K. R."
    q: 3
    i: 0
    kind: causal
    rigour: 2
---

# Learners' propensity to request LLM feedback is positively associated with posttest scores, indicating a self-selection effect

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3` · `i0` negligible
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i0` The control condition's predicted propensity to request LLM feedback was positively associated with posttest scores (β = 0.06, p = .040), and the ITT-by-propensity interaction was positive but non-significant (β = 0.04, p = .307). [→ Thomas 2025](#thomas-2025)

## Evidence

### Thomas 2025

Thomas, D. R., Borchers, C., Bhushan, S., Gatz, E., Gupta, S., & Koedinger, K. R. (2025). LLM-Generated Feedback Supports Learning If Learners Choose to Use It. arXiv. [doi:10.1007/978-3-032-03870-8_33](https://doi.org/10.1007/978-3-032-03870-8_33)

`q3 · i0` · `causal · r2`

Linear mixed model adjusting for predicted feedback propensity (ElasticNet regression, 10-fold cross-validation, ROC-AUC M = 0.75) on the randomized within-subject tutor data. The quote prints "β = 0.06, 95% CI [0.00, 0.12], p = .040" — a small standardized coefficient below 0.2.

> "The model (Table 2) revealed a significant selection effect, where the Control condition’s predicted propensity to request LLM feedback was positively associated with posttest scores (β = 0.06, 95% CI [0.00, 0.12], p = .040)."

## Discussion


## Related Claims
- [After propensity adjustment, only two of seven lessons show statistically significant learning benefits from LLM feedback (β = 0.33 and β = 0.28)](llm-feedback-lesson-heterogeneity.md) — related
- [Mere assignment of LLM feedback availability (ITT) did not significantly improve posttest performance](itt-availability-no-significant-effect.md) — related
