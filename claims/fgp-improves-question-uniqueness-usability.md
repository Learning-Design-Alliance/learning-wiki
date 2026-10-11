---
type: claim
title: Fine-grained prompting substantially improves question uniqueness and usability of LLM-generated educational questions compared with Chain-of-Thought prompting
description: Fine-grained prompting substantially improves question uniqueness and usability of LLM-generated educational questions compared with Chain-of-Thought prompting
id: fgp-improves-question-uniqueness-usability
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: fgp-uniqueness-2
    title: fgp-uniqueness-2
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Fine-grained prompting substantially improves question uniqueness and usability of LLM-generated educational questions compared with Chain-of-Thought prompting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Fine-grained prompting raises usability scores across all models in the computer science task, with Qwen2.5-7B increasing from 74.56% to 98.94%. [→ fgp-uniqueness-2](#fgp-uniqueness-2)

## Evidence

### fgp-uniqueness-2

Xiaolong Wang, Zhe Zhao, Song Lai, Chaoli Zhang, Zijie Geng, Yu Tong, Ye Wei, and Qingsong Wen. 2026. From Memorization to Creation: Evaluating the Cognitive Depth of LLM-Generated Educational Questions. Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1 (KDD '26). https://doi.org/10.1145/3770854.3785686

`q2 · i?` · `causal · r1`

Usability analysis after filtering, reported in the RQ2 results section for the computer science task under FGP. Qwen2.5-7B's usability "increases from 74.56% to 98.94%", with GLM-4-9B and InternLM3-8B reaching 99.43% and 99.08%.

> "In the computer science task, the usability score ofQwen2.5-7Bincreases from 74.56% to 98.94%, whileGLM-4-9BandInternLM3-8Breach 99.43% and 99.08%, respectively."

## Discussion


## Related Claims
- [Fine-grained prompting improves Bloom-level category consistency and knowledge coverage of generated questions in the computer science domain](fgp-improves-catcons-knowcov.md) — related
- [The Bloom-driven framework generalizes to social-science questions, with automated rubrics agreeing strongly with experts on usability but only modestly on Bloom level](social-science-generalization-human-agreement.md) — related
