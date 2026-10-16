---
type: claim
title: Random shot selection yields the worst originality-similarity combination, while greedy and constraint-satisfaction selection raise originality without increasing item redundancy
description: Random shot selection yields the worst originality-similarity combination, while greedy and constraint-satisfaction selection raise originality without increasing item redundancy
id: shot-selection-originality-similarity-tradeoff
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: antonio-laverghetta-jr-2024
    resource: "https://doi.org/10.48550/arxiv.2409.00202"
    title: "Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202 [doi:10.48550/arxiv.2409.00202](https://doi.org/10.48550/arxiv.2409.00202)"
    author: Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
  - id: antonio-laverghetta-jr-2024-2
    resource: "https://arxiv.org/abs/2409.00202"
    title: "Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202"
    author: Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty
    q: 2
    i: "?"
    kind: design
    rigour: "?"
---

# Random shot selection yields the worst originality-similarity combination, while greedy and constraint-satisfaction selection raise originality without increasing item redundancy

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r?`, 1 design `r?` · `q2`

## Subclaims
`q2 i?` Random shot selection produces mostly low-originality items with the highest similarity peak; greedy and constraint satisfaction achieve lower similarity and higher originality consistently, with similarity remaining generally static as originality increases. [→ Antonio Laverghetta Jr. 2024](#antonio-laverghetta-jr-2024)
`q2 i?` In the full last-round univariate comparison, many more item pairs with cosine similarity of 1.0 occur under greedy than constraint satisfaction shot selection. [→ Antonio Laverghetta Jr. 2024 (2)](#antonio-laverghetta-jr-2024-2)

## Evidence

### Antonio Laverghetta Jr. 2024

Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202 [doi:10.48550/arxiv.2409.00202](https://doi.org/10.48550/arxiv.2409.00202)

`q2 · i?` · `causal · r?`

Numerical analysis of the generated item pool plotted as a joint histogram of originality and mean cosine similarity (Results §4.2, Fig. 4), comparing random, greedy, and constraint-satisfaction shot selection. The article reports random selection obtained "the worst combination of results"; no inferential statistic is printed.

> "We observe that random shot selection obtains the worst combination of results: not only are most items low on originality, but the distributionalso peaks the highest on similarity."

### Antonio Laverghetta Jr. 2024 (2)

Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202

`q2 · i?` · `design · r?`

Univariate histogram of cosine similarity for all last-round items under greedy versus constraint satisfaction (Results §4.2, Fig. 5). The article reports "many more" duplicate items under greedy selection and notes greedy also peaks at higher density toward the lower end of the distribution.

> "Although both methods generate some item pairs with cosine similarities of1.0, there are many more such items for greedy shot selection, indicating a much larger fraction of extremely similar item content."

## Discussion


## Related Claims
- [CPIG's iterative exemplar selection consistently improves the originality of LLM responses to generated CPS items by the last round of item generation](cpig-improves-response-originality-over-iterations.md) — related
- [Uniform (redundant) contexts yield higher semantic similarity ratings than diverse contexts](redundant-contexts-improve-semantic-representations.md) — related
