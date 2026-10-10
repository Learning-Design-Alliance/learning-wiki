---
type: claim
title: Implicit demographic conditioning inflates AES scores in some models, with Llama-70B scores rising 1.57 points over its own default, while GPT models remain stable
description: Implicit demographic conditioning inflates AES scores in some models, with Llama-70B scores rising 1.57 points over its own default, while GPT models remain stable
id: implicit-conditioning-inflates-aes-scores-llama-70b
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
sources:
  - id: donya-rooein-2026
    resource: "https://arxiv.org/abs/2609.16993"
    title: "Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993"
    author: Donya Rooein, Luca Benedetto, Dirk Hovy
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: donya-rooein-2026-2
    resource: "https://arxiv.org/abs/2609.16993"
    title: "Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993"
    author: Donya Rooein, Luca Benedetto, Dirk Hovy
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Implicit demographic conditioning inflates AES scores in some models, with Llama-70B scores rising 1.57 points over its own default, while GPT models remain stable

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Under the implicit condition, Llama-70B essay scores inflate by +1.57 points relative to its own default (p<0.001), the largest deviation across all models and conditions. [→ Donya Rooein 2026](#donya-rooein-2026)
`q2 i?` GPT models are the most stable in AES, with no significant score shifts from explicit or implicit personas relative to human ratings. [→ Donya Rooein 2026 (2)](#donya-rooein-2026-2)

## Evidence

### Donya Rooein 2026

Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993

`q2 · i?` · `causal · r2`

Automated essay scoring experiment with paired t-tests on 40 per-essay means under three prompting conditions. Llama-70B showed the largest implicit-condition inflation; the human mean score was 3.02±1.00. The printed value is a score deviation, not a standardized effect size.

> "The Imp condition reveals the starkest effect: Llama-70B scores inflate by +1.57 points relative to its own default (p<0.001 ), the largest deviation observed across all models and conditions."

### Donya Rooein 2026 (2)

Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993

`q2 · i?` · `causal · r2`

Same AES experiment: GPT-mini and GPT-nano showed no significant score shifts from either explicit or implicit persona conditioning relative to human ratings, while several Llama and Qwen models shifted significantly (e.g., Llama-3B +0.48, p<0.01, in the Model condition).

> "In addition, GPT models are the most stable, and neither Exp nor Imp personas produce significant shifts in scores relative to human ratings."

## Discussion


## Related Claims
- [Explicitly mentioned education and SES cues lead most models to produce less readable responses for higher-education users, showing partial readability adaptation](explicit-education-cues-readability-adaptation.md) — related
