---
type: claim
title: "Strongest LLMs reach only about 29.5% final pass rate on Basic Education KC planning and drop to 14.6% on Higher Education"
description: "Strongest LLMs reach only about 29.5% final pass rate on Basic Education KC planning and drop to 14.6% on Higher Education"
id: llm-low-final-pass-kc-planning
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
    kind: design
    rigour: 2
---

# Strongest LLMs reach only about 29.5% final pass rate on Basic Education KC planning and drop to 14.6% on Higher Education

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The top-performing DeepSeek-V3.1 achieves a 29.5% Final Pass Rate in Basic Education, falling to 14.6% in Higher Education, with similar drops for other models. [→ Yu Liu 2026](#yu-liu-2026)

## Evidence

### Yu Liu 2026

Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang. (2026). PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning. arXiv. https://arxiv.org/abs/2609.18861

`q2 · i?` · `design · r2`

Benchmark evaluation of ten open-source LLMs (1B to 30B+) on PersonaPath under a closed-loop protocol, reported as pass rates in Table 4. The article reports the top model's Final Pass Rate "falling from 29.5% to just 14.6%" between Basic and Higher Education, with Qwen3-30B-A3B (CoT) declining from 27.7% to 10.8%. No effect size is printed.

> "the Final Pass Rate of the top-performing DeepSeek-V3.1 drops by approximately half, falling from 29.5% to just 14.6%. The drop appears across all model scales: the runner-up Qwen3-30B-A3B (CoT) declines from 27.7% to 10.8%"

## Discussion


## Related Claims
- [Adaptivity to individual learners is the primary bottleneck for LLMs in KC path planning](adaptivity-bottleneck-llm-path-planning.md) — related
- [Chain-of-Thought prompting improves KC planning for Qwen models but its effect varies by model and educational stage](cot-effect-varies-model-stage-kc-planning.md) — related
- [Retrieval augmentation raises path Validity but not the joint Final Pass rate](rag-raises-validity-not-final-pass.md) — related
