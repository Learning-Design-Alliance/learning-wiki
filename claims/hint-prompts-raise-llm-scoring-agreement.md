---
type: claim
title: "Hint-based prompts raise ChatGPT scoring agreement with human experts to 98–100%, while no-hint prompts are unstable (Q2 precision 0.42)"
description: "Hint-based prompts raise ChatGPT scoring agreement with human experts to 98–100%, while no-hint prompts are unstable (Q2 precision 0.42)"
id: hint-prompts-raise-llm-scoring-agreement
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: satoshi-takahashi-2026
    resource: "https://arxiv.org/abs/2609.25790"
    title: "Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada. (2026). Automating Constructive Assessment with Large Language Models: Toward Scalable and Repeated Evaluation of Practical Competence. arXiv. https://arxiv.org/abs/2609.25790"
    author: Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: satoshi-takahashi-2026-2
    resource: "https://arxiv.org/abs/2609.25790"
    title: "Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada. (2026). Automating Constructive Assessment with Large Language Models: Toward Scalable and Repeated Evaluation of Practical Competence. arXiv. https://arxiv.org/abs/2609.25790"
    author: Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Hint-based prompts raise ChatGPT scoring agreement with human experts to 98–100%, while no-hint prompts are unstable (Q2 precision 0.42)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`

## Subclaims
`q3 i?` Under the hint condition, agreement of 98% or higher was achieved for all questions, with perfect agreement (100%) for Q1 and Q2; under the no-hint condition results varied, with Q2 precision only 0.42. [→ Satoshi Takahashi 2026](#satoshi-takahashi-2026)
`q3 i?` When ChatGPT scored its own generated problem, perfect agreement was observed (Fleiss' κ = 1.00 for Q1 and Q2). [→ Satoshi Takahashi 2026 (2)](#satoshi-takahashi-2026-2)

## Evidence

### Satoshi Takahashi 2026

Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada. (2026). Automating Constructive Assessment with Large Language Models: Toward Scalable and Repeated Evaluation of Practical Competence. arXiv. https://arxiv.org/abs/2609.25790

`q3 · i?` · `causal · r2`

Experiment 2 compared two prompt conditions (no-hints vs. hints with human-scored examples) on descriptive answers to the ChatGPT-generated problem; scoring was repeated nine times with majority vote and evaluated with accuracy, precision, recall, and F1.

> "By contrast, under the hint condition, an agreement of 98% or higher was achieved for all questions, with perfect agreement (100%) recorded for Q1 and Q2."

### Satoshi Takahashi 2026 (2)

Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada. (2026). Automating Constructive Assessment with Large Language Models: Toward Scalable and Repeated Evaluation of Practical Competence. arXiv. https://arxiv.org/abs/2609.25790

`q3 · i?` · `design · r2`

Experiment 1 agreement analysis (Table 4): 9-ChatGPT agreement on the ChatGPT-generated problem reached 100.00% for Q1 and Q2 and 97.67% for Q3, with Fleiss' κ of 1.00, 1.00, and 0.97.

> "Furthermore, when ChatGPT itself scored the ChatGPT-generated problem, perfect agreement was observed, confirming even higher consistency."

## Discussion


## Related Claims
- [ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality](chatgpt-zero-shot-relevance-extraction-unreliable.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [ChatGPT's exam scores were within 10% of human grades 70% of the time in a study of AI-based grading](chatgpt-grading-within-10-percent-human.md) — related
