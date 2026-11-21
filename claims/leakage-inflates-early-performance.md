---
type: claim
title: Temporal leakage, especially through post-cutoff assessment information, severely inflates apparent early-warning performance at early cutoffs
description: Temporal leakage, especially through post-cutoff assessment information, severely inflates apparent early-warning performance at early cutoffs
id: leakage-inflates-early-performance
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

# Temporal leakage, especially through post-cutoff assessment information, severely inflates apparent early-warning performance at early cutoffs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` At t=7, leaky variants raise RF ROC-AUC from 0.7151 (strict) to 0.9669 (Leaky-All) and GBDT from 0.7147 to 0.9704; assessment leakage alone lifts RF to 0.9616. [→ Ngoc Luyen Lê 2026](#ngoc-luyen-le-2026)

## Evidence

### Ngoc Luyen Lê 2026

Ngoc Luyen Lê, Marie-Hélène Abel, and Bertrand Laforge. (2026). When Can We Trust Early Warnings? Leakage-Excluded Early Outcome Prediction from LMS Interaction Logs. arXiv preprint. [doi:10.1007/978-3-032-31660-8_11](https://doi.org/10.1007/978-3-032-31660-8_11)

`q2 · i?` · `design · r2`

Leakage-ablation experiment on OULAD comparing strict LEAP with intentionally leaky diagnostic variants; the article reports "RF increases from ROC-AUC0.7151 (Strict) to0.9669(Leaky-All)". No effect size is printed.

> "Att=7, RF increases from ROC-AUC0.7151 (Strict) to0.9669(Leaky-All), and GBDT increases from0.7147to0.9704."

## Discussion


## Related Claims
- [Random Forest performs best at the earliest cutoffs (days 7 and 14) while Gradient Boosting dominates from day 21 onward on OULAD under strict LEAP](leap-model-rankings-by-cutoff.md) — related
- [Under strict early availability, the predictive signal shifts from behavioral engagement at early cutoffs toward assessment evidence by the end of the course](predictive-signal-shift-engagement-to-assessment.md) — related
- [The largest single gain in best ROC-AUC under strict LEAP occurs between day 14 and day 21, indicating week 3 adds substantial predictive evidence](leap-week-3-gain.md) — related
