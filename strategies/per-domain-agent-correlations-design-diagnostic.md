---
type: strategy
id: per-domain-agent-correlations-design-diagnostic
title: Use per-domain agent correlations as a diagnostic tool for evidence-driven game design iteration
description: "The article recommends that game designers use the per-competency breakdown of the Agentic BKT pipeline diagnostically: \"by examining which domain agents produce significant correlations with learning outcomes, design..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: gabriel-machado-santos-2026
    resource: "https://arxiv.org/abs/2606.25358"
    title: "Gabriel Machado Santos, Rita Maria Silva Julia, Marcelo Zanchetta do Nascimento. (2026). Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games. Accepted for publication in the IEEE Conference on Games (CoG) 2026. https://arxiv.org/abs/2606.25358"
    author: Gabriel Machado Santos, Rita Maria Silva Julia, Marcelo Zanchetta do Nascimento
---

# Use per-domain agent correlations as a diagnostic tool for evidence-driven game design iteration

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q3` · 1 of 1 report an effect size · 3 claims rest on one study

## Description
The article recommends that game designers use the per-competency breakdown of the Agentic BKT pipeline diagnostically: "by examining which domain agents produce significant correlations with learning outcomes, designers can identify where a game succeeds or falls short in exercising target competencies, enabling evidence-driven iteration without a full redesign-and-retest cycle". The per-domain analysis in this study showed credit management and spending as the strongest behavioral predictors while investment logic exhibited a ceiling effect, which the authors link to the low share of investing events (2.3% versus 58.7% for credit and debt).

## Design Implications

### Context
#### Requirements
- A deployed serious game with the Agentic BKT pipeline (or equivalent per-domain assessment) and external outcome measures to correlate against
#### Constraints
- Per-domain correlations should be read in light of the volume of evidence each agent receives, rather than as direct comparisons of intrinsic difficulty across competencies

### Target Learners
- K-12 students playing financial literacy serious games

### Target Learning Goals
- Exercising and assessing target financial competencies during gameplay

### Affordances
- [Agentic Bkt Pipeline Architecture](../research-methods/stealth-assessment.md)

## Claims

- [Agentic BKT mastery estimates from gameplay correlate significantly with learning gain (r = 0.276) and post-test scores (r = 0.333), with no significant correlation with pre-test scores (r = -0.036)](../claims/agentic-bkt-mastery-correlates-with-learning-gain-posttest.md) [+W]
- [The full four-agent pipeline (domain decomposition plus expert-judge synthesis) approximately triples predictive validity compared to a single-LLM BKT baseline (r = 0.095, not significant)](../claims/domain-decomposition-triples-predictive-validity.md) [+W]
- [Per-domain correlations show credit management and spending are the strongest behavioral predictors of learning gain, while investment logic does not reach significance due to a ceiling effect and sparse events](../claims/per-domain-credit-spending-strongest-predictors.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Gabriel Machado Santos, Rita Maria Silva Julia, Marcelo Zanchetta do Nascimento. (2026). Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games. Accepted for publication in the IEEE Conference on Games (CoG) 2026. https://arxiv.org/abs/2606.25358
