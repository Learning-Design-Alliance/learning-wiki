---
type: claim
title: One-shot path generation raises Validity but lowers Adaptivity and Efficiency relative to step-by-step interaction
description: One-shot path generation raises Validity but lowers Adaptivity and Efficiency relative to step-by-step interaction
id: one-shot-generation-lowers-adaptivity
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: yu-liu-2026
    resource: "https://arxiv.org/abs/2609.18861"
    title: "Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang. (2026). PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning. arXiv. https://arxiv.org/abs/2609.18861"
    author: Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# One-shot path generation raises Validity but lowers Adaptivity and Efficiency relative to step-by-step interaction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Static generation increases Validity by 30.8 points for Qwen3-4B-2507 (CoT) but decreases Adaptivity by 28.8 points for Qwen3-30B-A3B (CoT) and Efficiency by 33.8 points for DeepSeek-R1-Distill-14B. [→ Yu Liu 2026](#yu-liu-2026)

## Evidence

### Yu Liu 2026

Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang. (2026). PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning. arXiv. https://arxiv.org/abs/2609.18861

`q2 · i?` · `causal · r2`

Comparison of step-by-step interactive planning with one-shot generation of the entire curriculum in a single turn, on Basic Education personas (Table 8). The article reports the printed percentage-point changes; no effect size is printed.

> "Static generation increases Validity by 30.8 percentage points for Qwen3-4B-2507 (CoT), while Adaptivity decreases by 28.8 points for Qwen3-30B-A3B (CoT) and Efficiency by 33.8 points for DeepSeek-R1-Distill-14B."

## Discussion


## Related Claims
- [Adaptivity to individual learners is the primary bottleneck for LLMs in KC path planning](adaptivity-bottleneck-llm-path-planning.md) — related
- [Chain-of-Thought prompting improves KC planning for Qwen models but its effect varies by model and educational stage](cot-effect-varies-model-stage-kc-planning.md) — related
- [Retrieval augmentation raises path Validity but not the joint Final Pass rate](rag-raises-validity-not-final-pass.md) — related
