---
type: claim
title: In simulation the router matches the empirically optimal subject strategy in 8 of 13 subjects, but retreats to a safe strategy where gains are marginal
description: In simulation the router matches the empirically optimal subject strategy in 8 of 13 subjects, but retreats to a safe strategy where gains are marginal
id: router-subject-strategy-alignment-simulation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: po-chin-chang-2026
    resource: "https://arxiv.org/abs/2606.20138"
    title: "Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138"
    author: Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: po-chin-chang-2026-2
    resource: "https://arxiv.org/abs/2606.20138"
    title: "Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138"
    author: Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# In simulation the router matches the empirically optimal subject strategy in 8 of 13 subjects, but retreats to a safe strategy where gains are marginal

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` In 8 of 13 evaluated subjects the router's predicted prompt exactly matched the empirically optimal prompt (Gap = 0.000), with an overall alignment rate (Gap≤0.01) of 69.2%. [→ Po-Chin Chang 2026](#po-chin-chang-2026)
`q2 i?` In History the router converged to Analytical_opt instead of the empirically superior Best strategy, reflecting risk-avoiding behavior when potential gains are marginal (<0.013). [→ Po-Chin Chang 2026 (2)](#po-chin-chang-2026-2)

## Evidence

### Po-Chin Chang 2026

Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138

`q2 · i?` · `causal · r2`

Empirical alignment analysis in simulation (Table 1) comparing the model's final predicted prompt against the maximum-average-score prompt per subject; non-matching subjects show regret margins averaging under 0.02.

> "In 8 out of the 13 evaluated subjects, the routing model achieved a perfect match (Gap = 0.000), successfully adopting the statistically optimal pedagogical strategy."

### Po-Chin Chang 2026 (2)

Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138

`q2 · i?` · `causal · r2`

Simulation routing-dynamics analysis (Figure 4b, Table 1): in History the model settles on Analytical_opt rather than Best, which the authors attribute to prioritizing "score stability over exploration" when gains are marginal (<0.013).

> "However, in subjects like History (see Table 1 and Figure 4b), the routing model converges to Analytical_opt, instead of the empirically superior Beststrategy."

## Discussion


## Related Claims
- [In simulation, an adaptive prompt router outperforms two static prompt baselines on pedagogical score across 390 scenarios](prompt-router-beats-static-baselines-simulation.md) — related
- [The adaptive router reduces turns in long conversations (turns≥5) but not across the unfiltered dataset](router-reduces-turns-long-conversations.md) — related
- [Live feedback shifts the router's strategy from the Feynman prompt favored in simulation to the scaffolding Coach prompt, with superior live performance](sim-to-real-strategy-shift-feynman-to-coach.md) — related
