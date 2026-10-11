---
type: claim
title: LLaMA shows a persona-conditioned vocabulary collapse for the Roma minority persona, with TTR falling 0.018 points below its own cross-persona mean
description: LLaMA shows a persona-conditioned vocabulary collapse for the Roma minority persona, with TTR falling 0.018 points below its own cross-persona mean
id: llama-ttr-collapse-roma-persona
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: alexis-popovici-2026
    resource: "https://arxiv.org/abs/2607.11292"
    title: "Alexis Popovici, Andrei Ionascu, Adrian Marius Dumitran. (2026). The Paternalistic Filter: Epistemic Injustice and Differential Refusal in LLM-Mediated History Education for Marginalized Romanian Students. arXiv preprint. https://arxiv.org/abs/2607.11292"
    author: Alexis Popovici, Andrei Ionascu, Adrian Marius Dumitran
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLaMA shows a persona-conditioned vocabulary collapse for the Roma minority persona, with TTR falling 0.018 points below its own cross-persona mean

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Lexical diversity (TTR) drops for specific personas in a model-specific, identity-conditioned pattern, despite uniform response lengths of 330–378 words. [→ Alexis Popovici 2026](#alexis-popovici-2026)

## Evidence

### Alexis Popovici 2026

Alexis Popovici, Andrei Ionascu, Adrian Marius Dumitran. (2026). The Paternalistic Filter: Epistemic Injustice and Differential Refusal in LLM-Mediated History Education for Marginalized Romanian Students. arXiv preprint. https://arxiv.org/abs/2607.11292

`q2 · i?` · `causal · r2`

TTR analysis of audit responses shown in Fig. 3. Response length was uniform across personas (330–378 words), mitigating TTR's length sensitivity; GPT_OSS showed a relative drop for the Low Tier persona, which the authors read as spontaneous persona-conditioned simplification.

> "LLaMA's TTR for Minoritatea Romă (0.632) falls 0.018 points below its own cross-persona mean—the largest within-model ethnic drop observed."

## Discussion


## Related Claims
- [LLaMA produces a fivefold higher victimization-to-politics vocabulary ratio for the Roma persona (≈0.15) than for elite peers (≈0.03)](agency-theft-victimization-framing.md) — related
- [LLM history tutors reduce marginalized students' access to contested geopolitical framing, with the coup theory appearing in 2.6% of Low Tier responses versus 7.9% for the baseline](epistemic-gatekeeping-coup-gap.md) — related
- [Engagement removal lowers the adaptive score, indicating the engagement generator realizes persona-conditioned style choices in narration](engagement-realizes-adaptive-style-in-narration.md) — related
