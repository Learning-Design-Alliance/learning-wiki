---
type: claim
title: On Spanish sentiment, the 2026 frontier model shows no advantage over the cheap model, with Haiku zero-shot at 0.923 versus Opus zero-shot at 0.884 and the head-to-head McNemar favoring Haiku
description: On Spanish sentiment, the 2026 frontier model shows no advantage over the cheap model, with Haiku zero-shot at 0.923 versus Opus zero-shot at 0.884 and the head-to-head McNemar favoring Haiku
id: frontier-no-spanish-sentiment-advantage-over-cheap
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: esteban-u-vega-barajas-2026
    resource: "https://arxiv.org/abs/2607.11873"
    title: "Esteban U. Vega Barajas. (2026). A Durability and Cross-Language Transfer Benchmark for a Validated Teaching-Feedback Classification Protocol. https://arxiv.org/abs/2607.11873"
    author: Esteban U. Vega Barajas
    q: 2
    i: "?"
---

# On Spanish sentiment, the 2026 frontier model shows no advantage over the cheap model, with Haiku zero-shot at 0.923 versus Opus zero-shot at 0.884 and the head-to-head McNemar favoring Haiku

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` On the Spanish held-out set, Claude Opus 4.8 shows no sentiment advantage over the cheaper Claude Haiku 4.5; the descriptive head-to-head favors Haiku. [→ Esteban U. Vega Barajas 2026](#esteban-u-vega-barajas-2026)

## Evidence

### Esteban U. Vega Barajas 2026

Esteban U. Vega Barajas. (2026). A Durability and Cross-Language Transfer Benchmark for a Validated Teaching-Feedback Classification Protocol. https://arxiv.org/abs/2607.11873

`q2 · i?`

Descriptive paired comparison of prompted LLM arms on the 233-comment Spanish held-out set. The article reports Haiku zero-shot sentiment weighted F1 of 0.923 versus Opus zero-shot at 0.884, with McNemar counts "𝑏=13, 𝑐=4 in Haiku’s favor"; no significance is claimed.

> "The 2026 frontier model shows no sentiment advantage over the cheap one on this held-out set: Haiku zero-shot reaches 0.923 against Opus zero-shot at 0.884, and the head-to-head McNemar is 𝑏=13, 𝑐=4 in Haiku’s favor."

## Discussion


## Related Claims
- [Sentiment classification transfers to English under the unchanged protocol, with a frozen multilingual encoder the strongest arm at wF1 0.73 and LLMs matching it only with few-shot prompting](english-sentiment-transfer-encoder-strongest.md) — related
- [The frozen BETO-2019 design and the modern e5-base encoder are numerically close on Spanish, with no descriptive separation on either task](frozen-beto-and-e5-no-descriptive-separation.md) — related
