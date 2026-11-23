---
type: claim
title: Sorting training paragraphs by length improves over random baselines, but the article reports no clear recipe on whether increasing or decreasing order is preferred
description: Sorting training paragraphs by length improves over random baselines, but the article reports no clear recipe on whether increasing or decreasing order is preferred
id: length-sorting-improves-no-clear-recipe
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: mixed
newest_evidence: 2016
sources:
  - id: yulia-tsvetkov-2016
    resource: "https://doi.org/10.18653/v1/p16-1013"
    title: "Yulia Tsvetkov, Manaal Faruqui, Wang Ling, Brian MacWhinney, Chris Dyer. (2016). Learning the Curriculum with Bayesian Optimization for Task-Specific Word Representation Learning. arXiv preprint. [doi:10.18653/v1/p16-1013](https://doi.org/10.18653/v1/p16-1013)"
    author: Yulia Tsvetkov, Manaal Faruqui, Wang Ling, Brian MacWhinney, Chris Dyer
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Sorting training paragraphs by length improves over random baselines, but the article reports no clear recipe on whether increasing or decreasing order is preferred

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Length-sorted curricula lead to substantial improvements over random baselines, though less pronounced than optimized curricula, with no consistent direction across tasks. [→ Yulia Tsvetkov 2016](#yulia-tsvetkov-2016)

## Evidence

### Yulia Tsvetkov 2016

Yulia Tsvetkov, Manaal Faruqui, Wang Ling, Brian MacWhinney, Chris Dyer. (2016). Learning the Curriculum with Bayesian Optimization for Task-Specific Word Representation Learning. arXiv preprint. [doi:10.18653/v1/p16-1013](https://doi.org/10.18653/v1/p16-1013)

`q2 · i?` · `causal · r2`

Results section comparing sorted baselines (long→short and short→long, following Spitkovsky et al.'s approach) against shuffled baselines in table 2; the quote is the article's own hedged statement. No effect sizes are printed.

> "Albeit not as pronounced as with optimized curriculum, sorting paragraphs by length can also lead to substantial improvements over random baselines, but there is no clear recipe on whether the models prefer curricula sorted in an increasing or decreasing order."

## Discussion


## Related Claims
- Optimized curricula for word representation training substantially outperform the strongest shuffled, sorted, and coherent baselines on downstream NLP tasks — related
- Learned curricula are task-specific: syntactic-simplicity orderings suit POS and parsing, prototypicality orderings suit sentiment, and NER prefers short-to-long paragraph order — related
- Random shuffling of training data is not essential: systems trained on coherent original-order data perform on par with, or better than, shuffled systems — related
- [Logit-gap (confidence margin) curricula consistently outperform the shuffled baseline, with Reverse CL providing the most consistent gains](logit-gap-curricula-reverse-most-consistent.md) — related
- [Problem-difficulty-based curricula consistently outperform random shuffling, with gains of up to 3–6% on easier datasets](problem-difficulty-curricula-beat-shuffled-baseline.md) — related
