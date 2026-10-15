---
type: claim
title: Retrieval augmentation raises path Validity but not the joint Final Pass rate
description: Retrieval augmentation raises path Validity but not the joint Final Pass rate
id: rag-raises-validity-not-final-pass
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
    kind: causal
    rigour: 2
---

# Retrieval augmentation raises path Validity but not the joint Final Pass rate

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` RAG raises Qwen3-4B-2507 Zero-shot Validity from 39.7% to 73.8% and Adaptivity from 12.5% to 19.3%, but Efficiency falls from 25.8% to 18.4% and Final Pass changes from 3.2% to 2.9%. [→ Yu Liu 2026](#yu-liu-2026)

## Evidence

### Yu Liu 2026

Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang. (2026). PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning. arXiv. https://arxiv.org/abs/2609.18861 [doi:10.48550/arxiv.2609.18861](https://doi.org/10.48550/arxiv.2609.18861)

`q2 · i?` · `causal · r2`

Controlled comparison of Qwen3-4B-2507 Zero-shot with and without retrieval augmentation (top-3 knowledge chunks via BAAI/bge-small-zh-v1.5 and FAISS) on 1,000 Basic Education personas, reported in Table 5. The article reports the printed percentage-point changes; no effect size is printed.

> "RAG raises Validity from 39.7% to 73.8%, a gain of 34.1 percentage points, and Adaptivity from 12.5% to 19.3%. Efficiency decreases from 25.8% to 18.4%, while Final Pass changes from 3.2% to 2.9%."

## Discussion


## Related Claims
- [Contextual noise from irrelevant textbooks broadly degrades KC planning, most in Validity and Efficiency](contextual-noise-degrades-kc-planning.md) — related
- [One-shot path generation raises Validity but lowers Adaptivity and Efficiency relative to step-by-step interaction](one-shot-generation-lowers-adaptivity.md) — related
- [Chain-of-Thought prompting improves KC planning for Qwen models but its effect varies by model and educational stage](cot-effect-varies-model-stage-kc-planning.md) — related
- [Strongest LLMs reach only about 29.5% final pass rate on Basic Education KC planning and drop to 14.6% on Higher Education](llm-low-final-pass-kc-planning.md) — related
