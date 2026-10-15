---
type: claim
title: The frozen BETO-2019 design and the modern e5-base encoder are numerically close on Spanish, with no descriptive separation on either task
description: The frozen BETO-2019 design and the modern e5-base encoder are numerically close on Spanish, with no descriptive separation on either task
id: frozen-beto-and-e5-no-descriptive-separation
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

# The frozen BETO-2019 design and the modern e5-base encoder are numerically close on Spanish, with no descriptive separation on either task

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` On the Spanish held-out set, frozen BETO-2019 embeddings and the modern multilingual e5-base encoder show no descriptive separation on thematic or sentiment classification. [→ Esteban U. Vega Barajas 2026](#esteban-u-vega-barajas-2026)

## Evidence

### Esteban U. Vega Barajas 2026

Esteban U. Vega Barajas. (2026). A Durability and Cross-Language Transfer Benchmark for a Validated Teaching-Feedback Classification Protocol. https://arxiv.org/abs/2607.11873 [doi:10.48550/arxiv.2607.11873](https://doi.org/10.48550/arxiv.2607.11873)

`q2 · i?` · `causal · r2`

Descriptive paired comparison of the two frozen-embedding arms under the identical protocol on the 233-comment Spanish held-out split. The article reports near-even McNemar counts (thematic 𝑏=29, 𝑐=28; sentiment 𝑏=12, 𝑐=17) and states "no significance test is run".

> "Frozen BETO-2019 and the modern e5-base encoder are numerically close, with no descriptive separation: thematic McNemar 𝑏=29, 𝑐=28 and sentiment 𝑏=12, 𝑐=17, and no significance test is run."

## Discussion


## Related Claims
- [Sentiment classification transfers to English under the unchanged protocol, with a frozen multilingual encoder the strongest arm at wF1 0.73 and LLMs matching it only with few-shot prompting](english-sentiment-transfer-encoder-strongest.md) — related
- [On Spanish sentiment, the 2026 frontier model shows no advantage over the cheap model, with Haiku zero-shot at 0.923 versus Opus zero-shot at 0.884 and the head-to-head McNemar favoring Haiku](frontier-no-spanish-sentiment-advantage-over-cheap.md) — related
- [Under the fixed protocol, hosted LLMs produce the largest gain on Spanish thematic classification, with thematic macro F1 rising from 0.46 (TF-IDF) to roughly 0.82-0.86 for the two hosted LLMs](llms-largest-gain-spanish-thematic-macro-f1.md) — related
