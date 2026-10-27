---
type: claim
title: "In classroom video labeling, high raw agreement (often exceeding 90%) co-occurred with low chance-corrected κ due to temporal misalignment"
description: "In classroom video labeling, high raw agreement (often exceeding 90%) co-occurred with low chance-corrected κ due to temporal misalignment"
id: raw-agreement-kappa-paradox-classroom-video
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: thomas-2026
    resource: "https://doi.org/10.48550/arxiv.2603.29141"
    title: "Thomas, D.R., Borchers, C., Vanacore, K.P., Koedinger, K.R., & Kizilcec, R.F. (2026). Modernizing Ground Truth: Four Shifts Toward Improving Reliability and Validity in AI in Education. https://arxiv.org/abs/2603.29141 [doi:10.48550/arxiv.2603.29141](https://doi.org/10.48550/arxiv.2603.29141)"
    author: "Thomas, D.R., Borchers, C., Vanacore, K.P., Koedinger, K.R., & Kizilcec, R.F."
    q: 2
    i: "?"
    kind: theoretical
    rigour: 2
---

# In classroom video labeling, high raw agreement (often exceeding 90%) co-occurred with low chance-corrected κ due to temporal misalignment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Researchers found a significant discrepancy between high raw agreement scores and low chance-corrected κ scores for instructional activity labels in classroom videos, attributed to the timed-event nature of the data. [→ Thomas 2026](#thomas-2026)

## Evidence

### Thomas 2026

Thomas, D.R., Borchers, C., Vanacore, K.P., Koedinger, K.R., & Kizilcec, R.F. (2026). Modernizing Ground Truth: Four Shifts Toward Improving Reliability and Validity in AI in Education. https://arxiv.org/abs/2603.29141 [doi:10.48550/arxiv.2603.29141](https://doi.org/10.48550/arxiv.2603.29141)

`q2 · i?` · `theoretical · r2`

The article reports, citing prior work, that raw agreement often exceeded 90% while chance-corrected κ was low for instructional activity labels in classroom videos. The authors attribute the paradox to slight temporal misalignments deflating κ despite conceptual consensus.

> "researchers found a significant discrepancy between high raw agreement scores (often exceeding 90%) and low chance-corrected κ scores for instructional activity labels in classroom videos [14]"

## Discussion


## Related Claims

- [Instructor co-designed tagging transforms raw LMS log data into structured event data reflecting course design and temporal context](clickstream-tagging-transforms-logs-into-contextualized-events.md) — related
- [Model and prompt choice account for only a small share of misalignment error, which concentrates in transcript-conditioned higher-order interactions](variance-decomposition-model-prompt-weak-levers.md) — related
- [Classroom events occur at different time scales requiring different modes of cognition](time-scales-require-different-modes-of-cognition.md)
- [Automated essay scoring can achieve high agreement with human raters but faces calibration constraints](aes-high-agreement-calibration-constraint.md) — related
- [Adding regex-based rules to few-shot LLM labeling improves agreement with human annotation (0.818 to 0.852 overall)](regex-rules-improve-fewshot-llm-labeling-accuracy.md) — related
- [On CK items, GradeOpt showed near-perfect alignment with human codes (κ = .88 and .85; QWK = .89 and .94), comparable to human–human agreement](gradeopt-near-perfect-ck-agreement.md) — related
- [Human–GPT coding agreement varied sharply by code, with near-chance or negative Kappa for co-ordination codes despite near-perfect agreement on others](gpt4-kappa-varies-by-dialogue-code.md) — related
- [The rule-based recipe annotation system reaches near-perfect inter-annotator agreement (Cohen's Kappa 0.85) and average accuracy 0.95 in a validation on sampled recipe segments.](relex-annotation-validation-kappa-accuracy.md) — related
- [Lower model performance on Prompt 2 tracks poor inter-annotator agreement (QWK 0.560 vs 0.758)](prompt2-low-performance-tracks-annotator-agreement.md) — related
