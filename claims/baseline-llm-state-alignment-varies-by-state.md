---
type: claim
title: "Baseline LLM chatbots align more closely with some states' history standards (e.g., Florida) than others (e.g., Texas, New York, Georgia), and no single model consistently aligns best across all states"
description: "Baseline LLM chatbots align more closely with some states' history standards (e.g., Florida) than others (e.g., Texas, New York, Georgia), and no single model consistently aligns best across all states"
id: baseline-llm-state-alignment-varies-by-state
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
    kind: design
    rigour: 2
---

# Baseline LLM chatbots align more closely with some states' history standards (e.g., Florida) than others (e.g., Texas, New York, Georgia), and no single model consistently aligns best across all states

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Baseline models generally group together in their state alignment, showing close alignment with Florida standards and lower alignment with Texas, New York, and Georgia, with the choice of model having relatively little impact. [→ Lisa Korver 2026](#lisa-korver-2026)

## Evidence

### Lisa Korver 2026

Lisa Korver, Tomo Lazovich, Shereif Reda. (2026). Large Language Models in K-12 Education: Alignment with State Curriculum Standards and Student Personas. [doi:10.48550/arXiv.2606.04846](https://doi.org/10.48550/arXiv.2606.04846)

`q2 · i?` · `design · r2`

Evaluation of baseline (unsteered) responses from Grok, GPT, and Gemini chatbots on five divergent U.S. History topics, scored with the State Alignment metric and shown in Figure 4. The article reports that "all three models show close alignment with Florida state standards" while alignment is lower for Texas, New York, and Georgia. No effect size is printed.

> "As a whole, the models are generally grouped in their alignment with each state, as all three models show close alignment with Florida state standards and have lower alignment with states likes Texas, New York, and Georgia."

## Discussion


## Related Claims
- [Models appear to infer state curriculum expectations from perceived political leanings rather than actual standards content, which can worsen misalignment (e.g., GPT-4's decreased Florida alignment)](models-infer-curriculum-from-political-leanings.md) — related
- [State curriculum standards are not strongly associated with state political orientation; model alignment does not systematically favor left- or right-leaning states](curricular-variation-not-tied-to-political-leaning.md) — reports the opposite
