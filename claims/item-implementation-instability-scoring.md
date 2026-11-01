---
type: claim
title: "Item-by-implementation instability is substantial: a model can be reliable on some items and unreliable on others, varying across studies and training regimes"
description: "Item-by-implementation instability is substantial: a model can be reliable on some items and unreliable on others, varying across studies and training regimes"
id: item-implementation-instability-scoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: michael-hardy-2026
    resource: "https://arxiv.org/abs/2603.04820"
    title: "Michael Hardy. (2026). Autoscoring Anticlimax: A Meta-analytic Understanding of AI's Short-answer Shortcomings and Wording Weaknesses. https://arxiv.org/abs/2603.04820"
    author: Michael Hardy
    q: 2
    i: "?"
    kind: quant-synthesis
    rigour: 2
---

# Item-by-implementation instability is substantial: a model can be reliable on some items and unreliable on others, varying across studies and training regimes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Item-varying random effects reveal that scoring reliability varies substantially across items within the same model, study, and training regime; study- and training-level item-deviation standard deviations are often larger than model-level ones. [→ Michael Hardy 2026](#michael-hardy-2026)

## Evidence

### Michael Hardy 2026

Michael Hardy. (2026). Autoscoring Anticlimax: A Meta-analytic Understanding of AI's Short-answer Shortcomings and Wording Weaknesses. https://arxiv.org/abs/2603.04820

`q2 · i?` · `quant-synthesis · r2`

Bayesian fit of the maximal item-varying random-effects specification on 890 QWK observations. The article reports "the study- and training-level item-deviation standard deviations are often larger than the model-level ones for several items". No effect size is printed.

> "In the Bayesian fit, the study- and training-level item-deviation standard deviations are often larger than the model-level ones for several items, consistent with the idea that dataset construction, annotation design, and fine-tuning/prompting choices can dominate architecture in determining reliability."

## Discussion


## Related Claims
- [Decoder-only (GPT-style) architectures underperform encoder-based architectures in short-answer scoring agreement with humans by a substantial margin](decoder-only-underperforms-encoders-scoring.md) — related
- [State interviewees raised three equity concerns about performance-based assessments: perceived lower rigor and tracking, uneven implementation quality, and inequitable or unreliable scoring](equity-concerns-performance-based-assessments.md) — related
