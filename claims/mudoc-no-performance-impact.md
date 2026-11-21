---
type: claim
title: Multimodal AI responses show no significant impact on problem-solving performance compared with text-only responses
description: Multimodal AI responses show no significant impact on problem-solving performance compared with text-only responses
id: mudoc-no-performance-impact
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: karan-taneja-2025
    resource: "https://doi.org/10.1007/978-3-031-98462-4_12"
    title: "Karan Taneja, Anjali Singh, and Ashok K. Goel. (2025). Towards a Multimodal Document-grounded Conversational AI System for Education. [doi:10.1007/978-3-031-98462-4_12](https://doi.org/10.1007/978-3-031-98462-4_12)"
    author: Karan Taneja, Anjali Singh, and Ashok K. Goel
    q: 3
    i: "?"
    kind: causal
    rigour: 1
---

# Multimodal AI responses show no significant impact on problem-solving performance compared with text-only responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` A linear mixed-effects model found system type did not affect rubric-scored problem-solving performance; MuDoC had a small but insignificant negative impact (β=-0.350). [→ Karan Taneja 2025](#karan-taneja-2025)

## Evidence

### Karan Taneja 2025

Karan Taneja, Anjali Singh, and Ashok K. Goel. (2025). Towards a Multimodal Document-grounded Conversational AI System for Education. [doi:10.1007/978-3-031-98462-4_12](https://doi.org/10.1007/978-3-031-98462-4_12)

`q3 · i?` · `causal · r1`

Linear mixed-effects model (Python statsmodels) of solution scores (0-12) with system and problem as fixed effects and participant random intercept, scored by the first author and a teaching assistant. The ANA problem also produced a significant decrease (ˆβ=-1.150, p=0.034).

> "Based on this model, we observe that the system did not impact the scores, MuDoC had a small but insignificant negative impact on student scores (ˆβ=-0.350, SE=0.542, p=0.518)."

## Discussion


## Related Claims
- [Learners prefer a multimodal document-grounded AI system over a text-only variant for engagement, interest and memorability in problem-solving while learning](mudoc-preferred-engagement-memorability.md) — related
- [Solving the easier problem (INC) with the multimodal system produced more favorable engagement, memorability and confidence ratings than solving the harder problem (ANA) with it](problem-order-effect-mudoc-ratings.md) — related
- [Document-grounded conversational AI with interleaved text-and-image responses (MuDoC) yields significantly higher post-test scores than a text-only conversational AI (TexDoC) in a visually rich STEM topic](mudoc-higher-posttest-than-texdoc.md) — reports the opposite
