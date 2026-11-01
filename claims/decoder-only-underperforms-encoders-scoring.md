---
type: claim
title: Decoder-only (GPT-style) architectures underperform encoder-based architectures in short-answer scoring agreement with humans by a substantial margin
description: Decoder-only (GPT-style) architectures underperform encoder-based architectures in short-answer scoring agreement with humans by a substantial margin
id: decoder-only-underperforms-encoders-scoring
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

# Decoder-only (GPT-style) architectures underperform encoder-based architectures in short-answer scoring agreement with humans by a substantial margin

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the Bayesian specification, the gpt indicator is negative (posterior mean ≈ -0.39, 95% credible interval excluding 0), indicating decoder-only architectures lag encoder-based ones in QWK agreement. [→ Michael Hardy 2026](#michael-hardy-2026)

## Evidence

### Michael Hardy 2026

Michael Hardy. (2026). Autoscoring Anticlimax: A Meta-analytic Understanding of AI's Short-answer Shortcomings and Wording Weaknesses. https://arxiv.org/abs/2603.04820

`q2 · i?` · `quant-synthesis · r2`

Bayesian re-estimation of the maximal item-varying random-effects meta-regression on 890 QWK observations. The gpt coefficient is "negative in the Bayesian specification (posterior mean≈−0.39 , with the 95% credible interval excluding 0 in the provided fit)". The abstract states decoders underperform encoders by 0.37.

> "The gpt coefficient is negative in the Bayesian specification (posterior mean≈−0.39 , with the 95% credible interval excluding 0 in the provided fit). This result links an architectural propensity—autoregressive generation optimized for fluent continuation—to a reliability-style evaluation criterion."

## Discussion


## Related Claims
- [Mid-range degradation is conditioned on task-specific adaptation: it is most severe for few-shot LLMs with few examples, decreases with more task-specific data, and is mildest for the fine-tuned encoder](task-specific-adaptation-conditions-mid-range-degradation.md) — related
- [LLMs cannot effectively perform in-context learning for short answer scoring, but cross-prompt pre-finetuning substantially boosts their zero-shot performance](llm-icl-insufficient-prefinetuning-boosts-zero-shot.md) — related
- [Human-perceived item difficulty (human-human QWK) does not reliably predict LLM scoring difficulty on the same items](human-difficulty-does-not-predict-llm-difficulty.md) — related
- [Item-by-implementation instability is substantial: a model can be reliable on some items and unreliable on others, varying across studies and training regimes](item-implementation-instability-scoring.md) — related
