---
type: claim
title: The largest single gain in best ROC-AUC under strict LEAP occurs between day 14 and day 21, indicating week 3 adds substantial predictive evidence
description: The largest single gain in best ROC-AUC under strict LEAP occurs between day 14 and day 21, indicating week 3 adds substantial predictive evidence
id: leap-week-3-gain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: ngoc-luyen-lê-2026
    resource: "https://doi.org/10.1007/978-3-032-31660-8_11"
    title: "Ngoc Luyen Lê, Marie-Hélène Abel, and Bertrand Laforge. (2026). When Can We Trust Early Warnings? Leakage-Excluded Early Outcome Prediction from LMS Interaction Logs. arXiv preprint. [doi:10.1007/978-3-032-31660-8_11](https://doi.org/10.1007/978-3-032-31660-8_11)"
    author: Ngoc Luyen Lê, Marie-Hélène Abel, and Bertrand Laforge
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The largest single gain in best ROC-AUC under strict LEAP occurs between day 14 and day 21, indicating week 3 adds substantial predictive evidence

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Best ROC-AUC jumps from 0.7404 at t=14 to 0.7851 at t=21 (+0.0447), the largest single improvement across cutoffs. [→ Ngoc Luyen Lê 2026](#ngoc-luyen-le-2026)

## Evidence

### Ngoc Luyen Lê 2026

Ngoc Luyen Lê, Marie-Hélène Abel, and Bertrand Laforge. (2026). When Can We Trust Early Warnings? Leakage-Excluded Early Outcome Prediction from LMS Interaction Logs. arXiv preprint. [doi:10.1007/978-3-032-31660-8_11](https://doi.org/10.1007/978-3-032-31660-8_11)

`q2 · i?` · `design · r2`

Numerical cutoff-by-cutoff benchmark on OULAD under strict LEAP; the article reports the change point "betweent=14andt=21(from0.7404to0.7851, i.e.,+0.0447)". No effect size is printed.

> "The largest single improve- ment in best ROC-AUC occurs betweent=14andt=21(from0.7404to0.7851, i.e.,+0.0447), suggesting that week 3 provides a substantial increase in predic- tive evidence beyond the first two weeks."

## Discussion


## Related Claims
- [Random Forest performs best at the earliest cutoffs (days 7 and 14) while Gradient Boosting dominates from day 21 onward on OULAD under strict LEAP](leap-model-rankings-by-cutoff.md) — related
- [Temporal leakage, especially through post-cutoff assessment information, severely inflates apparent early-warning performance at early cutoffs](leakage-inflates-early-performance.md) — related
