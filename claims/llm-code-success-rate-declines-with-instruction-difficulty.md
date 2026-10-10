---
type: claim
title: "LLM-generated robot control code succeeds on 100%, 94.4%, and 88.9% of simple, composite, and complex instructions respectively"
description: "LLM-generated robot control code succeeds on 100%, 94.4%, and 88.9% of simple, composite, and complex instructions respectively"
id: llm-code-success-rate-declines-with-instruction-difficulty
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: shenqi-lu-and-liangwei-zhang-2026
    resource: "https://arxiv.org/abs/2601.01196"
    title: "Shenqi Lu and Liangwei Zhang. (2026). EduSim-LLM: An Educational Platform Integrating Large Language Models and Robotic Simulation for Beginners. https://arxiv.org/abs/2601.01196"
    author: Shenqi Lu and Liangwei Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM-generated robot control code succeeds on 100%, 94.4%, and 88.9% of simple, composite, and complex instructions respectively

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In simulation, LLM-generated control code achieved success rates of 100% for simple, 94.4% for composite, and 88.9% for complex instructions, with success declining as difficulty increases. [→ Shenqi Lu and Liangwei Zhang 2026](#shenqi-lu-and-liangwei-zhang-2026)

## Evidence

### Shenqi Lu and Liangwei Zhang 2026

Shenqi Lu and Liangwei Zhang. (2026). EduSim-LLM: An Educational Platform Integrating Large Language Models and Robotic Simulation for Beginners. https://arxiv.org/abs/2601.01196

`q2 · i?` · `design · r2`

Dataset-based simulation evaluation of LLM-generated robot control code using Groq's llama-3.3-70b-versatile on three YouBot robots. The test set contained 108 instances across difficulty levels, with the article reporting "the success rates for simple, composite, and complex instructions are 100%, 94.4%, and 88.9%, respectively."

> "Aggregated over 36 cases per group, the success rates for simple, composite, and complex instructions are 100%, 94.4%, and 88.9%, respectively, as shown in Fig. 6 (B). The success rate decreases as the instruction difficulty level increases from simple to composite and complex."

## Discussion


## Related Claims
- [The article constructs an educational benchmark of 108 instruction instances grouped into simple, composite, and complex difficulty levels](edusim-llm-three-level-instruction-difficulty-benchmark.md) — related
- [A single natural-language command can be decomposed by an LLM into coordinated sequential action sequences for multiple robots](llm-decomposes-command-into-multi-robot-action-sequences.md) — related
