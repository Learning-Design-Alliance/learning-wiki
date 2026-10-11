---
type: claim
title: "CPIG's iterative exemplar selection consistently improves the originality of LLM responses to generated CPS items by the last round of item generation"
description: "CPIG's iterative exemplar selection consistently improves the originality of LLM responses to generated CPS items by the last round of item generation"
id: cpig-improves-response-originality-over-iterations
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: antonio-laverghetta-jr-2024
    resource: "https://arxiv.org/abs/2409.00202"
    title: "Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202"
    author: Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# CPIG's iterative exemplar selection consistently improves the originality of LLM responses to generated CPS items by the last round of item generation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`

## Subclaims
`q2 i?` Regardless of the item generator model, CPIG improves originality scores of responses by the last round, in some cases more than doubling the first-round score, with significant t-tests for both demographic and psychometric prompting styles. [→ Antonio Laverghetta Jr. 2024](#antonio-laverghetta-jr-2024)

## Evidence

### Antonio Laverghetta Jr. 2024

Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202

`q2 · i?` · `causal · r?`

Simulation-style experiments with multiple open-source and commercial LLMs as item and response generators, scored by a roberta-base originality model (Results §4.1, Fig. 2). The article reports the improvement was "more than doubling the score compared to the first round" in some cases; t-tests were significant (p<< 0.001) for demographic and psychometric prompting styles, but no effect size is printed.

> "Critically, regardless of the item generator,CPIG consistently improves originality scores of responses by the last round of item generation, in some casesmore than doubling the score compared to the first round."

## Discussion


## Related Claims
- [Response length is only weakly correlated with originality for most LLMs, suggesting CPIG's originality gains are not purely elaboration](length-originality-correlation-weak.md) — related
- [Random shot selection yields the worst originality-similarity combination, while greedy and constraint-satisfaction selection raise originality without increasing item redundancy](shot-selection-originality-similarity-tradeoff.md) — related
- [Demographic and psychometric response prompting produces higher-variance, heavier-tailed originality distributions than a no-context baseline, though still less variable than humans](response-prompting-styles-increase-variance.md) — related
