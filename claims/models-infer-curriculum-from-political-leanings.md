---
type: claim
title: "Models appear to infer state curriculum expectations from perceived political leanings rather than actual standards content, which can worsen misalignment (e.g., GPT-4's decreased Florida alignment)"
description: "Models appear to infer state curriculum expectations from perceived political leanings rather than actual standards content, which can worsen misalignment (e.g., GPT-4's decreased Florida alignment)"
id: models-infer-curriculum-from-political-leanings
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: lisa-korver-2026
    resource: "https://doi.org/10.48550/arXiv.2606.04846"
    title: "Lisa Korver, Tomo Lazovich, Shereif Reda. (2026). Large Language Models in K-12 Education: Alignment with State Curriculum Standards and Student Personas. [doi:10.48550/arXiv.2606.04846](https://doi.org/10.48550/arXiv.2606.04846)"
    author: Lisa Korver, Tomo Lazovich, Shereif Reda
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Models appear to infer state curriculum expectations from perceived political leanings rather than actual standards content, which can worsen misalignment (e.g., GPT-4's decreased Florida alignment)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4 shows very little variation in alignment across steering conditions except toward more conservative states (Alabama, Tennessee, Texas, Georgia), where it adopts a more ambiguous secession framing that reduces its alignment with Florida's slavery-centered standards. [→ Lisa Korver 2026](#lisa-korver-2026)

## Evidence

### Lisa Korver 2026

Lisa Korver, Tomo Lazovich, Shereif Reda. (2026). Large Language Models in K-12 Education: Alignment with State Curriculum Standards and Student Personas. [doi:10.48550/arXiv.2606.04846](https://doi.org/10.48550/arXiv.2606.04846)

`q2 · i?` · `causal · r2`

Steering evaluation for GPT-4 (Figure 8 context) showing its only notable alignment changes occurred when steered toward conservative states, driven by secession-crisis responses. The article reports the ambiguous framing "produces responses that more closely align with the educational standards of those states" while decreasing Florida alignment. No effect size is printed.

> "Rather than explicitly identifying slavery as the primary cause of secession, GPT-4 adopts a more ambiguous framing that gives greater consideration to additional political and economic factors. This shift produces responses that more closely align with the educational standards of those states."

## Discussion


## Related Claims
- [Baseline LLM chatbots align more closely with some states' history standards (e.g., Florida) than others (e.g., Texas, New York, Georgia), and no single model consistently aligns best across all states](baseline-llm-state-alignment-varies-by-state.md) — related
- [State curriculum standards are not strongly associated with state political orientation; model alignment does not systematically favor left- or right-leaning states](curricular-variation-not-tied-to-political-leaning.md) — related
