---
type: claim
title: Adaptivity to individual learners is the primary bottleneck for LLMs in KC path planning
description: Adaptivity to individual learners is the primary bottleneck for LLMs in KC path planning
id: adaptivity-bottleneck-llm-path-planning
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: yu-liu-2026
    resource: "https://doi.org/10.48550/arxiv.2609.18861"
    title: "Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang. (2026). PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning. arXiv. https://arxiv.org/abs/2609.18861 [doi:10.48550/arxiv.2609.18861](https://doi.org/10.48550/arxiv.2609.18861)"
    author: Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Adaptivity to individual learners is the primary bottleneck for LLMs in KC path planning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Models perform relatively well on Validity (DeepSeek-V3.1 at 90.9%) but no model exceeds 44.7% on Adaptivity in Basic Education. [→ Yu Liu 2026](#yu-liu-2026)

## Evidence

### Yu Liu 2026

Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang. (2026). PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning. arXiv. https://arxiv.org/abs/2609.18861 [doi:10.48550/arxiv.2609.18861](https://doi.org/10.48550/arxiv.2609.18861)

`q2 · i?` · `design · r2`

Results section analysis of Table 4 pass rates across the three evaluation dimensions. The article reports DeepSeek-V3.1's Validity pass rate at 90.9% while Adaptivity remains the bottleneck, with the top Adaptivity rate at 44.7% for Qwen3-30B-A3B (CoT) and 44.3% for DeepSeek-V3.1. No effect size is printed.

> "Adaptivityremains the primary bottleneck: even the top-performing Qwen3-30B-A3B (CoT) achieves only 44.7%, while DeepSeek-V3.1 reaches 44.3%. This reveals a gap in personalization"

## Discussion


## Related Claims
- [Strongest LLMs reach only about 29.5% final pass rate on Basic Education KC planning and drop to 14.6% on Higher Education](llm-low-final-pass-kc-planning.md) — related
- [One-shot path generation raises Validity but lowers Adaptivity and Efficiency relative to step-by-step interaction](one-shot-generation-lowers-adaptivity.md) — related
- [Chain-of-Thought prompting improves KC planning for Qwen models but its effect varies by model and educational stage](cot-effect-varies-model-stage-kc-planning.md) — related
- [Removing explicit mastery information from learner profiles mainly degrades Adaptivity](mastery-information-needed-for-adaptivity.md) — a narrower finding that bears on this claim
