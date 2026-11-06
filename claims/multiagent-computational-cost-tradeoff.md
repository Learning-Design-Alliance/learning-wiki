---
type: claim
title: Multi-agent strategies incur substantially higher computational costs than single-agent methods on EUNACOM evaluation
description: Multi-agent strategies incur substantially higher computational costs than single-agent methods on EUNACOM evaluation
id: multiagent-computational-cost-tradeoff
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: altermatt-fernando-r-2025
    resource: "https://doi.org/10.1186/s12909-025-07250-3"
    title: "Altermatt Fernando R., Neyem Andres, Sumonte Nicolas, Mendoza Marcelo, Villagran Ignacio, Lacassie Hector J. (2025). Performance of single-agent and multi-agent language models in Spanish language medical competency exams. BMC Medical Education. https://doi.org/10.1186/s12909-025-07250-3"
    author: Altermatt Fernando R., Neyem Andres, Sumonte Nicolas, Mendoza Marcelo, Villagran Ignacio, Lacassie Hector J.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Multi-agent strategies incur substantially higher computational costs than single-agent methods on EUNACOM evaluation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` MDAGENTS averaged 21.14 API calls and approximately 192 seconds per experiment, versus a single call within seconds for zero-shot and CoT. [→ Altermatt Fernando R. 2025](#altermatt-fernando-r-2025)

## Evidence

### Altermatt Fernando R. 2025

Altermatt Fernando R., Neyem Andres, Sumonte Nicolas, Mendoza Marcelo, Villagran Ignacio, Lacassie Hector J. (2025). Performance of single-agent and multi-agent language models in Spanish language medical competency exams. BMC Medical Education. https://doi.org/10.1186/s12909-025-07250-3

`q2 · i?` · `causal · r2`

Computational resource analysis in the Results section records API calls and mean completion time per strategy (Table 1); the quoted sentence contrasts MDAGENTS with single-call single-agent methods. The authors note these demands may limit scalability in low-resource or real-time settings.

> "In contrast to single-agent methods such as Zero-Shot and CoT, which require only a single API call and complete queries within seconds, MDAGENTS averages 21.14 API calls and approximately 192 seconds per experiment."

## Discussion


## Related Claims
- [CoT + few-shot prompting delivers high accuracy with minimal computational overhead, offering an efficient alternative to multi-agent frameworks](cot-few-shot-efficient-alternative.md) — related
- [MDAGENTS achieves the highest accuracy on Spanish-language EUNACOM questions, outperforming all other evaluated strategies](mdagents-highest-accuracy-eunacom.md) — related
- [Temperature settings (0.3, 0.6, 1.3) did not significantly affect GPT-4o accuracy on EUNACOM questions](temperature-no-effect-eunacom-accuracy.md) — related
