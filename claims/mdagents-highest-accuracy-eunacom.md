---
type: claim
title: MDAGENTS achieves the highest accuracy on Spanish-language EUNACOM questions, outperforming all other evaluated strategies
description: MDAGENTS achieves the highest accuracy on Spanish-language EUNACOM questions, outperforming all other evaluated strategies
id: mdagents-highest-accuracy-eunacom
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

# MDAGENTS achieves the highest accuracy on Spanish-language EUNACOM questions, outperforming all other evaluated strategies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` MDAGENTS achieved a mean accuracy of 89.97% (SD = 0.56%), significantly surpassing zero-shot and self-reflection strategies. [→ Altermatt Fernando R. 2025](#altermatt-fernando-r-2025)

## Evidence

### Altermatt Fernando R. 2025

Altermatt Fernando R., Neyem Andres, Sumonte Nicolas, Mendoza Marcelo, Villagran Ignacio, Lacassie Hector J. (2025). Performance of single-agent and multi-agent language models in Spanish language medical competency exams. BMC Medical Education. https://doi.org/10.1186/s12909-025-07250-3

`q2 · i?` · `causal · r2`

Automated evaluation of GPT-4o on 1,062 publicly available EUNACOM multiple-choice questions, each configuration run twice per temperature. The results section reports "MDAGENTS achieved a mean accuracy of 89.97% (SD = 0.56%)" with adjusted p < 0.01 versus zero-shot and self-reflection; no standardized effect size is printed.

> "MDAGENTS achieved a mean accuracy of 89.97% (SD = 0.56%), significantly surpassing simpler approaches, including zero-shot (85.90%, SD = 0.32%) and self-reflection (85.38%, SD = 0.22%) (all adjusted p < 0.01)."

## Discussion


## Related Claims
- [Multi-agent strategies incur substantially higher computational costs than single-agent methods on EUNACOM evaluation](multiagent-computational-cost-tradeoff.md) — related
- [CoT + few-shot prompting delivers high accuracy with minimal computational overhead, offering an efficient alternative to multi-agent frameworks](cot-few-shot-efficient-alternative.md) — related
- [GPT-4 achieves the highest pooled accuracy among LLMs (81%), significantly outperforming GPT-3.5 (60%)](gpt4-highest-accuracy-81-outperforms-gpt35.md) — related
- [GPT-4 achieves a pooled MCQ accuracy of 81% on medical licensing examinations, significantly surpassing GPT-3.5's 58%](gpt4-81-percent-pooled-accuracy-surpasses-gpt35.md) — related
- [Temperature settings (0.3, 0.6, 1.3) did not significantly affect GPT-4o accuracy on EUNACOM questions](temperature-no-effect-eunacom-accuracy.md) — related
