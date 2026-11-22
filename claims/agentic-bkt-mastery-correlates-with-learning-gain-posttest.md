---
type: claim
title: Agentic BKT mastery estimates from gameplay correlate significantly with learning gain (r = 0.276) and post-test scores (r = 0.333), with no significant correlation with pre-test scores (r = -0.036)
description: Agentic BKT mastery estimates from gameplay correlate significantly with learning gain (r = 0.276) and post-test scores (r = 0.333), with no significant correlation with pre-test scores (r = -0.036)
id: agentic-bkt-mastery-correlates-with-learning-gain-posttest
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-11-22
recheck_by: 2029
sources:
  - id: gabriel-machado-santos-2026
    resource: "https://doi.org/10.1109/cog67430.2026.11778888"
    title: "Gabriel Machado Santos, Rita Maria Silva Julia, Marcelo Zanchetta do Nascimento. (2026). Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games. Accepted for publication in the IEEE Conference on Games (CoG) 2026. [doi:10.1109/cog67430.2026.11778888](https://doi.org/10.1109/cog67430.2026.11778888)"
    author: Gabriel Machado Santos, Rita Maria Silva Julia, Marcelo Zanchetta do Nascimento
    q: 3
    i: 2
    kind: associational
    rigour: 1
---

# Agentic BKT mastery estimates from gameplay correlate significantly with learning gain (r = 0.276) and post-test scores (r = 0.333), with no significant correlation with pre-test scores (r = -0.036)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q3` · `i2` medium
> **Currency** · newest study 2026 · checked against its sources 2026-11-22 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i2` Mastery estimates from the Agentic BKT pipeline correlate significantly with learning gain (r = 0.276, p = 0.0001) and post-test scores (r = 0.333, p < 0.0001), providing convergent validity. [→ Gabriel Machado Santos 2026](#gabriel-machado-santos-2026)
`q3 i?` The mastery estimates show no significant correlation with pre-test scores (r = -0.036, p = 0.62), which the authors read as discriminant validity; a non-significant correlation does not by itself establish that the estimates capture learning rather than prior knowledge. [→ Gabriel Machado Santos 2026](#gabriel-machado-santos-2026)

## Evidence

### Gabriel Machado Santos 2026

Gabriel Machado Santos, Rita Maria Silva Julia, Marcelo Zanchetta do Nascimento. (2026). Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games. Accepted for publication in the IEEE Conference on Games (CoG) 2026. [doi:10.1109/cog67430.2026.11778888](https://doi.org/10.1109/cog67430.2026.11778888)

`q3 · i2` · `associational · r1`

Correlational analysis (Table IV, N = 193 first eligible sessions) comparing random, single-LLM, and Agentic BKT approaches against external test measures. The Agentic pipeline shows "a significant correlation with learning gain (r= 0.276,p= 0.0001)" and with post-test, with a null pre-test correlation.

> "the Agentic BKT pipeline achieves a significant correlation with learning gain (r= 0.276,p= 0.0001) and post-test score (r= 0.333,p <0.0001), approximately tripling the effect size relative to the baseline. Crucially, neither approach correlates with pre-test scores (Agentic: r=−0.036,p= 0.62"

## Discussion


## Related Claims
- [The full four-agent pipeline (domain decomposition plus expert-judge synthesis) approximately triples predictive validity compared to a single-LLM BKT baseline (r = 0.095, not significant)](domain-decomposition-triples-predictive-validity.md) — related
- [Per-domain correlations show credit management and spending are the strongest behavioral predictors of learning gain, while investment logic does not reach significance due to a ceiling effect and sparse events](per-domain-credit-spending-strongest-predictors.md) — a narrower finding that bears on this claim
- [Under persona simulation with hidden ground-truth mastery, Adaptive sessions yield lower final-belief mastery MAE (0.12) than Random-topic (0.16) and Frozen (0.20) controls, and belief updates shrink as estimates converge](collearn-adaptive-mastery-mae-convergence.md) — related
