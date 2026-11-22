---
type: claim
title: All models perform better on structured output tasks than on open-ended competencies, with significant per-model differences across competencies
description: All models perform better on structured output tasks than on open-ended competencies, with significant per-model differences across competencies
id: l2-bench-structured-vs-open-ended-competencies
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: james-edgell-2026
    resource: "https://doi.org/10.1609/aies.v9i2.43189"
    title: "James Edgell, Wm. Matthew Kennedy, Ben Knight, Danielle Carvalho, Martin Ku, Isaac Pattis. (2026). L2-Bench: An Evaluation Benchmark for Measuring LLM Capabilities in Second Language Education. [doi:10.1609/aies.v9i2.43189](https://doi.org/10.1609/aies.v9i2.43189)"
    author: James Edgell, Wm. Matthew Kennedy, Ben Knight, Danielle Carvalho, Martin Ku, Isaac Pattis
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# All models perform better on structured output tasks than on open-ended competencies, with significant per-model differences across competencies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Kruskal-Wallis tests per model show significant differences across the 12 competencies (p < 0.001 for all models). [→ James Edgell 2026](#james-edgell-2026)
`q2 i?` All models perform relatively well on structured output tasks (lesson planning, activity planning) but less well on open-ended competencies (conversational exchange, giving feedback, evaluating performance). [→ James Edgell 2026](#james-edgell-2026)
`q2 i?` No one frontier model dominates both structured and open-ended tasks; GPT 5.4 as conversational exchange partner is outperformed by Gemini 3 Flash and both small models. [→ James Edgell 2026](#james-edgell-2026)

## Evidence

### James Edgell 2026

James Edgell, Wm. Matthew Kennedy, Ben Knight, Danielle Carvalho, Martin Ku, Isaac Pattis. (2026). L2-Bench: An Evaluation Benchmark for Measuring LLM Capabilities in Second Language Education. [doi:10.1609/aies.v9i2.43189](https://doi.org/10.1609/aies.v9i2.43189)

`q2 · i?` · `design · r3`

Competency-level analysis of nine models across 1,000 tasks; Kruskal-Wallis tests per model determined all models show significant differences across competencies (p < 0.001), with eta-squared values from 0.089 to 0.189 reported in Table 2.

> "All models perform relatively well on structured output tasks (lesson planning, activity planning) but less well on open-ended competencies (conversational exchange, giving feedback, evaluating performance), as shown in Figure 1. Notably, no one frontier model dominates both structured and open-ended tasks."

## Discussion


## Related Claims
- [No significant overall difference in Learner+AI task performance across guidance types or LLM prompting, though examples and metacognitive questioning paired with an unprompted LLM showed exploratory gains](no-overall-performance-difference-guidance-llm-type.md) — related
