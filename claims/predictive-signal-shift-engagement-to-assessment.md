---
type: claim
title: Under strict early availability, the predictive signal shifts from behavioral engagement at early cutoffs toward assessment evidence by the end of the course
description: Under strict early availability, the predictive signal shifts from behavioral engagement at early cutoffs toward assessment evidence by the end of the course
id: predictive-signal-shift-engagement-to-assessment
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
    kind: associational
    rigour: 2
---

# Under strict early availability, the predictive signal shifts from behavioral engagement at early cutoffs toward assessment evidence by the end of the course

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` At t=7 engagement features dominate (total_clicks_t top for GBDT, importance ≈0.57); by t=56 assessment performance leads (avg_score_t importance ≈0.62 for GBDT, ≈0.33 for RF). [→ Ngoc Luyen Lê 2026](#ngoc-luyen-le-2026)

## Evidence

### Ngoc Luyen Lê 2026

Ngoc Luyen Lê, Marie-Hélène Abel, and Bertrand Laforge. (2026). When Can We Trust Early Warnings? Leakage-Excluded Early Outcome Prediction from LMS Interaction Logs. arXiv preprint. [doi:10.1007/978-3-032-31660-8_11](https://doi.org/10.1007/978-3-032-31660-8_11)

`q2 · i?` · `associational · r2`

Feature-importance and linear-coefficient analysis across cutoffs on OULAD under strict LEAP; the article reports "total_clicks_tis the top feature for GBDT with importance≈0.57" at t=7. No effect size is printed.

> "Att=7, engagement volume and activity regularity are most influential; for ex- ample,total_clicks_tis the top feature for GBDT with importance≈0.57."

## Discussion


## Related Claims
- [Temporal leakage, especially through post-cutoff assessment information, severely inflates apparent early-warning performance at early cutoffs](leakage-inflates-early-performance.md) — related
- [Random Forest performs best at the earliest cutoffs (days 7 and 14) while Gradient Boosting dominates from day 21 onward on OULAD under strict LEAP](leap-model-rankings-by-cutoff.md) — related
- [In an AI-based early warning system, the predictive importance of CAM dimensions shifted over an instructional unit, with affect/metacognition self-reports leading early and cognitive artifacts gaining accuracy toward the end](early-warning-system-cam-predictive-importance-shifts-over-unit.md) — a broader claim this one bears on
