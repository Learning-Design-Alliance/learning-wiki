---
type: claim
title: "The detectability of GenAI responses via PFS diminishes as pollution level increases, with most differences non-significant at 25% pollution"
description: "The detectability of GenAI responses via PFS diminishes as pollution level increases, with most differences non-significant at 25% pollution"
id: pfs-detectability-diminishes-with-pollution
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: alona-strugatski-and-giora-alexandron-2025
    resource: "https://arxiv.org/abs/2412.02713"
    title: "Alona Strugatski and Giora Alexandron. (2025). Applying Item Response Theory to Distinguish Between Human and Generative AI Responses to Multiple-Choice Assessments. LAK'25 pre-print. https://arxiv.org/abs/2412.02713"
    author: Alona Strugatski and Giora Alexandron
    q: 2
    i: "?"
    kind: design
    rigour: "?"
  - id: alona-strugatski-and-giora-alexandron-2025-2
    resource: "https://arxiv.org/abs/2412.02713"
    title: "Alona Strugatski and Giora Alexandron. (2025). Applying Item Response Theory to Distinguish Between Human and Generative AI Responses to Multiple-Choice Assessments. LAK'25 pre-print. https://arxiv.org/abs/2412.02713"
    author: Alona Strugatski and Giora Alexandron
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The detectability of GenAI responses via PFS diminishes as pollution level increases, with most differences non-significant at 25% pollution

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` At 5% and 10% pollution, Wilcoxon tests showed significant human-chatbot differences for ChatGPT with p-value < 0.0001 on all measures and both instruments, though ZU3 was non-significant for Gemini at 10% (p = 0.3655). [→ Alona Strugatski and Giora Alexandron 2025](#alona-strugatski-and-giora-alexandron-2025)
`q2 i?` At 25% pollution, differences for ZU3 become negligible across all chat models and instruments (minimal p = 0.1942), and G* and U3 also show no significant differences for most chatbot-instrument combinations. [→ Alona Strugatski and Giora Alexandron 2025 (2)](#alona-strugatski-and-giora-alexandron-2025-2)

## Evidence

### Alona Strugatski and Giora Alexandron 2025

Alona Strugatski and Giora Alexandron. (2025). Applying Item Response Theory to Distinguish Between Human and Generative AI Responses to Multiple-Choice Assessments. LAK'25 pre-print. https://arxiv.org/abs/2412.02713

`q2 · i?` · `design · r?`

Sensitivity analysis on 2x3x3 datasets at 5%, 10%, and 25% pollution following Karabatsos's framework. The article also reports Gemini's ZU3 "showed an insignificant result at the 10% pollution level (p-value=0.3655)".

> "At pollution levels of 5% and 10%, the Wilcoxon results revealed a significant difference for ChatGPT, with p-value<0.0001 on all measures and on both instruments"

### Alona Strugatski and Giora Alexandron 2025 (2)

Alona Strugatski and Giora Alexandron. (2025). Applying Item Response Theory to Distinguish Between Human and Generative AI Responses to Multiple-Choice Assessments. LAK'25 pre-print. https://arxiv.org/abs/2412.02713

`q2 · i?` · `design · r2`

At 25% pollution, G* and U3 also showed no significant differences for Claude and Gemini across both instruments and for ChatGPT on chemistry, with minimal p-value = 0.1138. Only G retained significance for ChatGPT and Claude on the psychometric test.

> "At a pollution level of 25%, the differences between human learners and AI-generated responses for the𝑍𝑈 3 measure become negligible across all chat models and instruments, with a minimal p-value of 0.1942 for ChatGPT-4o in the psychometric test"

## Discussion


## Related Claims
- [The three chatbots differ significantly in their PFS response patterns, but not uniformly across measures and instruments](chatbots-differ-in-pfs-patterns.md) — related
- [Chatbot response patterns on MCQ assessments show statistically significantly higher person-fit statistics than human respondents across instruments, chatbots, and PFS measures](pfs-chatbot-higher-than-human-mcq.md) — related
