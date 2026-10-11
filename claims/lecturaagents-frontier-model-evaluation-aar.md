---
type: claim
title: "Frontier-model choice affects LecturaAgents performance, with Gemini 3 Pro ranking first at 80.4% AAR"
description: "Frontier-model choice affects LecturaAgents performance, with Gemini 3 Pro ranking first at 80.4% AAR"
id: lecturaagents-frontier-model-evaluation-aar
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jaward-sesay-2026
    resource: "https://arxiv.org/abs/2606.16428"
    title: "Jaward Sesay, Yue Yu, Siwei Dong, Börje F. Karlsson. (2026). Lect¯uraAgents: A Multi-Agent Framework for Adaptive Personalized AI-Assisted Learning and Embodied Teaching. arXiv. https://arxiv.org/abs/2606.16428"
    author: Jaward Sesay, Yue Yu, Siwei Dong, Börje F. Karlsson
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Frontier-model choice affects LecturaAgents performance, with Gemini 3 Pro ranking first at 80.4% AAR

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across 280 generated lectures under seven frontier models, Gemini 3 Pro ranked first overall with an AAR of 80.4%, and model choice affected both content generation and embodied teaching quality. [→ Jaward Sesay 2026](#jaward-sesay-2026)

## Evidence

### Jaward Sesay 2026

Jaward Sesay, Yue Yu, Siwei Dong, Börje F. Karlsson. (2026). Lect¯uraAgents: A Multi-Agent Framework for Adaptive Personalized AI-Assisted Learning and Embodied Teaching. arXiv. https://arxiv.org/abs/2606.16428

`q2 · i?` · `design · r2`

Expert-scored pedagogical evaluation of 280 personalized lectures (40 per model, 10 per academic level) using weighted rubric-based AAR scoring by five expert educators. Gemini 3 Pro ranked first at 80.4% AAR; GPT-5.1 followed at 78.8%; Claude 4.5 Sonnet had the strongest TAQ at 80.4%.

> "Gemini 3 Pro ranks first overall with an AAR of 80.4%, supported by strong LCQ (80.2%), PQ (83.3%), AQ (81.6%), and TAQ (76.5%) scores. GPT-5.1 remains competitive with an AAR of 78.8%"

## Discussion


## Related Claims
- [Two of seven frontier LLMs show behavioral inconsistency between monitored and unmonitored conditions (Grok-4.1-fast 5.50; Gemini-3-Pro 5.00), while four show perfect consistency (1.0)](alignment-faking-inconsistency-educational-llms.md) — related
- [CDP improves item-difficulty recovery in both rank order and absolute alignment, with the largest gains for reasoning-enabled Gemini configurations](cdp-improves-item-difficulty-recovery.md) — related
- [LecturaAgents scores higher than Instructional Agents, GenMentor, and Learn Your Way on lecture content, personalization, and assessment quality](lecturaagents-outperforms-baselines-lcq-pq-aq.md) — related
