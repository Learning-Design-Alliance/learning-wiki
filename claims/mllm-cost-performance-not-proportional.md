---
type: claim
title: "Cost and performance are correlated but not proportional: GPT-5 mini scored 75% at $0.26 while Claude Opus 4 underperformed at 57.0% despite high cost"
description: "Cost and performance are correlated but not proportional: GPT-5 mini scored 75% at $0.26 while Claude Opus 4 underperformed at 57.0% despite high cost"
id: mllm-cost-performance-not-proportional
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: giulia-polverini-and-bor-gregorcic-2025
    resource: "https://doi.org/10.1088/1361-6404/ae03f8"
    title: "Giulia Polverini and Bor Gregorcic. (2025). Multimodal large language models and physics visual tasks: comparative analysis of performance and costs. [doi:10.1088/1361-6404/ae03f8](https://doi.org/10.1088/1361-6404/ae03f8)"
    author: Giulia Polverini and Bor Gregorcic
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Cost and performance are correlated but not proportional: GPT-5 mini scored 75% at $0.26 while Claude Opus 4 underperformed at 57.0% despite high cost

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The relationship between benchmark cost and accuracy is not proportional, with cheap outliers outperforming more expensive models. [→ Giulia Polverini and Bor Gregorcic 2025](#giulia-polverini-and-bor-gregorcic-2025)

## Evidence

### Giulia Polverini and Bor Gregorcic 2025

Giulia Polverini and Bor Gregorcic. (2025). Multimodal large language models and physics visual tasks: comparative analysis of performance and costs. [doi:10.1088/1361-6404/ae03f8](https://doi.org/10.1088/1361-6404/ae03f8)

`q2 · i?` · `design · r2`

Cost analysis plotting each model's average score against its normalized cost of running the 102-item benchmark once (Fig. 3, Table 4) found "the relationship is not proportional, and there are some interesting outliers."

> "First, while there is an overall correlation between cost and performance, the relationship is not proportional, and there are some interesting outliers."

## Discussion


## Related Claims
- [Within each provider's model family, successive performance tiers correlate with roughly 10–20 percentage-point accuracy increases](provider-tier-correlates-10-20-point-gains.md) — reports the opposite
- [FSM-based evaluation discriminates interactive quality across models, with GPT-5 Mini scoring highest and most tiers significantly separated](fsm-eval-discriminates-model-quality.md) — related
