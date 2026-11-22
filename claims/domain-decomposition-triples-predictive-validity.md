---
type: claim
title: The full four-agent pipeline (domain decomposition plus expert-judge synthesis) approximately triples predictive validity compared to a single-LLM BKT baseline (r = 0.095, not significant)
description: The full four-agent pipeline (domain decomposition plus expert-judge synthesis) approximately triples predictive validity compared to a single-LLM BKT baseline (r = 0.095, not significant)
id: domain-decomposition-triples-predictive-validity
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
    i: "?"
    kind: design
    rigour: 2
---

# The full four-agent pipeline (domain decomposition plus expert-judge synthesis) approximately triples predictive validity compared to a single-LLM BKT baseline (r = 0.095, not significant)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · checked against its sources 2026-11-22 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` The single-LLM BKT baseline yields a small positive trend with learning gain (r = 0.095, p = 0.19) and post-test (r = 0.112, p = 0.12) that does not reach statistical significance, while the full Agentic pipeline reaches significance; the baseline lacks both the four domain agents and the expert-judge synthesis, so the comparison does not separate the effect of domain decomposition from that of the synthesis. [→ Gabriel Machado Santos 2026](#gabriel-machado-santos-2026)

## Evidence

### Gabriel Machado Santos 2026

Gabriel Machado Santos, Rita Maria Silva Julia, Marcelo Zanchetta do Nascimento. (2026). Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games. Accepted for publication in the IEEE Conference on Games (CoG) 2026. [doi:10.1109/cog67430.2026.11778888](https://doi.org/10.1109/cog67430.2026.11778888)

`q3 · i?` · `design · r2`

Controlled ablation (Table IV, N = 193): the baseline shares Phase 2 event classification with the Agentic pipeline and differs only in lacking domain agents and judge synthesis. The baseline shows "a small positive trend with learning gain (r= 0.095,p= 0.19)" that is not significant.

> "The single-LLM BKT baseline yields a small positive trend with learning gain (r= 0.095,p= 0.19) and post-test (r= 0.112,p= 0.12), but neither reaches statistical significance. In contrast, the Agentic BKT pipeline achieves a significant correlation with learning gain"

## Discussion


## Related Claims
- [Agentic BKT mastery estimates from gameplay correlate significantly with learning gain (r = 0.276) and post-test scores (r = 0.333), with no significant correlation with pre-test scores (r = -0.036)](agentic-bkt-mastery-correlates-with-learning-gain-posttest.md) — related
- [Per-domain correlations show credit management and spending are the strongest behavioral predictors of learning gain, while investment logic does not reach significance due to a ceiling effect and sparse events](per-domain-credit-spending-strongest-predictors.md) — related
- [In a preliminary 2×3 controlled lesson study across five backbone LLMs, structured student agents produce more differentiated mastery and misconception traces than a baseline simulator](structured-student-agents-differentiated-mastery-traces.md) — related
- [Task decomposition into three segments yields the highest-rated LLM-generated tutor training lessons, while single-step generation yields the lowest](three-segment-decomposition-highest-rated-llm-lessons.md) — related
