---
type: claim
title: The small open-weights Qwen2.5-1.5B model is the weakest arm in both languages, with Spanish thematic weighted F1 of 0.31 zero-shot rising to 0.63 with few-shot
description: The small open-weights Qwen2.5-1.5B model is the weakest arm in both languages, with Spanish thematic weighted F1 of 0.31 zero-shot rising to 0.63 with few-shot
id: qwen-15b-weakest-arm-fewshot-recovers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: esteban-u-vega-barajas-2026
    resource: "https://doi.org/10.48550/arxiv.2607.11873"
    title: "Esteban U. Vega Barajas. (2026). A Durability and Cross-Language Transfer Benchmark for a Validated Teaching-Feedback Classification Protocol. https://arxiv.org/abs/2607.11873 [doi:10.48550/arxiv.2607.11873](https://doi.org/10.48550/arxiv.2607.11873)"
    author: Esteban U. Vega Barajas
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The small open-weights Qwen2.5-1.5B model is the weakest arm in both languages, with Spanish thematic weighted F1 of 0.31 zero-shot rising to 0.63 with few-shot

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` The open-weights Qwen2.5-1.5B arm is weakest on both languages; on Spanish four-class thematic classification, zero-shot wF1 is 0.31 and rises to 0.63 with few-shot examples. [→ Esteban U. Vega Barajas 2026](#esteban-u-vega-barajas-2026)

## Evidence

### Esteban U. Vega Barajas 2026

Esteban U. Vega Barajas. (2026). A Durability and Cross-Language Transfer Benchmark for a Validated Teaching-Feedback Classification Protocol. https://arxiv.org/abs/2607.11873 [doi:10.48550/arxiv.2607.11873](https://doi.org/10.48550/arxiv.2607.11873)

`q2 · i?` · `causal · r2`

Descriptive result from the Spanish durability benchmark on the 233-comment held-out set. The article reports the small open-weights model as "the weakest arm, especially zero-shot on the four-class thematic task, where wF1 is 0.31 and rises to 0.63 with few-shot", while running at zero API cost on-premise.

> "Attheoppositeend,thesmallopen-weights model Qwen2.5-1.5B is the weakest arm, especially zero-shot on the four-class thematic task, where wF1 is 0.31 and rises to 0.63 with few-shot."

## Discussion


## Related Claims

- [Under the fixed protocol, hosted LLMs produce the largest gain on Spanish thematic classification, with thematic macro F1 rising from 0.46 (TF-IDF) to roughly 0.82-0.86 for the two hosted LLMs](llms-largest-gain-spanish-thematic-macro-f1.md) — related
- [On Spanish sentiment, the 2026 frontier model shows no advantage over the cheap model, with Haiku zero-shot at 0.923 versus Opus zero-shot at 0.884 and the head-to-head McNemar favoring Haiku](frontier-no-spanish-sentiment-advantage-over-cheap.md)
- [Self-hosted open-weight LLMs offer privacy, reproducibility, and environmental advantages over commercial LLM interfaces in educational ITSs](self-hosted-llm-advantages-education.md) — related
