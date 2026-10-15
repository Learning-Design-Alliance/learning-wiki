---
type: claim
title: Sentiment classification transfers to English under the unchanged protocol, with a frozen multilingual encoder the strongest arm at wF1 0.73 and LLMs matching it only with few-shot prompting
description: Sentiment classification transfers to English under the unchanged protocol, with a frozen multilingual encoder the strongest arm at wF1 0.73 and LLMs matching it only with few-shot prompting
id: english-sentiment-transfer-encoder-strongest
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
    kind: design
    rigour: 2
---

# Sentiment classification transfers to English under the unchanged protocol, with a frozen multilingual encoder the strongest arm at wF1 0.73 and LLMs matching it only with few-shot prompting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the balanced English test split, the e5 encoder reaches weighted F1 0.73; LLMs reach parity only with few-shot prompting (0.72-0.73) while zero-shot sits near 0.67. [→ Esteban U. Vega Barajas 2026](#esteban-u-vega-barajas-2026)

## Evidence

### Esteban U. Vega Barajas 2026

Esteban U. Vega Barajas. (2026). A Durability and Cross-Language Transfer Benchmark for a Validated Teaching-Feedback Classification Protocol. https://arxiv.org/abs/2607.11873 [doi:10.48550/arxiv.2607.11873](https://doi.org/10.48550/arxiv.2607.11873)

`q2 · i?` · `design · r2`

English sentiment transfer experiment on the balanced 45,000-comment corpus; classical and encoder arms use the full 6,750-comment test split while LLM arms use a 1,500-comment cost-capped subset, so cross-rule values are not directly comparable. The article reports the encoder "strongest arm, at wF1 0.73".

> "On the full test split the modern encoder is the strongest arm, at wF1 0.73. Both LLMs match it only with few-shot prompting: zero-shot sits near 0.67 for Haiku and Opus alike, and few-shot reaches 0.72 to 0.73."

## Discussion


## Related Claims

- [The frozen BETO-2019 design and the modern e5-base encoder are numerically close on Spanish, with no descriptive separation on either task](frozen-beto-and-e5-no-descriptive-separation.md) — related
- [Under the fixed protocol, hosted LLMs produce the largest gain on Spanish thematic classification, with thematic macro F1 rising from 0.46 (TF-IDF) to roughly 0.82-0.86 for the two hosted LLMs](llms-largest-gain-spanish-thematic-macro-f1.md) — related
- [On Spanish sentiment, the 2026 frontier model shows no advantage over the cheap model, with Haiku zero-shot at 0.923 versus Opus zero-shot at 0.884 and the head-to-head McNemar favoring Haiku](frontier-no-spanish-sentiment-advantage-over-cheap.md) — related
- [The star-to-sentiment labeling rule agrees with human review-level labels at Cohen's kappa 0.66 with 82% accuracy on 3,000 RateMyProfessor teacher reviews](star-label-rule-kappa-066-82-percent.md)
