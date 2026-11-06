---
type: claim
title: Temperature settings (0.3, 0.6, 1.3) did not significantly affect GPT-4o accuracy on EUNACOM questions
description: Temperature settings (0.3, 0.6, 1.3) did not significantly affect GPT-4o accuracy on EUNACOM questions
id: temperature-no-effect-eunacom-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
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

# Temperature settings (0.3, 0.6, 1.3) did not significantly affect GPT-4o accuracy on EUNACOM questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Neither single-agent nor multi-agent strategies showed significant sensitivity to temperature adjustments across 0.3, 0.6, and 1.3. [→ Altermatt Fernando R. 2025](#altermatt-fernando-r-2025)

## Evidence

### Altermatt Fernando R. 2025

Altermatt Fernando R., Neyem Andres, Sumonte Nicolas, Mendoza Marcelo, Villagran Ignacio, Lacassie Hector J. (2025). Performance of single-agent and multi-agent language models in Spanish language medical competency exams. BMC Medical Education. https://doi.org/10.1186/s12909-025-07250-3

`q2 · i?` · `causal · r2`

Kruskal–Wallis tests across temperature conditions in the automated EUNACOM evaluation found no significant differences (p > 0.05 for all comparisons); the abstract also reports F2,54 = 1.45, p = 0.24. No effect size is printed, so impact is coded i? (no magnitude reported; not a null effect).

> "Neither the single-agent nor the multiagent strategies showed significant sensitivity to temperature adjustments (0.3, 0.6, 1.3), as evidenced by the Kruskal–Wallis test results (p > 0.05 for all comparisons)."

## Discussion


## Related Claims
- [Multi-agent strategies incur substantially higher computational costs than single-agent methods on EUNACOM evaluation](multiagent-computational-cost-tradeoff.md) — related
- [Temperature parameter has a statistically significant but negligible effect on GPT-4o exam accuracy (ηG² = 0.0017), with global accuracy peaking at temperature 0.23](temperature-effect-negligible-gpt4o-accuracy.md) — related
- [All three LLMs show near-perfect answer reproducibility under repeated API testing at zero temperature, highest for Claude 3.5 Sonnet (99.9%)](llm-kmle-reproducibility-near-perfect.md) — related
- [Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones](bootstrapping-self-consistency-flags-incorrect-answers.md) — related
- [MDAGENTS achieves the highest accuracy on Spanish-language EUNACOM questions, outperforming all other evaluated strategies](mdagents-highest-accuracy-eunacom.md) — related
